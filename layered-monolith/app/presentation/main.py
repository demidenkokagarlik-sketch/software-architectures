from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Shop Monolith API")

class ProductCreateDTO(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/products")
def list_products():
    return [{"id": 1, "name": "Desk", "price": 199.9}]

@app.post("/products", status_code=status.HTTP_201_CREATED)
def create_product(dto: ProductCreateDTO):
    return {"id": 1, "name": dto.name, "price": dto.price}