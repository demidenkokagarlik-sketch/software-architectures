import os
import psycopg2
from app.domain.models import Product

class PostgresProductRepository:
    def __init__(self):
        self.conn_params = {
            "host": os.getenv("DB_HOST", "db"),
            "port": os.getenv("DB_PORT", "5432"),
            "database": os.getenv("DB_NAME", "shop"),
            "user": os.getenv("DB_USER", "shop"),
            "password": os.getenv("DB_PASS", "shop")
        }

    def _get_connection(self):
        return psycopg2.connect(**self.conn_params)

    def list_products(self) -> list[Product]:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, price FROM products;")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [Product(id=row[0], name=row[1], price=float(row[2])) for row in rows]

    def create_product(self, product: Product) -> Product:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO products (name, price) VALUES (%s, %s) RETURNING id;",
            (product.name, product.price)
        )
        product_id = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()
        product.id = product_id
        return product