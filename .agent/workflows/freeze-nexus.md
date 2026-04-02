---
description: Freeze current project settings and workflows into the global Nexus Blueprint
---

Этот ворклоу обновляет центральный шаблон Nexus (Blueprint) на основе текущего проекта.

1. Синхронизирует `START.md`, `AGNOSTIC_ADR.md` и `PROJECT/memory.json`.
2. Копирует все ворклоу из `.agents/workflows/`.
3. Копирует основные скиллы.

// turbo
python "e:\Downloads\--ANTIGRAVITY store\IDE-optimus\PROJECT\scripts\freeze_nexus.py"
