from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
import models

router = APIRouter(tags=["Enrollment"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/enroll")
def enroll(user_id: int, course_id: int, db: Session = Depends(get_db)):

    enrollment = models.Enrollment(
        user_id=user_id,
        course_id=course_id
    )

    db.add(enrollment)
    db.commit()
    db.refresh(enrollment)

    return {
        "message": "Enrollment successful",
        "enrollment_id": enrollment.id
    }


@router.get("/my-courses/{user_id}")
def my_courses(user_id: int, db: Session = Depends(get_db)):

    enrollments = db.query(models.Enrollment).filter(
        models.Enrollment.user_id == user_id
    ).all()

    if not enrollments:
        raise HTTPException(
            status_code=404,
            detail="User not enrolled in any courses"
        )

    return enrollments