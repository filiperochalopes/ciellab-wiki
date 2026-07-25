# Code Search

Code Search retrieves CIEL concepts and external terminology codes. Use it when
you know the wording but not the code, when a QA suggestion is missing, or when
you need to compare candidates across sources.

## Search modes

| Mode | Best for | Main risk |
| --- | --- | --- |
| Exact code | A known source/code pair | Selecting the wrong source or version |
| Textual | Known words, prefixes, and terminology labels | Missing a differently worded synonym |
| Semantic | Meaning-oriented discovery using embeddings | A plausible but clinically incorrect neighbor |

CIEL searches can use the current HEAD mirror or a fixed version. External
terminologies are indexed on demand and may need a background indexing job
before semantic results are complete.

## Review a result

1. Select the terminology and version.
2. Start with an exact-code or textual query when possible.
3. Use semantic mode to broaden discovery.
4. Inspect status, preferred label, synonyms, and available hierarchy context.
5. Open the code in the authoritative terminology when the change is material.
6. Copy the source, code, display, and intended map type into the review.

Do not ask an LLM to invent a replacement code. CIEL Lab's MCP search can
retrieve indexed candidates, but the same verification rule applies.

## Semantic ranking limitation

Embeddings compress meaning into a similarity vector. A broad phrase can score
above a more specific post-coordinated expression. The behavior discussed in
[OpenConceptLab/ocl_issues#2389](https://github.com/OpenConceptLab/ocl_issues/issues/2389)
is a useful example: specificity and laterality may not dominate the nearest
neighbor score.

Use terminology filters, exact attributes, and human reranking when the
distinction is clinically meaningful.

## Comparison demonstration

<div class="ciellab-video-wrapper {{ R2_VIDEO_WRAPPER_CLASS }}">
  <video class="ciellab-video" controls preload="metadata">
    <source src="{{ R2_PUBLIC_BASE_URL }}/videos/2026-02-06-code-matching-comparison.webm" type="video/webm">
    Your browser does not support embedded WebM video.
  </video>
  <p class="ciellab-video-error" role="status" {{ R2_VIDEO_ERROR_HIDDEN }}>
    The video could not be loaded. The media file or Cloudflare R2 configuration may be unavailable.
  </p>
</div>
