from dataclasses import dataclass

from src.models.media_format import AudioFormat, VideoFormat
from src.utils.formatting import format_duration


@dataclass(frozen=True)
class VideoMetadata:
    url: str
    title: str
    channel: str
    duration: int
    video_formats: tuple[VideoFormat, ...]
    audio_formats: tuple[AudioFormat, ...]

    @property
    def has_formats(self) -> bool:
        return bool(self.video_formats or self.audio_formats)

    @property
    def summary(self) -> str:
        details = [self.channel] if self.channel else []
        if self.duration:
            details.append(format_duration(self.duration))
        return f"{self.title}\n{' · '.join(details)}"
