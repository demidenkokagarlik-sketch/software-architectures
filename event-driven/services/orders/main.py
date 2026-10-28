import os
import json
from datetime import datetime
from fastapi import FastAPI, status
from pydantic import BaseModel
from kafka import KafkaProducer

app = FastAPI(title="Orders Service (Producer)")

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")
producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BROKER],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

class OrderCreate(BaseModel):
    userId: int
    itemId: int
    qty: int

@app.post("/orders", status_code=status.HTTP_201_CREATED)
def create_order(order: OrderCreate):
    order_id = 101 # спрощений генератор ID для прикладу
    event_data = {
        "event": "OrderCreated",
        "orderId": order_id,
        "userId": order.userId,
        "itemId": order.itemId,
        "qty": order.qty,
        "ts": datetime.utcnow().isoformat()
    }
    
    # Публікуємо подію в Kafka
    producer.send("orders.events", event_data)
    producer.flush()
    
    return {"id": order_id, "status": "OrderCreated event published"}