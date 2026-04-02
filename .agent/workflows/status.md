---
description: Проверка состояния проекта и окружения
---
// turbo-all

1. Читаем статус из memory.json.

```powershell
Get-Content "e:\Downloads\--ANTIGRAVITY store\IDE-optimus\PROJECT\memory.json" | ConvertFrom-Json
```

2. Проверяем доступность Python и Go.

```powershell
python --version
go version
```

3. Проверка свободного места.

```powershell
Get-PSDrive C | Select-Object Free, Used
```
