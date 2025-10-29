from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime
from app.domain.task import Status

class TaskCreateDTO(BaseModel):
    title: str = Field(..., min_length=1)
    status: str = Field(...)

    @validator("status")
    def status_must_be_valid(cls, v):
        if v not in (Status.pending.value, Status.done.value):
            raise ValueError("status must be 'pending' or 'done'")
        return v

class TaskReadDTO(BaseModel):
    id: int
    title: str
    status: Status
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = {"from_attributes": True}
