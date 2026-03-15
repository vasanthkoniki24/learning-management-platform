from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
import models

router = APIRouter(tags=["Plans"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/plans")
def list_plans(db: Session = Depends(get_db)):

    plans = db.query(models.Plan).all()

    return plans