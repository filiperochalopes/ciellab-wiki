# Repository instructions

## CIEL Lab wiki maintenance

For any request to update, refresh, audit, or extend this wiki from changes in
`ciel-lab-v2`, `ciel-scripts`, GitHub issues, or Slack evidence:

1. Read `skills/update-ciellab-wiki/SKILL.md` completely before taking action.
2. Follow its incremental baseline workflow.
3. Resolve its reference links relative to
   `skills/update-ciellab-wiki/`.
4. Keep published documentation in English.
5. Treat the source repositories as read-only evidence unless the user
   explicitly requests changes to them.

## Slack media and Cloudflare R2

When an authorized Slack review identifies screenshots or videos:

1. Keep the raw download and its manifest entry under the Git-ignored
   `_private/` directory. Never commit raw Slack media.
2. Commit only small, reviewed, public-safe screenshots under
   `docs/assets/screenshots/`.
3. Review, redact when needed, and upload reviewed videos from
   `_private/slack-videos/` using `scripts/sync-media.sh`. This is a local,
   explicitly authorized action and requires `CLOUDFLARE_ACCOUNT_ID`,
   `R2_BUCKET`, `R2_ACCESS_KEY_ID`, and `R2_SECRET_ACCESS_KEY` in the ignored
   `.env` file.
4. Configure only the non-secret `R2_PUBLIC_BASE_URL` as a GitHub Actions
   repository variable. Do not place R2 S3 credentials in GitHub Actions or
   tracked files.
5. Confirm each uploaded object through its public URL before documenting it as
   available. Keep the English unavailable-video fallback when that verification
   is incomplete.
