from fastapi import APIRouter, Depends
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
def update_progress(enrollment_id: int, completed_lessons: int, progress_percent: int, db: Session = Depends(get_db)):

    progress = models.Progress(
        enrollment_id=enrollment_id,
        completed_lessons=completed_lessons,
        progress_percent=progress_percent
    )

    db.add(progress)
    db.commit()

    return {"message": "Progress updated"}


@router.get("/view")
def view_progress(enrollment_id: int, db: Session = Depends(get_db)):

    progress = db.query(models.Progress).filter(
        models.Progress.enrollment_id == enrollment_id
    ).first()

    return progress