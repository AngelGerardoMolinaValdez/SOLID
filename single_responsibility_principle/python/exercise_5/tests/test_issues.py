from unittest import TestCase
import sys

sys.path.append("src")

from src.issues.call import IssueCall

class TestIssues(TestCase):
    def test_issue_call_error(self):
        issue_error = IssueCall('ERROR')
        self.assertEqual(issue_error.process(), "error command executed successfully")
    
    def test_issue_call_process(self):
        issue_process = IssueCall('PROCESS')
        self.assertEqual(issue_process.process(), "process command executed successfully")
    
    def test_issue_call_task(self):
        issue_task = IssueCall('TASK')
        self.assertEqual(issue_task.process(), "task command executed successfully")
