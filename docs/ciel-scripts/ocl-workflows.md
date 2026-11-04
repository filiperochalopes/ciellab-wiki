# OCL workflows

These scripts prepare or apply OCL sources, collections, references, and bulk
imports.

## ICD-11 source preparation

`ocl_uploader_icd11.py` converts ICD-11 into OCL bulk-import JSONL. It can merge
post-coordinated codes, order dependencies, and create `NARROWER-THAN` mappings
to the first stem where the data model requires it.

Recommended sequence:

1. generate JSONL only;
2. validate line count, object types, and dependency order;
3. inspect post-coordinated examples;
4. create a new staging source;
5. import and review;
6. recreate an existing source only with explicit authorization and backup.

## Append CIEL-referenced ICD-11 concepts

`ocl_append_ciel_icd11_concepts.py` reads active CIEL ICD-11 mappings,
normalizes codes through the code-normalizer API, and emits missing target
concepts and mappings. It is designed to be idempotent.

Use `--version HEAD` only when the moving source is intentional. Prefer a fixed
version or pre-downloaded export ZIP for a reproducible run.

## Incremental lookup updates

`ocl_incremental_ciel_icd11_bulk_import.py` compares a CIEL export with a target
lookup source and writes only missing or changed objects. It caches target
state under `output/target-cache/`, keyed by the target `updated_at` value.

Refresh that cache when:

- the target was changed outside the script;
- `updated_at` is suspected to be stale;
- verification counts disagree with OCL.

## Description-property migration artifact

`ciel_description_properties_migration.py` prepares an offline, auditable OCL
Bulk Import NDJSON migration for [issue #2754](https://github.com/OpenConceptLab/ocl_issues/issues/2754).
It reads a CIEL export ZIP or JSON file and never uploads or applies changes.

The migration projects only explicit active-description markers into configured
flat locale properties: `DEF:` to `definition_<locale>`, `DESC:` to
`description_<locale>`, `CAPTION:` to `caption_<locale>`, and `REF:` to
`reference_<locale>`. It normalizes marker labels to uppercase while preserving
all other description characters, reports unsupported properties and conflicts,
removes stale legacy description metadata, and preserves unrelated extras.

Run it first against a fixed export and review its NDJSON plus JSON/CSV audit
reports. Do not apply a generated file when the report identifies conflicting
marker values, ambiguous description linkage, or unsupported property codes.

## CIEL-to-ICD-11-WHO mapping-only workflow

Two offline scripts separate the migration of CIEL-to-ICD-11-WHO mappings from
CIEL HEAD itself.

1. `export_ciel_to_icd11_who_mappings.py` accepts only an immutable export of a
   **released** CIEL version. It creates a deterministic, mapping-only NDJSON
   bundle for `CIEL/CIEL-to-ICD-11-WHO`; it never calls OCL or uploads data.
2. Review the bundle, its hashes, audit JSON, rejected CSV, and mapping identity.
   Mapping IDs, external IDs, target source, target code, and map type are kept
   as evidence; mappings are not inferred from target code alone.
3. Import the reviewed proxy bundle manually.
4. `retire_ciel_icd11_who_head_mappings.py` can then prepare, from an immutable
   HEAD export, a separate reviewed retirement plan for the active HEAD mappings.
   It requires the proxy bundle as a cross-check and writes `__action: "DELETE"`
   entries for manual upload; OCL treats those entries as retirements, not hard
   deletion.
5. Reindex both sources after the reviewed imports complete. Large OCL bulk
   imports can exceed the automatic indexing threshold, so a successful upload
   alone is not evidence that mappings are searchable.
6. Create and verify a released version of the mapping-only source before relying
   on **Namespace** or other searches that restrict results to each repository's
   latest released version.

Do not reverse this order. A retirement plan must not be applied until the
mapping-only source was imported and verified.

## Reconcile a local CIEL HEAD with production

`sync_local_ciel_with_prod.py` compares an immutable production CIEL HEAD export
with a local CIEL HEAD export. It can download ready exports with read-only GET
requests or run entirely offline when both files are supplied. It produces an
auditable local bulk-import bundle, ordered parts when needed, audit JSON, and a
review CSV; it has no upload or apply mode.

Use the output only after reviewing the desired state. Upload it manually to the
local source with **Update existing** enabled. The reconciliation intentionally
covers only Bulk-Import-representable Concept and Mapping HEAD state; it does not
claim to synchronize source metadata, history, database IDs, timestamps, or
checksums.

## Collections and references

| Script | Purpose |
| --- | --- |
| `ocl_recreate_collection.py` | Recreate a collection from an export and remap references |
| `ocl_recreate_collection_refs.py` | Normalize references and optionally recreate/import them |
| `delete_collection_references.py` | Generate explicit `__action: DELETE` entries for HEAD references |

Always inspect the generated reference manifest. A reference can point across
sources and versions, so count equality alone is insufficient.

## Lookup corrections

The `ICD-11 Lookup Fixes` directory contains focused repair scripts for:

- non-leaf `isLeaf` metadata;
- names containing unknown/incorrect titles;
- retirement of non-normalized lookup concepts.

They share an OCL HEAD cache. Generate patch payloads first and apply only after
review.

## WHO ATC

`ocl_uploader_whoatc.py` converts WHO ATC data into JSONL or JSON and can
optionally upload the source. Preserve the upstream release identifier and
license/provenance metadata with the generated artifact.
