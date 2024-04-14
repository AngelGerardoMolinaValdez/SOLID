from .base import ContentBase
from .details import ContentDetails

class TextContent(ContentBase):
    """Text content class."""

    def display(self, details: ContentDetails) -> str:
        """Display the content."""
        return f"Displaying text with name: {details.name}, type: {details.type}, src: {details.src}"
