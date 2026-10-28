# Microservices + API Gateway Architecture

Архітектура складається з трьох незалежних мікросервісів (`catalog`, `users`, `orders`) та NGINX як єдиної точки входу (API Gateway)[cite: 5].

## Сервіси та маршрути (через Gateway на порт 8080):
- **Catalog Service**: `GET /catalog/items` — отримує список товарів[cite: 5].
- **Users Service**: `GET /users/:id` — отримує інформацію про користувача[cite: 5].
- **Orders Service**: `POST /orders` — створює нове замовлення[cite: 5].

## Перевірка:
```bash
# Отримати список товарів через шлюз
curl http://localhost:8080/catalog/items

# Створити замовлення через шлюз
curl -X POST http://localhost:8080/orders -H 'Content-Type: application/json' -d '{"userId":1,"itemId":1,"qty":1}'