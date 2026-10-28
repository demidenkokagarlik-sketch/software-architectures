from app.domain.models import Product
from app.infrastructure.repository import PostgresProductRepository

class ListProducts:
    def __init__(self, repo: PostgresProductRepository):
        self.repo = repo

    def execute(self) -> list[Product]:
        return self.repo.list_products()

class CreateProduct:
    def __init__(self, repo: PostgresProductRepository):
        self.repo = repo

    def execute(self, name: str, price: float) -> Product:
        product = Product(id=None, name=name, price=price)
        return self.repo.create_product(product)