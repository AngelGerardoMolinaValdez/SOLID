from .base import Command
from .types import IssueType

class IssueIdentifier:
    """Issue identifier class.
    
    Attributes:
    id: int -- Issue identifier.
    type: IssueType -- Issue type.
    """
    def create_issue(self, issue_type: str, *args, **kwargs):
        try:
            issue: Command = IssueType[issue_type].value
            return issue(*args, **kwargs)
        except ValueError:
            raise ValueError(f"Invalid issue type: {issue_type}")
