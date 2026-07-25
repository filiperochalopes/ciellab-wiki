#!/usr/bin/env bash
set -euo pipefail

: "${CLOUDFLARE_ACCOUNT_ID:?Set CLOUDFLARE_ACCOUNT_ID}"
: "${R2_BUCKET:?Set R2_BUCKET}"
: "${R2_ACCESS_KEY_ID:?Set R2_ACCESS_KEY_ID}"
: "${R2_SECRET_ACCESS_KEY:?Set R2_SECRET_ACCESS_KEY}"

command -v aws >/dev/null 2>&1 || {
  echo "The AWS CLI is required. Install it before running this script." >&2
  exit 1
}

export AWS_ACCESS_KEY_ID="${R2_ACCESS_KEY_ID}"
export AWS_SECRET_ACCESS_KEY="${R2_SECRET_ACCESS_KEY}"
export AWS_DEFAULT_REGION="auto"

endpoint="https://${CLOUDFLARE_ACCOUNT_ID}.r2.cloudflarestorage.com"

aws s3 sync \
  _private/slack-videos/ \
  "s3://${R2_BUCKET}/videos/" \
  --endpoint-url "${endpoint}" \
  --cache-control "public,max-age=31536000,immutable" \
  --exclude ".DS_Store"

echo "Media sync complete. Review the bucket and its public custom domain."

