from abc import ABC, abstractmethod

class ReportViewer(ABC):
    """Base class for report viewer."""

    @abstractmethod
    def view(self, data: dict) -> str:
        """View the report."""
        pass

class ReportCreator(ABC):
    """Base class for report creator."""

    @abstractmethod
    def create(self, data: dict) -> str:
        """Create the report."""
        pass
