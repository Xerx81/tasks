from pydantic import BaseModel
from typing import Optional


class TaskBase(BaseModel):
    description: Optional[str] = None


# Request
class TaskCreate(TaskBase):
    title: str


class TaskUpdate(TaskBase):
    title: str | None = None


# Response
class TaskRead(TaskBase):
    id: int
    title: str

    class Config:
        from_attributes = True
