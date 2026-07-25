# Validation gates

Run from the wiki root.

## Required

1. Validate Python:

   ```bash
   .venv/bin/python -m py_compile hooks/env.py scripts/source_baseline.py
   ```

2. Validate the source report:

   ```bash
   .venv/bin/python scripts/source_baseline.py report
   ```

3. Build without R2:

   ```bash
   R2_PUBLIC_BASE_URL= \
   SITE_URL=https://filiperochalopes.github.io/ciellab-wiki/ \
   .venv/bin/mkdocs build --strict
   ```

4. Confirm:
   - no unresolved `{{ BASELINE_... }}` or `{{ R2_... }}` placeholders;
   - footer hashes match `source-baseline.yml`;
   - the provenance page contains full commits;
   - required search terms appear in `site/search/search_index.json`;
   - `_private/`, `.env`, and `site/` remain ignored.

5. Inspect `git status` in the wiki and both evidence repositories. Confirm the
   wiki update did not modify either evidence repository.

## When video markup changes

Build once with a sample R2 origin and confirm generated video URLs, hidden
fallback state, and the runtime fallback script:

```bash
R2_PUBLIC_BASE_URL=https://media.example.org \
SITE_URL=https://filiperochalopes.github.io/ciellab-wiki/ \
.venv/bin/mkdocs build --strict --site-dir /tmp/ciellab-wiki-r2-test
```

Then rebuild the normal site without R2.

## When workflows change

Parse `.github/workflows/*.yml`, confirm GitHub Pages permissions, and verify
that no Cloudflare Pages deployment credentials were reintroduced.

## Secret and privacy review

Search tracked text for token/password patterns and inspect new screenshots.
Do not print discovered secret values into logs or the final response.

## Baseline integrity

After capture:

1. rerun the strict build;
2. verify footer and page hashes;
3. review the `source-baseline.yml` diff;
4. ensure evidence review-through dates were not advanced beyond actual
   coverage.

