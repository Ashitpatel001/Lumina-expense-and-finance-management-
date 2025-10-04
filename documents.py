from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from app.db import models, session as db_session
from app.core.security import get_current_active_user
from app.services.rag_service import rag_service
import uuid

router = APIRouter()

@router.post("/{project_id}/upload", status_code=201)
async def upload_document(
    project_id: uuid.UUID,
    file: UploadFile = File(...),
    db: Session = Depends(db_session.get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    contents = await file.read()
    extracted_text = rag_service.extract_text_from_pdf(contents)

    db_document = models.Document(
        project_id=project_id,
        s3_key=f"uploads/{project_id}/{file.filename}",
        original_filename=file.filename,
        extracted_text=extracted_text
    )
    db.add(db_document)
    db.commit()
    db.refresh(db_document)

    rag_service.add_document(doc_id=str(db_document.id), text=extracted_text)
    return {"filename": file.filename, "document_id": db_document.id}

@router.get("/search")
def search_documents(query: str, current_user: models.User = Depends(get_current_active_user)):
    if not query:
        raise HTTPException(status_code=400, detail="Query cannot be empty.")
    results = rag_service.semantic_search(query)
    return {"query": query, "results": results}