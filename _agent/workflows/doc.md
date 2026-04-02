---
description: Генерация технической документации по текущему кейсу или проекту Legal-DevOps
---

# /doc — Technical Documentation Generator (Legal-DevOps)

Генерация структурированной технической документации по кейсу или всему проекту.

### 1. Определить scope

Агент должен определить, что документировать:
- Конкретный кейс (`PROJECT/LEGAL_DEVOPS/case-NNNN/`)
- Весь проект (общая архитектура)

### 2. Собрать данные

Автоматически сканируются:
- `PROJECT/CONSTITUTION.md` — архитектурные правила
- `PROJECT/fault_registry.json` — известные ошибки
- `.agents/skills/` — доступные навыки
- `.agents/workflows/` — доступные воркфлоу
- Скрипты в корне (`gen_*.py`, `legal_*.py`)
- Шаблоны в `templates/`

### 3. Сгенерировать документ

Результат — файл `PROJECT/DOCS/TECHNICAL_BRIEF.md` содержит:

- **Architecture Overview**: Структура проекта и зависимости.
- **Active Skills**: Список навыков из `.agents/skills/`.
- **Script Map**: Все активные скрипты, сгруппированные по назначению.
- **Case Summary**: Краткое описание активных юридических кейсов.
- **Known Issues**: Из `fault_registry.json`.

### 4. Финализация

Вывод готового документа и сохранение в `PROJECT/DOCS/`.
