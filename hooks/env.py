"""Build-time substitutions for media and documentation provenance."""

from __future__ import annotations

import os
from pathlib import Path
from urllib.parse import quote

import yaml


BASELINE_PATH = Path(__file__).resolve().parent.parent / "source-baseline.yml"


def _load_baseline() -> dict[str, object]:
    with BASELINE_PATH.open(encoding="utf-8") as baseline_file:
        return yaml.safe_load(baseline_file)


def _source(baseline: dict[str, object], key: str) -> dict[str, object]:
    sources = baseline["sources"]
    assert isinstance(sources, dict)
    source = sources[key]
    assert isinstance(source, dict)
    return source


def _working_tree_summary(source: dict[str, object]) -> str:
    working_tree = source["working_tree"]
    assert isinstance(working_tree, dict)
    if not working_tree["dirty"]:
        return "Clean"

    changed = working_tree["changed_path_count"]
    untracked = working_tree["untracked_path_count"]
    return f"Dirty — {changed} changed paths, including {untracked} untracked"


def on_config(config: dict[str, object]) -> dict[str, object]:
    baseline = _load_baseline()
    ciel_lab = _source(baseline, "ciel_lab_v2")
    ciel_scripts = _source(baseline, "ciel_scripts")
    ocl_skills = _source(baseline, "ocl_skills")
    site_url = str(config["site_url"]).rstrip("/")
    baseline_url = f"{site_url}/reference/source-baseline/"

    config["copyright"] = (
        "Source baseline: "
        f"CIEL Lab <code>{str(ciel_lab['commit'])[:7]}</code> · "
        f"CIEL Scripts <code>{str(ciel_scripts['commit'])[:7]}</code> · "
        f"OCL Skills <code>{str(ocl_skills['commit'])[:7]}</code> · "
        f'<a href="{baseline_url}">details</a>'
    )
    return config


def on_page_markdown(markdown: str, **_: object) -> str:
    base_url = os.getenv("R2_PUBLIC_BASE_URL", "").strip().rstrip("/")
    is_configured = bool(base_url)
    baseline = _load_baseline()
    ciel_lab = _source(baseline, "ciel_lab_v2")
    ciel_scripts = _source(baseline, "ciel_scripts")
    ocl_skills = _source(baseline, "ocl_skills")
    reviewed_evidence = baseline["reviewed_evidence"]
    assert isinstance(reviewed_evidence, dict)
    slack = reviewed_evidence["slack"]
    assert isinstance(slack, dict)
    github_issue = reviewed_evidence["github_issue"]
    assert isinstance(github_issue, dict)
    ocl_skills_issue = reviewed_evidence["ocl_skills_issue"]
    assert isinstance(ocl_skills_issue, dict)

    replacements = {
        "{{ BASELINE_CAPTURED_AT }}": str(baseline["captured_at"]),
        "{{ BASELINE_CIEL_LAB_REPOSITORY }}": str(ciel_lab["repository"]),
        "{{ BASELINE_CIEL_LAB_BRANCH }}": str(ciel_lab["branch"]),
        "{{ BASELINE_CIEL_LAB_BRANCH_URL }}": (
            f"{ciel_lab['repository']}/tree/{quote(str(ciel_lab['branch']), safe='/')}"
        ),
        "{{ BASELINE_CIEL_LAB_COMMIT }}": str(ciel_lab["commit"]),
        "{{ BASELINE_CIEL_LAB_COMMIT_SHORT }}": str(ciel_lab["commit"])[:7],
        "{{ BASELINE_CIEL_LAB_COMMIT_URL }}": (
            f"{ciel_lab['repository']}/commit/{ciel_lab['commit']}"
        ),
        "{{ BASELINE_CIEL_LAB_COMMIT_DATE }}": str(ciel_lab["commit_date"]),
        "{{ BASELINE_CIEL_LAB_WORKTREE }}": _working_tree_summary(ciel_lab),
        "{{ BASELINE_CIEL_LAB_COMPARE_URL }}": (
            f"{ciel_lab['repository']}/compare/{ciel_lab['commit']}..."
            f"{quote(str(ciel_lab['branch']), safe='/')}"
        ),
        "{{ BASELINE_CIEL_SCRIPTS_REPOSITORY }}": str(ciel_scripts["repository"]),
        "{{ BASELINE_CIEL_SCRIPTS_BRANCH }}": str(ciel_scripts["branch"]),
        "{{ BASELINE_CIEL_SCRIPTS_BRANCH_URL }}": (
            f"{ciel_scripts['repository']}/tree/"
            f"{quote(str(ciel_scripts['branch']), safe='/')}"
        ),
        "{{ BASELINE_CIEL_SCRIPTS_COMMIT }}": str(ciel_scripts["commit"]),
        "{{ BASELINE_CIEL_SCRIPTS_COMMIT_SHORT }}": str(ciel_scripts["commit"])[:7],
        "{{ BASELINE_CIEL_SCRIPTS_COMMIT_URL }}": (
            f"{ciel_scripts['repository']}/commit/{ciel_scripts['commit']}"
        ),
        "{{ BASELINE_CIEL_SCRIPTS_COMMIT_DATE }}": str(ciel_scripts["commit_date"]),
        "{{ BASELINE_CIEL_SCRIPTS_WORKTREE }}": _working_tree_summary(ciel_scripts),
        "{{ BASELINE_CIEL_SCRIPTS_COMPARE_URL }}": (
            f"{ciel_scripts['repository']}/compare/{ciel_scripts['commit']}..."
            f"{quote(str(ciel_scripts['branch']), safe='/')}"
        ),
        "{{ BASELINE_OCL_SKILLS_REPOSITORY }}": str(ocl_skills["repository"]),
        "{{ BASELINE_OCL_SKILLS_BRANCH }}": str(ocl_skills["branch"]),
        "{{ BASELINE_OCL_SKILLS_BRANCH_URL }}": (
            f"{ocl_skills['repository']}/tree/"
            f"{quote(str(ocl_skills['branch']), safe='/')}"
        ),
        "{{ BASELINE_OCL_SKILLS_COMMIT }}": str(ocl_skills["commit"]),
        "{{ BASELINE_OCL_SKILLS_COMMIT_SHORT }}": str(ocl_skills["commit"])[:7],
        "{{ BASELINE_OCL_SKILLS_COMMIT_URL }}": (
            f"{ocl_skills['repository']}/commit/{ocl_skills['commit']}"
        ),
        "{{ BASELINE_OCL_SKILLS_COMMIT_DATE }}": str(ocl_skills["commit_date"]),
        "{{ BASELINE_OCL_SKILLS_WORKTREE }}": _working_tree_summary(ocl_skills),
        "{{ BASELINE_OCL_SKILLS_COMPARE_URL }}": (
            f"{ocl_skills['repository']}/compare/{ocl_skills['commit']}..."
            f"{quote(str(ocl_skills['branch']), safe='/')}"
        ),
        "{{ BASELINE_SLACK_REVIEWED_THROUGH }}": str(slack["reviewed_through"]),
        "{{ BASELINE_ISSUE_URL }}": str(github_issue["url"]),
        "{{ BASELINE_ISSUE_REVIEWED_THROUGH }}": str(
            github_issue["reviewed_through"]
        ),
        "{{ BASELINE_OCL_SKILLS_ISSUE_URL }}": str(ocl_skills_issue["url"]),
        "{{ BASELINE_OCL_SKILLS_ISSUE_REVIEWED_THROUGH }}": str(
            ocl_skills_issue["reviewed_through"]
        ),
    }

    rendered = (
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
    for placeholder, value in replacements.items():
        rendered = rendered.replace(placeholder, value)
    return rendered
