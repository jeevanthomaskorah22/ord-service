from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import Order
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.post("/orders")
def create_order(user_id: int, product_id: int, quantity: int, db: Session = Depends(get_db)):
    new_order = Order(user_id=user_id, product_id=product_id, quantity=quantity)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return {"message": "Order created", "order_id": new_order.id}
