from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Boolean
from database import Base
from datetime import datetime

class User(Base):

    __tablename__ = "courses_user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    role = Column(String)
    password_hash = Column(String)


class Course(Base):

    __tablename__ = "courses_course"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    instructor_id = Column(Integer)
    is_premium = Column(Boolean)


class Enrollment(Base):

    __tablename__ = "courses_enrollment"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    course_id = Column(Integer)
    enrolled_on = Column(DateTime, default=datetime.utcnow)


class Progress(Base):

    __tablename__ = "courses_progress"

    id = Column(Integer, primary_key=True)
    enrollment_id = Column(Integer)
    completed_lessons = Column(Integer)
    progress_percent = Column(Integer)


class Plan(Base):

    __tablename__ = "courses_plan"

    id = Column(Integer,primary_key=True)
    name = Column(String)
    price = Column(Float)
    duration_days = Column(Integer)


class Subscription(Base):

    __tablename__ = "courses_subscription"

    id = Column(Integer,primary_key=True)
    user_id = Column(Integer)
    plan_id = Column(Integer)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    status = Column(String)



class Payment(Base):

    __tablename__ = "courses_payment"

    id = Column(Integer,primary_key=True)
    user_id = Column(Integer)
    plan_id = Column(Integer)
    amount = Column(Float)
    payment_date = Column(DateTime)