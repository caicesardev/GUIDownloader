import sys

from src.windows.main_window import MainWindow
from PySide6.QtCore import (
    QCoreApplication,
    QLocale,
    QTranslator,
)
from PySide6.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    translator = QTranslator()
    if translator.load(QLocale(), "", "", ":/app/i18n"):
        QCoreApplication.installTranslator(translator)
    app.installTranslator(translator)

    gui = MainWindow()
    gui.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
