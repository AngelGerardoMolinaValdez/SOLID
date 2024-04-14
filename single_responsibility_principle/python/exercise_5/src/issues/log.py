from .base import IssueLogger

class IssueLoggerPdf(IssueLogger):
    """Issue logger for pdf."""

    def log(self, message: str) -> str:
        """Log the issue."""
        return "pdf issue logged: " + message

class IssueLoggerHtml(IssueLogger):
    """Issue logger for html."""

    def log(self, message: str) -> str:
        """Log the issue."""
        return "html issue logged: " + message

class IssueLoggerPlainText(IssueLogger):
    """Issue logger for plain text."""

    def log(self, message: str) -> str:
        """Log the issue."""
        return "plain text issue logged: " + message
