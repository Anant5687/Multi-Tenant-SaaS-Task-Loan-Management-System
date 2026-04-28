"""
User Routes - API endpoints for user management
Handles HTTP requests and delegates business logic to UserService
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.conn import get_db
from schemas.users_schemas import UserResponse, UsersRequest
from services.users_services import UserService

router = APIRouter(prefix="/user", tags=["USERS"])


@router.post("/create", response_model=UserResponse)
def create_user(data: UsersRequest, db: Session = Depends(get_db)):
    """
    Create a new user
    
    Args:
        data: User creation request data
        db: Database session
        
    Returns:
        Created user details
    """
    return UserService.create_user(data, db)


@router.get("/all", response_model=list[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    """
    Retrieve all users
    
    Args:
        db: Database session
        
    Returns:
        List of all users
    """
    return UserService.get_all_users(db)


@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: str, db: Session = Depends(get_db)):
    """
    Retrieve a specific user by ID
    
    Args:
        user_id: The user ID to retrieve
        db: Database session
        
    Returns:
        User details
    """
    return UserService.get_user_by_id(user_id, db)


@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: str, data: UsersRequest, db: Session = Depends(get_db)):
    """
    Update a user's information
    
    Args:
        user_id: The user ID to update
        data: Updated user data
        db: Database session
        
    Returns:
        Updated user details
    """
    return UserService.update_user(user_id, data, db)


@router.delete("/{user_id}")
def delete_user(user_id: str, db: Session = Depends(get_db)):
    """
    Delete a user
    
    Args:
        user_id: The user ID to delete
        db: Database session
        
    Returns:
        Success message
    """
    return UserService.delete_user(user_id, db)