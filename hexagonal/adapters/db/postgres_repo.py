import os
import psycopg2
from hexagonal.core.domain import Order
from hexagonal.core.ports import OrderRepository

class PostgresOrderRepository(OrderRepository):
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

    def create(self, order: Order) -> str:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO orders (id, sku, qty) VALUES (%s, %s, %s);",
            (order.id, order.sku, order.qty)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return order.id

    def get_by_id(self, order_id: str) -> Order | None:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, sku, qty FROM orders WHERE id = %s;", (order_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if not row:
            return None
        return Order(order_id=row[0], sku=row[1], qty=row[2])