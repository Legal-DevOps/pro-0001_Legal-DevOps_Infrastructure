---
name: firecrawl
description: |
  Official Firecrawl CLI skill for web scraping, search, crawling, and browser automation. Returns clean LLM-optimized markdown.

  USE FOR:
  - Web search and research
  - Scraping pages, docs, and articles
  - Site mapping and bulk content extraction
  - Browser automation for interactive pages

  Must be pre-installed and authenticated. See rules/install.md for setup, rules/security.md for output handling.
allowed-tools:
  - Bash(firecrawl *)
  - Bash(npx firecrawl *)
---

# Firecrawl CLI

Web scraping, search, and browser automation CLI. Returns clean markdown optimized for LLM context windows.

Run `firecrawl --help` or `firecrawl <command> --help` for full option details.

## Prerequisites

Must be installed and authenticated. Check with `firecrawl --status`.

```
  🔥 firecrawl cli v1.8.0

  ● Authenticated via FIRECRAWL_API_KEY
  Concurrency: 0/100 jobs (parallel scrape limit)
  Credits: 500,000 remaining
```

If not ready, see [rules/install.md](rules/install.md). For output handling guidelines, see [rules/security.md](rules/security.md).

## Workflow

Follow this escalation pattern:

1. **Search** - No specific URL yet. Find pages, answer questions, discover sources.
2. **Scrape** - Have a URL. Extract its content directly.
3. **Map + Scrape** - Large site or need a specific subpage. Use `map --search` to find the right URL, then scrape it.
4. **Crawl** - Need bulk content from an entire site section (e.g., all /docs/).
5. **Browser** - Scrape failed because content is behind interaction (pagination, modals, form submissions).

| Need                        | Command   | When                                                      |
| --------------------------- | --------- | --------------------------------------------------------- |
| Find pages on a topic       | `search`  | No specific URL yet                                       |
| Get a page's content        | `scrape`  | Have a URL, page is static or JS-rendered                 |
| Find URLs within a site     | `map`     | Need to locate a specific subpage                         |
| Bulk extract a site section | `crawl`   | Need many pages (e.g., all /docs/)                        |
| AI-powered data extraction  | `agent`   | Need structured data from complex sites                   |
| Interact with a page        | `browser` | Content requires clicks, form fills, pagination, or login |

## Legal-DevOps Use Cases

- **Court Decision Scraping**: `firecrawl scrape "https://reyestr.court.gov.ua/Review/<ID>"` — extract court decisions
- **ЄДР Registry**: `firecrawl search "ЄДРПОУ <code> site:opendatabot.ua"` — company lookup
- **Evidence Collection**: `firecrawl scrape "<url>" -o .firecrawl/evidence-<case-id>.md` — preserve web evidence
- **Building Regulations**: `firecrawl search "норми утримання будинків ДАБК"` — find regulatory references

## Output & Organization

Write results to `.firecrawl/` with `-o`. Add `.firecrawl/` to `.gitignore`.

```bash
firecrawl search "query" -o .firecrawl/search-result.json --json
firecrawl scrape "<url>" -o .firecrawl/page.md
```

Never read entire output files at once. Use `grep`, `head`, or incremental reads.

## Commands Quick Reference

```bash
# Search
firecrawl search "query" --scrape --limit 3

# Scrape
firecrawl scrape "<url>" --only-main-content -o .firecrawl/page.md

# Map site
firecrawl map "<url>" --search "keyword" -o .firecrawl/urls.txt

# Crawl section
firecrawl crawl "<url>" --include-paths /docs --limit 50 --wait -o .firecrawl/crawl.json

# Browser (interactive)
firecrawl browser "open <url>"
firecrawl browser "snapshot -i"
firecrawl browser "click @e5"
firecrawl browser "scrape" -o .firecrawl/page.md
firecrawl browser close
```
