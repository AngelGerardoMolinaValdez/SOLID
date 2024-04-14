from .identifier import IssueIdentifier
from .resolver import IssueResolver


class IssueCall:
    def __init__(self, issue_type: str) -> None:
        self.issue_type = issue_type
    
    def process(self) -> str:
        return IssueResolver(IssueIdentifier().create_issue(self.issue_type)).resolve()
