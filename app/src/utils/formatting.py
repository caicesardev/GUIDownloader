BYTE_UNITS = ("B", "KB", "MB", "GB", "TB")

CODEC_NAMES = {
    "avc1": "H.264",
    "avc3": "H.264",
    "hev1": "H.265",
    "hvc1": "H.265",
    "vp9": "VP9",
    "vp09": "VP9",
    "av01": "AV1",
    "mp4a": "AAC",
    "opus": "Opus",
    "vorbis": "Vorbis",
    "mp3": "MP3",
    "flac": "FLAC",
}


def format_bytes(size: float) -> str:
    unit_index = 0
    while size >= 1024 and unit_index < len(BYTE_UNITS) - 1:
        size /= 1024
        unit_index += 1
    unit = BYTE_UNITS[unit_index]
    return f"{size:.0f} {unit}" if unit == "B" else f"{size:.1f} {unit}"


def format_duration(total_seconds: float) -> str:
    minutes, seconds = divmod(int(total_seconds), 60)
    hours, minutes = divmod(minutes, 60)
    if hours:
        return f"{hours}:{minutes:02}:{seconds:02}"
    return f"{minutes}:{seconds:02}"


def friendly_codec_name(codec: str) -> str:
    codec_family = codec.split(".")[0].lower()
    return CODEC_NAMES.get(codec_family, codec_family.upper())
