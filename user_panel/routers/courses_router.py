from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
import models

router = APIRouter(prefix="/courses", tags=["Courses"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def get_courses(db: Session = Depends(get_db)):

    courses = db.query(models.Course).all()

    if not courses:
        raise HTTPException(
            status_code=404,
            detail="No courses available"
        )

    return courses


@router.get("/{course_id}")
def get_course(course_id: int, db: Session = Depends(get_db)):

    course = db.query(models.Course).filter(
        models.Course.id == course_id
    ).first()

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return course