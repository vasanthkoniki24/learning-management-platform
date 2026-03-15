from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from database import SessionLocal
import models

router = APIRouter(tags=["Subscriptions"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/subscribe")
def subscribe(user_id: int, plan_id: int, db: Session = Depends(get_db)):

    plan = db.query(models.Plan).filter(
        models.Plan.id == plan_id
    ).first()

    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")

    start = datetime.utcnow()
    end = start + timedelta(days=plan.duration_days)

    subscription = models.Subscription(
        user_id=user_id,
        plan_id=plan_id,
        start_date=start,
        end_date=end,
        status="active"
    )

    payment = models.Payment(
        user_id=user_id,
        plan_id=plan_id,
        amount=plan.price,
        payment_date=datetime.utcnow()
    )

    db.add(subscription)
    db.add(payment)
    db.commit()

    return {"message": "Subscription successful"}