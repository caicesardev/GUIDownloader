import yt_dlp  # type: ignore

from typing import Any
from constants import APP_NAME
from src.models.download import Download
from PySide6.QtCore import (
    Signal,
    QThread,
    QSettings,
)


class DownloadWorker(QThread):

    """
    Class that represents a download worker.

    Attributes:
        finished (Signal): Signal that emits when the download is finished.
        d_finished (Signal): Signal that emits when the download is finished.
        progress (Signal): Signal that emits the download progress.
        speed (Signal): Signal that emits the download speed.
        is_running (Signal): Signal that emits when the download is running.
    """

    # Signals
    finished = Signal()
    d_finished = Signal()
    progress = Signal(int)
    speed = Signal(float)
    is_running = Signal()

    def __init__(self, download: Download) -> None:
        """
        Constructor.

        Args:
            download (Download): Download object
        """
        super(DownloadWorker, self).__init__()
        self.download: Download = download
        self.ffmpeg_path = QSettings(APP_NAME, "ffmpeg_path")

    def run(self) -> None:
        url: str = self.download.get_url()
        audio_only: bool = self.download.get_audio_only()
        user_format: str = self.download.get_format()
        ydl_opts: dict[str, Any] = {}

        if not url:
            self.d_finished.emit()
            return

        if audio_only:
            if user_format == "mp4":
                preferred_codec = "aac"
            else:
                preferred_codec = user_format

            ydl_opts = {
                "format": "bestaudio/best",
                "ffmpeg_location": self.ffmpeg_path,
                "postprocessors": [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": preferred_codec,
                    "preferredquality": self.download.get_quality(),
                }],
                "progress_hooks": [self.progress_hook],
                "outtmpl": f"{self.download.get_download_path()}/%(title)s.%(ext)s"
            }
        else:
            ydl_opts = {
                "ffmpeg_location": self.ffmpeg_path,
                "format": f"bestvideo+bestaudio[ext={user_format}]/best",
                "merge_output_format": user_format,
                "progress_hooks": [self.progress_hook],
                "outtmpl": f"{self.download.get_download_path()}/%(title)s.%(ext)s"
            }

        if not ydl_opts:
            self.d_finished.emit()
            return

        with yt_dlp.YoutubeDL(ydl_opts) as ytdl:
            ytdl.download([url])  # type:ignore

        self.d_finished.emit()

    def cancel(self) -> None:
        self.terminate()
        self.finished.emit()

    def progress_hook(self, response: dict[str, Any]):
        if response["status"] == "downloading":
            speed: Any = response["speed"]
            downloaded_percent = (
                response["downloaded_bytes"] * 100) / response["total_bytes"]
            self.progress.emit(downloaded_percent)
            self.speed.emit(speed)
