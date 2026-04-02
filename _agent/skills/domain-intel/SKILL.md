---
name: domain-intel
description: |
  Passive domain reconnaissance — subdomains, SSL certs, WHOIS, DNS records, domain availability.
  Zero dependencies, zero API keys. Pure Python stdlib. Works on Windows, Linux, macOS.

  USE FOR:
  - Subdomain discovery via Certificate Transparency logs (crt.sh)
  - SSL certificate inspection (expiry, cipher, SANs, issuer)
  - WHOIS lookup (registrar, registration dates, name servers)
  - DNS records (A, AAAA, MX, NS, TXT, CNAME)
  - Domain availability checks (passive: DNS + WHOIS + SSL signals)
  - Bulk multi-domain analysis
  - Legal-DevOps OSINT investigations (corporate domain mapping)

version: 1.1.0
author: NousResearch/hermes-agent (ported to NEXUS by Antigravity)
license: MIT
metadata:
  hermes:
    tags: [osint, domain, dns, whois, ssl, recon, legal-devops]
    category: research
    related_skills: [osint-tactician]
---

# Domain Intelligence — Passive OSINT

Passive domain reconnaissance using only Python stdlib.
**Zero dependencies. Zero API keys. Works on Windows (PowerShell + Python).**

## When to Use

- User asks: "найди поддомены example.com", "проверь SSL сертификат", "кому принадлежит домен"
- Legal-DevOps task: mapping corporate infrastructure for a case
- Checking domain availability before registering
- Passive pre-engagement recon before OSINT investigation

## Helper Script

This skill includes `scripts/domain_intel.py`. Run via:

```powershell
# Subdomain discovery via Certificate Transparency logs
python ".agents\skills\domain-intel\scripts\domain_intel.py" subdomains example.com

# SSL certificate inspection
python ".agents\skills\domain-intel\scripts\domain_intel.py" ssl example.com

# WHOIS lookup
python ".agents\skills\domain-intel\scripts\domain_intel.py" whois example.com

# DNS records
python ".agents\skills\domain-intel\scripts\domain_intel.py" dns example.com

# Domain availability check
python ".agents\skills\domain-intel\scripts\domain_intel.py" available coolstartup.io

# Bulk analysis
python ".agents\skills\domain-intel\scripts\domain_intel.py" bulk example.com github.com --checks ssl,dns
```

All output is structured JSON.

## Available Commands

| Command      | What it does                              | Data source                       |
|--------------|-------------------------------------------|-----------------------------------|
| `subdomains` | Find subdomains from certificate logs     | crt.sh (HTTPS)                    |
| `ssl`        | Inspect TLS certificate details           | Direct TCP:443 to target          |
| `whois`      | Registration info, registrar, dates       | WHOIS servers (TCP:43)            |
| `dns`        | A, AAAA, MX, NS, TXT, CNAME records      | System DNS + Google DoH           |
| `available`  | Check if domain is registered             | DNS + WHOIS + SSL signals         |
| `bulk`       | Run multiple checks on multiple domains   | All of the above                  |

## Pitfalls

- WHOIS queries use TCP:43 — may be blocked on restrictive networks
- Some WHOIS servers redact registrant info (GDPR) — notify user
- crt.sh can be slow for very popular domains (thousands of certs)
- Availability check is heuristic-based (3 passive signals) — not authoritative
- On Windows: use `python` not `python3`
- `.ua` domains supported (whois.ua)

---
*Ported from NousResearch/hermes-agent by Antigravity NEXUS.*
