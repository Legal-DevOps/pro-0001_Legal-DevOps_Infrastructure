---
description: Создание резервной копии критических файлов проекта
---
// turbo-all

1. Создаем папку для бэкапов.

```powershell
New-Item -ItemType Directory -Force -Path "e:\Downloads\--ANTIGRAVITY store\IDE-optimus\BACKUPS"
```

2. Копируем ключевые файлы с временной меткой.

```powershell
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$target = "e:\Downloads\--ANTIGRAVITY store\IDE-optimus\BACKUPS\$timestamp"
New-Item -ItemType Directory -Force -Path $target
Copy-Item -Path "e:\Downloads\--ANTIGRAVITY store\IDE-optimus\PROJECT\memory.json", "e:\Downloads\--ANTIGRAVITY store\IDE-optimus\START.md", "e:\Downloads\--ANTIGRAVITY store\IDE-optimus\PROJECT\NEXUS-TURBO.py" -Destination $target
```

3. Бэкап завершен.
