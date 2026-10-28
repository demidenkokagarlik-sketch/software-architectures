from fastapi import FastAPI

app = FastAPI(title="Catalog Service")

@app.get("/items")
def get_items():
    return [
        {"id": 1, "name": "Laptop"},
        {"id": 2, "name": "Mouse"}
    ]