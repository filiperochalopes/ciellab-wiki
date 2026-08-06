# Evidence and provenance

This wiki is a synthesized operating guide, not a raw conversation archive.

## Product decision

[OpenConceptLab/ocl_issues#2609](https://github.com/OpenConceptLab/ocl_issues/issues/2609)
asks for a maintainable CIEL Lab wiki with:

- documented major features and workflows;
- sidebar navigation and global search;
- screenshots, videos, cross-links, and step-by-step guidance;
- reusable page structures;
- a selected and justified platform.

The issue discussion initially converged on Material for MkDocs, Cloudflare
Pages, and R2. The final implementation keeps Material and R2 but uses GitHub
Pages for the public static site. This removes Cloudflare Pages and Access from
the initial topology while preserving R2 for large media.

## Code evidence

The initial pages were derived from:

- the React routes, menus, and feature pages in `ciel-lab-v2/web`;
- FastAPI, Strawberry GraphQL, service, repository, Celery, Qdrant, embedding,
  OCL, and MCP adapters in `ciel-lab-v2/api`;
- deployment definitions for MySQL, Valkey, Qdrant, workers, Nginx, and
  S3-compatible artifacts;
- the canonical `ciel-scripts/README.md` and the scripts it indexes.

When this wiki and the code disagree, verify the deployed version and update
the documentation in the same change as the behavior.

## Slack sample

The source conversation is a private direct-message channel. The review used:

- a complete paginated search for the literal term `ciellab`, covering matches
  from September 2025 through July 2026;
- focused searches for Bulk Validation, fixed problems, worklists, cache,
  semantic search, retired codes, release, translation, and MCP;
- screenshots and video metadata attached to relevant messages.

The synthesis emphasized repeated questions, confirmed behavior, resolved
defects, and explanations supported by the codebase. It does not publish raw
private messages or private Slack permalinks.

## Topics promoted into documentation

- Required Class Mapping filter semantics and partial review;
- CSV mapping-candidate import, Concept ID and Map ID identity checks, and the
  IMO Procedures review workflow;
- retired codes without a native replacement;
- reports versus durable worklists;
- immediate validation versus Bulk Validation;
- HEAD cache reset and rebuild behavior;
- semantic search specificity and external terminology indexing;
- release backup, QA gate, diff, and artifacts;
- MCP token setup and mandatory human approval;
- translation and display-name review.

## Issue cross-references

- [#2609 — CIEL Lab wiki](https://github.com/OpenConceptLab/ocl_issues/issues/2609)
- [#2401 — QA rule work referenced by the implementation](https://github.com/OpenConceptLab/ocl_issues/issues/2401)
- [#2389 — semantic matching and specificity](https://github.com/OpenConceptLab/ocl_issues/issues/2389)
- [#2535 — CIEL HEAD/MCP cache behavior](https://github.com/OpenConceptLab/ocl_issues/issues/2535)
- [#2608 — IMO procedure mapping workflow](https://github.com/OpenConceptLab/ocl_issues/issues/2608)

## Exclusion policy

Never transfer the following from evidence into this public site:

- credentials, tokens, passwords, or connection strings;
- patient or private personal information;
- unrelated private discussion;
- private meeting links;
- licensed source files that cannot be redistributed;
- an unverified claim from one message.
