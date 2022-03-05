import sys
import os
import subprocess
import youtube_dl

from ui.ui_MainWindow import Ui_MainWindow
from about import About

from pytube import YouTube
from hurry.filesize import size, si

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
    speed = Signal(float)

    def __init__(self, url):
        super(Worker, self).__init__()

        self.url = url

    def run(self):
        windows_dir = "C:/users/%username%/Downloads/%(title)s.%(ext)s"
        linux_dir = "/home/downloads/%(title)%s.%(ext)s"
        ydl_opts = {
            "progress_hooks": [self.callable_hook],
            'outtmpl': windows_dir if os.name == "nt" else linux_dir
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.url])
        self.finished.emit()

    def callable_hook(self, response):
        if response["status"] == "downloading":
            speed = response["speed"]
            downloaded_percent = (
                response["downloaded_bytes"]*100)/response["total_bytes"]
            self.progress.emit(downloaded_percent)
            self.speed.emit(speed)


# MainWindow.
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.init_ui()

        self.input.editingFinished.connect(
            self.handle_editing_finished)

        # self.input.returnPressed.connect(
        #    lambda: self.update_menu_stream(self.input.text()))

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
            self.yt = YouTube(self.input.text())

            # https://www.youtube.com/watch?v=dP15zlyra3c <- For testings

            self.download_button.setEnabled(False)
            self.download_button.setText("Actualmente descargando...")

            # Create a QThread object.
            self.thread = QThread()
            # Create a worker object.
            self.worker = Worker(self.input.text())
            # Move worker to the thread.
            self.worker.moveToThread(self.thread)
            # Connect signals and slots
            self.thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.on_download_finished)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)

            self.worker.progress.connect(self.update_progress_bar)
            self.worker.progress.connect(self.update_status_bar)
            self.worker.speed.connect(self.update_speed_lbl)

            self.thread.start()

        except Exception:
            self.download_button.setEnabled(True)
            self.download_button.setText("Descargar")
            QMessageBox.information(
                self,
                "Enlace no válido",
                "El enlace introducido no es válido o no se pudo recopilar.")

    def update_progress_bar(self, value):
        self.progress_bar.setValue(value)

    def update_status_bar(self, value):
        self.status_bar.showMessage(f"Descargando {self.yt.title} || {value}%")

    def update_speed_lbl(self, value):
        self.speed_label.setText(f"Velocidad: {size(value, system=si)}/s")

    def on_download_finished(self):
        self.status_bar.showMessage("Descarga finalizada", 3000)
        self.progress_bar.setValue(0)
        self.speed_label.clear()
        QMessageBox.information(
            self,
            "Descarga completada",
            f"Se ha completado la descarga de {self.yt.title}.mp4")
        self.download_button.setText("Descargar")
        self.download_button.setEnabled(True)

    def handle_editing_finished(self):
        if self.input.isModified():
            self.url = self.input.text()
            # self.update_menu_stream(self.url)
        self.input.setModified(False)

    """ 
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
    """

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
