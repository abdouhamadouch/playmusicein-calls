import unittest
from types import SimpleNamespace

import media_play


class MediaUrlTests(unittest.TestCase):
    def test_youtube_url(self):
        update = SimpleNamespace(effective_message=SimpleNamespace(
            text="/video https://youtu.be/abc123", caption=None
        ))
        self.assertEqual(media_play._url_from_command(update), "https://youtu.be/abc123")

    def test_direct_mp4_url(self):
        url = "https://cdn.example.com/movie.mp4"
        update = SimpleNamespace(effective_message=SimpleNamespace(
            text=f"/video {url}", caption=None
        ))
        self.assertEqual(media_play._url_from_command(update), url)

    def test_hls_url(self):
        url = "https://media.example.com/live/index.m3u8?token=abc"
        update = SimpleNamespace(effective_message=SimpleNamespace(
            text=f"/video {url}", caption=None
        ))
        self.assertEqual(media_play._url_from_command(update), url)

    def test_url_in_caption(self):
        url = "https://cdn.example.com/clip.webm"
        update = SimpleNamespace(effective_message=SimpleNamespace(
            text=None, caption=f"please play {url}"
        ))
        self.assertEqual(media_play._url_from_command(update), url)

    def test_reject_local_hosts(self):
        for url in (
            "http://localhost/video.mp4",
            "http://127.0.0.1/video.mp4",
            "http://192.168.1.2/video.mp4",
            "http://169.254.169.254/latest/meta-data",
        ):
            with self.subTest(url=url):
                self.assertFalse(media_play._media_url(url))

    def test_reject_non_http_schemes(self):
        self.assertFalse(media_play._media_url("file:///etc/passwd"))


if __name__ == "__main__":
    unittest.main()
