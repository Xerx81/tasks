from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_current_admin, get_current_user
from app.db.session import get_db
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskRead, TaskUpdate


router = APIRouter(prefix="/api/v1/tasks", tags=["Tasks"])


@router.post("/", response_model=TaskRead)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    admin = Depends(get_current_admin)
):
    """
    Create new task.
    Only admin can create task.
    """
    new_task = Task(
        title=task.title,
        description=task.description,
        created_by=admin.id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


@router.get("/", response_model=list[TaskRead])
def read_tasks(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    """
    Get all tasks.
    All users can read tasks.
    """
    tasks = db.query(Task).all()
    return tasks


@router.get("/{task_id}", response_model=TaskRead)
def read_task(
    task_id: int,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    """
    Get task by id.
    """
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


@router.put("/{task_id}", response_model=TaskRead)
def update_task(
    task_id: int,
    task_data: TaskUpdate,
    db: Session = Depends(get_db),
    admin = Depends(get_current_admin),
):
    """
    Update task.
    Only admin can update task.
    """
    # Check if task exists
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if task_data.title is not None:
        task.title = task_data.title

    if task_data.description is not None:
        task.description = task_data.description

    db.commit()
    db.refresh(task)

    return task


@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    admin = Depends(get_current_admin)
):
    """
    Delete task.
    Only admin can delete task.
    """
    # Check if task exists
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()

    return
