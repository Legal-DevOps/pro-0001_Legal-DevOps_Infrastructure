<div align="center">
  <a href="https://legal-devops.vercel.app/" target="_blank">
    <img src="https://img.shields.io/badge/LIVE_DEMO-legal--devops.vercel.app-10b981?style=for-the-badge&logo=vercel&logoColor=white" alt="Live Demo" />
  </a>
</div>

<br>

# ⚖️ Legal-DevOps Infrastructure

> **Law as Code. Data as State. Justice as a Process.**

An automated management system for complex legal cases.
Built on DevOps principles: every case is treated as a software project with its own isolated database, task tracker, audit trail, and dashboard.

---

## 🧠 Architecture: Multi-Agent System (MAS)

The project is orchestrated by **5 specialized agents**, each handling a specific domain of responsibility:

| AGT | Agent | Role | File |
|:---:|:---|:---|:---|
| AGT-000 | **NEXUS Orchestrator** | Task decomposition, prioritization, and routing | `NEXUS_ORCHESTRATOR.py` |
| AGT-001 | **Legal Analyst** | Chain-of-Thought reasoning, Hallucination Guard | *(Nexus mode)* |
| AGT-002 | **Archivist** | SHA256-verification, JSON-memory, context management | `archivarius_core.py` |
| AGT-003 | **Comms Agent** | Telegram/Email interfacing, pre-send HITL control | `send_dna_to_telegram.py` |
| AGT-004 | **Psychology Analyst** | Bureaucratic tone analysis, negotiation tactics | `analyze_response.py` |

Comprehensive Agent Prompt Manifest: [`agents_manifest.json`](./agents_manifest.json)

---

## 📂 Project Structure

```text
pro-0001_Legal-DevOps_Infrastructure/
│
├── 📊 dashboard.html              ← Entry point (open in browser)
├── 🤖 NEXUS_ORCHESTRATOR.py       ← Central system dispatcher
├── 🧱 archivarius_core.py         ← Archive engine and dashboard renderer
├── 🔍 analyze_response.py         ← AGT-004: Psychological analysis (NEW)
├── 📋 legal_questionnaire.py      ← Interactive assistant for fact gathering
├── 📦 setup_dashboard.py          ← UI and task initialization
├── 🔢 renumber_docs.py            ← Archive document sequencer
├── 📡 send_dna_to_telegram.py     ← Telegram notification relay
├── 📜 agents_manifest.json        ← Multi-Agent System Manifest
├── 📘 MODERNIZATION_ROADMAP.md    ← Development Roadmap
│
├── archive/
│   └── 0001/                      ← Demo Case
│       ├── dashboard.html         ← Premium Dashboard 2.0
│       ├── database/
│       │   ├── case_info.json     ← Core case metadata
│       │   ├── parties.json       ← Stakeholders (Plaintiffs, Witnesses)
│       │   ├── tasks.json         ← Deadlines and task orchestration
│       │   └── history.json       ← Complete event logger (audit trail)
│       ├── final_output/          ← Enumerated output documents (001–024)
│       ├── plan/                  ← Strategic action plans
│       ├── logs/                  ← Agent event logs
│       └── raw_data/              ← Raw evidence files
│
└── database/
    ├── government_registry.json   ← Local Government Registry Config
    └── ngo_registry.json          ← NGO and Human Rights DB
```

---

## 🚀 Quick Start (NEXUS CLI)

All operations are executed through the centralized entry point — `nexus.py`:

```shell
# View all cases and progress
python nexus.py cases

# Detailed case status (tasks, participants, documents, deadlines)
python nexus.py status 0001

# Rebuild operational Dashboard
python nexus.py dashboard

# Parse government response (AGT-004: Psychoanalysis)
python nexus.py analyze --file "path/to/letter.txt"

# Push document via Telegram (with HITL confirmation)
python nexus.py send --case 0001 --doc 004

# Verify case integrity (SHA256, File checks, JSON structural integrity)
python nexus.py audit 0001

# Launch interactive fact-gathering questionnaire
python nexus.py questionnaire

# Execute full system build step
python nexus.py assembly
```

> Legacy command scripts (`python setup_dashboard.py`, `analyze_response.py`, etc.) are still backwards compatible.

---

## 📊 Dashboard 2.0 — Core Features

| Feature | Description |
|:---|:---|
| 🔍 **Real-Time Search** | Instant filtering across all tasks and evidentiary documents |
| 📊 **Case Progress Bar** | Visual indicator for `done/total` task states |
| 🔥 **Deadline Tracking** | Automated states: `🔥 Urgent! 3d left`, `⚠️ Upcoming`, `🚨 Overdue` |
| 🚨 **Priority Badges** | `CRITICAL` / `HIGH` / `NORMAL` color-coded severity metrics |
| 🗄️ **Evidence Vault** | Registry of documents heavily integrated with SHA256 hashes |
| 📋 **Quick Copy** | One-click copy document payload to clipboard |
| 📥 **Download MD** | Download markdown files directly from the execution card |
| 📱 **Telegram Push** | Submits rendered files via Telegram bots in a single execution |

---

## 🗄️ Evidence Vault (Document Registry)

All rendered evidence pieces in `final_output/` follow strict standard formatting `NNN_NAME.md`:

| ID | Document | Purpose |
|:---:|:---|:---|
| 001 | `Legal_Brief_Template_EN` | Standardized foundational legal brief |
| 002 | `Official_Inquiry_Gov` | Inquiry aimed at federal data registries |
| 003 | `Court_Appeal_Draft` | Standardized draft for pre-trial litigation |
| 004 | `International_Appeal_EN` | Specialized layout for international body submission |

---

## 🤖 AGT-004: Psychological Analyzer

Parses the **bureaucratic semantic tone** behind government letters and calculates counter-tactics:

```text
🔴 HOSTILE     → Tactic: De-escalation + Evidentiary Shield
🟠 DEFENSIVE   → Tactic: Scope narrowing + Responsibility assertion
🟡 BUREAUCRATIC→ Tactic: Deadline control + Legal Escalation
🔵 NEUTRAL     → Tactic: Clarification + Additional data provision
🟢 COOPERATIVE → Tactic: Accelerated processing + Agreement lock-in
```

Features embedded **manipulation detectors** (status attack patterns, blockading, and responsibility shifting).

---

## 🛡️ Security Protocol

- **HITL (Human-in-the-Loop)**: Any payload delivery to external entities requires strict manual supervisor execution.
- **SHA256 Verification**: Final documents adopt hash footprints to enforce immutable provenance.
- **Audit Trail**: Every action logged internally to `history.json` complete with Unix timestamps.
- **Env Integrity**: API keys stored securely and solely via ignored `.env` config.

---

## 📋 Stakeholder Role Map

| Role | Alias | Contact Vector |
|:---|:---|:---|
| Subject | [Client ID / Name] | [Encrypted Contact] |
| Defendant | [Corporate / Entity Name] | [Legal Dep. Email] |
| Witness | [Witness / Agent ID] | [Verified Contact] |

---

## 🗺️ Roadmap Array

Development tracking available at: [`MODERNIZATION_ROADMAP.md`](./MODERNIZATION_ROADMAP.md)

- [ ] **Phase Alpha**: Baseline NLP parser for ingestion of physical PDF/Photo documents
- [ ] **Phase Beta**: Multi-Case Context Manager (operating on concurrent branches 0002, 0003...)
- [ ] **Phase Gamma**: Automated Deadline Pinging via customized Telegram Daemons

---

*Powered by **Antigravity Nexus** | Legal-DevOps v4.0 | 2026*
