# Bulk Validation

Bulk Validation runs deterministic QA rules against an OCL source/version and
stores the output as a report.

## When to run it

Use Bulk Validation:

- before a release;
- after a large import or repair;
- when investigating a rule family across the source;
- when a stable report is needed for a team review.

It is not necessary after every single edit. The concept forms provide
immediate validation; a bulk run is intentionally heavier.

## Run a report

1. Choose the OCL source and version. Use HEAD for release readiness.
2. Start validation.
3. Leave the page if needed; Celery runs the job in the background.
4. Return when the status is complete.
5. Filter by rule, severity, concept class, terminology system, or other
   available facets.
6. Download the report or select findings.
7. Save selected findings as a worklist.

The interface evolved from raw JSON output into persisted reports with filters,
downloads, and worklist creation. Prefer the structured UI for routine review.

### Narrow mapping findings by terminology system

When the current report contains mapping-based failures, the **Terminology
system** facet is available. Select one or more sources to isolate findings for
that terminology; source matching is case-insensitive, so variants in source
capitalization remain together. The same selection is retained in a filtered
CSV download and in a worklist created from the report.

## Rule catalog

The implementation contains rule identifiers through **FR32** (with intentional
gaps). They cover structural, name, description, mapping, vocabulary, and
external-terminology consistency checks. Use the rule description shown in the
report as the immediate contract.

Recent checks include:

- **FR-27:** a `SAME-AS` mapping must not coexist with primary and secondary
  ICD-10-WHO mappings for the same concept.
- **FR-28:** at most one active description may exist for each locale; retired
  descriptions do not count.
- **FR-29 to FR-32:** map type, mapping source, concept class, and datatype
  must use the canonical vocabulary offered by CIEL Lab's write paths. These
  checks compare values verbatim, so a near spelling is a finding rather than
  an automatic normalization.

FR-29 to FR-32 can be skipped operationally when their upstream vocabulary is
unavailable. A skipped check is recorded as unavailable; it is not evidence
that the value is valid. Correct the source/index condition and rerun the
report.

FR22 performs indexed terminology checks. It applies to supported indexed
terminologies, not only SNOMED CT. If a source has not been indexed or its index
is stale, the finding set can be incomplete.

## Job status, cancellation, and recovery

Bulk Validation runs on the dedicated **bulk** worker. The request returns a
persisted job; leaving the page does not cancel the scan. A background job is
expected to finish as **Succeeded**, **Failed**, or **Cancelled** rather than
remaining indefinitely in progress.

If a report is no longer needed, request cancellation from its job controls.
Cancellation is observed between batches, so a large scan can take a short time
to stop. Do not start a duplicate job while the first one is still pending or
running.

If a worker is interrupted, the service detects a stale job and marks it failed
rather than leaving it running forever. Review the failure message and run a new
report only after the worker, source, and HEAD mirror are healthy.

### Retired-concept checks

Some closed-vocabulary rules can also inspect retired concepts because release
artifacts still need to represent retired rows. In **QA > Settings**, a rule can
state whether it includes retired concepts. The report identifies findings on
retired concepts and exposes a corresponding filter; a report with no such
findings is not proof that every rule examined retired data.

When a retired mapping must be corrected, use the reviewed sequence: **Unretire**
the concept, correct the mapping with a canonical value, verify the save, then
retire it again if it should remain historical. See [Concept Manager](../tools/concept-manager.md#restore-a-retired-concept).

## Save a worklist

A report describes the source at run time. HEAD may move before review
finishes. A worklist preserves the selected review items and is therefore the
right unit for:

- assigning or resuming a cleanup;
- collecting candidate fixes;
- using the MCP App to prepare a preview;
- separating approved changes from unresolved findings.

When you select **Review** for filtered failures, name the worklist before it
is created. The suggested name includes the source, version, and active filters;
adjust it to make later worklist selection unambiguous. Worklists cannot be
renamed afterwards.

Opening an individual cross-concept finding can create a **Temporary worklist**
in Concept Manager. It contains the finding's concept and the related concepts
needed to compare or merge it. This browser-session worklist is not saved in
the worklist picker; create a normal worklist when the review must persist or
be resumed later.

## Recover from a cache reset

If a report suddenly fails or returns implausibly few results after a service
restart:

1. check whether the CIEL HEAD mirror exists;
2. run the normal CIEL refresh;
3. wait for the chained indexing job;
4. rerun the validation;
5. keep the existing worklist—do not recreate it solely because the cache was
   rebuilt.

## Release-readiness check

The Release page expects a completed HEAD report with zero errors from the last
24 hours. Run Bulk Validation after the final change set and before creating
the release.
