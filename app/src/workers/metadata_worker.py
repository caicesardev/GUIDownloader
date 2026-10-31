from typing import Any

import yt_dlp
from PySide6.QtCore import QThread, Signal
from yt_dlp.utils import YoutubeDLError

from src.services.format_parser import parse_metadata
from src.services.ydl_options import describe_error


class MetadataWorker(QThread):
    metadata_ready = Signal(object)
    failed = Signal(str)

    def __init__(self, url: str, ydl_options: dict[str, Any]) -> None:
        super().__init__()
        self._url = url
        self._ydl_options = {**ydl_options, "skip_download": True}

    def run(self) -> None:
        try:
            with yt_dlp.YoutubeDL(self._ydl_options) as ydl:
                info = ydl.extract_info(self._url, download=False)
        except YoutubeDLError as error:
            self.failed.emit(describe_error(error))
            return
        self.metadata_ready.emit(parse_metadata(info))
