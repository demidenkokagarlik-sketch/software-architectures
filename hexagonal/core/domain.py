import uuid

class Order:
    def __init__(self, sku: str, qty: int, order_id: str = None):
        if not sku or len(sku.strip()) == 0:
            raise ValueError("SKU cannot be empty")
        if qty <= 0:
            raise ValueError("Quantity must be greater than 0")
        
        self.id = order_id or str(uuid.uuid4())
        self.sku = sku
        self.qty = qty