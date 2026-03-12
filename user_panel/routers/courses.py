from fastapi import APIRouter, Depends
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

    return courses


@router.get("/{course_id}")
def course_details(course_id: int, db: Session = Depends(get_db)):

    course = db.query(models.Course).filter(models.Course.id == course_id).first()

    return course


@router.post("/")
def create_course(title: str, description: str, instructor_id: int, db: Session = Depends(get_db)):

    course = models.Course(
        title=title,
        description=description,
        instructor_id=instructor_id,
        status="active"
    )

    db.add(course)
    db.commit()

    return {"message": "Course created"}