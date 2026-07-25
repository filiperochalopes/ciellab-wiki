# Translation

The Translation tool imports machine-generated suggestions into a human review
workflow. It does not publish model output directly.

## Find translation work

Filter by:

- target locale;
- concept class;
- mapping source;
- English name text;
- translation or review state.

## Import suggestions

The import accepts NDJSON produced by the supported translation pipeline. Each
line should be independently parseable so one malformed result does not hide
the entire batch.

1. Generate or obtain the NDJSON file.
2. Import it as a translation batch.
3. Wait for background parsing to complete.
4. Filter the resulting rows.
5. Compare suggestions from the available algorithms.
6. Select or edit the preferred translated term.
7. Save the row, or save the reviewed page when all visible rows are ready.

## Human review checklist

- preserve the clinical meaning, not English word order;
- use the correct locale and regional convention;
- distinguish preferred names from synonyms;
- preserve intentional acronyms and proper names;
- check number, gender, laterality, and qualifiers;
- reject a fluent translation that changes scope;
- add a related translated term only when it is a legitimate synonym.

## Publication boundary

Imported suggestions are staged application data. The reviewer decides what is
accepted and the authorized OCL mutation is separate from model generation.

