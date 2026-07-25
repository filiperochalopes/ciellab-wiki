# Content routing

Use this map to place updates in one canonical location.

## Application changes

| Changed behavior | Primary documentation |
| --- | --- |
| Service topology, cache, vector search, embeddings, jobs | `docs/architecture/overview.md` |
| First-use requirements or access setup | `docs/getting-started/` |
| Dashboard metrics or refresh behavior | `docs/features/dashboard.md` |
| Required mappings, retired codes, display validation, bulk rules | `docs/features/quality-assurance/` |
| Concept editing, code lookup, translation | `docs/features/tools/` |
| Release diff, gate, artifact, notification, publication | `docs/features/release-workflow.md` |
| MCP tools, widget, authentication, approval boundary | `docs/features/mcp-app.md` |
| User preferences, OCL token, account administration | `docs/features/settings.md` |
| Repeated user question | `docs/troubleshooting/common-questions.md` |
| Confirmed corrected defect | `docs/troubleshooting/resolved-problems.md` |
| Current unresolved boundary | `docs/troubleshooting/known-limitations.md` |

## Script changes

| Changed behavior | Primary documentation |
| --- | --- |
| New script or category | `docs/ciel-scripts/index.md` |
| SNOMED, ICD-11, RxNorm, or OCL database loader | `docs/ciel-scripts/loaders.md` |
| OCL source, collection, reference, upload, or lookup repair | `docs/ciel-scripts/ocl-workflows.md` |
| CIEL QA, SQL export, enrichment, Liquibase publication | `docs/ciel-scripts/qa-and-release.md` |

Treat `ciel-scripts/README.md` as the canonical inventory. A new executable
script should normally be indexed there before the wiki describes it as
supported.

## Cross-cutting updates

- Update `docs/reference/evidence.md` when source methodology changes.
- Update `docs/reference/media-library.md` for published or pending recordings.
- Update `docs/deployment/github-pages.md`, `INSTALL.md`, and `.env.example`
  together when hosting variables or behavior change.
- Update `docs/reference/source-baseline.md` only for baseline workflow or
  presentation changes; source values come from `source-baseline.yml`.
- Add new pages to `mkdocs.yml`.

## Writing contract

- Use English.
- Prefer task-oriented headings and exact UI labels.
- State OCL source/version and freshness assumptions.
- Separate authoritative data, cached projection, suggestion, and human
  approval.
- Explain both normal verification and failure recovery.
- Link public GitHub issues near supported claims.
- Do not duplicate a full explanation across pages; link to the canonical one.

