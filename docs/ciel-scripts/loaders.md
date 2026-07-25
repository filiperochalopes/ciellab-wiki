# Terminology loaders

The loader scripts convert upstream formats into MySQL/MariaDB structures that
CIEL Lab can query consistently.

## Loader catalog

| Script | Input | Result |
| --- | --- | --- |
| `snomed_loader.py` | SNOMED CT RF2 snapshot | Local SNOMED database and standard views |
| `icd11_loader.py` | WHO ICD-11 Simple Tabulation | Downloaded/imported ICD-11 database and standard views |
| `ocl_loader.py` | Released OCL source | Concepts, names, status, and replacement-oriented local views |
| `rxnorm_loader.py` | RxNorm RRF files | Local RxNorm database and standard views |

## Common workflow

1. Obtain the upstream release through an authorized channel.
2. Record its version and expected input layout.
3. Configure `FLOW_DB_HOST`, `FLOW_DB_PORT`, `FLOW_DB_USER`, and
   `FLOW_DB_PASS`.
4. Run the script with `--help` first.
5. Load into a release-specific database name.
6. Confirm active-code and retired-replacement view counts.
7. Compare a sample with the upstream terminology browser.
8. Trigger the CIEL Lab indexing job for that terminology/version.

## SNOMED CT

The SNOMED loader reads an RF2 snapshot. Licensing and distribution rules still
apply to the source archive and derived database. Use the companion
`SNOMED_FLOW.md` for the exact file layout expected by the current script.

## ICD-11

The ICD-11 loader obtains Simple Tabulation and materializes the standard views.
Additional scripts handle post-coordination exploration and normalization:

- `list_postcoordinated_browser_codes.py`;
- `compare_postcoord_export_to_ciel.py`;
- `qa_check_non_normalized_ciel_icd11_codes.py`;
- `qa_check_broken_icd11_mapping_parts.py`;
- `list_postcoordinated_scale_codes.py`.

A post-coordinated code must be normalized consistently before string
comparison. A missing exact string match is not proof that the clinical
expression is absent.

## RxNorm

The RxNorm loader reads RRF files and materializes the common interface. Use the
repository's `RXNORM_GUIDE.txt` for release-specific preparation.

## OCL source loader

`ocl_loader.py` pulls a released OCL source. Use a fixed version for a
reproducible local database; avoid treating moving HEAD as a stable release
input.

## After loading

The database is only the first projection. For semantic Code Search:

1. make the terminology/version available to the CIEL Lab worker;
2. enqueue the terminology indexing task;
3. wait for embeddings and Qdrant upserts to finish;
4. verify an exact code and a representative semantic query.

