---
description: Отправка уведомления или файлов в Telegram бот
---
// turbo-all

1. Проверка наличия расширения для уведомлений.

```powershell
pip install requests
```

2. Запуск скрипта отправки (требуется TOKEN и CHAT_ID в .env).

```powershell
python "e:\Downloads\--ANTIGRAVITY store\IDE-optimus\PROJECT\telegram_notify.py" --message "NEXUS: Система оптимизирована. Текущая RAM: $(Get-Process | Measure-Object -Property WorkingSet -Sum | Select-Object -ExpandProperty Sum) bytes"
```
