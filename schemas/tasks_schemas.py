from enum import Enum

class Status(str, Enum):
    IN_PROGRESS= "In-Progess"
    COMPLETED= "Completed"
    IN_REVIEW= "In-Review"
    BLOCKED= "Blocked"
    COMPLETED= "Completed"
    CONCELLED= "Cancelled"