import unittest

from src.services.youtube_url import is_youtube_url
from src.utils.formatting import format_bytes, format_duration, friendly_codec_name


class FormattingTest(unittest.TestCase):
    def test_formats_bytes_with_binary_units(self) -> None:
        self.assertEqual(format_bytes(512), "512 B")
        self.assertEqual(format_bytes(1536), "1.5 KB")
        self.assertEqual(format_bytes(18816948), "17.9 MB")

    def test_formats_durations(self) -> None:
        self.assertEqual(format_duration(58), "0:58")
        self.assertEqual(format_duration(3725), "1:02:05")

    def test_translates_codec_identifiers(self) -> None:
        self.assertEqual(friendly_codec_name("avc1.640028"), "H.264")
        self.assertEqual(friendly_codec_name("av01.0.08M.08"), "AV1")
        self.assertEqual(friendly_codec_name("theora"), "THEORA")


class YoutubeUrlTest(unittest.TestCase):
    def test_accepts_youtube_urls(self) -> None:
        for url in (
            "https://www.youtube.com/watch?v=dP15zlyra3c",
            "youtube.com/watch?v=dP15zlyra3c",
            "https://youtu.be/dP15zlyra3c",
            "https://m.youtube.com/shorts/dP15zlyra3c",
            "https://music.youtube.com/watch?v=dP15zlyra3c",
        ):
            with self.subTest(url=url):
                self.assertTrue(is_youtube_url(url))

    def test_rejects_other_urls(self) -> None:
        for url in ("", "https://vimeo.com/123", "https://notyoutube.com/watch?v=x", "https://youtube.com/"):
            with self.subTest(url=url):
                self.assertFalse(is_youtube_url(url))


if __name__ == "__main__":
    unittest.main()
