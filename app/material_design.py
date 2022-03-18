import sys
import os
import subprocess
import getpass
import yt_dlp

from ui.ui_MaterialMainWindow import Ui_MainWindow
from about import About

from hurry.filesize import size, si
from PySide6.QtCore import (
    QSettings,
    QSize,
    QPoint,
    QLibraryInfo,
    QLocale,
    QTranslator,
    QThread,
    Signal,
)
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QStyle,
    QGraphicsDropShadowEffect
)

__version__ = "1.0.0"


# MainWindow.
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.setupUi(self)

        # Header buttons
        self.about_menu_action.clicked.connect(About)
        self.aboutqt_menu_action.clicked.connect(QApplication.aboutQt)
        self.restart_menu_action.clicked.connect(self.on_restart)
        self.exit_menu_action.clicked.connect(self.close)

        pixmap = QStyle.SP_TitleBarMenuButton
        icon = self.style().standardIcon(pixmap)
        self.aboutqt_menu_action.setIcon(QIcon(icon))

        pixmap2 = QStyle.SP_MessageBoxQuestion
        icon2 = self.style().standardIcon(pixmap2)
        self.about_menu_action.setIcon(QIcon(icon2))

        pixmap3 = QStyle.SP_BrowserReload
        icon3 = self.style().standardIcon(pixmap3)
        self.restart_menu_action.setIcon(QIcon(icon3))

        pixmap4 = QStyle.SP_ArrowLeft
        icon4 = self.style().standardIcon(pixmap4)
        self.exit_menu_action.setIcon(QIcon(icon4))

        pixmap5 = QStyle.SP_DialogCancelButton
        icon5 = self.style().standardIcon(pixmap5)
        self.cancel_button.setIcon(QIcon(icon5))

        self.status_bar.showMessage("Bienvenido", 5000)

    def on_restart(self):
        self.close()
        subprocess.Popen([sys.executable, "./material_design.py"])
        os.system('cls' if os.name == 'nt' else 'clear')


def main():
    app = QApplication(sys.argv)
    translator = QTranslator()
    translator.load("qtbase_" + QLocale.system().name(),
                    QLibraryInfo.location(QLibraryInfo.TranslationsPath))
    app.installTranslator(translator)

    gui = MainWindow()
    gui.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
