from hexagonal.core.domain import Order
from hexagonal.core.ports import OrderRepository

class CreateOrderUseCase:
    def __init__(self, repo: OrderRepository):
        self.repo = repo

    def execute(self, sku: str, qty: int) -> str:
        order = Order(sku=sku, qty=qty)
        return self.repo.create(order)

class GetOrderUseCase:
    def __init__(self, repo: OrderRepository):
        self.repo = repo

    def execute(self, order_id: str) -> Order | None:
        return self.repo.get_by_id(order_id)