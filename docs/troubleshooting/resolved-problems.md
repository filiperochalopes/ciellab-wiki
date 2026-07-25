# Resolved problems

This is a regression-oriented record of problems repeatedly discussed during
CIEL Lab development. It deliberately avoids private Slack links.

| Area | Earlier behavior | Current behavior or recovery | Public reference |
| --- | --- | --- | --- |
| Retired Codes | Rows without a terminology-supplied replacement could disappear, leaving unresolved mappings invisible. | The page keeps those retired mappings visible and allows a manual or Code Search replacement. | Verified in the current UI/code; no specific public issue linked |
| Retired Codes layout | Wide result content required awkward page-level horizontal scrolling. | Result layout was adjusted so the review controls remain usable. | Verified through the later product discussion |
| Retired Code suggestions | Loading some suggestion sets could fail the page. | Suggestion loading was corrected; a missing native replacement is now a normal review state. | Verified through the later product discussion |
| Bulk Validation presentation | Early runs returned a raw JSON-oriented result that was difficult to review. | Results are persisted as UI reports with rule/severity filters, downloads, and worklist creation. | [Issue #2401](https://github.com/OpenConceptLab/ocl_issues/issues/2401) and current code |
| FR22 terminology coverage | Indexed retirement checking was initially treated as SNOMED-specific. | The rule now targets supported indexed terminologies. An absent index is reported operationally rather than silently treated as clinical truth. | [Issue #2401](https://github.com/OpenConceptLab/ocl_issues/issues/2401) and current rule code |
| HEAD cache after restart | Bulk QA could fail after the service restarted or its cache was cleared. | The normal refresh chain repopulates the HEAD mirror and reindexes it. Durable worklists remain separate from the rebuildable cache. | Current worker/cache implementation; related [issue #2535](https://github.com/OpenConceptLab/ocl_issues/issues/2535) |
| Long-running review | A reviewer could lose the practical result set as moving HEAD changed. | Reports can create durable worklists, which are the supported resume point. | Current report/worklist implementation |
| MCP mutation safety | Early explanations made the boundary between AI proposal and persistence easy to misunderstand. | MCP tools prepare previews; the authenticated human widget performs the final commit. | Current MCP README and implementation |

## Regression checks

After changes in these areas, verify:

1. A retired mapping with no native replacement remains visible.
2. Manual replacement can use a candidate from the correct source/version.
3. Bulk Validation creates a filterable persisted report.
4. Selected findings create a worklist that remains available after HEAD
   refresh.
5. FR22 tests a non-SNOMED indexed terminology.
6. A cleared HEAD cache can be rebuilt without deleting durable worklists.
7. An MCP tool call cannot persist an OCL change without the human widget.

The semantic specificity behavior tracked in
[issue #2389](https://github.com/OpenConceptLab/ocl_issues/issues/2389) is not
listed as resolved. It remains a retrieval limitation and belongs under
[Known limitations](known-limitations.md).

