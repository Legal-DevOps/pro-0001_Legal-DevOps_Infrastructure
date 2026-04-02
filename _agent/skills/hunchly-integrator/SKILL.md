---
name: hunchly-integrator
description: |
  Digital Evidence Preservation framework for OSINT investigations.
  Based on Hunchly methodology — systematic capture, timestamping, and chain-of-custody tracking
  for web-based evidence in legal cases.

  USE FOR:
  - Preserving web evidence before it disappears (screenshots, HTML, metadata)
  - Maintaining chain of custody for digital evidence
  - Organizing OSINT findings per legal case
  - Court-admissible evidence collection workflow

version: 1.0.0
metadata:
  tags: [osint, evidence, forensics, legal, hunchly, chain-of-custody]
  category: forensics
  related_skills: [osint-tactician, domain-intel, firecrawl]
---

# Hunchly Evidence Integrator — Digital Forensics for Legal-DevOps

## Purpose

Systematic preservation of digital evidence for legal cases. Every piece of web-based evidence must be:
1. **Captured** — full page content saved (HTML + screenshot)
2. **Timestamped** — UTC timestamp at moment of capture
3. **Hashed** — SHA-256 hash of the captured file for integrity
4. **Catalogued** — linked to a specific case and investigation thread

## Evidence Capture Workflow

### Step 1: Initialize Case Evidence Directory

```
PROJECT/LEGAL_DEVOPS/case-NNNN/evidence/
├── web/              # Saved web pages (HTML/MD)
├── screenshots/      # Visual captures
├── metadata/         # JSON logs with timestamps and hashes
└── EVIDENCE_LOG.md   # Human-readable evidence index
```

### Step 2: Capture Evidence

Using Firecrawl or manual download:

```bash
# Capture web page
firecrawl scrape "<url>" -o PROJECT/LEGAL_DEVOPS/case-NNNN/evidence/web/evidence-001.md

# Generate timestamp + hash
python -c "
import hashlib, datetime, json, sys
with open(sys.argv[1], 'rb') as f:
    h = hashlib.sha256(f.read()).hexdigest()
meta = {
    'file': sys.argv[1],
    'url': sys.argv[2],
    'captured_at': datetime.datetime.utcnow().isoformat() + 'Z',
    'sha256': h,
    'collector': 'NEXUS Legal-DevOps Agent'
}
with open(sys.argv[3], 'w') as f:
    json.dump(meta, f, indent=2, ensure_ascii=False)
print(json.dumps(meta, indent=2))
" evidence-001.md "https://source-url" metadata/evidence-001.json
```

### Step 3: Log in EVIDENCE_LOG.md

```markdown
| ID | URL | Captured | SHA-256 | Description |
|:---|:----|:---------|:--------|:------------|
| E-001 | https://... | 2026-03-15T11:00:00Z | abc123... | Скриншот рекламного баннера |
```

### Step 4: Verify Integrity

Before submitting to court, verify that no evidence files have been tampered with:

```python
import hashlib, json
with open('metadata/evidence-001.json') as f:
    meta = json.load(f)
with open(meta['file'], 'rb') as f:
    current_hash = hashlib.sha256(f.read()).hexdigest()
assert current_hash == meta['sha256'], "EVIDENCE INTEGRITY COMPROMISED!"
print("✅ Evidence integrity verified")
```

## Chain of Custody Rules

1. **Never modify** original evidence files after capture
2. **Always hash** immediately after download
3. **Log every access** to evidence files
4. **UTC timestamps only** — no local timezone ambiguity
5. **One evidence file = one metadata JSON** — 1:1 mapping

## Integration with Other Skills

- **firecrawl**: Primary capture tool (`scrape`, `browser`)
- **domain-intel**: DNS/WHOIS evidence for domain ownership disputes
- **osint-tactician**: Methodology framework (Direction → Collection → Analysis)
- **legal_osint.py**: Ukrainian registry evidence (ЄДР, court decisions)

## OnionScan Reference

For dark web investigations, the original Hunchly integrator includes OnionScan (Go-based .onion scanner). Source code available in IDE-Optimus at `.agents/skills/hunchly-integrator/source/onionscan/`. Requires Go compiler and Tor. Activate only when explicitly needed.
