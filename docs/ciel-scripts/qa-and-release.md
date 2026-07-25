# QA and release assets

The scripts repository produces reproducible artifacts that supplement the CIEL
Lab UI.

## OpenMRS SQL

`generate_mysqldump_from_ocl_version.py` converts an OCL CIEL export ZIP or JSON
file into an OpenMRS 1.11-compatible concept dictionary dump.

Validate the result at two levels:

1. `tests/test_generate_mysqldump_from_ocl_version.py` compares parsed schema
   and INSERT data without a database.
2. `tests/test_generate_mysqldump_from_ocl_version.sh` imports reference and
   generated dumps into disposable MySQL databases and performs a semantic
   comparison.

Treat `PASS WITH CAVEAT` as a review state, not an unconditional release pass.

## Name validation assets

`generate_name_validation_assets.py` creates CIEL Lab-compatible CSV inputs from
WhoNamedIt and NCBI Taxonomy. Outputs separate:

- genus names;
- proper-name exceptions;
- eponym author data.

Record the upstream retrieval date so a later rule change can be reproduced.

## ICD-11 mapping QA

- `qa_check_non_normalized_ciel_icd11_codes.py` finds complex mappings that
  need normalization review.
- `qa_check_broken_icd11_mapping_parts.py` checks each mapped part against
  Simple Tabulation `Code` and `BlockId`.
- `check_newlyadded_icd11_codes_against_ciel_concepts.py` compares WHO
  changelog additions with CIEL.
- `check_retired_duplicate_mappings.py` detects duplicate mapping keys when at
  least one member is retired.

## Enrichment

`generate_expanded_synonyms.py` produces resumable NDJSON with expanded clinical
descriptions. Its output is model-generated and must be reviewed.

`etf_ciel_source_v2026_02_06_expanded_synonyms.py` merges reviewed descriptions
into OCL-ready output and can split large imports into ordered source, concept,
and mapping chunks.

## Publish to Liquibase Runner

`liquibaserunner_upload.sh` uploads a ZIP through the GitHub Contents API. It
reads `LIQUIBASE_RUNNER_TOKEN` from a private `.env`. Before upload:

1. verify the SQL tests;
2. inspect archive contents and version names;
3. confirm the target repository/path;
4. preserve the checksum;
5. publish with a least-privilege token.

