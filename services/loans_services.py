from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.loans_models import Loans_Schema
from schemas.loans_schemas import LoanRequest, LoanResponse

class LoansService:

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
        new_loan = Loans_Schema(**data.dict())

        new_loan.id = f"LN-{db.query(Loans_Schema).count() + 1}"

        db.add(new_loan)
        db.commit()
        db.refresh(new_loan)
        return new_loan
    
    @staticmethod
    def update_loan(id: str, data: LoanRequest, db: Session):
        loan = LoansService.get_loan_by_id(id, db)

        for key, value in data.dict().items():
            setattr(loan, key, value)

        db.commit()
        db.refresh(loan)

        return loan