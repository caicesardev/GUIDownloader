import re

YOUTUBE_URL_PATTERN = re.compile(
    r"^(https?://)?([\w-]+\.)?(youtube\.com|youtube-nocookie\.com|youtu\.be)/\S+$",
    re.IGNORECASE,
)


def is_youtube_url(url: str) -> bool:
    return YOUTUBE_URL_PATTERN.match(url) is not None
