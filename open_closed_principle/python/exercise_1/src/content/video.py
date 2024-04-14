from .base import ContentBase
from .details import ContentDetails

class VideoContent(ContentBase):
    """Video content class."""

    def display(self, details: ContentDetails) -> str:
        """Display the content."""
        return f"Displaying video with name: {details.name}, type: {details.type}, src: {details.src}"
