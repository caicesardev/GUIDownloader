import sys

from ui.Settings_ui import Ui_Settings
from constants import APP_NAME
from pathlib import Path

from PySide6.QtCore import QSettings
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QFileDialog,
    QLineEdit
)


class SettingsWindow(QDialog, Ui_Settings):
    def __init__(self, parent=None):
        super(SettingsWindow, self).__init__()

        self.parent = parent  # type: ignore

        self.init_ui()
        self.get_settings()
        self.set_settings()
        self.exec()

    def init_ui(self):
        self.setupUi(self)
        self.open_btn.clicked.connect(
            lambda: self.open_folder(self.path_edit))
        self.open_ffmpeg_path.clicked.connect(
            lambda: self.open_folder(self.ffmpeg_path_edit))

    def open_folder(self, widget: QLineEdit) -> bool:
        path = QFileDialog.getExistingDirectory(
            self,
            self.tr("Abrir carpeta"),
            widget.text()
        )

        if path == "":
            return False

        widget.setText(path)

        return True

    def get_settings(self) -> None:
        self.preferences = QSettings(APP_NAME, "Preferences")

    def set_settings(self) -> None:
        self.path_edit.setText(
            str(
                self.preferences.value(
                    "download_path",
                    str(Path.home() / "Downloads")
                )
            )
        )

        self.ffmpeg_path_edit.setText(
            str(
                self.preferences.value(
                    "ffmpeg_path"
                )
            )
        )

    def closeEvent(self, event) -> None:
        self.preferences.setValue("download_path", self.path_edit.text())
        self.preferences.setValue("ffmpeg_path", self.ffmpeg_path_edit.text())
        event.accept()


def main():
    app = QApplication(sys.argv)
    gui = SettingsWindow()
    gui.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
