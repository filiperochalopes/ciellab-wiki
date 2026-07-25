#!/usr/bin/env python3
"""Report or capture the codebase baseline used by the wiki."""

from __future__ import annotations

import argparse
import hashlib
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parent.parent
BASELINE_PATH = ROOT / "source-baseline.yml"
DEFAULT_REPOSITORIES = {
    "ciel_lab_v2": ROOT.parent / "ciel-lab-v2",
    "ciel_scripts": ROOT.parent / "ciel-scripts",
}


def git(repo: Path, *args: str, check: bool = True) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        check=check,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def git_bytes(repo: Path, *args: str) -> bytes:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True,
        capture_output=True,
    )
    return result.stdout


def load_baseline() -> dict[str, Any]:
    return yaml.safe_load(BASELINE_PATH.read_text(encoding="utf-8"))


def repository_paths() -> dict[str, Path]:
    return {
        "ciel_lab_v2": Path(
            os.getenv("CIEL_LAB_V2_PATH", DEFAULT_REPOSITORIES["ciel_lab_v2"])
        ).expanduser(),
        "ciel_scripts": Path(
            os.getenv("CIEL_SCRIPTS_PATH", DEFAULT_REPOSITORIES["ciel_scripts"])
        ).expanduser(),
    }


def ensure_repository(path: Path) -> None:
    if not (path / ".git").exists():
        raise SystemExit(f"Not a Git repository: {path}")


def normalize_remote(remote: str) -> str:
    if remote.startswith("git@github.com:"):
        return f"https://github.com/{remote.removeprefix('git@github.com:').removesuffix('.git')}"
    return remote.removesuffix(".git")


def status_lines(repo: Path) -> list[str]:
    status = git(repo, "status", "--porcelain=v1")
    return status.splitlines() if status else []


def working_tree_state(repo: Path) -> dict[str, Any]:
    status = status_lines(repo)
    untracked = sorted(git(repo, "ls-files", "--others", "--exclude-standard").splitlines())
    tracked_diff = git_bytes(repo, "diff", "HEAD", "--binary")

    untracked_digest = hashlib.sha256()
    for relative_path in untracked:
        untracked_digest.update(relative_path.encode("utf-8"))
        untracked_digest.update(b"\0")
        untracked_digest.update((repo / relative_path).read_bytes())
        untracked_digest.update(b"\0")

    return {
        "dirty": bool(status),
        "changed_path_count": len(status),
        "untracked_path_count": len(untracked),
        "tracked_diff_sha256": hashlib.sha256(tracked_diff).hexdigest(),
        "untracked_content_sha256": (
            untracked_digest.hexdigest() if untracked else None
        ),
    }


def report() -> int:
    baseline = load_baseline()
    paths = repository_paths()

    for key, repo in paths.items():
        ensure_repository(repo)
        source = baseline["sources"][key]
        stored_commit = source["commit"]
        current_commit = git(repo, "rev-parse", "HEAD")
        current_branch = git(repo, "branch", "--show-current") or "(detached HEAD)"
        status = status_lines(repo)

        print(f"\n{source['name']}")
        print(f"  repository: {repo}")
        print(f"  baseline:   {stored_commit}")
        print(f"  current:    {current_commit}")
        print(f"  branch:     {current_branch}")
        print(f"  worktree:   {'dirty' if status else 'clean'}")

        exists = subprocess.run(
            ["git", "-C", str(repo), "cat-file", "-e", f"{stored_commit}^{{commit}}"],
            capture_output=True,
        ).returncode == 0
        if not exists:
            print("  error: baseline commit is not available locally; fetch the repository.")
            continue

        commits = git(repo, "log", "--oneline", "--decorate", f"{stored_commit}..HEAD")
        print("\n  Commits after baseline:")
        print(f"  {commits.replace(chr(10), chr(10) + '  ')}" if commits else "  (none)")

        diff_stat = git(repo, "diff", "--stat", f"{stored_commit}..HEAD")
        print("\n  Committed diff summary:")
        print(f"  {diff_stat.replace(chr(10), chr(10) + '  ')}" if diff_stat else "  (none)")

        print("\n  Uncommitted paths:")
        print("\n".join(f"  {line}" for line in status) if status else "  (none)")

    return 0


def capture(allow_dirty: bool) -> int:
    baseline = load_baseline()
    paths = repository_paths()
    captured_sources: dict[str, dict[str, Any]] = {}

    for key, repo in paths.items():
        ensure_repository(repo)
        working_tree = working_tree_state(repo)
        if working_tree["dirty"] and not allow_dirty:
            raise SystemExit(
                f"{repo} has local changes. Review/commit them or pass --allow-dirty."
            )

        previous = baseline["sources"][key]
        captured_sources[key] = {
            "name": previous["name"],
            "repository": normalize_remote(git(repo, "remote", "get-url", "origin")),
            "branch": git(repo, "branch", "--show-current") or "(detached HEAD)",
            "commit": git(repo, "rev-parse", "HEAD"),
            "commit_date": git(repo, "show", "-s", "--format=%cI", "HEAD"),
            "working_tree": working_tree,
            "note": (
                "Documentation also considered intentional local changes at capture time."
                if working_tree["dirty"]
                else "Documentation was reviewed against a clean working tree."
            ),
        }

    baseline["captured_at"] = datetime.now(timezone.utc).replace(
        microsecond=0
    ).isoformat().replace("+00:00", "Z")
    baseline["sources"] = captured_sources

    temporary_path = BASELINE_PATH.with_suffix(".yml.tmp")
    temporary_path.write_text(
        yaml.safe_dump(baseline, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )
    temporary_path.replace(BASELINE_PATH)
    print(f"Updated {BASELINE_PATH}")
    print("Review the diff and advance evidence dates only after reviewing those sources.")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("report", help="Report changes after the stored baseline")

    capture_parser = subparsers.add_parser(
        "capture", help="Capture current reviewed repository states"
    )
    capture_parser.add_argument(
        "--confirm-reviewed",
        action="store_true",
        help="Confirm that documentation review is complete",
    )
    capture_parser.add_argument(
        "--allow-dirty",
        action="store_true",
        help="Explicitly include uncommitted local changes in the baseline",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.command == "report":
        return report()
    if not args.confirm_reviewed:
        raise SystemExit("capture requires --confirm-reviewed")
    return capture(args.allow_dirty)


if __name__ == "__main__":
    sys.exit(main())
