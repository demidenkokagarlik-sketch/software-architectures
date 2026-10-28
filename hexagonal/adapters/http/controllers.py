from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from hexagonal.config.container import get_order_repository
from hexagonal.core.usecases import CreateOrderUseCase, GetOrderUseCase

app = FastAPI(title="Hexagonal Architecture API")

repo = get_order_repository()

class OrderCreateDTO(BaseModel):
    sku: str = Field(..., min_length=1)
    qty: int = Field(..., gt=0)

@app.post("/orders", status_code=status.HTTP_201_CREATED)
def create_order(dto: OrderCreateDTO):
    try:
        use_case = CreateOrderUseCase(repo)
        order_id = use_case.execute(sku=dto.sku, qty=dto.qty)
        return {"id": order_id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/orders/{order_id}")
def get_order(order_id: str):
    use_case = GetOrderUseCase(repo)
    order = use_case.execute(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"id": order.id, "sku": order.sku, "qty": order.qty}