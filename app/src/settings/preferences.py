from pathlib import Path

from PySide6.QtCore import QByteArray, QSettings

from constants import APP_NAME, DEFAULT_DOWNLOAD_DIRECTORY

DOWNLOAD_DIRECTORY_KEY = "download_path"
FFMPEG_LOCATION_KEY = "ffmpeg_path"
WINDOW_GEOMETRY_KEY = "window/geometry"


class Preferences:
    def __init__(self) -> None:
        self._settings = QSettings(APP_NAME, "Preferences")

    @property
    def download_directory(self) -> Path:
        stored = str(self._settings.value(DOWNLOAD_DIRECTORY_KEY, "") or "")
        return Path(stored) if stored else DEFAULT_DOWNLOAD_DIRECTORY

    @download_directory.setter
    def download_directory(self, directory: Path) -> None:
        self._settings.setValue(DOWNLOAD_DIRECTORY_KEY, str(directory))

    @property
    def ffmpeg_location(self) -> str:
        return str(self._settings.value(FFMPEG_LOCATION_KEY, "") or "")

    @ffmpeg_location.setter
    def ffmpeg_location(self, location: str) -> None:
        self._settings.setValue(FFMPEG_LOCATION_KEY, location.strip())

    @property
    def window_geometry(self) -> QByteArray | None:
        geometry = self._settings.value(WINDOW_GEOMETRY_KEY)
        return geometry if isinstance(geometry, QByteArray) else None

    @window_geometry.setter
    def window_geometry(self, geometry: QByteArray) -> None:
        self._settings.setValue(WINDOW_GEOMETRY_KEY, geometry)
