# CIEL Lab Wiki

<div class="ciellab-hero" markdown>

CIEL Lab is a workspace for maintaining the CIEL concept dictionary: inspect
terminology content, run repeatable quality checks, stage fixes, manage
translations, and prepare releases without losing the audit trail back to OCL.

This wiki explains the product as it exists in the codebase and records the
operational knowledge that had previously lived across source code, issue
threads, and Slack conversations.

</div>

## Choose a task

| If you need to… | Start here |
| --- | --- |
| Understand the complete system | [Architecture overview](architecture/overview.md) |
| Learn the interface | [Product tour](getting-started/product-tour.md) |
| Find and update a concept | [Concept Manager](features/tools/concept-manager.md) |
| Find an external terminology code | [Code Search](features/tools/code-search.md) |
| Check the current CIEL HEAD | [Quality assurance](features/quality-assurance/overview.md) |
| Resume a long QA review | [Bulk Validation](features/quality-assurance/bulk-validation.md) |
| Prepare a release | [Release workflow](features/release-workflow.md) |
| Use CIEL Lab from an AI client | [MCP App](features/mcp-app.md) |
| Operate terminology loaders and exports | [CIEL scripts](ciel-scripts/index.md) |

## Search is local and complete

Use the search box or ++cmd+k++. Material for MkDocs builds a Lunr-compatible
index from every page and loads it in the browser. Search is:

- full-text and instant;
- aware of page titles, headings, and body text;
- typo-suggesting, highlighted, and shareable;
- independent of Algolia or another hosted search service.

The index covers written documentation, captions, and video descriptions.
Video speech is not searchable until a transcript is added to its page.

## How the product fits together

CIEL Lab combines a React application, a FastAPI/GraphQL backend, OCL, cached
HEAD data, terminology loaders, vector search, and asynchronous workers. The
short version is:

1. OCL remains the source of truth.
2. CIEL Lab caches and indexes content so review tools stay responsive.
3. Quality checks and user actions create reviewable reports or worklists.
4. Human reviewers approve changes before they are written to OCL.
5. Release automation produces diffs and SQL artifacts from an approved state.

See the [system infographic](architecture/overview.md) for the full data flow.

!!! note "Documentation scope"

    This is operational guidance, not a replacement for OCL authorization or
    release governance. Features that mutate OCL require a user-specific OCL
    API token and the appropriate permission.

