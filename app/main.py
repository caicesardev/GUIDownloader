import sys
from ui.ui_MainWindow import Ui_MainWindow

from pytube import YouTube

from PySide6.QtGui import QIcon
from PySide6.QtCore import (
    QLibraryInfo,
    QLocale,
    QObject,
    QTranslator,
)
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMenu,
    QMessageBox,
)

__version__ = "1.0.0"


# Worker class.
class Worker(QObject):
    def __init__(self):
        super(Worker, self).__init__()

    def run(self):
        ...


# MainWindow.
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setupUi(self)

        self.input.setText(
            "https://www.youtube.com/watch?v=x7X9w_GIm1s")  # borrar

        self.input.editingFinished.connect(
            self.handle_editing_finished)

        self.input.returnPressed.connect(
            lambda: self.update_menu_stream(self.input.text()))

        # Download button.
        self.download_button.clicked.connect(self.download)

    def download(self):
        try:
            # YouTube downloader.
            self.yt = YouTube(self.url)
            self.yt.streams.get_highest_resolution().download()
        except Exception as e:
            print(e)
            QMessageBox.information(
                self,
                "Enlace no válido",
                "El enlace introducido no es válido o no se puede recopilar.")

    def handle_editing_finished(self):
        if self.input.isModified():
            self.url = self.input.text()
            self.update_menu_stream(self.url)
        self.input.setModified(False)

    def update_menu_stream(self, url):
        # Streams menu.
        menu = QMenu(self)
        yt = YouTube(url)
        for stream in yt.streams:
            menu.addAction(
                QIcon("../res/images/downloading.png"),
                f'{stream}', self.download)
        self.select_strm_button.setMenu(menu)


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
