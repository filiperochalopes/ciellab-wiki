# Media library

Large media is stored outside Git. Every published file must have a descriptive
filename, a page that explains why it matters, and a reviewed R2 object.

## Published path plan

| R2 object | Documentation use |
| --- | --- |
| `videos/2026-01-15-concept-save.webm` | Concept Manager save sequence |
| `videos/2026-01-15-concept-search-after-save.webm` | Retrieval after a save |
| `videos/2026-02-06-code-matching-comparison.webm` | Code Search comparison |

These three files remain available locally under the Git-ignored
`_private/slack-videos/` directory, have been uploaded to the reviewed R2
`videos/` prefix, and are referenced by the feature pages. They become playable
on the deployed wiki once its `R2_PUBLIC_BASE_URL` GitHub Actions variable is
configured to the bucket's public origin.

## Pending source recordings

The Slack sample identified six additional recordings, ranging from
approximately 11 MB to 24 MB, including:

- post-coordination and semantic ranking;
- an OpenMRS workflow showcase;
- four July 2026 CIEL Lab workflow demonstrations.

Slack's connected file reader rejected files over its download limit, and the
browser's authenticated download route was blocked locally. Their Slack file
IDs, target names, sizes, topics, and pending status are preserved in the
Git-ignored `_private/slack-media-manifest.json`.

Download them manually from the authenticated Slack conversation into
`_private/slack-videos/`, using the manifest target names. Then review, trim,
redact if necessary, and run `./scripts/sync-media.sh`.

## Screenshots

The initial reviewed screenshots are versioned because they are small:

- Required Class Mappings;
- Mapping-candidate CSV import and IMO Procedures review (six WebP screenshots
  from [issue #2608](https://github.com/OpenConceptLab/ocl_issues/issues/2608));
- Release workflow;
- Release SQL artifact action menu (Liquibase conversion and CIELAdmin deploy);
- Release pipeline notification settings and Chrome permission recovery;
- Concept Manager.

Before adding a screenshot:

1. crop unrelated browser and desktop UI;
2. remove tokens, email addresses, notifications, and private names;
3. prefer representative test content;
4. write useful alt text;
5. Keep the image reasonably compressed for a fast static-site build.

## Transcripts

Add an English transcript immediately below a video when the spoken explanation
contains knowledge that should be searchable. A useful transcript:

- removes greetings and unrelated conversation;
- preserves UI labels and error messages;
- includes terminology source and version;
- separates observed behavior from the proposed fix;
- links to the relevant feature or issue.
