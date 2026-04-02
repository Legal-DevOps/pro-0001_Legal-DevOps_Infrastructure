---
description: Сканирование .md файлов на дубликаты и устаревший контент
---
// turbo-all

1. Поиск всех Markdown файлов в проекте.

```powershell
Get-ChildItem -Path "e:\Downloads\--ANTIGRAVITY store\IDE-optimus" -Filter *.md -Recurse
```

2. Анализ файлов на наличие "// TODO" и пустых секций.

```powershell
Select-String -Path "e:\Downloads\--ANTIGRAVITY store\IDE-optimus\*.md" -Pattern "// TODO", "implement"
```

3. Рекомендация по актуализации документации.
