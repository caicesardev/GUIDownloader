from pathlib import Path

from PySide6.QtWidgets import QDialog, QFileDialog, QLineEdit, QWidget

from src.settings.preferences import Preferences
from ui.Settings_ui import Ui_Settings


class SettingsWindow(QDialog, Ui_Settings):
    def __init__(self, preferences: Preferences, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self._preferences = preferences
        self.path_edit.setText(str(preferences.download_directory))
        self.ffmpeg_path_edit.setText(preferences.ffmpeg_location)
        self._connect_signals()

    def _connect_signals(self) -> None:
        self.open_btn.clicked.connect(lambda: self._choose_directory(self.path_edit))
        self.open_ffmpeg_path.clicked.connect(lambda: self._choose_directory(self.ffmpeg_path_edit))
        self.path_edit.textChanged.connect(self._save_download_directory)
        self.ffmpeg_path_edit.textChanged.connect(self._save_ffmpeg_location)

    def _choose_directory(self, target: QLineEdit) -> None:
        directory = QFileDialog.getExistingDirectory(self, "Seleccionar carpeta", target.text())
        if directory:
            target.setText(str(Path(directory)))

    def _save_download_directory(self, directory: str) -> None:
        self._preferences.download_directory = Path(directory)

    def _save_ffmpeg_location(self, location: str) -> None:
        self._preferences.ffmpeg_location = location
