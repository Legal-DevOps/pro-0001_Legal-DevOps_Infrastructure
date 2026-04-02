---
description: Initialize a new legal case with a sequential ID
---

This command triggers the creation of a brand new project vault. The system will automatically assign the next available ID.

### ➕ Action: Start New Case

Run the interactive discovery protocol to set up the new context.
// turbo

```powershell
python nexus.py questionnaire
```

### Steps

1. **Assign ID**: System checks current `archive/` folders and increments the ID.
2. **Structure**: Folders `database`, `final_output`, `logs`, and `plan` will be created.
3. **Primary Manifest**: `project_manifest.json` will be initialized with your input.
4. **Active State**: The session will immediately switch focus to this new Case ID.
