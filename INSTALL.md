# Install and deploy

This guide configures the CIEL Lab Wiki with:

- GitHub Pages for the public static site;
- Cloudflare R2 for reviewed videos;
- GitHub Actions for continuous deployment from `main`.

Cloudflare Pages and Cloudflare Access are not required.

## 1. Local prerequisites

Install:

- Python 3.12 or later;
- Git;
- the AWS CLI, used only to upload media to R2.

Prepare the project:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

The `.env` file is ignored by Git.

## 2. Local variables

Edit `.env`:

```dotenv
SITE_URL=https://openconceptlab.github.io/ciellab-wiki/
R2_PUBLIC_BASE_URL=

CLOUDFLARE_ACCOUNT_ID=replace-with-account-id
R2_BUCKET=ciellab-wiki-media
R2_ACCESS_KEY_ID=replace-with-r2-access-key-id
R2_SECRET_ACCESS_KEY=replace-with-r2-secret-access-key
```

### Variable reference

| Variable | Used by | Secret | Description |
| --- | --- | --- | --- |
| `SITE_URL` | MkDocs and GitHub Actions | No | Canonical public wiki URL, including the repository path and trailing slash |
| `R2_PUBLIC_BASE_URL` | MkDocs and the browser | No | Public R2 custom-domain origin, for example `https://media.example.org` |
| `CLOUDFLARE_ACCOUNT_ID` | Local R2 sync | No | Cloudflare account containing the R2 bucket |
| `R2_BUCKET` | Local R2 sync | No | R2 bucket name |
| `R2_ACCESS_KEY_ID` | Local R2 sync | Yes | Bucket-scoped S3-compatible Access Key ID |
| `R2_SECRET_ACCESS_KEY` | Local R2 sync | Yes | Bucket-scoped S3-compatible Secret Access Key |

Do not add the R2 access keys to the public documentation or repository.

Load local variables and preview:

```bash
set -a
source .env
set +a
mkdocs serve
```

If `R2_PUBLIC_BASE_URL` is empty, video positions deliberately display the
English unavailable-video message while the rest of the page remains usable.

## 3. Create the GitHub repository

Create a repository for this directory, for example:

```text
OpenConceptLab/ciellab-wiki
```

The default workflow expects `main` as the production branch.

For the example repository, the project Pages URL is:

```text
https://openconceptlab.github.io/ciellab-wiki/
```

If the final repository owner or name differs, use its corresponding URL for
`SITE_URL`.

## 4. Enable GitHub Pages

In the repository:

1. Open **Settings → Pages**.
2. Under **Build and deployment**, choose **GitHub Actions** as the source.
3. Open **Settings → Actions → General**.
4. Ensure GitHub Actions is allowed to run the repository workflows.

The included workflow already has the required `pages: write` and
`id-token: write` permissions.

## 5. Configure GitHub Actions variables

Open **Settings → Secrets and variables → Actions → Variables** and create:

| Name | Example |
| --- | --- |
| `SITE_URL` | `https://openconceptlab.github.io/ciellab-wiki/` |
| `R2_PUBLIC_BASE_URL` | `https://media.example.org` |

`R2_PUBLIC_BASE_URL` is optional. Leave it absent until the public R2 domain is
working. A missing value does not fail the documentation build.

No GitHub Actions secrets are required for the Pages deployment. The workflow
does not upload media to R2 because raw videos are intentionally excluded from
Git.

## 6. Create the Cloudflare R2 bucket

In Cloudflare:

1. Open **Storage & databases → R2 object storage**.
2. Create a Standard storage bucket named `ciellab-wiki-media`.
3. Open the bucket's **Settings**.
4. Connect a public custom domain such as `media.example.org`.
5. Keep the `r2.dev` development URL disabled after the custom domain works.

The custom domain must belong to a zone available in the same Cloudflare
account.

## 7. Configure R2 CORS

In the bucket's **Settings → CORS Policy**, allow `GET` from:

```text
https://openconceptlab.github.io
```

Also add the final wiki custom-domain origin if one is used. Origins do not
include a path, so do not append `/ciellab-wiki/` to the CORS origin.

A minimal policy needs:

- allowed origin: the GitHub Pages origin;
- allowed method: `GET`;
- optional exposed headers: `Content-Length`, `Content-Range`, and
  `Accept-Ranges`;
- a reasonable browser cache duration.

After changing CORS on a custom domain that has already cached media, purge that
hostname's Cloudflare cache.

## 8. Create R2 upload credentials

From the R2 overview, select **Manage API Tokens** and create a user or account
token with:

- **Object Read & Write** permission;
- access restricted to `ciellab-wiki-media`.

Copy the generated Access Key ID and Secret Access Key into the local `.env`.
The secret is shown only once.

The sync script uses the S3-compatible endpoint:

```text
https://<CLOUDFLARE_ACCOUNT_ID>.r2.cloudflarestorage.com
```

## 9. Review and upload videos

Raw Slack media is stored locally under:

```text
_private/slack-videos/
```

Review every file for credentials, private messages, notifications, personal
data, and licensing before publishing it.

Load `.env`, then upload:

```bash
set -a
source .env
set +a
./scripts/sync-media.sh
```

The script uploads to:

```text
s3://ciellab-wiki-media/videos/
```

Verify an object directly:

```text
https://media.example.org/videos/2026-01-15-concept-save.webm
```

After successful verification, set the GitHub Actions variable
`R2_PUBLIC_BASE_URL` to the custom-domain origin.

## 10. Deploy

Push the source to `main`. GitHub Actions runs:

```text
.github/workflows/github-pages.yml
```

The workflow builds with `mkdocs build --strict` and publishes the generated
artifact to the `github-pages` environment.

Pull requests and non-main pushes run `.github/workflows/ci.yml` without
publishing.

## 11. Verify production

Check:

1. The Pages deployment completed successfully.
2. Search finds `Qdrant`, `worklist`, and `retired code`.
3. The infrastructure Mermaid diagram renders.
4. Screenshots load.
5. Each configured R2 video plays and supports seeking.
6. A deliberately incorrect media filename shows the unavailable-video message
   without removing the surrounding documentation.
7. `_private/`, `.env`, and raw Slack files are absent from the Pages artifact.

## Custom GitHub Pages domain

Configure the custom domain under **Settings → Pages**. Then update:

```dotenv
SITE_URL=https://wiki.example.org/
```

Update the R2 CORS policy to include `https://wiki.example.org`, and update the
GitHub Actions `SITE_URL` variable.

## Troubleshooting

### The site works but every video shows the fallback

Confirm:

- `R2_PUBLIC_BASE_URL` exists as a GitHub Actions variable;
- it contains only the origin and no trailing slash;
- the objects exist under the `videos/` prefix;
- the bucket custom domain is public;
- the R2 CORS policy allows the GitHub Pages origin.

### The Pages workflow does not deploy

Confirm that **Settings → Pages → Source** is set to **GitHub Actions** and the
workflow has permission to use Pages.

### The site URL contains the repository twice

Set `SITE_URL` to the complete project Pages URL exactly once:

```text
https://<owner>.github.io/<repository>/
```

