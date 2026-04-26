from pydantic import BaseModel

from enum import Enum

class Roles(str, Enum):
    ADMIN= "Admin"
    MANAGER= "Manager"
    USER= "User"