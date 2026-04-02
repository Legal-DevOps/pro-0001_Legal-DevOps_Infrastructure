---
description: Switch between legal cases or initialize a new one (context management)
---

This workflow helps you manage your active project context. You can see available cases, switch to a specific one, or start a new "Case Vault" from scratch.

### 1. Identify Existing Cases

Run this command to see all currently registered cases in your infrastructure.
// turbo

```powershell
python nexus.py cases
```

### 2. Switch Context

To "load" the context of a specific case and see its current status, deadlines, and risks:
// turbo

```powershell
python nexus.py status <CASE_ID_HERE>
```

### 3. Initialize New Case

If you want to start "from the beginning" with a completely new case, run the interactive questionnaire. This will create a new ID and directory structure.
// turbo

```powershell
python nexus.py questionnaire
```

### 4. Cold Start: Scenario 0000 (The Origin)

To start a completely fresh context using the **Master Template (0000)**, use this shortcut. This is ideal for a totally "clean slate" start.
// turbo

```powershell
python nexus.py status 0000
```

### 5. Build/Rebuild Project

After switching context or updating data, use the orchestrator to ensure all documents and dashboards are in sync.
// turbo

```powershell
python nexus.py assembly <CASE_ID_HERE>
```
