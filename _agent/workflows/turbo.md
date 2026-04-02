---
description: Мгновенная оптимизация ресурсов (CPU, RAM, Junk)
---
// turbo-all

1. Запускаем NEXUS TURBO для очистки системы.

```powershell
python "e:\Downloads\--ANTIGRAVITY store\IDE-optimus\PROJECT\NEXUS-TURBO.py"
```

2. Проверка текущего состояния ресурсов после очистки.

```powershell
Get-Process | Sort-Object WorkingSet -Descending | Select-Object -First 5 -Property Name, @{Name='WS(MB)';Expression={[math]::Round($_.WorkingSet / 1MB, 2)}}
```
