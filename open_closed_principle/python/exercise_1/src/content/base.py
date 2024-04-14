from abc import ABC, abstractmethod
from .details import ContentDetails

class ContentBase(ABC):
    """Base class for content."""

    @abstractmethod
    def display(self, details: ContentDetails) -> str:
        """Display the content."""
        pass
