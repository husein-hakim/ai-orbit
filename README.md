# AIOrbit MCP Data Extraction & Curation Pipeline

## Overview
This repository contains the complete enterprise-grade data extraction, verification, scoring, and curation pipeline for the **Model Context Protocol (MCP)** module of **AIOrbit**. The dataset contains **10,594 verified, high-quality MCP Servers and Clients** across 31 industry categories, strictly adhering to AIOrbit quality benchmarks, 100-point scoring framework, and zero-duplicate guarantees.

---

## Key Metrics & Statistics

| Metric | Value |
|---|---|
| **Total Curated Records** | **10,594** |
| **MCP Servers** | **9,995** |
| **MCP Clients** | **599** |
| **Official Products / Integrations** | 77+ (Anthropic, Microsoft, GitHub, Google, AWS, Cloudflare, Supabase, Neon, Sentry, Linear, Docker, etc.) |
| **Average Quality Score** | **75.9 / 100** |
| **Quality Score Range** | 70 – 87 (100% pass ≥ 70 threshold) |
| **Duplicate Records** | **0** (Strict canonical deduplication on URLs and Names) |
| **Missing Fields** | **0** (Complete metadata across all **35** required fields) |
| **Unique Categories** | 31 canonical domains |

---

## Data Sources (Priority Hierarchy)

1. **Priority 1 — Creati.ai**: `https://creati.ai/mcp/server/` & `https://creati.ai/mcp/client/` (Ingested via high-speed Cloudflare CDN data feeds with full product metadata, tools, cases, and languages)
2. **Priority 2 — Official Reference Implementations & Registries**: `modelcontextprotocol/servers`, `modelcontextprotocol.io`
3. **Priority 2 — Curated Ecosystem Directories**: `punkpeye/awesome-mcp-servers`, `wong2/awesome-mcp-servers`, `appcypher/awesome-mcp-servers`
4. **Registry Discovery & Indexing**: Glama.ai, Smithery, NPM `@modelcontextprotocol` & `mcp-server` registries
5. **Primary Source Verification**: Official vendor websites, GitHub organizations, documentation portals, and repository metadata.

---

## Category Distribution (Top Domains)

- **Developer Tools**: 7,822 records (SDKs, code execution, sandbox, linters, debuggers)
- **Finance & Fintech**: 409 records (crypto, DeFi, market data, portfolio analytics)
- **Search & Research**: 316 records (web search, scraping, academic indexers, semantic search)
- **Knowledge & Memory**: 307 records (knowledge graphs, vector memory, Obsidian, RAG)
- **Security**: 210 records (vulnerability scanners, IAM, secret management, CVE lookups)
- **Multimedia & Audio**: 153 records (image/video generation, audio transcription, TTS/STT)
- **Workplace & Productivity**: 142 records (task management, calendars, documentation)
- **Communication**: 137 records (Slack, Discord, Telegram, email, messaging)
- **Databases**: 110 records (PostgreSQL, MySQL, SQLite, MongoDB, Redis, Neon, Supabase, DuckDB, ClickHouse)
- **Cloud & DevOps**: 108 records (AWS, GCP, Azure, Cloudflare, Docker, Kubernetes, Terraform)
- **Gaming & Entertainment**: 96 records
- **Browser Automation**: 91 records (Playwright, Puppeteer, Selenium)
- **Marketing & SEO**: 87 records
- **Monitoring & Observability**: 64 records (Datadog, Sentry, Grafana, Prometheus)
- **Research**: 57 records
- **Travel & Transportation**: 50 records
- **Data Platforms & Pipelines**: 48 records
- **Data Science & Analytics**: 48 records
- **Location Services**: 48 records
- **Social Media**: 47 records
- **Healthcare & Life Sciences**: 46 records
- **File Systems**: 45 records
- **Legal & Compliance**: 37 records
- **E-Commerce**: 32 records
- **IoT & Hardware**: 29 records

- **Customer Support & CRM**: 24 records
- **Version Control & Git**: 22 records
- **AI/ML & MCP Clients**: 19 records
- **Education, Lifestyle & Language**: 24 records

---

## Pipeline Workflow

```
┌────────────────────────────────────────────────────────┐
│ Discovery Sources                                      │
│ (Awesome Lists, Official Repos, NPM Registry, Glama)   │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ Extraction & Normalization                              │
│ (Standardize categories, clean names, extract owner)   │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ Verification & Enrichment                              │
│ (Official company domains, GitHub avatars, metadata)   │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ Quality Scoring (100-Point Rubric)                     │
│ (Usefulness, Quality, Activity, Adoption, Docs, Trust) │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ Deduplication & Filtering                              │
│ (Canonical URL matching, name deduplication, score ≥70)│
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ Final Outputs (CSV, TSV, JSON)                         │
│ data/final/mcp_dataset.csv                             │
│ data/final/mcp_dataset.tsv                             │
│ data/final/mcp_dataset.json                            │
└────────────────────────────────────────────────────────┘
```

---


## Repository Structure

```
ai-orbit/
├── README.md                              # Project overview and metrics
├── requirements.txt                       # Dependencies
├── run.py                                 # Multi-domain ingestion pipeline entry point
├── src/                                   # Ingestion engine architecture
│   ├── __init__.py
│   ├── pipeline.py                        # Orchestrator across 14 ecosystem domains
│   ├── normalizer.py                      # Common entity schema & stable UUIDv5 generation
│   ├── deduplicator.py                    # Cross-domain deduplication & canonicalization
│   ├── relationship_mapper.py             # Knowledge graph & relationship generator
│   ├── validator.py                       # Schema sanitizer and format validator
│   └── extractors/                        # Domain-specific extractors
│       ├── __init__.py
│       ├── mcp.py                         # Top verified MCP servers & clients loader
│       ├── models.py                      # Hugging Face API & frontier foundation models
│       ├── companies.py                   # Leading AI labs & infrastructure firms
│       ├── tools.py                       # Top conversational and coding tools
│       ├── repositories.py                # GitHub Search API open-source projects
│       ├── news.py                        # Live RSS feeds and landmark announcements
│       ├── videos.py                      # Technical architecture deep-dive videos
│       ├── robots.py                      # Autonomous humanoid & mobile robots
│       ├── devices.py                     # Data center GPUs, ASICs & edge devices
│       ├── tasks.py                       # Core tasks users accomplish with AI
│       ├── collections.py                 # Benchmarks, prompt markets & awesome lists
│       ├── personal.py                    # Personal companions & wellness assistants
│       ├── creative.py                    # Creative generative tools (video/image/music)
│       └── new_entities.py                # High-impact recent launches (2024-2025)
├── data/
│   ├── final/                             # Final MCP Deliverables
│   │   ├── mcp_dataset.csv                # Final 3,844 records dataset (CSV, 35 columns)
│   │   ├── mcp_dataset.tsv                # Final 3,844 records dataset (TSV, Google Sheets ready)
│   │   └── mcp_dataset.json               # Final 3,844 records dataset (JSON)
│   └── ingestion/                         # Multi-Domain Ingestion Deliverables
│       ├── entities.json                  # 257 ecosystem entities across 14 domains
│       ├── relationships.json             # 261 ecosystem relationships graph
│       └── summary.json                   # Ingestion run execution metadata
├── scripts/                               # Data curation and transformation utilities
│   ├── build_full_dataset.py              # Complete 3,800+ records build pipeline
│   ├── remediate_dataset.py               # Schema expansion (22 → 35 fields) + score recalibration
│   ├── cleanup_descriptions.py            # Removes markdown artifacts from descriptions
│   ├── normalize_descriptions.py          # Grammar normalization for descriptions
│   ├── prepare_google_sheet.py            # TSV export and Google Sheets helper
│   ├── extract_mcp_data.py                # Base extraction logic
│   ├── add_more_records.py                # Curated enrichment batch
│   └── add_batch3.py                      # Seed extensions
└── docs/
    └── methodology.md                     # In-depth methodology, scoring & schema definitions
```

---

## Quality Assurance & Verification

- ✅ **Zero Duplicates**: Strict deduplication using canonical GitHub repository paths and lowercase normalized names.
- ✅ **100% URL Validity**: All entries point to verified GitHub repositories, official company websites, or product documentation.
- ✅ **Full Schema Compliance**: Exact match with AIOrbit specifications — **all 35 required fields** present in every record.
- ✅ **High Scoring Standard**: 100% of included records achieve Quality Score ≥ 70.
- ✅ **Clean Descriptions**: All boilerplate and markdown artifacts removed. Descriptions follow consistent professional format.
- ✅ **Rich Metadata**: Every record includes `integrations`, `supported_ai_clients`, `supported_models`, `api_availability`, `mcp_transport`, `documentation_url`, `activity_score`, `overall_score`, `verification_source`, and `notes`.

---

## AI Orbit Ecosystem Ingestion Pipeline

Per the project specification (`AI Orbit Ecosystem Data Ingestion Pipeline.pdf`), a production-grade multi-domain ingestion engine is implemented under `src/` to populate the broader AI Orbit ecosystem.

### Key Ingestion Metrics
- **Total Unique Entities**: 257 records across 14 categories (Target: 250–300)
- **Total Ecosystem Relationships**: 261 relationships across 10 semantic predicates
- **Domain Coverage**: Models, Tools, Companies, News, Videos, Robots, Devices, Repositories, MCP, Collections, Personal AI, Tasks, Creative Tools, and Recent Launches
- **Schema Compliance**: 100% compliant with common entity schema (`id`, `entity_type`, `name`, `description`, `url`, `categories`, `source`, `ingested_at`) plus domain-specific metadata

---

## How to Run

### 1. Execute Multi-Domain Ingestion Pipeline (All 14 Domains)
```bash
# Install dependencies
pip3 install -r requirements.txt

# Run complete ingestion pipeline (generates entities.json, relationships.json, summary.json)
python3 run.py
```

### 2. Rebuild MCP Standalone Dataset (3,844 Records)
```bash
# Rebuild the complete 3,800+ record dataset from sources
python3 scripts/build_full_dataset.py

# Apply full schema remediation (adds 13 new fields, fixes descriptions, recalibrates scores)
python3 scripts/remediate_dataset.py

# Final description cleanup (markdown artifacts, grammar)
python3 scripts/cleanup_descriptions.py
python3 scripts/normalize_descriptions.py

# Format TSV and view Google Sheets import instructions
python3 scripts/prepare_google_sheet.py
```


