from unittest import TestCase
import sys

sys.path.append("src")

from src.content.text import TextContent
from src.content.image import ImageContent
from src.content.video import VideoContent
from src.content.details import ContentDetails
from src.content.manager import ContentManager

class TestContentManager(TestCase):
    def test_display_content(self):
        text_content = TextContent()
        image_content = ImageContent()
        video_content = VideoContent()
        manager = ContentManager()

        details = ContentDetails("content", "text", "content.txt")
        self.assertEqual(manager.display_content(text_content, details), "Displaying text with name: content, type: text, src: content.txt")

        details = ContentDetails("content", "image", "content.jpg")
        self.assertEqual(manager.display_content(image_content, details), "Displaying image with name: content, type: image, src: content.jpg")

        details = ContentDetails("content", "video", "content.mp4")
        self.assertEqual(manager.display_content(video_content, details), "Displaying video with name: content, type: video, src: content.mp4")
