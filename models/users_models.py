from db.conn import BASE
from sqlalchemy import Column, TIMESTAMP, text, String
from schemas.users_schemas import Roles


class Users_Schema(BASE):
    __tablename__ = "users"

    id= Column(String, primary_key=True, nullable=False)
    name= Column(String, nullable=False)
    email= Column(String, nullable=False, unique=False)
    password= Column(String, nullable=False)
    role= Column(Roles, nullable=False)
    tenant_id= Column(String)
    created_at= Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
