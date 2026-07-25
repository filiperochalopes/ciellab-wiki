# CIEL Lab Wiki

Internal product and operations documentation for CIEL Lab, published as a
public static site.

The wiki uses:

- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) for the
  documentation experience
- Material's built-in client-side search for instant, indexed full-text search
  without a hosted search service
- GitHub Pages for the generated static site
- Cloudflare R2 for videos and other large media

This repository contains the documentation source and deployment automation.
Downloaded Slack media is kept under `_private/`, excluded from Git, and must
be reviewed before it is uploaded to R2.

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
set -a && source .env && set +a
mkdocs serve
```

Open <http://127.0.0.1:8000>.

## Validate a production build

```bash
mkdocs build --strict
```

The generated site is written to `site/`. It is never committed.

## Deploy

The GitHub Actions workflow builds and deploys `site/` to GitHub Pages on every
push to `main`. Configure these repository variables:

- `SITE_URL` — the GitHub Pages or custom-domain URL
- `R2_PUBLIC_BASE_URL` — the public custom domain of the R2 bucket

No GitHub secret is required to publish the site. R2 upload credentials stay in
the local `.env` and are used only by `scripts/sync-media.sh`.

See [INSTALL.md](INSTALL.md) for the complete GitHub Pages and Cloudflare R2
setup.

## Documentation evidence

The initial structure was derived from:

- `OpenConceptLab/ocl_issues#2609`
- the `ciel-lab-v2` application codebase
- the `ciel-scripts` operational repository
- a broad sample of the CIEL Lab Slack discussion with Andrew

The resulting evidence map and editorial policy are recorded in
[Evidence and provenance](docs/reference/evidence.md). Private Slack
permalinks, credentials, personal data, and raw transcripts are intentionally
not published.
