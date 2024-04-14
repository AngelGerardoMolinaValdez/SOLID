from report.base import ReportCreator

class ReportCreatorJson(ReportCreator):
    """Report creator for console."""

    def create(self, data: dict) -> str:
        """Create the report."""
        return "json report created with data: " + str(data)

class ReportCreatorCsv(ReportCreator):
    """Report creator for console."""

    def create(self, data: dict) -> str:
        """Create the report."""
        return "csv report created with data: " + str(data)

class ReportCreatorXml(ReportCreator):
    """Report creator for console."""

    def create(self, data: dict) -> str:
        """Create the report."""
        return "xml report created with data: " + str(data)
