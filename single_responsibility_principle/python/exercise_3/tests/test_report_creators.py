from unittest import TestCase
import sys

sys.path.append("src")

from src.report.creator import ReportCreatorJson, ReportCreatorCsv, ReportCreatorXml

class TestReportCreators(TestCase):
    def test_report_creator_json(self):
        data = {"key": "value"}
        report_creator_json = ReportCreatorJson()
        report = report_creator_json.create(data)
        self.assertEqual(report, "json report created with data: {'key': 'value'}")

    def test_report_creator_csv(self):
        data = {"key": "value"}
        report_creator_csv = ReportCreatorCsv()
        report = report_creator_csv.create(data)
        self.assertEqual(report, "csv report created with data: {'key': 'value'}")

    def test_report_creator_xml(self):
        data = {"key": "value"}
        report_creator_xml = ReportCreatorXml()
        report = report_creator_xml.create(data)
        self.assertEqual(report, "xml report created with data: {'key': 'value'}")
