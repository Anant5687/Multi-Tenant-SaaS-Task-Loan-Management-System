from pydantic import BaseModel
from models.enums.loan_enum import Status

class LoanRequest(BaseModel):
    id: str
    user_id: str
    amount: int
    status: Status
    approved_by: str
    tenant_id: str


class LoanResponse(LoanRequest):
    pass

    class Config:
        from_attributes: True