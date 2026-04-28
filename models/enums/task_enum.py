from enum import Enum

class Status(str, Enum):
    IN_PROGRESS= "In-Progress"
    IN_REVIEW= "In-Review"
    BLOCKED= "Blocked"
    COMPLETED= "Completed"
    CANCELLED= "Cancelled"