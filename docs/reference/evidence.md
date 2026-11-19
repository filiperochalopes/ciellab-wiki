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
- the canonical [`ocl-skills` README](https://github.com/filiperochalopes/ocl-skills)
  and the versioned skill contracts, schemas, validation, and examples it indexes.

When this wiki and the code disagree, verify the deployed version and update
the documentation in the same change as the behavior.

## Slack review method

The evidence review is restricted to two explicitly authorized OpenMRS Slack
conversations: one direct conversation and one designated workspace
conversation. The documentation process paginates the complete bounded history
from 7 September 2026, opens every in-scope reply thread, and treats messages as
private evidence rather than as publication-ready text.

The synthesis promotes only repeated questions, confirmed behavior, resolved
defects, and operational guidance that can be corroborated in current code,
tests, or a public issue. It does not publish raw private messages, private
permalinks, attachment URLs, personal context, or credentials.

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
- QA rule execution settings, deferred checks, retired-concept scope, and per-rule finding behavior;
- restoration of an accidentally retired concept;
- incomplete mapping drafts and their QA feedback boundary;
- background job completion, cancellation, and stale-job recovery;
- Concept Quick View and worklist resolution controls;
- actionable OCL validation messages on rejected writes.

## Issue cross-references

- [OCL Mapper #665 — CIEL Bridge to RxNorm clinical drugs](https://github.com/OpenConceptLab/ocl_online/issues/665)
- [#2609 — CIEL Lab wiki](https://github.com/OpenConceptLab/ocl_issues/issues/2609)
- [#2401 — QA rule work referenced by the implementation](https://github.com/OpenConceptLab/ocl_issues/issues/2401)
- [#2389 — semantic matching and specificity](https://github.com/OpenConceptLab/ocl_issues/issues/2389)
- [#2535 — CIEL HEAD/MCP cache behavior](https://github.com/OpenConceptLab/ocl_issues/issues/2535)
- [#2608 — IMO procedure mapping workflow](https://github.com/OpenConceptLab/ocl_issues/issues/2608)
- [#2680 — clinical attribute and OCL support-skill installation](https://github.com/OpenConceptLab/ocl_issues/issues/2680)
- [#2741 — one active description per locale](https://github.com/OpenConceptLab/ocl_issues/issues/2741)
- [#2742 — QA rule execution settings](https://github.com/OpenConceptLab/ocl_issues/issues/2742)
- [#2743 — QA rule finding behavior](https://github.com/OpenConceptLab/ocl_issues/issues/2743)
- [#2750 — unretire a concept](https://github.com/OpenConceptLab/ocl_issues/issues/2750)
- [#2751 — actionable OCL write errors](https://github.com/OpenConceptLab/ocl_issues/issues/2751)
- [#2754 — description-property migration](https://github.com/OpenConceptLab/ocl_issues/issues/2754)
- [#2755 — Concept Quick View](https://github.com/OpenConceptLab/ocl_issues/issues/2755)
- [#2756 — worklist resolution control](https://github.com/OpenConceptLab/ocl_issues/issues/2756)

## Exclusion policy

Never transfer the following from evidence into this public site:

- credentials, tokens, passwords, or connection strings;
- patient or private personal information;
- unrelated private discussion;
- private meeting links;
- licensed source files that cannot be redistributed;
- an unverified claim from one message.
