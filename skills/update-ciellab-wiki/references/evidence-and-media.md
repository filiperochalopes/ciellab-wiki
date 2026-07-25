# Evidence and media

## Slack sampling

Use the review-through date in `source-baseline.yml` as the lower bound.
Within the authorized conversation:

1. Search the product name and common variants.
2. Search focused terms for features changed in the code diff.
3. Search `has:file` and video/image file types.
4. Search bug language such as `fixed`, `error`, `failed`, `working`, and
   `resolved`.
5. Search workflow terms such as `worklist`, `bulk validation`, `release`,
   `retired`, `mapping`, `translation`, `cache`, `MCP`, `Qdrant`, and
   `embedding`.
6. Paginate until the bounded window is exhausted.
7. Read the parent thread and nearby context for selected evidence.

Do not infer that a discussed fix is current. Verify it in code, tests, the
deployed UI when requested, or a public issue.

Advance `reviewed_through` only when the complete intended window was covered.
If access or pagination was incomplete, preserve the previous date and report
the gap.

## Evidence classification

Classify each useful item as:

- user question;
- current instruction;
- bug report;
- proposed design;
- confirmed fix;
- known limitation;
- operational recovery;
- demonstration media.

Turn repeated questions into durable Q&A. Link public issues when the issue
directly supports the claim. Do not add a link merely because issue numbers
appear nearby.

## Security

Never transfer:

- passwords, PATs, OCL tokens, database credentials, or connection strings;
- private Slack permalinks;
- meeting URLs;
- patient or private personal information;
- unrelated names or notifications;
- licensed terminology source files that cannot be redistributed.

If exposed credentials are discovered, omit their values and advise rotation in
the handoff.

## Media lifecycle

1. Record Slack file metadata in the ignored private manifest.
2. Download into `_private/slack-videos/` or `_private/slack-screenshots/`.
3. Inspect and redact before publication.
4. Copy only reviewed screenshots into `docs/assets/screenshots/`.
5. Keep videos out of Git and sync reviewed files to R2.
6. Add captions and transcripts for searchable knowledge.

For connector size limits or authenticated-download failures, record
`pending_authenticated_download` or another precise status. Do not fabricate a
local file, public URL, transcript, or successful upload.

