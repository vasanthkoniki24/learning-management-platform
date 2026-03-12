from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from datetime import datetime
import models

router = APIRouter(prefix="/enroll", tags=["Enrollments"])


# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Enroll in a course
@router.post("/")
def enroll(user_id: int, course_id: int, db: Session = Depends(get_db)):

    enrollment = models.Enrollment(
        user_id=user_id,
        course_id=course_id,
        enrolled_on = datetime.utcnow()
    )

    db.add(enrollment)
    db.commit()

    return {"message": "Successfully enrolled in course"}


# View enrolled courses
@router.get("/my-courses")
def my_courses(user_id: int, db: Session = Depends(get_db)):

    enrollments = db.query(models.Enrollment).filter(
        models.Enrollment.user_id == user_id
    ).all()

    return enrollments