from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class VideoMetadata:
    video_id: str = field(default="")
    title: str = field(default="")
    fulltitle: str = field(default="")
    description: str = field(default="")
    thumbnail: str = field(default="")
    duration: int = field(default=0)
    duration_string: str = field(default="")
    view_count: int = field(default=0)
    like_count: int = field(default=0)
    channel: str = field(default="")
    channel_url: str = field(default="")
    channel_is_verified: bool = False
    comment_count: int = field(default=0)
    webpage_url: str = field(default="")
    original_url: str = field(default="")
    uploader: str = field(default="")
    uploader_id: str = field(default="")
    uploader_icon: str = field(default="")
    upload_date: str = field(default="")
    uploader_subscribers: int = field(default=0)
    uploader_description: str = field(default="")
    uploader_video_count: int = field(default=0)
    uploader_channel_count: int = field(default=0)
    channel_follower_count: int = field(default=0)
    uploader_subscriber_count: int = field(default=0)
    # Dictionary to store formats (video/audio)
    formats: Dict[str, List[str]] = field(default_factory=lambda: {})

    def set_video_formats(self, video_formats: List[str]) -> None:
        self.formats["video_formats"] = video_formats

    def set_audio_formats(self, audio_formats: List[str]) -> None:
        self.formats["audio_formats"] = audio_formats
