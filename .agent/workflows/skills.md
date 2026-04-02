---
description: Управление Skill-Vault — просмотр, создание и активация навыков NEXUS
---

// turbo-all

Этот воркфлоу открывает доступ к хранилищу навыков NEXUS Skill Vault.

1. Просмотр существующих навыков.

```powershell
Get-ChildItem -Path "e:\Downloads\--ANTIGRAVITY store\pro-0001_Legal-DevOps_Infrastructure\PROJECT\NEXUS-Skill-Vault\skills" -Directory | Select-Object Name
```

2. Просмотр конкретного навыка (замените <SkillName>).

```powershell
Get-Content "e:\Downloads\--ANTIGRAVITY store\pro-0001_Legal-DevOps_Infrastructure\PROJECT\NEXUS-Skill-Vault\skills\<SkillName>\SKILL.md"
```

3. Чтобы создать новый навык — активировать Skill-Genesis.
