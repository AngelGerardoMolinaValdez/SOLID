from enum import Enum
from .task import Task
from .process import Process
from .error import Error

class IssueType(Enum):
    """Issue type enumeration.
    
    Attributes:
    ERROR: int -- Error issue type.
    PROCESS: int -- Process issue type.
    TASK: int -- Task issue type.
    """
    ERROR = Error
    PROCESS = Process
    TASK = Task
