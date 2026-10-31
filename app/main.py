import sys

from PySide6.QtCore import QLibraryInfo, QLocale, QTranslator
from PySide6.QtWidgets import QApplication

from constants import APP_NAME, VERSION
from src.windows.main_window import MainWindow

APP_LOCALE = QLocale(QLocale.Language.Spanish)


def install_qt_translations(app: QApplication) -> None:
    translator = QTranslator(app)
    translations_path = QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath)
    if translator.load(APP_LOCALE, "qtbase", "_", translations_path):
        app.installTranslator(translator)


def main() -> None:
    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    app.setApplicationVersion(VERSION)
    install_qt_translations(app)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
