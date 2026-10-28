import os
import csv
from hexagonal.core.domain import Order
from hexagonal.core.ports import OrderRepository

class CsvOrderRepository(OrderRepository):
    def __init__(self):
        self.file_path = os.getenv("CSV_PATH", "/data/orders.csv")
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        if not os.path.exists(self.file_path):
            with open(self.file_path, mode="w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["id", "sku", "qty"])

    def create(self, order: Order) -> str:
        with open(self.file_path, mode="a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([order.id, order.sku, order.qty])
        return order.id

    def get_by_id(self, order_id: str) -> Order | None:
        if not os.path.exists(self.file_path):
            return None
        with open(self.file_path, mode="r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["id"] == order_id:
                    return Order(order_id=row["id"], sku=row["sku"], qty=int(row["qty"]))
        return None