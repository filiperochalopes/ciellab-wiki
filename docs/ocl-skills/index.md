# OCL support skills

[OCL skills](https://github.com/filiperochalopes/ocl-skills) is the companion
repository for repeatable, agent-assisted OCL operations. It is separate from
CIEL Lab and `ciel-scripts`: each skill contains its own OCL reference material,
schema, validation, and examples so it can be installed in a supported AI client
without a local CIEL Lab checkout.

The wiki reviews this repository as a third evidence source. Its current reviewed
commit is [`{{ BASELINE_OCL_SKILLS_COMMIT_SHORT }}`]({{ BASELINE_OCL_SKILLS_COMMIT_URL }}).

## Available skills

| Skill | Use it for | Safety boundary |
| --- | --- | --- |
| [`bulk-import-create-concepts`](https://github.com/filiperochalopes/ocl-skills/tree/main/skills/bulk-import-create-concepts) | Staging many new OCL concepts, reviewing them as CSV, and producing a timestamped zipped JSONL bulk-import file. The `ciel` profile applies CIEL rules, including a required `SAME-AS` self mapping. | It never uploads, retires, deletes, or writes to OCL. A human reviews the CSV and uploads the ZIP. |
| [`ocl-overview`](https://github.com/filiperochalopes/ocl-skills/tree/main/skills/ocl-overview) | Reading a structured organization or source summary, including validation profile, locales, automatic IDs, versions, and post-import verification. | Read-only; confirm the CLI session and target before using output to prepare a batch. |

The repository also keeps separate planned skills for retiring, updating, and
mapping concepts. Do not substitute the creation skill for those operations.

## Install the CIEL bulk-concept skill in Claude Desktop

The latest public guidance is in [OCL issue #2680](https://github.com/OpenConceptLab/ocl_issues/issues/2680), whose final comments show this workflow:

1. Remove the existing version of the skill from Claude Desktop.
2. Download the current ZIP from the [OCL skills repository](https://github.com/filiperochalopes/ocl-skills).
3. Unzip it, then create a ZIP containing only the `skills/bulk-import-create-concepts` folder.
4. In Claude Desktop, open **User avatar** (bottom left) → **Settings** → **Skills** → **Add** → **Upload**, then select that ZIP.
5. Start a request with a prompt such as:

   ```text
   Use $bulk-import-create-concepts to create CIEL concepts based on this spreadsheet.
   ```

![Claude Desktop’s Skills upload flow, from OCL issue 2680](https://github.com/user-attachments/assets/a005d154-e157-4b9e-a575-ff93443896c2)

*Installation screenshot published in [OCL issue #2680](https://github.com/OpenConceptLab/ocl_issues/issues/2680). The folder itself—not the whole repository archive—is the upload unit.*

## Use the creation workflow safely

1. Confirm the target owner type, owner, source, validation profile, default locale, and supported locales. For CIEL-governed content, select the `ciel` profile only after the destination is confirmed.
2. Classify each concept deliberately. A concept class and datatype are editorial decisions, not values to let defaults infer.
3. Draft the batch, including any `extras`. For the `clinical` attribute, the current CIEL rule is boolean `false` for a non-clinical concept; omit the attribute for the default clinical behavior.
4. Run the skill validation and resolve every error. Review warnings, especially name types and unknown extras keys.
5. Review the generated CSV and explicitly approve it before producing the ZIP.
6. Upload the ZIP manually in OCL, then verify both the concepts and the expected mapping count. The importer summary counts concept lines and may not show nested mappings.

!!! warning "OCL filtering is not yet a clinical-only workflow"

    Issue [#2680](https://github.com/OpenConceptLab/ocl_issues/issues/2680) records why `clinical=false` is useful metadata but is not, by itself, a practical OCL Term Browser filter for selecting all clinical concepts: the browser UI lacks negative filtering. Use an API URL with advanced desired filters only when its semantics have been reviewed for the intended source and version; do not claim that the UI automatically exposes a clinical-only filter.

## Maintaining this documentation

Every wiki refresh must run `scripts/source_baseline.py report` against
`ocl-skills` as well as CIEL Lab and CIEL scripts. When the OCL skills changes
are reviewed, record its exact commit in `source-baseline.yml`; the footer and
this page will render its short hash automatically.

## Related

- [Source baseline](../reference/source-baseline.md)
- [CIEL scripts](../ciel-scripts/index.md)
- [OCL issue #2680 — clinical attribute and skill-installation guidance](https://github.com/OpenConceptLab/ocl_issues/issues/2680)
