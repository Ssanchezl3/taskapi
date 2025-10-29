from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class Status(str, Enum):
    pending = "pending"
    completed = "completed"

class Task(BaseModel):
    id: int
    title: str
    description: str = ""
    status: Status = Status.pending
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()

class TaskCreate(BaseModel):
    title: str
    description: str = ""
    status: Status = Status.pending
