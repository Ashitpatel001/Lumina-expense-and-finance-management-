from pydantic import BaseModel, EmailStr
from typing import Optional
import uuid
from app.db.models import UserRole

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str
    role: UserRole = UserRole.employee

class User(UserBase):
    id: uuid.UUID
    is_active: bool
    role: UserRole

    class Config:
        from_attributes = True