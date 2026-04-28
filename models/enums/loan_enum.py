from enum import Enum

class Status(str, Enum):
    PENDING= "Pending"
    APPROVED= "Approved"
    REJECTED= "Rejected"