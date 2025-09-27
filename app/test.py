import yt_dlp


def get_available_formats_and_qualities(url: str):
    ydl_opts = {
        "format": "all",
        "noplaylist": True,  # No procesar listas de reproducción
        "quiet": True,       # Silencia la salida
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        formats = info_dict.get("formats", [])

        video_formats = set()
        video_qualities = set()
        audio_formats = set()
        audio_qualities = set()

        for fmt in formats:
            ext = fmt.get("ext")
            resolution = fmt.get("resolution")
            acodec = fmt.get("acodec")
            abr = fmt.get("abr")  # Audio Bitrate

            # Video formats and qualities
            if fmt.get("vcodec") != "none":
                video_formats.add(ext)
                if resolution:
                    video_qualities.add(resolution)

            # Audio formats and qualities
            if acodec != "none":
                audio_formats.add(ext)
                if abr:
                    audio_qualities.add(f"{abr}k")

        # Convertir sets a listas ordenadas
        video_formats = sorted(list(video_formats))
        video_qualities = sorted(list(video_qualities), reverse=True)
        audio_formats = sorted(list(audio_formats))
        audio_qualities = sorted(list(audio_qualities), reverse=True)

        return video_formats, video_qualities, audio_formats, audio_qualities


# Ejemplo de uso
url = "https://www.youtube.com/watch?v=dP15zlyra3c"
video_formats, video_qualities, audio_formats, audio_qualities = get_available_formats_and_qualities(
    url
)

print("Video Formats:", video_formats)
print("Video Qualities:", video_qualities)
print("Audio Formats:", audio_formats)
print("Audio Qualities:", audio_qualities)
