import os
import json
import time
from kafka import KafkaConsumer, KafkaProducer

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")

print("Notifications Service starting...")
time.sleep(15)

consumer = KafkaConsumer(
    'payment.events',
    bootstrap_servers=[KAFKA_BROKER],
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='notif-group'
)

producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BROKER],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("Notifications Service listening for payment events...")

for message in consumer:
    event = message.value
    if event.get("event") == "PaymentCaptured":
        order_id = event["orderId"]
        print(f"[Notifications] Sending Email for orderId: {order_id}, Amount: {event['amount']}")
        
        # Публікація фінальної події EmailSent
        email_event = {
            "event": "EmailSent",
            "orderId": order_id,
            "to": "user@example.com",
            "ts": event["ts"]
        }
        producer.send("notifications.events", email_event)
        producer.flush()
        print(f"[Notifications] EmailSent event published for orderId: {order_id}")