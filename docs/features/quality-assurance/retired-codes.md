# Retired Codes

Use Retired Codes to find CIEL mappings whose target code is no longer active in
an indexed external terminology.

## Why replacement is not automatic

A retired code does not always have a native replacement. Even when a
terminology publishes a replacement, it may be broader, narrower, or split into
multiple codes. CIEL Lab therefore treats replacement suggestions as a review
queue, not an automatic migration.

## Review a finding

1. Select the CIEL source/version.
2. Choose the external terminology source.
3. load the findings.
4. Inspect the retired target, its status, and any native replacement metadata.
5. Compare the CIEL concept meaning with the replacement candidate.
6. If no replacement is supplied, search manually in Code Search.
7. Choose the correct map type.
8. Save the approved change.
9. rerun the check.

## Source-specific truth

Retirement and replacement must be evaluated against the selected source and
version. Do not infer status from a similarly named source or from another
release. The standardized terminology loader view
`vw_retired_code_replacement` supplies a common shape, but the underlying
terminology remains authoritative.

## No native replacement

The current UI keeps retired mappings visible even when the terminology does
not publish a replacement. This behavior was corrected after reviewers found
that hiding those rows made unresolved work disappear.

For these rows:

1. open Code Search;
2. constrain the search to the correct source/version;
3. verify the candidate in the authoritative browser;
4. return and enter the mapping manually;
5. document ambiguity in the worklist rather than forcing a weak match.

