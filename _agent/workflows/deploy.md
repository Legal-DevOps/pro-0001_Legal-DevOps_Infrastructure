---
description: Деплой проекта из PROJECT/ в BotCommander (→ localhost:9999)
---
1. Проверка готовности инфраструктуры.

```powershell
if (Test-Path "e:\Downloads\--ANTIGRAVITY store\IDE-optimus\PROJECT\NEXUS-orchestrator") { echo "Orchestrator OK" }
```

2. Запуск симуляции деплоя (имитация сборки и переноса).

```powershell
echo "Building NEXUS artifacts..."
echo "Scaling up to Turbo Prod..."
```

3. Проект доступен по адресу localhost:9999 (Simulated).
