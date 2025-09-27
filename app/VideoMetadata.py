from dataclasses import dataclass
from typing import List, Dict


@dataclass
class VideoMetadata:
    """
    Dataclass to store video metadata.

    Attributes:
        title (str): Title of the video.
        description (str): Description of the video.
        thumbnail (str): URL of the thumbnail image.
        duration (int): Duration of the video in seconds.
        views (int): Number of views.
        uploader (str): Name of the uploader.
        uploader_url (str): URL of the uploader's channel.
        uploader_id (str): Unique identifier of the uploader.
        uploader_icon (str): URL of the uploader's icon image.
        uploader_subscribers (int): Number of subscribers of the uploader.
        uploader_description (str): Description of the uploader.
        uploader_video_count (int): Number of videos uploaded by the uploader.
        uploader_channel_count (int): Number of channels associated with the uploader.
        uploader_follower_count (int): Number of followers of the uploader.
        uploader_subscriber_count (int): Number of subscribers of the uploader.
        formats (dict): Available formats for video and audio.
    """
    video_id: str
    title: str
    fulltitle: str
    description: str
    thumbnail: str
    duration: int
    duration_string: str
    view_count: int
    like_count: int
    channel: str
    channel_url: str
    channel_is_verified: bool
    comment_count: int
    webpage_url: str
    original_url: str
    uploader: str
    uploader_id: str
    uploader_icon: str
    upload_date: str
    uploader_subscribers: int
    uploader_description: str
    uploader_video_count: int
    uploader_channel_count: int
    channel_follower_count: int
    uploader_subscriber_count: int
    formats: Dict[str, List[str]]  # Dictionary to store formats (video/audio)

    def set_video_formats(self, video_formats: List[str]) -> None:
        """
        Sets the available video formats.

        Args:
            video_formats (List[str]): List of available video formats.
        """
        self.formats["video_formats"] = video_formats

    def set_audio_formats(self, audio_formats: List[str]) -> None:
        """
        Sets the available audio formats.

        Args:
            audio_formats (List[str]): List of available audio formats.
        """
        self.formats["audio_formats"] = audio_formats
