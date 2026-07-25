"""Small MkDocs hook for build-time media URL substitution."""

from __future__ import annotations

import os


def on_page_markdown(markdown: str, **_: object) -> str:
    base_url = os.getenv("R2_PUBLIC_BASE_URL", "").strip().rstrip("/")
    is_configured = bool(base_url)

    return (
        markdown.replace("{{ R2_PUBLIC_BASE_URL }}", base_url)
        .replace(
            "{{ R2_VIDEO_WRAPPER_CLASS }}",
            "" if is_configured else "ciellab-video-unconfigured",
        )
        .replace(
            "{{ R2_VIDEO_ERROR_HIDDEN }}",
            "hidden" if is_configured else "",
        )
    )
