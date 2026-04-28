from pydantic import BaseModel, EmailStr
from models.enums.user_enum import Roles
from datetime import datetime


class UsersRequest(BaseModel):
    name:str
    email:EmailStr
    password: str
    role: Roles
    tenant_id: str


class UserResponse(BaseModel):
    id:str
    name:str
    email:EmailStr
    role: Roles
    tenant_id: str
    created_at: datetime

    class Config:
        from_attributes: True