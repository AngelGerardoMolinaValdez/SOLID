from content.image import ImageContent
from content.text import TextContent
from content.video import VideoContent
from content.details import ContentDetails
from content.manager import ContentManager


def main():
    text_content = TextContent()
    image_content = ImageContent()
    video_content = VideoContent()
    manager = ContentManager()

    details = ContentDetails("content", "text", "content.txt")
    print(manager.display_content(text_content, details))

    details = ContentDetails("content", "image", "content.jpg")
    print(manager.display_content(image_content, details))

    details = ContentDetails("content", "video", "content.mp4")
    print(manager.display_content(video_content, details))

if __name__ == "__main__":
    main()
