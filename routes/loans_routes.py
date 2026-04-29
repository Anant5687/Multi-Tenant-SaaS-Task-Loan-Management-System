from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from models.loans_models import Loans_Schema
from schemas.loans_schemas import LoanRequest, LoanResponse
from db.conn import get_db
from services.loans_services import LoansService

router = APIRouter(prefix="/loans", tags=["Loans"])

@router.get("/all", response_model= list[LoanResponse])
def get_all_loans(db: Session = Depends(get_db)):
    return LoansService.get_all_loans(db)

@router.get("/loan/{id}", response_model=LoanResponse)
def get_loan_by_id(id: str, db: Session= Depends(get_db)):
    return LoansService.get_loan_by_id(id, db)

@router.post("/create", response_model=LoanResponse)
def create_loan(data: LoanRequest, db: Session= Depends(get_db)):
    return LoansService.create_loan(data, db)

@router.put("/update/{id}", response_model=LoanResponse)
def update_loan(id: str,
                 data: LoanRequest,
                 amount: float=Query(...),
                 status: str=Query(...),
                 db: Session= Depends(get_db)
                ):
    return LoansService.update_loan(id, amount, status, data, db)