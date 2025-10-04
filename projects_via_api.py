from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import uuid

from app.db import models, session
from app.schemas import project as project_schema
from app.core.security import get_current_active_user

router = APIRouter()

@router.post("/", response_model=project_schema.Project, status_code=201)
def create_project(
    project: project_schema.ProjectCreate,
    db: Session = Depends(session.get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    db_project = models.Project(**project.model_dump(), created_by_id=current_user.id)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

@router.get("/", response_model=List[project_schema.Project])
def read_projects(
    skip: int = 0, limit: int = 100,
    db: Session = Depends(session.get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    projects = db.query(models.Project).offset(skip).limit(limit).all()
    return projects