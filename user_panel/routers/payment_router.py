from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
import models

router = APIRouter(tags=["Payments"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/payments")
def payment_history(user_id: int, db: Session = Depends(get_db)):

    payments = db.query(models.Payment).filter(
        models.Payment.user_id == user_id
    ).all()

    return payments