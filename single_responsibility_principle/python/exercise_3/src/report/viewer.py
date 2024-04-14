from report.base import ReportViewer

class ReportViewerConsole(ReportViewer):
    """Report viewer for console."""

    def view(self, data: dict) -> str:
        """View the report."""
        return ">>> console report viewed: " + str(data)
    
class ReportViewerHtml(ReportViewer):
    """Report viewer for html."""

    def view(self, data: dict) -> str:
        """View the report."""
        return "<h1>report viewed</h1>: " + str(data)

class ReportViewerJson(ReportViewer):
    """Report viewer for json."""

    def view(self, data: dict) -> str:
        """View the report."""
        return "{report: " + str(data) + "}"
