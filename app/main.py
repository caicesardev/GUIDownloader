from importlib.resources import path
import sys
import os
import subprocess
import yt_dlp

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
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMenu,
    QMessageBox,
    QStyle
)

__version__ = "1.0.0"


# Worker class.
class Worker(QThread):
    finished = Signal()
    d_finished = Signal()
    progress = Signal(int)
    speed = Signal(float)
    is_running = Signal()

    def __init__(self, url=""):
        super(Worker, self).__init__()

        self.url = url
        self.resuming = False
        self.is_running = True
        self.username = os.getlogin()

    def run(self):
        windows_dir = f"C:/users/{self.username}/Downloads/GUIDownloader/%(title)s.%(ext)s"
        linux_dir = "/home/downloads/%(title)%s.%(ext)s"
        self.ydl_opts = {
            "progress_hooks": [self.callable_hook],
            "outtmpl": windows_dir if os.name == "nt" else linux_dir
        }

        with yt_dlp.YoutubeDL(self.ydl_opts) as self.ytdl:
            print("\n--> is_running from with:", self.is_running)
            self.ytdl.download([self.url])

        self.d_finished.emit()

    def cancel(self):
        print("--> Stopping and terminating thread...")

        self.terminate()
        self.finished.emit()

        print("--> Worker Thread stopped and killed. <--")

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

        # self.input.returnPressed.connect(
        #    lambda: self.update_menu_stream(self.input.text()))

        # Download button.
        self.download_button.clicked.connect(self.download)

    def init_ui(self):
        self.setupUi(self)

        # Menu buttons
        self.about_menu_action.triggered.connect(About)
        self.aboutqt_menu_action.triggered.connect(QApplication.aboutQt)
        self.restart_menu_action.triggered.connect(self.on_restart)
        self.exit_menu_action.triggered.connect(sys.exit)
        self.cancel_button.clicked.connect(self.cancel_download)

        self.worker = Worker()

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

    def download(self):
        try:
            self.yt = YouTube(self.input.text())
            self.username = os.getlogin()

            # https://www.youtube.com/watch?v=dP15zlyra3c <- For testings

            path = f"C:/users/{self.username}/Downloads/{self.yt.title}.mp4"
            # If the file is not yet downloaded.
            if not os.path.exists(path):
                self.download_button.setEnabled(False)
                self.download_button.setText("Actualmente descargando...")
                self.cancel_button.setEnabled(True)

                # Create a worker object.
                self.worker = Worker(url=self.input.text())
                self.worker.progress.connect(self.update_progress_bar)
                self.worker.progress.connect(self.update_status_bar)
                self.worker.speed.connect(self.update_speed_lbl)
                # Connect signals and slots
                self.worker.d_finished.connect(self.on_download_finished)

                self.worker.start()

            else:
                QMessageBox.information(
                    self,
                    "Vídeo ya descargado",
                    "El vídeo ya está descargado.")

        except Exception:
            self.download_button.setEnabled(True)
            self.download_button.setText("Descargar")
            self.cancel_button.setEnabled(False)
            QMessageBox.information(
                self,
                "Enlace no válido",
                "El enlace introducido no es válido o no se pudo recopilar.")

    def cancel_download(self):
        answer = QMessageBox.question(
            self,
            "Confirmar cancelación de la descarga",
            "¿Estás seguro de que quieres cancelar la descarga?")
        if answer == QMessageBox.Yes:
            self.worker.cancel()
            self.status_bar.showMessage("Descarga cancelada", 3000)
            self.progress_bar.setValue(0)
            self.speed_label.clear()
            self.cancel_button.setEnabled(False)
            self.download_button.setText("Descargar")
            self.download_button.setEnabled(True)

    def update_progress_bar(self, value):
        self.progress_bar.setValue(value)

    def update_status_bar(self, value):
        self.status_bar.showMessage(f"Descargando {self.yt.title} || {value}%")

    def update_speed_lbl(self, value):
        self.speed_label.setText(f"Velocidad: {size(value, system=si)}B/s")

    def on_download_finished(self):
        self.status_bar.showMessage("Descarga finalizada", 3000)
        self.progress_bar.setValue(0)
        self.speed_label.clear()
        self.cancel_button.setEnabled(False)
        QMessageBox.information(
            self,
            "Descarga completada",
            f"Se ha completado la descarga de {self.yt.title}.mp4")
        self.download_button.setText("Descargar")
        self.download_button.setEnabled(True)

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
