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
5. Filter by rule, severity, concept class, or terminology.
6. Download the report or select findings.
7. Save selected findings as a worklist.

The interface evolved from raw JSON output into persisted reports with filters,
downloads, and worklist creation. Prefer the structured UI for routine review.

## Rule catalog

The implementation contains rule identifiers **FR01 through FR25**. They cover
structural, name, mapping, and external-terminology consistency checks. Use the
rule description shown in the report as the immediate contract; when changing
a rule, update both its implementation and this wiki.

FR22 performs indexed terminology checks. It applies to supported indexed
terminologies, not only SNOMED CT. If a source has not been indexed or its index
is stale, the finding set can be incomplete.

## Save a worklist

A report describes the source at run time. HEAD may move before review
finishes. A worklist preserves the selected review items and is therefore the
right unit for:

- assigning or resuming a cleanup;
- collecting candidate fixes;
- using the MCP App to prepare a preview;
- separating approved changes from unresolved findings.

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

