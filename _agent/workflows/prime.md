---
description: Запуск режима "Nexus Prime" — выход за рамки Gemini MD для автономного управления системой и проектом
---
// turbo-all

Этот воркфлоу активирует расширенные возможности Antigravity Nexus Prime, объединяя системный контроль, автономную разработку и внешние интеграции.

1. **Анализ Хаоса (Pillar 4)**:
   Сканирование текущей директории и ресурсов системы для определения оптимального пути.

   ```powershell
   # Проверка ресурсов и структуры проекта
   Write-Host "--- SYSTEM AUDIT ---"
   Get-Process | Sort-Object CPU -Descending | Select-Object -First 5
   Get-PSDrive -PSProvider FileSystem
   Write-Host "--- PROJECT STRUCTURE ---"
   Get-ChildItem -Recurse -Depth 2
   ```

2. **Генерация Концепта (Pillar 2 & 3)**:
   Я создаю файл `PRIME_CONCEPT.md` с тремя вариантами реализации, включая:
   - Сценарий автоматизации Windows (PowerShell/Services).
   - Сценарий контейнеризации (Docker/Scale).
   - Интеграционный сценарий (API/Bots/Dashboards).

3. **Autonomous Execution (Pillar 2)**:
   После выбора варианта я приступаю к реализации с использованием принципа **Zero-Guessing**:
   - Написание кода (Python/Go/PS).
   - Самостоятельный запуск и исправление ошибок (Self-Correction).
   - Валидация через логи и скриншоты.

4. **Документирование и Снапшот**:
   Обновление `memory.json` и создание инструкции по эксплуатации.

Для активации просто опиши общую идею в `START.md` и введи `/prime`.
