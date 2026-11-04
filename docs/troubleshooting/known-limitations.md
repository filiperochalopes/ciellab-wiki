# Known limitations

This page distinguishes product boundaries from defects.

## Semantic search

- Similarity is not clinical equivalence.
- Highly specific qualifiers can be underweighted.
- Post-coordinated expressions may not have one indexed point matching the
  complete meaning.
- External results depend on the selected version being indexed.

Mitigation: constrain, inspect, and verify; never apply solely from score order.
Reranking and specificity behavior are discussed in
[issue #2389](https://github.com/OpenConceptLab/ocl_issues/issues/2389).

## Moving HEAD

HEAD changes during review. A report can become stale and a result count can
change after refresh.

Mitigation: record the report time and preserve long-running work as a
worklist. Use a fixed release for reproducibility.

## Cache and index recovery

Valkey and Qdrant are rebuildable projections. Immediately after a reset:

- QA may fail or look empty;
- semantic search may be incomplete;
- dashboard values may temporarily fall back or lag.

Mitigation: complete the regular HEAD refresh and indexing chain before manual
data repair.

## Retired-code replacement

A terminology may not publish a replacement, or may publish a non-equivalent
one-to-many change.

Mitigation: keep the finding open and perform manual terminology review.

## MCP name-filter performance

A broad MCP search filtered by names can still be slow while it performs a
large CIEL scan. Narrow the source, locale, class, or mapping criteria before
asking for a wide name filter, and treat the result as a review set rather than
a real-time type-ahead surface. Incremental CIEL reindexing is not currently a
published capability; refresh work remains full-rebuild oriented.

Tracked by [ciel-lab-v2#84](https://github.com/filiperochalopes/ciel-lab-v2/issues/84)
and [ciel-lab-v2#68](https://github.com/filiperochalopes/ciel-lab-v2/issues/68).

## Production observability rollout

Slow SQL, GraphQL, and OCL timing signals exist in the application, but their
production usefulness depends on the deployed database configuration, restart,
and a fresh observation window. Do not treat the presence of the feature in code
as proof that production attribution is already complete.

Tracked by [ciel-lab-v2#82](https://github.com/filiperochalopes/ciel-lab-v2/issues/82).

## Large bulk imports and mapping-only sources

A successful large OCL bulk import is not, by itself, proof that its mappings
are searchable. Imports above the server's automatic-index threshold can be
saved without an indexing task, so reindex the affected source before using
mapping search or association views.

Namespace and related global mapping searches can also restrict results to the
latest **released** version of each repository. A mapping-only source with only
HEAD may therefore remain absent from those views even after it is indexed.
Create and verify the intended released version before treating the absence as a
mapping loss.

This behavior was reproduced for the CIEL-to-ICD-11-WHO migration and is
tracked by [issue #2990](https://github.com/OpenConceptLab/ocl_issues/issues/2990)
for better warnings and the remaining repository-version question.

## Concept merge compensation

A merge spans several OCL writes, so it cannot be made atomic across requests.
CIEL Lab compensates completed writes when a later step fails, but compensation
can also fail. A `rollback_failed` job requires manual OCL review; do not retry
the merge until the source and target names, mapping, and retirement state are
known.

## MCP scope

The MCP experience is intentionally preview-first. It cannot remove human
approval or grant OCL permissions that the current user does not have.

## Video search

MkDocs indexes the text around a video, not its audio stream.

Mitigation: add a concise caption and an English transcript. The transcript is
then included in the normal local search index.

## Public-site boundary

GitHub Pages and the R2 custom domain are public in this design. They must not
contain raw transcripts, credentials, protected terminology distributions, or
unreviewed Slack attachments.
