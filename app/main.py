import sys
import os
import re
import subprocess
import getpass
from time import sleep
import traceback

from constants import *
from Download import Download
from VideoMetadata import VideoMetadata
from MetaWorker import MetaWorker
from DownloadWorker import DownloadWorker
from ui.MainWindow_ui import Ui_MainWindow
from pathlib import Path
from about import About
from settings import Settings

from hurry.filesize import size, si  # type: ignore
from PySide6.QtCore import (
    QSettings,
    QSize,
    QPoint,
    QLibraryInfo,
    QLocale,
    QTranslator,
)
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QComboBox,
)


# MainWindow.
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.init_ui()

        self.get_settings()
        self.set_settings()

        self.username: str = getpass.getuser()
        self.video_metadata: VideoMetadata = None

    def init_ui(self) -> None:
        self.setupUi(self)

        # For testings
        self.url_input.setText("https://www.youtube.com/watch?v=dP15zlyra3c")
        self.url_input.editingFinished.connect(self.on_url_input_finished)

        # Download button.
        self.download_button.clicked.connect(self.download)

        # Menu buttons
        self.action_about.triggered.connect(About)
        self.action_about_qt.triggered.connect(QApplication.aboutQt)
        self.action_restart.triggered.connect(self.on_restart)
        self.action_exit.triggered.connect(self.close)
        self.action_settings.triggered.connect(lambda: Settings(self))

    def get_settings(self) -> None:
        self.w_attrib = QSettings("GUIDownloader", "WindowAttributes")
        self.preferences = QSettings("GUIDownloader", "Preferences")

    def set_settings(self) -> None:
        # Initial window size/pos last saved. Use default values for first time.
        pos: QPoint = self.w_attrib.value("pos", QPoint(50, 50))
        if any(x < 0 for x in (pos.x(), pos.y())):
            pos = QPoint(50, 50)
        self.resize(self.w_attrib.value("size", QSize(270, 225)))
        self.move(pos)
        self.download_path = self.preferences.value(
            "download_path",
            str(Path.home() / "Downloads")
        )

    def save_settings(self) -> None:
        # Remember window postion and size on exit.
        self.w_attrib.setValue("size", self.size())
        self.w_attrib.setValue("pos", self.pos())

    def download(self) -> None:
        try:
            url = self.url_input.text()

            if not url:
                self.status_bar.showMessage(
                    self.tr("Por favor, introduce una URL."),
                    3000
                )
                return

            if not self.video_metadata:
                return

            video_path: str = f"{self.download_path}/{self.video_metadata.title}.{self.combo_video_format.currentText().lower()}"
            audio_path: str = f"{self.download_path}/{self.video_metadata.title}.{self.combo_audio_format.currentText().lower()}"

            audio_only: bool = True if self.tab_widget.currentWidget(
            ).objectName() == "audio_tab" else False

            # If the file is not already downloaded.
            if not os.path.exists(video_path) and not os.path.exists(audio_path):
                self.download_button.setEnabled(False)
                self.download_button.setText("Actualmente descargando...")
                # Create a download object.
                download = Download({
                    'url': url,
                    'format': self.combo_video_format.currentText(),
                    'quality': '',
                    'audio_only': audio_only,
                    'download_path': audio_path if audio_only else video_path
                })
                # Create a worker object.
                self.worker = DownloadWorker(download)
                # Connect worker signals and slots with UI.
                self.worker.progress.connect(self.update_progress_bar)
                self.worker.progress.connect(self.update_status_bar)
                self.worker.speed.connect(self.update_speed_lbl)
                self.worker.d_finished.connect(self.on_download_finished)
                # Start the worker.
                self.worker.start()
            else:
                QMessageBox.information(
                    self,
                    "Vídeo ya descargado",
                    "El vídeo o audio ya está descargado."
                )

        except Exception as e:
            print(traceback.format_exc())
            QMessageBox.information(
                self,
                "Enlace no válido",
                "El enlace introducido no es válido o no se pudo recopilar."
            )

    def get_video_metadata(self) -> bool:
        try:
            success: bool = True
            self.download_button.setEnabled(False)
            self.status_bar.showMessage(self.tr("Obteniendo metadatos..."), -1)
            self.meta_worker = MetaWorker(self.url_input.text())
            self.meta_worker.finished.connect(self.on_meta_worker_finished)
            self.meta_worker.start()
        except Exception as e:
            success = False
            print(e)

        return success

    @staticmethod
    def is_valid_yt(url: str) -> bool:
        yt_regex = r'^(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.+$'
        return re.match(yt_regex, url) is not None

    def update_progress_bar(self, value):
        self.progress_bar.setValue(value)

    def update_status_bar(self, value):
        self.status_bar.showMessage(
            f"Descargando {self.video_metadata.title} - {value}%"
        )

    def update_speed_lbl(self, value):
        # self.speed_label.setText(f"Velocidad: {size(value, system=si)}B/s")
        pass

    def populate_format_combo_box(self, combo_box: QComboBox, formats: list) -> None:
        if not combo_box.isEnabled():
            combo_box.setEnabled(True)

        if not formats:
            return

        combo_box.clear()
        combo_box.addItems(formats)

    def on_url_input_finished(self) -> None:
        if not self.is_valid_yt(self.url_input.text()):
            self.status_bar.showMessage(
                self.tr("Por favor, introduce una URL de YouTube válida."),
                3000
            )
            return

        if self.video_metadata and self.video_metadata.original_url == self.url_input.text():
            self.status_bar.showMessage(
                self.tr("Por favor, introduce una URL diferente."),
                3000
            )
            return

        self.get_video_metadata()

    def on_meta_worker_finished(self, value: VideoMetadata) -> None:
        self.video_metadata = value
        self.status_bar.clearMessage()
        self.populate_format_combo_box(
            self.combo_video_format,
            self.video_metadata.formats["video_formats"]
        )
        self.populate_format_combo_box(
            self.combo_audio_format,
            self.video_metadata.formats["audio_formats"]
        )
        if self.video_metadata:
            self.download_button.setEnabled(True)

    def on_download_finished(self) -> None:
        self.download_button.setEnabled(True)
        self.download_button.setText(self.tr("Descargar"))
        self.status_bar.showMessage(self.tr("Descarga completada."), 3000)
        self.progress_bar.setValue(0)
        QMessageBox.information(
            self,
            self.tr("Descarga completada."),
            self.tr(
                f"Se ha completado la descarga de {self.video_metadata.title}.{self.combo_video_format.currentText().lower()}"
            )
        )

    def on_restart(self) -> None:
        self.close()
        subprocess.Popen([sys.executable, "./main.py"])
        os.system('cls' if os.name == 'nt' else 'clear')

    # Event called when trying to exit the program.
    def closeEvent(self, event) -> None:
        self.save_settings()
        event.accept()


def main():
    app = QApplication(sys.argv)
    translator = QTranslator()
    translator.load("qtbase_" + QLocale.system().name(),
                    QLibraryInfo.path(QLibraryInfo.TranslationsPath))
    app.installTranslator(translator)

    gui = MainWindow()
    gui.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
