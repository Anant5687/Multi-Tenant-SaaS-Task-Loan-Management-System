from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.loans_models import Loans_Schema
from schemas.loans_schemas import LoanRequest
from models.tenants_models import Tenants_Schema
from models.users_models import Users_Schema

class LoansService:

    @staticmethod
    def validate_loan_request(data: LoanRequest, db: Session):
        tenant= db.query(Tenants_Schema).filter(
            Tenants_Schema.id == data.tenant_id
        ).first()

        if not tenant:
            raise HTTPException(
                status_code=404,
                detail=f"Tenant not present with {data.tenant_id}"
            )
        
        check_user_id = db.query(Users_Schema).filter(
            Users_Schema.id == data.user_id
        ).first()

        if not check_user_id:
            raise HTTPException(
                status_code=404,
                detail=f"Tenant not present with {data.user_id}"
            )

        check_approved_id = db.query(Users_Schema).filter(
            Users_Schema.id == data.approved_by
        ).first()

        if not check_approved_id:
            raise HTTPException(
                status_code=404,
                detail=f"Tenant not present with {data.approved_by}"
            )

    @staticmethod
    def get_all_loans(db: Session):
        return db.query(Loans_Schema).all()
    
    @staticmethod
    def get_loan_by_id(id: str, db: Session):
        loan = db.query(Loans_Schema).filter(Loans_Schema.id == id).first()

        if not loan:
            raise HTTPException(status_code=404, detail="Loan not found")

        return loan
    

    @staticmethod
    def create_loan(data: LoanRequest, db: Session):

        LoansService.validate_loan_request(data, db)

        new_loan = Loans_Schema(**data.dict())

        new_loan.id = f"LN-{db.query(Loans_Schema).count() + 1}"

        db.add(new_loan)
        db.commit()
        db.refresh(new_loan)
        return new_loan
    
    @staticmethod
    def update_loan(id: str, amount: float, status: str, data: LoanRequest, db: Session):
        LoansService.validate_loan_request(data, db)

        loan = LoansService.get_loan_by_id(id, db)

        for key, value in data.dict().items():
            setattr(loan, key, value)

        loan.amount = amount
        loan.status = status

        db.commit()
        db.refresh(loan)

        return loan