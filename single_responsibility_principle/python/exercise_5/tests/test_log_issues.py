from unittest import TestCase
import sys

sys.path.append("src")

from src.issues.call import IssueCall
from src.issues.log import IssueLoggerPdf, IssueLoggerHtml, IssueLoggerPlainText

class TestLogIssues(TestCase):
    def test_issue_logger_pdf(self):
        issue_pdf = IssueLoggerPdf()
        issue_error = IssueCall('ERROR')
        self.assertEqual(issue_pdf.log(issue_error.process()), "pdf issue logged: error command executed successfully")
    
    def test_issue_logger_html(self):
        issue_html = IssueLoggerHtml()
        issue_process = IssueCall('PROCESS')
        self.assertEqual(issue_html.log(issue_process.process()), "html issue logged: process command executed successfully")
    
    def test_issue_logger_plain_text(self):
        issue_plain_text = IssueLoggerPlainText()
        issue_task = IssueCall('TASK')
        self.assertEqual(issue_plain_text.log(issue_task.process()), "plain text issue logged: task command executed successfully")
