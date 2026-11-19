# OCL Mapper: CIEL Bridge to RxNorm and OMOP

Use this external custom algorithm to explore medication matches in OCL Mapper.
It uses CIEL names, translations, and brand synonyms to find ingredient mappings,
then proposes RxNorm clinical drugs and OMOP RxNorm Extension clinical drugs for
review. The combined algorithm is in **test phase**, not a built-in CIEL Lab
feature or an approved clinical mapping. See [OCL Mapper issue #665](https://github.com/OpenConceptLab/ocl_online/issues/665).

## Before you start

- Sign in to OCL Mapper with an account permitted to use external custom algorithms.
- Have your own OCL API token available. The external service receives this token
  and uses it to access OCL as you; only use an endpoint you trust. Never share
  the token in documentation, screenshots, or issue comments.
- Use a medication list and check the target source and version for your project.
  Availability depends on CIEL mappings and the content loaded in RxNorm and the
  OMOP RxNorm Extension.

## Configure the algorithm

1. Open your map project and go to **Configuration** → **Algorithms**.
2. Add a **Custom** algorithm.
3. In **API URL**, enter the complete combined endpoint, including `$match`:

   ```text
   https://oclmap-custom-algorithms.filipelopes.med.br/api/ciel-bridge-rxnorm-omop/$match
   ```

4. Leave the URL field so Mapper can retrieve the algorithm details. The name
   should populate as **CIEL Bridge RxNorm + OMOP RxNorm Extension**.
5. Enter your own OCL token in **API Token** and save the project configuration.
   If Mapper asks for the token again in a later session, re-enter it.
6. Run matching on a small set of medication rows and review the candidates.

The earlier `/api/ciel-bridge-rxnorm/$match` endpoint covers RxNorm only; use the
combined URL above when testing both RxNorm and OMOP. The shortened URL mentioned
in the issue question is incomplete.

## Verify and review

Check that the algorithm name appears in the project and that test rows return
plausible candidates. Compare the ingredient, strength, dose form, target source,
and code with the input and the authoritative terminology before accepting any
mapping. A candidate is a suggestion, not a clinical validation or automatic
approval. Absence of a candidate does not prove that no suitable drug exists.

The service reads CIEL mappings to `/orgs/NLM/sources/RxNorm/` and
`/orgs/OHDSI/sources/OMOP-RxNorm-Extension/`. A selected RxNorm version applies
to RxNorm; the OMOP extension is not pinned by Mapper's target version. In the
current implementation, combinations split across the two repositories are not
combined, and OMOP branded-drug concepts are not proposed. Results depend on
source content and configuration and may change as those sources change.

## Troubleshooting

- **The algorithm details do not populate:** check the full URL, including
  `$match`, and whether the external service is reachable. Check that your account
  can use custom algorithms.
- **Authentication fails:** check that you entered your own valid OCL API token;
  re-enter it if requested. Do not send it to support in an issue or message.
- **No suitable result:** check the medication text, source coverage, CIEL mappings,
  and selected RxNorm version. Review manually rather than assuming a match.
- **Service error:** retry later; an unavailable OCL service or missing dose-form
  value set can prevent matching. Contact the service operator if it persists.

The description endpoint was checked for this documentation, but an authenticated
match and end-to-end Mapper workflow were not independently tested. The original
issue's evaluation questions, including accuracy and cost, should not be treated
as settled by this setup guide.
