---
description: Запуск Agnostic Architecture Workflow — глубокий сравнительный анализ технологий без привязки к стеку NEXUS.
---
// turbo-all

Этот воркфлоу отключает приоритет предустановленного стека (Python/Go) и заставляет систему действовать как независимый технический архитектор.

1. **Extraction of Hard Requirements**:
   Я анализирую задачу из `START.md` по следующим критериям:
   - **Scale**: Ожидаемое количество пользователей/запросов.
   - **Complexity**: Уровень сложности логики (CRUD vs AI vs Real-time).
   - **Environment**: Ограничения ОС, железа и сети.
   - **Legacy**: Необходимость интеграции с существующим кодом.

2. **Technology Matrix Generation**:
   Я формирую таблицу-сравнение для 3-х альтернативных подходов (например: Java/Spring, Node.js/Fastify, Rust/Axum), игнорируя стандартный NEXUS-пакет.

3. **Trade-offs Analysis (The Matrix)**:
   Для каждого варианта я провожу оценку:
   - **Speed of Development** (от 1 до 10).
   - **Runtime Performance** (Latency/Throughput).
   - **Maintainability** (Сложность поддержки).
   - **Ecosystem Maturity** (Наличие готовых библиотек).

4. **Architecture Decision Record (ADR) + Hardware Spec**:
   Я генерирую файл `AGNOSTIC_ADR.md`, который содержит:
   - **Context**: Почему мы проводим анализ.
   - **Options**: Описание предложенных стеков.
   - **Decision**: Обоснованный выбор конкретного стека.
   - **Hardware Requirement Specification**:
     - *Minimum*: Минимальное железо для запуска (Low-load).
     - *Recommended*: Железо для целевой нагрузки (Target 100k msg/s).
     - *System Configuration*: Параметры ОС (число дескрипторов, размер страниц памяти и т.д.).
   - **Consequences**: Что мы выигрываем и чем жертвуем.

5. **Approval Strategy**:
   Воркфлоу останавливается и запрашивает подтверждение выбранного ADR перед написанием первой строки кода.

Для активации введите `/agnostic` после описания задачи.
