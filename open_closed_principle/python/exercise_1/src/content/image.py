from .base import ContentBase
from .details import ContentDetails

class ImageContent(ContentBase):
    """Image content class."""

    def display(self, details: ContentDetails) -> str:
        """Display the content."""
        return f"Displaying image with name: {details.name}, type: {details.type}, src: {details.src}"
