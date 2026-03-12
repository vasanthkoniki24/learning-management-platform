from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models
from auth import create_access_token
# from pydantic import BaseModel

router = APIRouter(prefix="/users", tags=["Users"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# class RegisterRequest(BaseModel):
#     name:str
#     email:str
#     password:str
#     role:str


@router.post("/register")
def register(name:str, email:str, password: str, role: str, db: Session = Depends(get_db)):

    existing_user = db.query(models.User).filter(models.User.email == email).first()

    if existing_user:
        return{"error":"User already exists"}
    
    
    user = models.User(
        name=name,
        email=email,
        password_hash=password,
        role=role
    )

    db.add(user)
    db.commit()

    return {"message": "User registered successfully"}


@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.email == email).first()

    if not user:
        return {"error": "Invalid credentials"}

    token = create_access_token({"user_id": user.id})

    return {
        "access_token": token,
        "token_type": "bearer"
    }