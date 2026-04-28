from db.conn import BASE
from sqlalchemy import Column, text, TIMESTAMP, String, Integer
from models.enums.loan_enum import Status

class Loans_Schema(BASE):
    __tablename__ = "loans"

    id= Column(String, primary_key=True, unique=True)
    user_id= Column(String, nullable=False)  #(FK users.id)
    amount= Column(Integer, nullable=False)
    status= Column(Status, nullable=False)
    approved_by= Column(String , nullable=(False)) #(FK users.id)
    tenant_id= Column(String, nullable=False)
    created_at= Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))