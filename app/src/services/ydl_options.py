from typing import Any

from yt_dlp.utils import YoutubeDLError

SUPPORTED_JS_RUNTIMES = ("deno", "node", "bun")
ERROR_PREFIX = "ERROR: "


def base_options(ffmpeg_location: str | None) -> dict[str, Any]:
    options: dict[str, Any] = {
        "quiet": True,
        "no_warnings": True,
        "noprogress": True,
        "noplaylist": True,
        "color": "no_color",
        "js_runtimes": {runtime: {} for runtime in SUPPORTED_JS_RUNTIMES},
    }
    if ffmpeg_location:
        options["ffmpeg_location"] = ffmpeg_location
    return options


def describe_error(error: YoutubeDLError) -> str:
    return str(error).removeprefix(ERROR_PREFIX).strip()
