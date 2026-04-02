---
description: Generate a comprehensive technical description of a legal-devops project
---

This workflow automates the creation of a "Technical Architecture & State" document for a specific project vault. It summarizes the vault's anatomy, data structures, and current pipeline status.

### 1. Identify Target Case

Choose the Case ID for which you want to generate the technical description.
// turbo

```powershell
python nexus.py cases
```

### 2. Deep Scan & Audit

Verify the integrity of the project before documenting its state.
// turbo

```powershell
python nexus.py audit <CASE_ID>
```

### 3. Generate Description

The agent will now analyze the database files (`case_info.json`, `project_manifest.json`, `tasks.json`) and the directory structure to produce a `PROJECT_TECH_SPEC.md` inside the project folder.

**The document will include:**

- **Vault Anatomy**: File map and SHA256 hash tracking.
- **Data Schema**: Summary of parties, roles, and logical connections.
- **Pipeline Progress**: Completed vs. pending document generations.
- **Risk Assessment**: Technical and legal blockers identified by the system.

### 4. Finalize Artifact

Write the generated content to:
`archive/<CASE_ID>/PROJECT_TECH_SPEC.md`
