from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
import models

router = APIRouter(prefix="/progress", tags=["Progress"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/update")
def update_progress(enrollment_id: int,
                    completed_lessons: int,
                    progress_percent: int,
                    db: Session = Depends(get_db)):

    progress = models.Progress(
        enrollment_id=enrollment_id,
        completed_lessons=completed_lessons,
        progress_percent=progress_percent
    )

    db.add(progress)
    db.commit()

    return {"message": "Progress updated successfully"}


@router.get("/view/{enrollment_id}")
def view_progress(enrollment_id: int, db: Session = Depends(get_db)):

    progress = db.query(models.Progress).filter(
        models.Progress.enrollment_id == enrollment_id
    ).first()

    if not progress:
        raise HTTPException(
            status_code=404,
            detail="Progress not found"
        )

    return progress