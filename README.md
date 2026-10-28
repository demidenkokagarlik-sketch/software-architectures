# Програмні архітектури — навчальний проєкт

Проєкт містить чотири окремі приклади реалізації архітектур програмного забезпечення на Python. Кожна папка має власний `README.md`, Dockerfile/Compose, приклади запитів і тести там, де це передбачено завданням.[cite: 1]

## Структура

* `layered-monolith/` — багатошаровий REST API товарів + PostgreSQL, SQL-міграція, DI через application use-cases, multi-stage Dockerfile і юніт-тести.[cite: 1]
* `hexagonal/` — ядро, порт `OrderRepository`, адаптери Postgres/CSV та перемикання через `REPO_ADAPTER`.[cite: 1]
* `microservices/` — Catalog, Users, Orders та NGINX API Gateway, 4 контейнери, healthchecks, OpenAPI і e2e-перевірка.[cite: 1]
* `event-driven/` — Orders producer, Billing consumer, Notifications consumer, Kafka + Zookeeper, створення топіка, SQLite-дедуплікація та JSON Schema подій.[cite: 1]

## Запуск (виконувати команди з відповідної папки)

```bash
cd layered-monolith
docker compose up --build
