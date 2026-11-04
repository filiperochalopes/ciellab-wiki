# Quality assurance

CIEL Lab uses two complementary forms of validation:

- **focused QA tools** answer one operational question and support immediate
  repair;
- **Bulk Validation** applies a deterministic rule catalog to a source/version
  and stores a complete report.

In-form validation should catch obvious errors while an editor is working. A
bulk report is the reproducible pre-release check and the best way to coordinate
a larger cleanup.

## Choose the right tool

| Question | Tool |
| --- | --- |
| Which concept classes lack a required target mapping? | Required Class Mappings |
| Which existing mappings now point to retired codes? | Retired Codes |
| Which names have a display or casing finding? | Display Issues |
| Does HEAD pass the complete release rule set? | Bulk Validation |
| How do I preserve a review while HEAD continues to change? | Save report findings as a worklist |

## Safe review pattern

1. Select the intended OCL source and version.
2. Confirm the data timestamp.
3. Run the narrowest useful check.
4. Filter to a manageable group.
5. Save a worklist before a long review.
6. Inspect each suggested code in its authoritative terminology.
7. Apply approved changes.
8. rerun the relevant validation and confirm the result.

## Reports and worklists

A **report** is the output of a validation run at a point in time. A **worklist**
is a durable set of items selected for human review. Reports can become stale as
HEAD changes; worklists are the checkpoint that lets a reviewer resume without
depending on the original query returning the same rows.

## Configure the QA catalog

Open **QA > Settings** to review where each code-defined QA rule runs. The
settings are global: they apply to all curators because Bulk Validation runs as
a background job. Administrators can change them; other users can inspect the
current configuration but cannot edit it.

1. Find the rule under its category.
2. Use the **Bulk Validation** switch to include or exclude it from new bulk
   reports.
3. Use the **Concept Editor** switch to include or exclude it from draft
   validation.
4. Use the trailing **…** menu for **Show worklist button**, **Use dynamic
   focus**, and—where the rule supports it—**Retired concepts**. Presentation
   switches do not change whether a rule runs; retired-concept scope states
   whether that rule evaluates historical rows in a bulk report.

A disabled rule is not evaluated, rather than being evaluated and hidden.
Rules marked **Instant** use the draft itself and can block a save. **Deferred**
rules need the HEAD mirror or a reference-terminology index, so the editor shows
their pending state without blocking initial editing. Some switches are locked
when the rule cannot run in that context or the form already prevents the
violation.

The single-active-description-per-locale rule is a current CIEL QA convention:
retired descriptions do not count. Do not generalize it into a universal OCL
modeling rule; a future workflow may deliberately need more than one description
role in one locale.

Allow up to 30 seconds for a global change to reach another API worker. Verify
the effective setting by reloading **QA > Settings** before interpreting a new
bulk report or editor result.

## Release gate

The Release workflow expects a recent successful HEAD bulk validation. The
observed implementation requires a zero-error HEAD report within the previous
24 hours. Warnings still require judgment, but an error is a hard signal that
the source is not release-ready.

The deterministic rules and UI behavior were developed under
[OpenConceptLab/ocl_issues#2401](https://github.com/OpenConceptLab/ocl_issues/issues/2401).
