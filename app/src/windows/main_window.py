import sys
from collections.abc import Iterable
from pathlib import Path
from typing import Any

from PySide6.QtCore import QProcess, QSignalBlocker, QUrl
from PySide6.QtGui import QCloseEvent, QDesktopServices
from PySide6.QtWidgets import QApplication, QComboBox, QMainWindow, QMessageBox

from src.models.download_request import (
    AudioDownloadRequest,
    AudioOutput,
    DownloadRequest,
    VideoDownloadRequest,
)
from src.models.video_metadata import VideoMetadata
from src.services.ffmpeg_locator import locate_ffmpeg
from src.services.ydl_options import base_options
from src.services.youtube_url import is_youtube_url
from src.settings.preferences import Preferences
from src.windows.about_window import AboutWindow
from src.windows.settings_window import SettingsWindow
from src.workers.download_worker import DownloadWorker
from src.workers.metadata_worker import MetadataWorker
from ui.MainWindow_ui import Ui_MainWindow

STATUS_TIMEOUT_MS = 5000
DOWNLOAD_LABEL = "Descargar"
CANCEL_LABEL = "Cancelar"

ComboOptions = Iterable[tuple[str, Any]]


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self._preferences = Preferences()
        self._default_description = self.lbl_app_description.text()
        self._requested_url = ""
        self._metadata: VideoMetadata | None = None
        self._metadata_worker: MetadataWorker | None = None
        self._download_worker: DownloadWorker | None = None
        self._restore_geometry()
        self._connect_signals()

    def _restore_geometry(self) -> None:
        geometry = self._preferences.window_geometry
        if geometry is not None:
            self.restoreGeometry(geometry)

    def _connect_signals(self) -> None:
        self.url_input.editingFinished.connect(self._fetch_metadata)
        self.combo_video_quality.currentIndexChanged.connect(self._show_video_containers)
        for selector in (
            self.combo_video_quality,
            self.combo_video_format,
            self.combo_audio_quality,
            self.combo_audio_format,
        ):
            selector.currentIndexChanged.connect(self._update_download_availability)
        self.tab_widget.currentChanged.connect(self._update_download_availability)
        self.download_button.clicked.connect(self._toggle_download)
        self.action_settings.triggered.connect(self._open_settings)
        self.action_restart.triggered.connect(self._restart)
        self.action_exit.triggered.connect(self.close)
        self.action_about.triggered.connect(self._open_about)
        self.action_about_qt.triggered.connect(QApplication.aboutQt)

    def _ydl_options(self) -> dict[str, Any]:
        return base_options(locate_ffmpeg(self._preferences.ffmpeg_location))

    def _fetch_metadata(self) -> None:
        url = self.url_input.text().strip()
        if not url or url == self._requested_url or self._is_busy():
            return
        if not is_youtube_url(url):
            self.status_bar.showMessage("Introduce una URL de YouTube válida.", STATUS_TIMEOUT_MS)
            return
        self._requested_url = url
        self._clear_metadata()
        worker = MetadataWorker(url, self._ydl_options())
        worker.metadata_ready.connect(self._show_metadata)
        worker.failed.connect(self._show_metadata_error)
        worker.finished.connect(self._on_metadata_worker_finished)
        self._metadata_worker = worker
        self.url_input.setEnabled(False)
        self.status_bar.showMessage("Obteniendo formatos disponibles…")
        worker.start()

    def _show_metadata(self, metadata: VideoMetadata) -> None:
        if not metadata.has_formats:
            self._show_metadata_error("No se han encontrado formatos descargables para esta URL.")
            return
        self._metadata = metadata
        self.lbl_app_description.setText(metadata.summary)
        self._fill_combo(self.combo_video_quality, ((video.label, video) for video in metadata.video_formats))
        self._fill_combo(self.combo_audio_quality, ((audio.label, audio) for audio in metadata.audio_formats))
        self._fill_combo(self.combo_audio_format, ((output.label, output) for output in AudioOutput))

    def _show_metadata_error(self, message: str) -> None:
        QMessageBox.warning(self, "No se pudo obtener el vídeo", message)

    def _on_metadata_worker_finished(self) -> None:
        self.url_input.setEnabled(True)
        if self._metadata is None:
            self._requested_url = ""
            self.status_bar.clearMessage()
            return
        self.status_bar.showMessage(
            f"{len(self._metadata.video_formats)} formatos de vídeo y "
            f"{len(self._metadata.audio_formats)} de audio disponibles.",
            STATUS_TIMEOUT_MS,
        )

    def _clear_metadata(self) -> None:
        self._metadata = None
        self.lbl_app_description.setText(self._default_description)
        for selector in (
            self.combo_video_quality,
            self.combo_video_format,
            self.combo_audio_quality,
            self.combo_audio_format,
        ):
            self._fill_combo(selector, ())

    def _show_video_containers(self) -> None:
        video_format = self.combo_video_quality.currentData()
        containers = video_format.compatible_containers if video_format else ()
        self._fill_combo(self.combo_video_format, ((container.upper(), container) for container in containers))

    @staticmethod
    def _fill_combo(combo: QComboBox, options: ComboOptions) -> None:
        with QSignalBlocker(combo):
            combo.clear()
            for label, value in options:
                combo.addItem(label, value)
            combo.setCurrentIndex(0 if combo.count() else -1)
        combo.setEnabled(combo.count() > 0)
        combo.currentIndexChanged.emit(combo.currentIndex())

    def _update_download_availability(self) -> None:
        if not self._is_downloading():
            self.download_button.setEnabled(self._selected_request() is not None)

    def _selected_request(self) -> DownloadRequest | None:
        if self._metadata is None:
            return None
        if self.tab_widget.currentWidget() is self.audio_tab:
            return self._selected_audio_request(self._metadata)
        return self._selected_video_request(self._metadata)

    def _selected_video_request(self, metadata: VideoMetadata) -> VideoDownloadRequest | None:
        video_format = self.combo_video_quality.currentData()
        container = self.combo_video_format.currentData()
        if video_format is None or container is None:
            return None
        return VideoDownloadRequest(metadata.url, self._preferences.download_directory, video_format, container)

    def _selected_audio_request(self, metadata: VideoMetadata) -> AudioDownloadRequest | None:
        audio_format = self.combo_audio_quality.currentData()
        output = self.combo_audio_format.currentData()
        if audio_format is None or output is None:
            return None
        return AudioDownloadRequest(metadata.url, self._preferences.download_directory, audio_format, output)

    def _toggle_download(self) -> None:
        if self._is_downloading():
            self._cancel_download()
        else:
            self._start_download()

    def _start_download(self) -> None:
        request = self._selected_request()
        if request is None:
            return
        ffmpeg_location = locate_ffmpeg(self._preferences.ffmpeg_location)
        if request.requires_ffmpeg and ffmpeg_location is None:
            QMessageBox.warning(
                self,
                "FFmpeg no encontrado",
                "Este formato necesita FFmpeg. Indica su carpeta en Archivo > Configuración.",
            )
            return
        worker = DownloadWorker(request, base_options(ffmpeg_location))
        worker.progress_changed.connect(self.progress_bar.setValue)
        worker.status_changed.connect(self.status_bar.showMessage)
        worker.cancellable_changed.connect(self.download_button.setEnabled)
        worker.completed.connect(self._show_download_completed)
        worker.failed.connect(self._show_download_error)
        worker.cancelled.connect(self._show_download_cancelled)
        worker.finished.connect(self._on_download_worker_finished)
        self._download_worker = worker
        self._set_downloading(True)
        worker.start()

    def _cancel_download(self) -> None:
        if self._download_worker is None:
            return
        self._download_worker.request_cancel()
        self.download_button.setEnabled(False)
        self.status_bar.showMessage("Cancelando descarga…")

    def _set_downloading(self, downloading: bool) -> None:
        self.url_input.setEnabled(not downloading)
        self.tab_widget.setEnabled(not downloading)
        self.download_button.setText(CANCEL_LABEL if downloading else DOWNLOAD_LABEL)
        if downloading:
            self.download_button.setEnabled(True)
        else:
            self._update_download_availability()

    def _show_download_completed(self, filepath: str) -> None:
        downloaded_file = Path(filepath)
        self.status_bar.showMessage("Descarga completada.", STATUS_TIMEOUT_MS)
        dialog = QMessageBox(
            QMessageBox.Icon.Information,
            "Descarga completada",
            f"Se ha guardado «{downloaded_file.name}».",
            QMessageBox.StandardButton.Ok,
            self,
        )
        open_folder_button = dialog.addButton("Abrir carpeta", QMessageBox.ButtonRole.ActionRole)
        dialog.exec()
        if dialog.clickedButton() is open_folder_button:
            QDesktopServices.openUrl(QUrl.fromLocalFile(str(downloaded_file.parent)))

    def _show_download_error(self, message: str) -> None:
        self.status_bar.clearMessage()
        QMessageBox.critical(self, "Error en la descarga", message)

    def _show_download_cancelled(self) -> None:
        self.status_bar.showMessage("Descarga cancelada.", STATUS_TIMEOUT_MS)

    def _on_download_worker_finished(self) -> None:
        self.progress_bar.setValue(0)
        self._set_downloading(False)

    def _is_downloading(self) -> bool:
        return self._download_worker is not None and self._download_worker.isRunning()

    def _is_busy(self) -> bool:
        is_fetching = self._metadata_worker is not None and self._metadata_worker.isRunning()
        return is_fetching or self._is_downloading()

    def _open_settings(self) -> None:
        SettingsWindow(self._preferences, self).exec()

    def _open_about(self) -> None:
        AboutWindow(self).exec()

    def _restart(self) -> None:
        if self.close():
            QProcess.startDetached(sys.executable, self._relaunch_arguments())

    @staticmethod
    def _relaunch_arguments() -> list[str]:
        if getattr(sys, "frozen", False):
            return sys.argv[1:]
        return [str(Path(sys.argv[0]).resolve()), *sys.argv[1:]]

    def _confirm_exit_during_download(self) -> bool:
        answer = QMessageBox.question(
            self,
            "Descarga en curso",
            "Hay una descarga en curso. ¿Quieres cancelarla y salir?",
        )
        return answer == QMessageBox.StandardButton.Yes

    def _stop_workers(self) -> None:
        if self._download_worker is not None:
            self._download_worker.request_cancel()
            self._download_worker.wait()
        if self._metadata_worker is not None:
            self._metadata_worker.wait()

    def closeEvent(self, event: QCloseEvent) -> None:
        if self._is_downloading() and not self._confirm_exit_during_download():
            event.ignore()
            return
        self._stop_workers()
        self._preferences.window_geometry = self.saveGeometry()
        event.accept()
