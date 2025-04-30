from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models.content import Content
from app.schemas.content import ContentCreate
from app.database.session import get_db


class ContentService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_content(self, content_id: int):
        return self.db.query(Content).filter(Content.id == content_id).first()

    def get_contents(self, skip: int = 0, limit: int = 100):
        return self.db.query(Content).offset(skip).limit(limit).all()

    def create_content(self, content: ContentCreate, owner_id: int):
        db_content = Content(**content.dict(), owner_id=owner_id)
        self.db.add(db_content)
        self.db.commit()
        self.db.refresh(db_content)
        return db_content

    def update_content(self, content_id: int, content: ContentCreate, owner_id: int):
        db_content = self.get_content(content_id)
        if not db_content:
            raise HTTPException(status_code=404, detail="Content not found")
        if db_content.owner_id != owner_id:
            raise HTTPException(status_code=403, detail="Not enough permissions")
        for key, value in content.dict().items():
            setattr(db_content, key, value)
        self.db.commit()
        self.db.refresh(db_content)
        return db_content

    def delete_content(self, content_id: int, owner_id: int):
        db_content = self.get_content(content_id)
        if not db_content:
            raise HTTPException(status_code=404, detail="Content not found")
        if db_content.owner_id != owner_id:
            raise HTTPException(status_code=403, detail="Not enough permissions")
        self.db.delete(db_content)
        self.db.commit()
        return {"ok": True}