---
description: Запуск автономного Мета-Оркестратора для анализа и улучшения всех кейсов системы
---

// turbo-all

Этот воркфлоу заставляет агента проанализировать накопленный опыт и применить новые навыки к старым делам.

1. Запуск Автопилота:
```powershell
python "e:\Downloads\--ANTIGRAVITY store\pro-0001_Legal-DevOps_Infrastructure\PROJECT\scripts\nexus_autopilot.py"
```

2. Проверка сгенерированного плана:
```powershell
Get-Content "e:\Downloads\--ANTIGRAVITY store\pro-0001_Legal-DevOps_Infrastructure\PROJECT\AUTOPILOT_PLAN.json"
```

3. Для активации плана — дайте команду "Исполняй Автопилот".
