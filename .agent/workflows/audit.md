---
description: Поиск секретов и потенциальных уязвимостей в коде
---
---
description: Поиск секретов и потенциальных уязвимостей в коде (Legal-DevOps)
---
// turbo-all

1. Проверка на наличие жестко заданных паролей, API-ключей или токенов.

```powershell
grep -rEi "api_key|password|secret|token|auth" "e:\Downloads\--ANTIGRAVITY store\pro-0001_Legal-DevOps_Infrastructure" --exclude-dir=".venv" --exclude-dir=".agents" --exclude-dir="archive"
```

2. Анализ структуры проекта на наличие лишних папок.

```powershell
Get-ChildItem -Path "e:\Downloads\--ANTIGRAVITY store\pro-0001_Legal-DevOps_Infrastructure" -Depth 1
```

3. Проверка безопасности завершена.
