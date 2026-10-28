import os
import json
import time
from datetime import datetime
from kafka import KafkaConsumer, KafkaProducer

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")

# Ідемпотентність: зберігаємо оброблені ID подій в пам'яті
processed_events = set()

print("Billing Service starting, waiting for Kafka...")
time.sleep(10) # пауза для стабілізації кафки

consumer = KafkaConsumer(
    'orders.events',
    bootstrap_servers=[KAFKA_BROKER],
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='billing-group'
)

producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BROKER],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("Billing Service listening for events...")

for message in consumer:
    event = message.value
    if event.get("event") == "OrderCreated":
        order_id = event["orderId"]
        
        # Перевірка на ідемпотентність
        if order_id in processed_events:
            print(f"[Billing] Duplicate event ignored for orderId: {order_id}")
            continue
            
        processed_events.add(order_id)
        print(f"[Billing] Processing payment for orderId: {order_id}")
        
        # Генерація події PaymentCaptured
        payment_event = {
            "event": "PaymentCaptured",
            "orderId": order_id,
            "amount": event["qty"] * 100,
            "ts": datetime.utcnow().isoformat()
        }
        producer.send("payment.events", payment_event)
        producer.flush()
        print(f"[Billing] PaymentCaptured published for orderId: {order_id}")