from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.tasks_models import TASK_MODEL
from schemas.tasks_schemas import TaskRequest

class TaskService:
    
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
        new_task = TASK_MODEL(**data.dict())

        len = db.query(TASK_MODEL).count()
        new_task.id= f"TSK-{len + 1}"

        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        return new_task
    
    @staticmethod
    def update_task(id: str, data: TaskRequest, db: Session):
        task = TaskService.get_task_by_id(id, db)

        for key, value in data.dict().items():
            setattr(task, key, value)

        db.commit()
        db.refresh(task)
        return task
