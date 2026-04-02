# Skill: OSINT-Tactician (Methodology & Forensics)

**OSINT Framework & Evidence Handling**
*Structured methodology based on the Intelligence Cycle and Hunchly principles.*

## Description
This skill provides a structured framework for conducting OSINT investigations within NEXUS Legal-DevOps. It combines the **Intelligence Cycle** (Direction, Collection, Processing, Analysis, Dissemination) with **Forensic Evidence Preservation** principles.

## Capabilities
1.  **Investigation Planning**: Create a structured investigation plan based on target criteria (Email, Domain, Person, Company).
2.  **Evidence Logging**: Guidelines and tools for preserving digital evidence with timestamps and source metadata.
3.  **Methodology Flow**: Step-by-step workflows for:
    *   Corporate Reconnaissance (ЄДР, OpenData, YouControl)
    *   People Discovery (PEP checks, social graphs)
    *   Infrastructure Mapping (DNS/IP/SSL)
    *   Financial Trail Analysis (bank records, transaction patterns)
4.  **Legal Integration**: Evidence collected via this framework is admissible — chain of custody preserved.

## Core Methodology: The OSINT Cycle
1.  **Direction**: Define the investigation goals and legal boundaries.
2.  **Collection**: Gathering raw data from search engines, registries, and technical tools.
3.  **Processing**: Organizing raw data (e.g., converting names to emails, mapping domains to IPs).
4.  **Analysis**: Finding patterns, red flags, and connections.
5.  **Reporting**: Creating the final Dossier/Intelligence Report.

## Tools (Available in this project)
- **`domain-intel`**: Technical domain reconnaissance (subdomains, SSL, WHOIS, DNS).
- **`legal_osint.py`**: Ukrainian legal registry lookups (ЄДР, court decisions).
- **`archivarius_core.py`**: Document archive analysis.

## Usage Guide
When starting a new investigation:
1.  Create case directory in `PROJECT/LEGAL_DEVOPS/case-NNNN/osint/`.
2.  Apply the **Direction** template to define what you are looking for.
3.  Use the **Collection** phase tools to gather data.
4.  Generate an **Intelligence Report** as structured Markdown.
5.  Validate evidence chain before including in legal documents.
