# Writing guide

The wiki is Markdown in Git. Keep a page close to the feature it documents and
make every workflow searchable without requiring a video.

## Feature page template

```markdown
# Feature name

One paragraph: what problem the feature solves and when to use it.

## Before you start

- required permission;
- required source/version or data state;
- important safety boundary.

## Complete the task

1. Use exact UI labels.
2. Describe one action per step.
3. State the expected result.

## Verify

Explain how to confirm the authoritative result.

## Troubleshooting

### Symptom written as a question

Cause, evidence, and safe recovery.

## Related

- [Related feature](path.md)
- [Relevant issue](https://github.com/...)
```

## Rules

- Write in English.
- Use the UI label as it appears in the deployed application.
- Say which terminology source/version a result depends on.
- Distinguish observed behavior from a recommendation.
- Prefer one canonical explanation and link to it.
- Put common questions under question-shaped headings.
- Add alt text and a caption or explanation for every visual.
- Add a transcript when video speech contains unique instructions.
- Never include secrets or private Slack permalinks.

## Updating from Slack or an issue

1. Identify a repeated question or confirmed behavior.
2. Verify it in the current code or deployed application.
3. Remove personal and conversational context.
4. Write the durable rule in the relevant feature page.
5. Add a public issue link when it improves traceability.
6. Record a new limitation when evidence is incomplete.

## Incremental source review

Before updating code-derived documentation:

```bash
.venv/bin/python scripts/source_baseline.py report
```

Review commits, changed paths, and local changes after the stored baseline.
Update the affected pages, validate the site, and only then capture the new
reviewed state:

```bash
.venv/bin/python scripts/source_baseline.py capture --confirm-reviewed
```

The capture refuses dirty codebases unless `--allow-dirty` is explicit. See
[Source baseline](../reference/source-baseline.md) for the complete policy.

## Preview and test

```bash
mkdocs serve
mkdocs build --strict
```

Before merging, search for the new feature name and the terms a user is likely
to type. Confirm that headings and captions return useful results.

## Media

Commit small reviewed screenshots under `docs/assets/screenshots/`. Keep raw and
large media under `_private/`, which is ignored. Publish reviewed videos to R2
through `scripts/sync-media.sh`.
