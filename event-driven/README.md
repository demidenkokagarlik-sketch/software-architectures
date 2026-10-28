# Event-Driven Architecture (Kafka)

Асинхронна взаємодія сервісів через брокер повідомлень Apache Kafka.

## Сервіси та топіки:
- **orders**: приймає POST /orders, публікує подію `OrderCreated` в топік `orders.events`.
- **billing**: споживає `orders.events`, забезпечує ідемпотентність, публікує `PaymentCaptured` в `payment.events`.
- **notifications**: споживає `payment.events`, імітує відправку email, публікує `EmailSent`.

## Перевірка:
```bash
curl -X POST localhost:5002/orders -d '{"userId":1,"itemId":2,"qty":1}' -H 'Content-Type: application/json'