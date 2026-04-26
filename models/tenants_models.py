from db.conn import BASE
from sqlalchemy import Column , String, TIMESTAMP, text

class Tenants_Schema(BASE):
    __tablename__ = "tenants"

    id= Column(String, primary_key=True, nullable=False)
    company_name= Column(String, unique=True, nullable=False)
    created_at= Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))