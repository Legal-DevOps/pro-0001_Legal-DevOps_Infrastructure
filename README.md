# ⚖️ Legal-DevOps Infrastructure
>
> **Law as Code. Data as State. Justice as a Process.**

Система автоматизированного управления сложными юридическими кейсами.  
Построена на принципах DevOps: каждое дело — это проект с базой данных, задачами, историей и дашбордом.

---

## 🧠 Архитектура: Мультиагентная Система (MAS)

Проект управляется **5 специализированными агентами**, каждый со своей областью ответственности:

| AGT | Агент | Роль | Файл |
|:---:|:---|:---|:---|
| AGT-000 | **NEXUS Orchestrator** | Декомпозиция, приоритизация, маршрутизация | `NEXUS_ORCHESTRATOR.py` |
| AGT-001 | **Legal Analyst** | Chain-of-Thought анализ, Hallucination Guard | *(режим Nexus)* |
| AGT-002 | **Archivist** | SHA256-верификация, JSON-память, контекст | `archivarius_core.py` |
| AGT-003 | **Comms Agent** | Telegram/Email, HITL-контроль перед отправкой | `send_dna_to_telegram.py` |
| AGT-004 | **Psychology Analyst** | Тональность ответов, тактика переговоров | `analyze_response.py` |

Манифест всех агентов с промпт-инструкциями: [`agents_manifest.json`](./agents_manifest.json)

---

## 📂 Структура Проекта

```
pro-0001_Legal-DevOps_Infrastructure/
│
├── 📊 dashboard.html              ← Точка входа (открыть в браузере)
├── 🤖 NEXUS_ORCHESTRATOR.py       ← Центральный диспетчер системы
├── 🧱 archivarius_core.py         ← Движок архива и рендерер дашборда
├── 🔍 analyze_response.py         ← AGT-004: Психологический анализ (NEW)
├── 📋 legal_questionnaire.py      ← Ассистент-опросник для сбора фактов
├── 📦 setup_dashboard.py          ← Инициализация задач и сборка UI
├── 🔢 renumber_docs.py            ← Нумерация документов архива
├── 📡 send_dna_to_telegram.py     ← Отправка документов в Telegram
├── 📜 agents_manifest.json        ← Манифест мультиагентной системы
├── 📘 MODERNIZATION_ROADMAP.md    ← Дорожная карта развития
│
├── archive/
│   └── 0001/                      ← Кейс #0001 (активный)
│       ├── dashboard.html         ← Premium Dashboard 2.0
│       ├── database/
│       │   ├── case_info.json     ← Основная информация о деле
│       │   ├── parties.json       ← Участники (стороны, свидетели)
│       │   ├── tasks.json         ← Задачи с дедлайнами и статусами
│       │   └── history.json       ← Полный журнал событий (audit trail)
│       ├── final_output/          ← 24 пронумерованных документа (001–024)
│       ├── plan/                  ← Стратегии и планы действий
│       ├── logs/                  ← Логи агентов (psych_analysis_log.json)
│       └── raw_data/              ← Исходные данные и улики
│
└── database/
    ├── government_registry.json   ← Реестр госорганов Украины
    └── ngo_registry.json          ← Реестр НКО и правозащитных организаций
```

---

## 🚀 Быстрый Старт (NEXUS CLI)

Все команды доступны через единую точку входа — `nexus.py`:

```powershell
# Список всех кейсов с прогрессом
python nexus.py cases

# Детальный статус кейса (задачи, участники, документы, дедлайны)
python nexus.py status 0001

# Пересобрать Dashboard
python nexus.py dashboard

# Анализ ответа госоргана (AGT-004: психоанализ)
python nexus.py analyze --file "path/to/letter.txt"

# Отправить документ в Telegram (с HITL-подтверждением)
python nexus.py send --case 0001 --doc 004

# Проверка целостности кейса (SHA256, файлы, JSON)
python nexus.py audit 0001

# Интерактивный опросник для сбора фактов
python nexus.py questionnaire

# Полная сборка системы
python nexus.py assembly
```

> Старые команды (`python setup_dashboard.py`, `python analyze_response.py` и т.д.) по-прежнему работают.

---

## 📊 Dashboard 2.0 — Возможности

| Функция | Описание |
|:---|:---|
| 🔍 **Поиск в реальном времени** | Мгновенная фильтрация по всем задачам и документам |
| 📊 **Прогресс-бар дела** | Визуальный индикатор `done/total` задач |
| 🔥 **Дедлайн-индикаторы** | Автоматически: `🔥 Горит! 3д`, `⚠️ Скоро`, `🚨 Просрочено` |
| 🚨 **Приоритет-бейджи** | `CRITICAL` / `HIGH` / `NORMAL` с цветовой кодировкой |
| 🗄️ **Evidence Vault** | Реестр всех 24 документов с SHA256-хешами |
| 📋 **Копировать RU/UA** | Мгновенное копирование текста документа в буфер |
| 📥 **Скачать MD** | Скачивание Markdown-файла прямо из карточки |
| 📱 **Telegram Push** | Отправка документов через бота одной командой |

---

## 🗄️ Evidence Vault (Реестр Документов)

Все документы в `final_output/` пронумерованы по стандарту `NNN_NAME.md`:

| № | Документ | Назначение |
|:---:|:---|:---|
| 001 | `Legal_Brief_Template_EN` | Стандартный правовой бриф |
| 002 | `Official_Inquiry_Gov` | Запрос в государственные реестры |
| 003 | `Court_Appeal_Draft` | Черновик досудебной претензии |
| 004 | `International_Appeal_EN` | Апелляция в международные инстанции |

---

## 🤖 AGT-004: Психологический Анализатор

Определяет **тональность** ответа госоргана и даёт стратегию переговоров:

```
🔴 HOSTILE     → Тактика: De-escalation + Правовой Щит
🟠 DEFENSIVE   → Тактика: Сужение запроса + Ответственность  
🟡 BUREAUCRATIC→ Тактика: Контроль дедлайна + Эскалация
🔵 NEUTRAL     → Тактика: Уточнение + Предоставление данных
🟢 COOPERATIVE → Тактика: Ускорение + Фиксация договоренности
```

Дополнительно: **детектор манипуляций** (атака на статус, блокирование, перекладывание).

---

## 🛡️ Принципы Безопасности

- **HITL (Human-in-the-Loop)**: любая отправка в госорган требует явного подтверждения
- **SHA256 Verification**: все финальные документы имеют хеш-подпись для гарантии неизменности
- **Audit Trail**: каждое действие логируется в `history.json` с timestamp
- **Env Variables**: API-ключи хранятся только в `.env`, не в коде

---

## 📋 Ролевая Карта Участников

| Роль | Имя | Контакт |
|:---|:---|:---|
| Subject | [Client ID / Name] | [Encrypted Contact] |
| Defendant | [Corporate / Entity Name] | [Legal Dep. Email] |
| Witness | [Witness / Agent ID] | [Verified Contact] |

---

## 🗺️ Дорожная Карта

Подробнее: [`MODERNIZATION_ROADMAP.md`](./MODERNIZATION_ROADMAP.md)

- [ ] **Phase Alpha**: NLP-парсер входящих PDF/фото документов
- [ ] **Phase Beta**: Multi-Case Manager (параллельные дела 0002, 0003...)
- [ ] **Phase Gamma**: Auto-Deadline Notifier через Telegram бота

---

*Powered by **Antigravity Nexus** | Legal-DevOps v2.0 | 2026*
