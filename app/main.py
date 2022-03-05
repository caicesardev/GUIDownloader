import sys
import os
import subprocess
from ui.ui_MainWindow import Ui_MainWindow
from about import About

from pytube import YouTube

from PySide6.QtGui import QIcon
from PySide6.QtCore import (
    QLibraryInfo,
    QLocale,
    QObject,
    QTranslator,
    QThread,
    Signal,
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
    finished = Signal()
    progress = Signal(int)

    def __init__(self, url):
        super(Worker, self).__init__()

        print("Init")
        self.url = url
        self.yt = YouTube(self.url, on_progress_callback=self.report_progress)
        self.yv = self.yt.streams.get_highest_resolution()
        print("Finish init")

    def run(self):
        print("Downloading")
        self.yv.download("C:/users/Edu/Downloads")
        print("Finished download")
        self.finished.emit()

    def report_progress(self, stream, chunk, bytes_remaining):
        self.progress.emit(round((1-bytes_remaining/self.yv.filesize)*100, 3))
        print(round((1-bytes_remaining/self.yv.filesize)*100, 3), '% done...')


# MainWindow.
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.init_ui()

        self.input.editingFinished.connect(
            self.handle_editing_finished)

        self.input.returnPressed.connect(
            lambda: self.update_menu_stream(self.input.text()))

        # Download button.
        self.download_button.clicked.connect(self.download)

    def init_ui(self):
        self.setupUi(self)

        # Menu buttons
        self.about_menu_action.triggered.connect(About)
        self.restart_menu_action.triggered.connect(self.on_restart)
        self.exit_menu_action.triggered.connect(sys.exit)

        self.status_bar.showMessage("Bienvenido", 5000)

    def download(self):
        try:
            self.download_button.setEnabled(False)
            self.select_strm_button.setEnabled(False)
            self.download_button.setText("Actualmente descargando...")

            # YouTube downloader.
            self.url = self.input.text()
            self.yt = YouTube(self.url)
            self.status_bar.showMessage(f"Descargando {self.yt.title} || 0%")

            # Create a QThread object.
            self.thread = QThread()
            # Create a worker object.
            self.worker = Worker(self.url)
            # Move worker to the thread.
            self.worker.moveToThread(self.thread)
            # Connect signals and slots
            self.thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(
                lambda: self.on_download_finished(self.yt.title))
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)

            self.worker.progress.connect(self.update_progress_bar)
            self.worker.progress.connect(self.update_status_bar)

            self.thread.start()

        except Exception as e:
            print(e)
            QMessageBox.information(
                self,
                "Enlace no válido",
                "El enlace introducido no es válido o no se puede recopilar.")

    def update_progress_bar(self, value):
        self.progress_bar.setValue(value)

    def update_status_bar(self, value):
        self.status_bar.showMessage(f"Descargando {self.yt.title} || {value}%")

    def on_download_finished(self, f_name):
        self.status_bar.showMessage("Descarga finalizada", 3000)
        self.progress_bar.setValue(0)
        QMessageBox.information(
            self,
            "Descarga completada",
            f"Se ha completado la descarga de {f_name}.mp4")
        self.download_button.setText("Descargar")
        self.download_button.setEnabled(True)
        self.select_strm_button.setEnabled(True)

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
                f'{stream}',
                self.download)
        self.select_strm_button.setMenu(menu)

    def on_restart(self):
        self.close()
        subprocess.Popen([sys.executable, "./main.py"])
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
