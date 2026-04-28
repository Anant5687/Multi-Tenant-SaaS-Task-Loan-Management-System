"""
User Services - Business logic layer for user operations
Handles all database operations and business logic for users
"""

from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.users_models import Users_Schema
from schemas.users_schemas import UsersRequest


class UserService:
    """Service class for user-related operations"""

    @staticmethod
    def create_user(data: UsersRequest, db: Session) -> Users_Schema:
        """
        Create a new user in the database
        
        Args:
            data: User request data
            db: Database session
            
        Returns:
            Created user object
            
        Raises:
            HTTPException: If user already exists
        """
        # Check if user already exists
        existing_user = db.query(Users_Schema).filter(
            Users_Schema.email == data.email
        ).first()

        if existing_user:
            raise HTTPException(
                status_code=400,
                detail=f"User already registered with {data.email}"
            )

        # Generate user ID
        user_count = db.query(Users_Schema).count()
        user_id = f"USR-{user_count + 1}"

        # Create new user
        new_user = Users_Schema(**data.dict())
        new_user.id = user_id

        # Save to database
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user

    @staticmethod
    def get_all_users(db: Session) -> list[Users_Schema]:
        """
        Retrieve all users from the database
        
        Args:
            db: Database session
            
        Returns:
            List of all users
        """
        return db.query(Users_Schema).all()

    @staticmethod
    def get_user_by_id(user_id: str, db: Session) -> Users_Schema:
        """
        Retrieve a specific user by ID
        
        Args:
            user_id: The user ID to search for
            db: Database session
            
        Returns:
            User object
            
        Raises:
            HTTPException: If user is not found
        """
        user = db.query(Users_Schema).filter(Users_Schema.id == user_id).first()

        if not user:
            raise HTTPException(
                status_code=404,
                detail=f"User not found with ID: {user_id}"
            )

        return user

    @staticmethod
    def delete_user(user_id: str, db: Session) -> dict:
        """
        Delete a user from the database
        
        Args:
            user_id: The user ID to delete
            db: Database session
            
        Returns:
            Success message
            
        Raises:
            HTTPException: If user is not found
        """
        user = UserService.get_user_by_id(user_id, db)

        db.delete(user)
        db.commit()

        return {"message": f"User {user_id} deleted successfully"}

    @staticmethod
    def update_user(user_id: str, data: UsersRequest, db: Session) -> Users_Schema:
        """
        Update a user in the database
        
        Args:
            user_id: The user ID to update
            data: Updated user data
            db: Database session
            
        Returns:
            Updated user object
            
        Raises:
            HTTPException: If user is not found
        """
        user = UserService.get_user_by_id(user_id, db)

        # Update user fields
        for key, value in data.dict().items():
            setattr(user, key, value)

        db.commit()
        db.refresh(user)

        return user
