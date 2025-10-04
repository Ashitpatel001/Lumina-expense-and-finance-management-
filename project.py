from pydantic import BaseModel
from typing import Optional
import uuid

class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None
    budget: Optional[float] = None

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: uuid.UUID
    created_by_id: uuid.UUID

    class Config:
        from_attributes = True