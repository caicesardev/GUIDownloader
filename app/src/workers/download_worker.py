from pathlib import Path
from typing import Any

import yt_dlp
from PySide6.QtCore import QThread, Signal
from yt_dlp.utils import DownloadCancelled, YoutubeDLError

from src.models.download_request import DownloadRequest
from src.services.ydl_options import describe_error
from src.utils.formatting import format_bytes, format_duration

OUTPUT_TEMPLATE = "%(title)s.%(ext)s"
NO_CODEC = "none"
POSTPROCESSOR_MESSAGES = {
    "Merger": "Uniendo vídeo y audio…",
    "ExtractAudio": "Convirtiendo audio…",
}
DEFAULT_POSTPROCESSOR_MESSAGE = "Procesando…"


class DownloadWorker(QThread):
    progress_changed = Signal(int)
    status_changed = Signal(str)
    completed = Signal(str)
    failed = Signal(str)
    cancelled = Signal()
    cancellable_changed = Signal(bool)

    def __init__(self, request: DownloadRequest, ydl_options: dict[str, Any]) -> None:
        super().__init__()
        self._request = request
        self._ydl_options = ydl_options
        self._cancel_requested = False
        self._partial_files: set[Path] = set()

    def request_cancel(self) -> None:
        self._cancel_requested = True

    def run(self) -> None:
        try:
            with yt_dlp.YoutubeDL(self._download_options()) as ydl:
                info = ydl.extract_info(self._request.url, download=True)
        except DownloadCancelled:
            self._remove_partial_files()
            self.cancelled.emit()
            return
        except YoutubeDLError as error:
            self.failed.emit(describe_error(error))
            return
        self.completed.emit(self._final_filepath(info))

    def _download_options(self) -> dict[str, Any]:
        return {
            **self._ydl_options,
            **self._request.ydl_options(),
            "paths": {"home": str(self._request.destination)},
            "outtmpl": OUTPUT_TEMPLATE,
            "progress_hooks": [self._on_progress],
            "postprocessor_hooks": [self._on_postprocessing],
        }

    def _on_progress(self, progress: dict[str, Any]) -> None:
        if self._cancel_requested:
            raise DownloadCancelled()
        if progress["status"] != "downloading":
            return
        self._partial_files.add(Path(progress["tmpfilename"]))
        self.cancellable_changed.emit(True)
        total_bytes = progress.get("total_bytes") or progress.get("total_bytes_estimate")
        if total_bytes:
            self.progress_changed.emit(int(progress["downloaded_bytes"] * 100 / total_bytes))
        self.status_changed.emit(self._describe_progress(progress))

    def _on_postprocessing(self, progress: dict[str, Any]) -> None:
        if progress["status"] == "started":
            self.cancellable_changed.emit(False)
            message = POSTPROCESSOR_MESSAGES.get(progress["postprocessor"], DEFAULT_POSTPROCESSOR_MESSAGE)
            self.status_changed.emit(message)

    @staticmethod
    def _describe_progress(progress: dict[str, Any]) -> str:
        stream = progress.get("info_dict", {})
        stream_kind = "vídeo" if stream.get("vcodec", NO_CODEC) != NO_CODEC else "audio"
        details = [f"Descargando {stream_kind}"]
        if speed := progress.get("speed"):
            details.append(f"{format_bytes(speed)}/s")
        if eta := progress.get("eta"):
            details.append(f"quedan {format_duration(eta)}")
        return " · ".join(details)

    def _remove_partial_files(self) -> None:
        for partial_file in self._partial_files:
            partial_file.unlink(missing_ok=True)

    @staticmethod
    def _final_filepath(info: dict[str, Any]) -> str:
        downloads = info.get("requested_downloads") or [{}]
        return downloads[-1].get("filepath", "")
