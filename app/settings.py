import sys

from ui.Settings_ui import Ui_Settings
from pathlib import Path

from PySide6.QtCore import (
    QLibraryInfo,
    QLocale,
    QTranslator,
    QSettings,
)
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QFileDialog,
)


# Settings.
class Settings(QDialog, Ui_Settings):
    def __init__(self, parent=None):
        super(Settings, self).__init__()

        self.parent = parent

        self.init_ui()

        self.get_settings()
        self.set_settings()

        self.exec()

    def init_ui(self):
        self.setupUi(self)
        self.open_btn.clicked.connect(self.open_folder)

    def open_folder(self) -> None:
        self.path = QFileDialog.getExistingDirectory(
            self,
            self.tr("Abrir carpeta"),
            self.path_edit.text()
        )

        if self.path != '':
            self.path_edit.setText(self.path)

    def get_settings(self) -> None:
        self.preferences = QSettings("GUIDownloader", "Preferences")

    def set_settings(self) -> None:
        self.path_edit.setText(self.preferences.value(
            "download_path", str(Path.home() / "Downloads")))

    def closeEvent(self, event) -> None:
        self.preferences.setValue("download_path", self.path_edit.text())
        self.parent.download_path = self.path_edit.text()
        event.accept()


def main():
    app = QApplication(sys.argv)
    translator = QTranslator()
    translator.load("qtbase_" + QLocale.system().name(),
                    QLibraryInfo.location(QLibraryInfo.TranslationsPath))
    app.installTranslator(translator)

    gui = Settings()
    gui.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
