from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.content import Content, ContentCreate
from app.services.content import ContentService
from app.database.session import get_db
from app.utils.security import get_current_user
from app.models.user import User

router = APIRouter(prefix="/contents", tags=["contents"])

@router.post("/", response_model=Content)
def create_content(
    content: ContentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    content_service = ContentService(db)
    return content_service.create_content(content=content, owner_id=current_user.id)

@router.get("/", response_model=List[Content])
def read_contents(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    content_service = ContentService(db)
    return content_service.get_contents(skip=skip, limit=limit)

@router.get("/{content_id}", response_model=Content)
def read_content(content_id: int, db: Session = Depends(get_db)):
    content_service = ContentService(db)
    db_content = content_service.get_content(content_id=content_id)
    if db_content is None:
        raise HTTPException(status_code=404, detail="Content not found")
    return db_content

@router.put("/{content_id}", response_model=Content)
def update_content(
    content_id: int,
    content: ContentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    content_service = ContentService(db)
    return content_service.update_content(
        content_id=content_id,
        content=content,
        owner_id=current_user.id
    )

@router.delete("/{content_id}")
def delete_content(
    content_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    content_service = ContentService(db)
    return content_service.delete_content(
        content_id=content_id,
        owner_id=current_user.id
    )