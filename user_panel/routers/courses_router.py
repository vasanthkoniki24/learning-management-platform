from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
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
def get_courses(user_id: int, db: Session = Depends(get_db)):

    now = datetime.utcnow()

    subscription = db.query(models.Subscription).filter(
        models.Subscription.user_id == user_id,
        models.Subscription.status == "active",
        models.Subscription.end_date >= now
    ).first()

    # If user has active subscription show all courses
    if subscription:
        courses = db.query(models.Course).all()

    # If no subscription show only free courses
    else:
        courses = db.query(models.Course).filter(
            models.Course.is_premium == False
        ).all()

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