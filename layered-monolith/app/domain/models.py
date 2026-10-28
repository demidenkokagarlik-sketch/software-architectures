class Product:
    def __init__(self, id: int | None, name: str, price: float):
        if not name or len(name.strip()) == 0 or len(name) > 100:
            raise ValueError("Invalid product name (must be 1-100 chars)")
        if price <= 0:
            raise ValueError("Price must be greater than 0")
        
        self.id = id
        self.name = name
        self.price = price