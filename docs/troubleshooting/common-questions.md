# Common questions

These answers consolidate recurring questions from product use, code review,
issue discussions, and the CIEL Lab Slack history.

## Why did my saved concept not immediately appear in search?

The authoritative save and every read projection do not update at exactly the
same instant. Wait for the save response, then reload or search again. If the
item is still missing, confirm that you are searching the same source/version
and that the HEAD mirror/index task is healthy.

Do not create a duplicate solely because an immediate semantic search did not
return the item.

## What is the difference between Reload and Refresh?

**Reload** reads the latest data already held by CIEL Lab. **Refresh** pulls from
OCL and can trigger expensive cache and index rebuilds. Use Reload during normal
review and Refresh when OCL changed but the scheduled projection is stale.

## Why did Bulk Validation fail after services restarted?

The CIEL HEAD mirror may have been cleared before it was repopulated. Run the
normal HEAD refresh, wait for chained indexing to finish, and rerun validation.
Existing durable worklists should not be discarded.

## Should I run Bulk Validation after every edit?

No. Use immediate form validation for an individual edit. Run Bulk Validation
for a source-wide check, major batch, investigation, or pre-release gate.

## Why is my incomplete mapping not shown as a QA finding?

A mapping row that is still being entered is a draft, not a completed mapping.
Finish the source, target code, and map type, then review the resulting
validation. The editor preserves incomplete drafts while QA state refreshes so
that a partial row is not mistaken for a confirmed defect.

## Can I stop a Bulk Validation that I no longer need?

Yes. Request cancellation from the job controls and wait for the worker to
finish its current batch. Do not create a duplicate while the first job remains
pending or running. If a worker was interrupted, read the terminal job status;
a stale job is failed for review rather than assumed to have completed.

## What is the difference between a report and a worklist?

A report is a point-in-time validation result. A worklist is a durable selection
for human review. Convert findings to a worklist when the task will continue
while HEAD changes.

## Why does a text search not find the middle of a word?

Interactive text search is designed for word-prefix matching. Search from the
start of a word, such as `diabe` for `diabetes`, rather than from a buried
fragment such as `abetes`. This keeps type-ahead search fast and consistent
across search surfaces. Use a reviewed contains filter only for a deliberate
non-interactive investigation.

## Why is a recent edit visible in one view but not another?

CIEL Lab has different read paths. A live OCL read can reflect a successful
write immediately, while a GraphQL, HEAD-mirror, or index-backed view may wait
for its refresh or reindex cycle. Confirm the authoritative OCL state before
retrying an edit, then allow the affected projection to catch up.

## Why is a retired code shown without a replacement?

Many terminologies do not publish a one-to-one native replacement. CIEL Lab
keeps the finding visible so it cannot be forgotten. Search the correct source
and version manually, verify clinical meaning, and leave the item unresolved if
no safe replacement exists.

## Why does the semantic result look plausible but wrong?

Embeddings rank similarity, not clinical equivalence. A broad lexical match can
outscore a specific code, especially for qualifiers and post-coordination.
Constrain the source/version, use exact attributes, and verify in the
authoritative terminology.

## Does MCP search every external terminology?

Only sources and versions available to CIEL Lab and indexed for the requested
search path can be retrieved. CIEL HEAD has its own mirror/index lifecycle;
external terminologies may be indexed on demand.

## Can the AI client apply a change directly?

No. MCP tools prepare previews. A human reviews and commits through the
authenticated widget with personal OCL authorization.

## Why did an FR22 result omit a terminology?

FR22 depends on an available external terminology index. Confirm that the
source/version is supported and its indexing task completed. The current rule
is intended to cover supported indexed terminologies, not only SNOMED CT.

## Are the wiki and its videos private?

The GitHub Pages site is public. Only reviewed, public-safe content may be
published. Raw Slack evidence remains ignored by Git. R2 media is public when
served from the configured public custom domain.
