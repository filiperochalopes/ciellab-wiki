# Source baseline

This page records the exact source state used for the current documentation
review. It prevents the wiki from silently claiming coverage of code that was
added after the review.

**Captured:** `{{ BASELINE_CAPTURED_AT }}`

## Codebase baseline

| Source | Branch | Reviewed commit | Commit date | Working tree at capture |
| --- | --- | --- | --- | --- |
| [CIEL Lab v2]({{ BASELINE_CIEL_LAB_REPOSITORY }}) | [`{{ BASELINE_CIEL_LAB_BRANCH }}`]({{ BASELINE_CIEL_LAB_BRANCH_URL }}) | [`{{ BASELINE_CIEL_LAB_COMMIT_SHORT }}`]({{ BASELINE_CIEL_LAB_COMMIT_URL }}) | `{{ BASELINE_CIEL_LAB_COMMIT_DATE }}` | {{ BASELINE_CIEL_LAB_WORKTREE }} |
| [CIEL scripts]({{ BASELINE_CIEL_SCRIPTS_REPOSITORY }}) | [`{{ BASELINE_CIEL_SCRIPTS_BRANCH }}`]({{ BASELINE_CIEL_SCRIPTS_BRANCH_URL }}) | [`{{ BASELINE_CIEL_SCRIPTS_COMMIT_SHORT }}`]({{ BASELINE_CIEL_SCRIPTS_COMMIT_URL }}) | `{{ BASELINE_CIEL_SCRIPTS_COMMIT_DATE }}` | {{ BASELINE_CIEL_SCRIPTS_WORKTREE }} |
| [OCL skills]({{ BASELINE_OCL_SKILLS_REPOSITORY }}) | [`{{ BASELINE_OCL_SKILLS_BRANCH }}`]({{ BASELINE_OCL_SKILLS_BRANCH_URL }}) | [`{{ BASELINE_OCL_SKILLS_COMMIT_SHORT }}`]({{ BASELINE_OCL_SKILLS_COMMIT_URL }}) | `{{ BASELINE_OCL_SKILLS_COMMIT_DATE }}` | {{ BASELINE_OCL_SKILLS_WORKTREE }} |

### Full commit identifiers

```text
CIEL Lab v2: {{ BASELINE_CIEL_LAB_COMMIT }}
CIEL scripts: {{ BASELINE_CIEL_SCRIPTS_COMMIT }}
OCL skills: {{ BASELINE_OCL_SKILLS_COMMIT }}
```

!!! warning "The initial baseline included local changes"

    Both working copies contained local changes when the first documentation
    review was captured. The versioned `source-baseline.yml` records the dirty
    state, changed-path counts, tracked-diff fingerprints, and the untracked
    content fingerprint where applicable. A commit identifier alone does not
    represent those local changes.

## Review changes since this baseline

Use the comparison links for a quick remote review:

- [CIEL Lab changes since the baseline]({{ BASELINE_CIEL_LAB_COMPARE_URL }})
- [CIEL scripts changes since the baseline]({{ BASELINE_CIEL_SCRIPTS_COMPARE_URL }})
- [OCL skills changes since the baseline]({{ BASELINE_OCL_SKILLS_COMPARE_URL }})

For local working copies, run:

```bash
.venv/bin/python scripts/source_baseline.py report
```

The report shows:

- commits after the stored baseline;
- the file-level diff summary;
- the current branch and HEAD;
- uncommitted or untracked paths that are not represented by a commit.

## Incremental documentation cycle

1. Run the baseline report.
2. Review only the commits and changed paths after the stored commit.
3. Inspect new Slack material after **{{ BASELINE_SLACK_REVIEWED_THROUGH }}**.
4. Update affected feature, architecture, troubleshooting, and script pages.
5. Build and review the wiki.
6. Move the baseline only after the documentation review is complete.

To record clean reviewed working copies:

```bash
.venv/bin/python scripts/source_baseline.py capture --confirm-reviewed
```

The capture command refuses dirty codebases by default. If local uncommitted
changes were intentionally part of the review, make that decision explicit:

```bash
.venv/bin/python scripts/source_baseline.py capture \
  --confirm-reviewed \
  --allow-dirty
```

Review the resulting `source-baseline.yml` diff before committing it.

## Evidence dates

The code hashes describe code coverage. Slack and issue evidence have their own
review-through dates in `source-baseline.yml`; they should be advanced only
after the corresponding new material has been reviewed.

| Evidence source | Reviewed through |
| --- | --- |
| Private CIEL Lab Slack conversation | `{{ BASELINE_SLACK_REVIEWED_THROUGH }}` |
| [Wiki issue 2609]({{ BASELINE_ISSUE_URL }}) | `{{ BASELINE_ISSUE_REVIEWED_THROUGH }}` |
| [OCL skills guide issue 2680]({{ BASELINE_OCL_SKILLS_ISSUE_URL }}) | `{{ BASELINE_OCL_SKILLS_ISSUE_REVIEWED_THROUGH }}` |
