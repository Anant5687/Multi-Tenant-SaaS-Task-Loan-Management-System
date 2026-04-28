from enum import Enum
from pydantic import BaseModel
from models.enums.task_enum import Status

class TaskRequest(BaseModel):
    id: str
    title: str
    description: str
    status: Status
    assigned_to: str
    created_by: str
    tenant_id: str

class TaskResponse(TaskRequest):
    pass

    class Config:
        from_attributes: True