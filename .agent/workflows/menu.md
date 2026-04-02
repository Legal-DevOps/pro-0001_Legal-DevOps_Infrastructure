---
description: Показать все доступные команды и воркфлоу
---
// turbo-all

1. Вывод списка всех доступных команд из папки воркфлоу.

```powershell
Get-ChildItem -Path "e:\Downloads\--ANTIGRAVITY store\IDE-optimus\.agents\workflows" -Filter *.md | Select-Object Name, @{Name='Description';Expression={(Get-Content $_.FullName | Select-String "description:").Line.Split(':')[1].Trim()}}
```

2. Для запуска используйте "/" + имя команды.
