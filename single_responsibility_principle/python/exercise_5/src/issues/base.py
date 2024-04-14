from abc import ABC, abstractmethod

class Command(ABC):
    """Base class for command."""

    @abstractmethod
    def execute(self) -> str:
        """Execute the command."""
        pass

class IssueLogger(ABC):
    """Base class for issue logger."""

    @abstractmethod
    def log(self, message: str) -> str:
        """Log the issue."""
        pass
