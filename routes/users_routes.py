from fastapi import APIRouter, Depends, HTTPException
from schemas.users_schemas import UserResponse, UsersRequest
from sqlalchemy.orm import Session
from db.conn import get_db
from models.users_models import Users_Schema

router = APIRouter(prefix="/user", tags=["USERS"])


@router.post("/create", response_model=UserResponse)
def create_user(data: UsersRequest, db:Session=Depends(get_db)):
    existing_user = db.query(Users_Schema).filter(Users_Schema.email == data.email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail=f"User already reqistered with ${data.email}")

    new_user = Users_Schema(**data.dict())

    new_user.id = f"USR-{len(db.query(Users_Schema).all()) + 1}"

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/all", response_model=list[UserResponse])
def get_all_users(db:Session=Depends(get_db)):
    return db.query(Users_Schema).all()

@router.get("/user/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: str, db: Session= Depends(get_db)):
    user = db.query(Users_Schema).filter(Users_Schema.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail= f"User not found with this {user_id}")
    
    return user