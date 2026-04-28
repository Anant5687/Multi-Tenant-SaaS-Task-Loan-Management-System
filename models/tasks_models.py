from db.conn import BASE
from sqlalchemy import Column, INTEGER, String, TIMESTAMP, text
from  models.enums.task_enum import Status

class TASK_MODEL(BASE):
    __tablename__ = "tasks"

    id= Column(String, unique=True, primary_key=True)
    title= Column(String, nullable=False)
    description= Column(String)
    status= Column(Status)
    assigned_to= Column(String, nullable=False)  # (FK users.id)
    created_by= Column(String, nullable=False)  # (FK users.id)
    tenant_id= Column(String, nullable=False)
    created_at= Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))