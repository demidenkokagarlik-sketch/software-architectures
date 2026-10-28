from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI(title="Orders Service")

ORDERS = []

class OrderCreate(BaseModel):
    userId: int
    itemId: int
    qty: int

@app.post("/orders", status_code=status.HTTP_201_CREATED)
def create_order(order: OrderCreate):
    order_id = len(ORDERS) + 1
    new_order = {
        "id": order_id,
        "userId": order.userId,
        "itemId": order.itemId,
        "qty": order.qty
    }
    ORDERS.append(new_order)
    return {"id": order_id}