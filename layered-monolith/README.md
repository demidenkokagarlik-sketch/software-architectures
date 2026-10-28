# Layered Monolith (Багатошарова архітектура)

Класична багатошарова архітектура з чітким розподілом відповідальності за шарами: `Presentation -> Application -> Domain -> Infrastructure`.

## Структура шарів:
- **`app/presentation/`** — контролери, роути та точка входу (FastAPI).
- **`app/application/`** — бізнес-логіка та сценарії використання (use cases).
- **`app/domain/`** — доменні моделі та бізнес-правила.
- **`app/infrastructure/`** — робота з базою даних, репозиторії та міграції.

## Запуск:
```bash
docker compose up --build