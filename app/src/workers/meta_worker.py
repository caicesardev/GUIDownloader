import yt_dlp

from typing import Any, List, Dict
from src.models.video_metadata import VideoMetadata
from PySide6.QtCore import (
    Signal,
    QThread,
)


class MetaWorker(QThread):
    """
    Class that represents a meta worker. This worker is used to 
    extract metadata from a video asynchronously.
    """

    # Signals
    finished = Signal(VideoMetadata)
    video_formats = Signal(list)
    audio_formats = Signal(list)

    def __init__(self, url: str, key: str = "metadata") -> None:
        """
        Constructor.
        """
        super(MetaWorker, self).__init__()
        self.url: str = url
        self.key: str = key
        self.metadata: VideoMetadata
        self.formats: Dict[str, List[str]] = {
            "video_formats": [], "audio_formats": []
        }

    def run(self) -> None:
        if not self.url:
            self.finished.emit(self.metadata)
            return

        ydl_opts: Dict[str, Any] = {
            "format": "all",
            "noplaylist": True,
            "quiet": True,
            "no_warnings": True,
            "skip_download": True,
        }

        meta_dict = {}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            meta_dict = ydl.extract_info(self.url, download=False)
            self.metadata = meta_dict.get(self.key, {})  # type: ignore
            self.formats = self.extract_formats(meta_dict.get("formats", []))
            self.metadata = self.extract_metadata(meta_dict)

        # TODO: DEBUG. Delete this
        with open("metadata.txt", "w", encoding="utf-8") as f:
            f.write(meta_dict.__str__())

        # Emit the metadata and formats/qualities
        self.finished.emit(self.metadata)
        self.video_formats.emit(self.formats["video_formats"])
        self.audio_formats.emit(self.formats["audio_formats"])

    def extract_formats(self, formats: List[Dict[str, Any]]) -> Dict[str, List[str]]:
        """
        Extract available video and audio formats from metadata.
        """
        video_formats: set[str] = set()
        audio_formats: set[str] = set()

        for fmt in formats:
            ext: str = ''
            if fmt.get("vcodec") != "none":  # Video format
                ext = fmt.get("ext", "")
                video_formats.add(ext)
            if fmt.get("acodec") != "none":  # Audio format
                ext = fmt.get("ext", "")
                audio_formats.add(ext)

        return {
            "video_formats": sorted(video_formats),
            "audio_formats": sorted(audio_formats),
        }

    def extract_metadata(self, meta_dict: Dict[str, Any]) -> VideoMetadata:
        """
        Extract video metadata from the dictionary.
        """
        return VideoMetadata(
            video_id=meta_dict.get("id", ""),
            title=meta_dict.get("title", ""),
            fulltitle=meta_dict.get("fulltitle", ""),
            description=meta_dict.get("description", ""),
            thumbnail=meta_dict.get("thumbnail", ""),
            duration=meta_dict.get("duration", 0),
            duration_string=meta_dict.get("duration_string", 0),
            view_count=meta_dict.get("view_count", 0),
            like_count=meta_dict.get("like_count", 0),
            channel=meta_dict.get("channel", ""),
            channel_url=meta_dict.get("channel_url", ""),
            channel_is_verified=meta_dict.get("channel_is_verified", ""),
            comment_count=meta_dict.get("comment_count", ""),
            webpage_url=meta_dict.get("webpage_url", ""),
            original_url=meta_dict.get("original_url", ""),
            uploader=meta_dict.get("uploader", ""),
            uploader_id=meta_dict.get("uploader_id", ""),
            uploader_icon=meta_dict.get("uploader_icon", ""),
            upload_date=meta_dict.get("upload_date", ""),
            uploader_subscribers=meta_dict.get("uploader_subscriber_count", 0),
            uploader_description=meta_dict.get("uploader_description", ""),
            uploader_video_count=meta_dict.get("uploader_video_count", 0),
            uploader_channel_count=meta_dict.get("uploader_channel_count", 0),
            channel_follower_count=meta_dict.get("channel_follower_count", 0),
            uploader_subscriber_count=meta_dict.get(
                "uploader_subscriber_count", 0),
            formats=self.formats
        )
