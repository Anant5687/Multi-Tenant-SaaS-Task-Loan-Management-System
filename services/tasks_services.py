from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.tasks_models import TASK_MODEL
from schemas.tasks_schemas import TaskRequest
from models.users_models import Users_Schema

class TaskService:

    @staticmethod
    def validate_user(data: TaskRequest, db: Session):
        user_for_assignment= db.query(Users_Schema).filter(
            Users_Schema.id == data.assigned_to
        ).first()

        if not user_for_assignment:
            raise HTTPException(
                status_code=404,
                detail=f"User not found with {data.assigned_to}"
            )

        user_for_creation= db.query(Users_Schema).filter(
            Users_Schema.id == data.created_by
        ).first()

        if not user_for_creation:
            raise HTTPException(
                status_code=404,
                detail=f"User not found with {data.created_by}"
            )
        
        return True



    @staticmethod
    def get_all_tasks(db: Session):
        return db.query(TASK_MODEL).all()
    
    @staticmethod
    def get_task_by_id(id: str, db:Session):
        task = db.query(TASK_MODEL).filter(TASK_MODEL.id == id).first()

        if not task:
            raise HTTPException(status_code=404, detail="No task found")
        
        return task
    
    @staticmethod
    def delete_task(id:str, db: Session):
        task = TaskService.get_task_by_id(id, db)

        db.delete(task)
        db.commit()
        return task
    
    @staticmethod
    def create_task(data:TaskRequest, db:Session):

        TaskService.validate_user(data, db)

        new_task = TASK_MODEL(**data.dict())

        len = db.query(TASK_MODEL).count()
        new_task.id= f"TSK-{len + 1}"

        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        return new_task
    
    @staticmethod
    def update_task(id: str, data: TaskRequest, db: Session):
        TaskService.validate_user(data, db)

        task = TaskService.get_task_by_id(id, db)

        for key, value in data.dict().items():
            setattr(task, key, value)

        db.commit()
        db.refresh(task)
        return task
