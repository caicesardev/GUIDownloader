import sys
import os
import subprocess
import getpass
import yt_dlp

from ui.ui_MainWindow import Ui_MainWindow
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
    QGraphicsDropShadowEffect,
)

__version__ = "1.0.0"


# Worker class.
class Worker(QThread):
    finished = Signal()
    d_finished = Signal()
    progress = Signal(int)
    speed = Signal(float)
    is_running = Signal()

    def __init__(self, url="", frmat="", quality="", audio_only=""):
        super(Worker, self).__init__()

        self.url = url
        self.format = frmat.lower()
        self.quality = quality.lower()
        self.audio_only = audio_only
        self.is_running = True
        self.username = getpass.getuser()

    def run(self):
        windows_dir = f"C:/users/{self.username}/Downloads/GUIDownloader/%(title)s.%(ext)s"
        linux_dir = f"/home/{self.username}/Downloads/GUIDownloader/%(title)s.%(ext)s"
        ffmpeg = "./ffmpeg/bin/ffmpeg.exe"
        print(self.format)
        # Audio only.
        if self.audio_only:
            self.ydl_opts = {
                "format": "bestaudio/best",
                "ffmpeg_location": ffmpeg,
                "postprocessors": [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": self.format,
                    "preferredquality": self.quality,
                }],
                "progress_hooks": [self.callable_hook],
                "outtmpl": windows_dir if os.name == "nt" else linux_dir
            }
        # Video
        else:
            self.ydl_opts = {
                "ffmpeg_location": ffmpeg,
                "postprocessors": [{
                    "key": "FFmpegVideoConvertor",
                    "preferedformat": self.format,
                }],
                "progress_hooks": [self.callable_hook],
                "outtmpl": windows_dir if os.name == "nt" else linux_dir
            }
        with yt_dlp.YoutubeDL(self.ydl_opts) as self.ytdl:
            self.ytdl.download([self.url])

        self.d_finished.emit()

    def cancel(self):
        print("\n--> Stopping and terminating thread...")

        self.terminate()
        self.finished.emit()

        print("--> Worker Thread stopped and killed <--")

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

        # Get app settings.
        self.get_settings()

        # Set app settings.
        self.set_settings()

        # Download button.
        self.download_button.clicked.connect(self.download)

    def init_ui(self):
        self.setupUi(self)

        # Shadows
        self.shadow = QGraphicsDropShadowEffect(blurRadius=35)
        self.header_frame.setGraphicsEffect(self.shadow)
        self.shadow2 = QGraphicsDropShadowEffect(
            blurRadius=40,
            color="#cfcfcf")
        self.container_frame.setGraphicsEffect(self.shadow2)

        # Menu buttons
        self.about_menu_action.clicked.connect(About)
        self.aboutqt_menu_action.clicked.connect(QApplication.aboutQt)
        self.restart_menu_action.clicked.connect(self.on_restart)
        self.exit_menu_action.clicked.connect(self.close)
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

        # On video radio button clicked.
        self.vid_radio_btn.toggled.connect(self.on_vid_radio_toggled)
        # On audio radio button clicked.
        self.audio_radio_btn.toggled.connect(self.on_audio_radio_toggled)

        self.status_bar.showMessage("Bienvenido", 5000)

    def get_settings(self):
        self.w_attrib = QSettings("GUIDownloader", "WindowAttributes")
        self.preferences = QSettings("GUIDownloader", "Preferences")

    def set_settings(self):
        # Initial window size/pos last saved. Use default values for first time.
        self.resize(self.w_attrib.value("size", QSize(270, 225)))
        self.move(self.w_attrib.value("pos", QPoint(50, 50)))

        # User's last downlaod preference.
        if self.preferences.value("DownloadVideo", "true") == "true":
            self.vid_radio_btn.setChecked(True)
            self.audio_tab.setEnabled(False)
        if self.preferences.value("DownloadAudio", "false") == "true":
            self.audio_radio_btn.setChecked(True)
            self.audio_tab.setEnabled(True)

        # Set user's last input default to 1.
        self.vf_combo_box.setCurrentIndex(
            self.preferences.value("VideoFormat", 0))
        self.vq_combo_box.setCurrentIndex(
            self.preferences.value("VideoQuality", 0))
        self.af_combo_box.setCurrentIndex(
            self.preferences.value("AudioFormat", 0))
        self.aq_combo_box.setCurrentIndex(
            self.preferences.value("AudioQuality", 0))

    def download(self):
        """

        Formats Available: 

        # These will be the selectable formats. 

        -->     Video      <--

        MP4 | WEBM | MKV | AVI

        -->     Audio     <--

        MP3 | M4A | WAV | OGG

        """

        try:
            self.username = getpass.getuser()

            with yt_dlp.YoutubeDL({}) as ydl:
                meta = ydl.extract_info(
                    self.input.text(),
                    download=False)
            self.vid_title = meta['title']

            # https://www.youtube.com/watch?v=dP15zlyra3c <- For testings

            if self.vid_radio_btn.isChecked():
                frmat = self.vf_combo_box.currentText()
                quality = self.vq_combo_box.currentText()
                audio_only = False

                win_path = f"C:/users/{self.username}/Downloads/GUIDownloader/{self.vid_title}.{self.vf_combo_box.currentText().lower()}"
                lin_path = f"/home/{self.username}/Downloads/GUIDownloader/{self.vid_title}.{self.vf_combo_box.currentText().lower()}"

            if self.audio_radio_btn.isChecked():
                frmat = self.af_combo_box.currentText()
                quality = self.aq_combo_box.currentText()
                audio_only = True

                win_path = f"C:/users/{self.username}/Downloads/GUIDownloader/{self.vid_title}.{self.af_combo_box.currentText().lower()}"
                lin_path = f"/home/{self.username}/Downloads/GUIDownloader/{self.vid_title}.{self.af_combo_box.currentText().lower()}"

            print(f"\nFormat: {frmat} \nQuality: {quality}\n")

            # If the file is not yet downloaded.
            if not os.path.exists(win_path) or os.path.exists(lin_path):
                self.download_button.setEnabled(False)
                self.download_button.setText("Actualmente descargando...")
                self.cancel_button.setEnabled(True)

                # Create a worker object.
                self.worker = Worker(url=self.input.text(),
                                     frmat=frmat,
                                     quality=quality,
                                     audio_only=audio_only)
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

        except Exception as e:
            print(f"--> Download Error <-- \n{e}")
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

    def on_vid_radio_toggled(self, enabled):
        if enabled:
            self.tab_widget.setCurrentIndex(0)
            self.video_tab.setEnabled(True)
            self.audio_tab.setEnabled(False)

    def on_audio_radio_toggled(self, enabled):
        if enabled:
            self.tab_widget.setCurrentIndex(1)
            self.audio_tab.setEnabled(True)
            self.video_tab.setEnabled(False)

    def update_progress_bar(self, value):
        self.progress_bar.setValue(value)

    def update_status_bar(self, value):
        self.status_bar.showMessage(
            f"Descargando {self.vid_title} || {value}%")

    def update_speed_lbl(self, value):
        self.speed_label.setText(f"Velocidad: {size(value, system=si)}B/s")

    def on_download_finished(self):
        self.status_bar.showMessage("Descarga finalizada", 3000)
        self.progress_bar.setValue(0)
        self.speed_label.clear()
        self.cancel_button.setEnabled(False)
        self.download_button.setText("Descargar")
        self.download_button.setEnabled(True)
        if self.vid_radio_btn.isChecked():
            frmat = self.vf_combo_box.currentText().lower()
        if self.audio_radio_btn.isChecked():
            frmat = self.af_combo_box.currentText().lower()
        QMessageBox.information(
            self,
            "Descarga completada",
            f"Se ha completado la descarga de {self.vid_title}.{frmat}")

    def on_restart(self):
        self.close()
        subprocess.Popen([sys.executable, "./main.py"])
        os.system('cls' if os.name == 'nt' else 'clear')

    # Event that is called when trying to exit the program.
    def closeEvent(self, event) -> None:
        # Remember window postion and size on exit.
        self.w_attrib.setValue("size", self.size())
        self.w_attrib.setValue("pos", self.pos())
        # Remember user's last input.
        self.preferences.setValue(
            "DownloadVideo", self.vid_radio_btn.isChecked())
        self.preferences.setValue(
            "DownloadAudio", self.audio_radio_btn.isChecked())
        self.preferences.setValue(
            "VideoFormat", self.vf_combo_box.currentIndex())
        self.preferences.setValue(
            "VideoQuality", self.vq_combo_box.currentIndex())
        self.preferences.setValue(
            "AudioFormat", self.af_combo_box.currentIndex())
        self.preferences.setValue(
            "AudioQuality", self.aq_combo_box.currentIndex())


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
