---
description: Запуск тестов и проверка качества кода
---
---
description: Запуск тестов и проверка качества кода (Legal-DevOps)
---
// turbo-all

1. Поиск и запуск тестов Python в папке PROJECT.

```powershell
python -m unittest discover -s "e:\Downloads\--ANTIGRAVITY store\pro-0001_Legal-DevOps_Infrastructure\PROJECT\LEGAL_DEVOPS\scripts" -p "test_*.py"
```

2. Выполнение базовой проверки синтаксиса всех скриптов.

```powershell
Get-ChildItem -Path "e:\Downloads\--ANTIGRAVITY store\pro-0001_Legal-DevOps_Infrastructure\PROJECT\LEGAL_DEVOPS\scripts\*.py" | ForEach-Object { python -m py_compile $_.FullName }
```

3. Тестирование завершено.
