import os
from hexagonal.adapters.db.postgres_repo import PostgresOrderRepository
from hexagonal.adapters.file.csv_repo import CsvOrderRepository
from hexagonal.core.ports import OrderRepository

def get_order_repository() -> OrderRepository:
    adapter_type = os.getenv("REPO_ADAPTER", "db")
    if adapter_type == "file":
        return CsvOrderRepository()
    return PostgresOrderRepository()