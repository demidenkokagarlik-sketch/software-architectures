from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Hexagonal Architecture API")

class OrderCreate(BaseModel):
    sku: str
    qty: int = Field(..., gt=0)

@app.post("/orders", status_code=status.HTTP_201_CREATED)
def create_order(order: OrderCreate):
    return {"id": "ord-123", "sku": order.sku, "qty": order.qty}

@app.get("/orders/{order_id}")
def get_order(order_id: str):
    if order_id != "ord-123":
        raise HTTPException(status_code=404, detail="Order not found")
    return {"id": order_id, "sku": "ABC", "qty": 2}