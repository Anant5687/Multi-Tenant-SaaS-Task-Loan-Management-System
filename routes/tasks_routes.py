from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from models.tasks_models import TASK_MODEL
from schemas.tasks_schemas import TaskRequest, TaskResponse
from db.conn import get_db
from services.tasks_services import TaskService

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/create", response_model=TaskResponse)
def create_task(data:TaskRequest, db: Session= Depends(get_db)):
    return TaskService.create_task(data, db)

@router.get("/task/{id}", response_model=TaskResponse)
def get_task_by_id(id: str, db: Session= Depends(get_db)):
    return TaskService.get_task_by_id(id, db)

@router.get("/all", response_model=list[TaskResponse])
def get_all_tasks(db: Session=Depends(get_db)):
    return TaskService.get_all_tasks(db)

@router.put("/update/{id}", response_model=TaskResponse)
def update_task(id: str, data: TaskRequest, db: Session= Depends(get_db)):
    return TaskService.update_task(id, data, db)

@router.delete("/delete/{id}", response_model=TaskResponse)
def delete_task(id: str, db:Session=Depends(get_db)):
    return TaskService.delete_task(id, db)