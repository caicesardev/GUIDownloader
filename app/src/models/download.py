from typing import Any


class Download:

    """
    Class that represents a download.

    Attributes:
        url (str): The url of the download.
        format (str): The format of the download.
        quality (str): The quality of the download.
        audio_only (bool): Whether the download is audio only or not.
        download_path (str): The path where the download will be saved.
    """

    def __init__(self, options: dict[str, Any]) -> None:
        """
        Constructor.

        Args:
            options (dict): {
                    url:str
                    format:str
                    quality:str
                    audio_only:bool
                    download_path:str
                }
        """

        self.url: str = options['url'] if options['url'] else ''
        self.format: str = options['format'] if options['format'] else ''
        self.quality: str = options['quality'] if options['quality'] else ''
        self.audio_only: bool = options['audio_only'] if options['audio_only'] else True
        self.download_path: str = options['download_path'] if options['download_path'] else ''

    def get_url(self) -> str:
        return self.url

    def set_url(self, value: str) -> None:
        self.url = value

    def get_format(self) -> str:
        return self.format

    def get_quality(self) -> str:
        return self.quality

    def get_audio_only(self) -> bool:
        return self.audio_only

    def set_audio_only(self, value: bool) -> None:
        self.audio_only = value

    def get_download_path(self) -> str:
        return self.download_path

    def set_download_path(self, value: str) -> None:
        self.download_path = value

    def __str__(self) -> str:
        return f'Url: {self.url}\nFormat: {self.format}\nQuality: {self.quality}\nAudio Only: {self.audio_only}\nDownload Path: {self.download_path}'
