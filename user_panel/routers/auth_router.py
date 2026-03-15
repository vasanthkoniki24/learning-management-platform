from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from auth import create_access_token
import models

router = APIRouter(prefix="/auth",tags=["Authentication"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register(name: str, email: str, password: str, role: str,
             db: Session = Depends(get_db)):

    existing = db.query(models.User).filter(
        models.User.email == email
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    user = models.User(
        name=name,
        email=email,
        role=role,
        password_hash=password
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return {
        "message": "User registered successfully",
        "user_id": user.id
    }



@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):

    user = db.query(models.User).filter(
        models.User.email == email
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if user.password_hash != password:
        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )
    
    token = create_access_token({"user_id": user.id})

    return {
        # "message": "Login successful",
        # "user_id": user.id,
        # "role": user.role
        "access_token": token,
        "token_type": "bearer"
    }