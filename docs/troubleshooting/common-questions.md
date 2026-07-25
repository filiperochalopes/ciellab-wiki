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

## What is the difference between a report and a worklist?

A report is a point-in-time validation result. A worklist is a durable selection
for human review. Convert findings to a worklist when the task will continue
while HEAD changes.

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
