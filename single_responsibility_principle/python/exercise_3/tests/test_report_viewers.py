from unittest import TestCase
import sys

sys.path.append("src")

from src.report.viewer import ReportViewerConsole, ReportViewerHtml, ReportViewerJson

class TestReportViewers(TestCase):
    def test_report_viewer_console(self):
        data = {"key": "value"}
        report_viewer_console = ReportViewerConsole()
        report = report_viewer_console.view(data)
        self.assertEqual(report, ">>> console report viewed: {'key': 'value'}")

    def test_report_viewer_html(self):
        data = {"key": "value"}
        report_viewer_html = ReportViewerHtml()
        report = report_viewer_html.view(data)
        self.assertEqual(report, "<h1>report viewed</h1>: {'key': 'value'}")

    def test_report_viewer_json(self):
        data = {"key": "value"}
        report_viewer_json = ReportViewerJson()
        report = report_viewer_json.view(data)
        self.assertEqual(report, "{report: {'key': 'value'}}")
