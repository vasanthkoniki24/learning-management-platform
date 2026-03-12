from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base

class User(Base):

    __tablename__ = "courses_user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    role = Column(String)
    password_hash = Column(String)


class Course(Base):

    __tablename__ = "courses_course"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    instructor_id = Column(Integer)
    status = Column(String)


class Enrollment(Base):

    __tablename__ = "courses_enrollment"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    course_id = Column(Integer)
    enrolled_on = Column(DateTime,default=datetime.utcnow)


class Progress(Base):

    __tablename__ = "courses_progress"

    id = Column(Integer, primary_key=True, index=True)
    enrollment_id = Column(Integer)
    completed_lessons = Column(Integer)
    progress_percent = Column(Integer)