#!/usr/bin/env python3
"""capture_gate.py — the Phase-0 capture gate for the self-improvement loop.

Converts the discretionary `cycle-discipline` / `failure-is-a-finding` rules into
a deterministic gate: a cycle must not end "clean" unless it produced **(a)** a new
`docs/agent/cycle-log.md` row AND **(b)** at least one new/edited
`docs/wiki/findings/` or `docs/wiki/concepts/` page with valid attribution
frontmatter + ≥1 cite. This is the mechanism that was missing on 2026-06-08, when
the P2 record capture only happened because a human asked.

Design doc: `docs/agent/meta-learning-automation.md` (Gap 2 / Phase 0).

Two open questions, resolved here:

- **What counts as "verified" for the cite requirement?** → *any cite*: a non-empty
  `cites:` frontmatter list (the canonical mechanism — 99/100 findings use it) OR an
  inline reference to a `docs/source/`/`docs/wiki/` path or an external URL/arxiv id.
  We deliberately do NOT require a triple-verify pass here — that gates *submission*,
  not *capture*; the anti-bloat lint (Phase 4) + human promotion gate are the counters
  to low-value findings, per the design doc.
- **Hard-block or warn?** → the *hook wrapper* decides via `EINSTEIN_CAPTURE_GATE`
  (`warn` default / `block` / `off`) and the Stop-hook `stop_hook_active` guard so a
  session is never trapped mid-debug. This module only computes pass/fail + reasons.

This module is stdlib-only (no `einstein` import) so the hook runs without the venv.

Usage::

    python3 docs/tools/capture_gate.py --repo . --base main
    #   exit 0 + prints "OK ..." when the gate passes (or cannot be evaluated)
    #   exit 1 + prints the failure reason when it fails
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

# A cycle-log data row: "| 7 | P2-... | ...". Header/separator rows start with
# "| # |" or "|---", which the leading-integer requirement excludes.
_ROW_RE = re.compile(r"^\+\|\s*\d+\s*\|")

# Inline-citation fallback when a page omits the `cites:` frontmatter field.
_INLINE_CITE_RE = re.compile(r"docs/(?:source|wiki)/|https?://|arxiv\.org|arXiv:\d", re.IGNORECASE)

_VALID_AUTHORS = {"agent", "human", "hybrid"}

CYCLE_LOG = "docs/agent/cycle-log.md"
CAPTURE_DIRS = ("docs/wiki/findings/", "docs/wiki/concepts/")


# --------------------------------------------------------------------------- git


def _git(repo: Path, *args: str) -> str:
    """Run a git command in `repo`; return stdout (stripped). Raises on error."""
    out = subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True,
        text=True,
        check=True,
    )
    return out.stdout


def _merge_base(repo: Path, base: str) -> str:
    """Resolve the diff anchor: merge-base(base, HEAD) so we only see *this*
    branch's additions, not divergence on `base`. Falls back to `base` itself."""
    try:
        return _git(repo, "merge-base", base, "HEAD").strip() or base
    except subprocess.CalledProcessError:
        return base


def changed_files(repo: Path, anchor: str) -> set[str]:
    """Repo-relative paths changed since `anchor` — committed-or-working-tree diff
    (tracked) ∪ untracked-not-ignored. Mirrors what a reviewer would see as "new
    this branch/cycle"."""
    tracked = _git(repo, "diff", "--name-only", anchor).splitlines()
    untracked = _git(repo, "ls-files", "--others", "--exclude-standard").splitlines()
    return {p.strip() for p in (*tracked, *untracked) if p.strip()}


# ---------------------------------------------------------------- frontmatter


def parse_frontmatter(text: str) -> dict[str, object]:
    """Minimal YAML-frontmatter parser — enough for attribution + cite checks.

    Handles `key: scalar`, `key: [a, b]` (inline list), and a block list::

        cites:
          - a
          - b

    Returns {} when there is no leading `---` frontmatter block.
    """
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    block = text[3:end].splitlines()
    meta: dict[str, object] = {}
    cur_key: str | None = None
    for raw in block:
        line = raw.rstrip()
        if not line.strip():
            continue
        item = re.match(r"\s*-\s+(.*)$", line)
        if item and cur_key is not None:
            meta.setdefault(cur_key, [])
            val = meta[cur_key]
            if isinstance(val, list):
                val.append(item.group(1).strip())
            continue
        kv = re.match(r"(\w[\w-]*):\s*(.*)$", line)
        if not kv:
            continue
        key, rest = kv.group(1), kv.group(2).strip()
        cur_key = key
        if rest == "":
            meta[key] = []  # may be filled by a following block list
        elif rest.startswith("[") and rest.endswith("]"):
            inner = rest[1:-1].strip()
            meta[key] = [x.strip() for x in inner.split(",") if x.strip()]
        else:
            meta[key] = rest
    return meta


def has_valid_frontmatter(meta: dict[str, object]) -> bool:
    """Valid attribution per `.claude/rules/wiki-attribution.md`: a `type` and an
    `author` in {agent, human, hybrid}."""
    author = str(meta.get("author", "")).strip().lower()
    return bool(meta.get("type")) and author in _VALID_AUTHORS


def has_cite(meta: dict[str, object], body: str) -> bool:
    """≥1 cite: a non-empty `cites:` list, OR a non-empty related_* list, OR an
    inline source/wiki/URL reference in the body."""
    for key in ("cites", "related_findings", "related_concepts"):
        val = meta.get(key)
        if isinstance(val, list) and val:
            return True
        if isinstance(val, str) and val.strip():
            return True
    return bool(_INLINE_CITE_RE.search(body))


# ------------------------------------------------------------------- the gate


def cycle_row_added(repo: Path, anchor: str) -> bool:
    """True when the diff since `anchor` adds ≥1 cycle-log *data* row."""
    try:
        diff = _git(repo, "diff", "-U0", anchor, "--", CYCLE_LOG)
    except subprocess.CalledProcessError:
        return False
    return any(_ROW_RE.match(line) for line in diff.splitlines())


def qualifying_capture_pages(repo: Path, changed: set[str]) -> list[str]:
    """Changed findings/concepts pages that have valid frontmatter + ≥1 cite."""
    out: list[str] = []
    for rel in sorted(changed):
        if not rel.endswith(".md"):
            continue
        if not rel.startswith(CAPTURE_DIRS):
            continue
        if Path(rel).name.upper() == "README.MD":
            continue
        fp = repo / rel
        if not fp.exists():
            continue  # deleted
        text = fp.read_text(encoding="utf-8", errors="replace")
        meta = parse_frontmatter(text)
        if has_valid_frontmatter(meta) and has_cite(meta, text):
            out.append(rel)
    return out


def check_capture(repo: Path, base: str) -> tuple[bool, list[str]]:
    """Evaluate the gate. Returns (passed, reasons).

    On any git error the gate *passes* (returns True) — it must never trap a
    session on infrastructure failure; the worst case is a missed nag.
    """
    repo = repo.resolve()
    try:
        anchor = _merge_base(repo, base)
        changed = changed_files(repo, anchor)
    except subprocess.CalledProcessError as exc:
        return True, [f"capture-gate: cannot evaluate (git error: {exc}); passing"]

    reasons: list[str] = []
    if not cycle_row_added(repo, anchor):
        reasons.append(
            f"no new {CYCLE_LOG} row since {base} (every cycle owes one row — cycle-discipline)"
        )
    pages = qualifying_capture_pages(repo, changed)
    if not pages:
        reasons.append(
            "no new/edited findings/ or concepts/ page with valid frontmatter "
            "(type + author) and ≥1 cite (failure-is-a-finding)"
        )
    if reasons:
        return False, reasons
    return True, [f"captured: {CYCLE_LOG} row + {len(pages)} cited page(s): {pages}"]


# -------------------------------------------------------------------- CLI


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", default=".", help="repo root (default: cwd)")
    ap.add_argument("--base", default="main", help="base ref to diff against (default: main)")
    args = ap.parse_args(argv)

    passed, reasons = check_capture(Path(args.repo), args.base)
    if passed:
        print("OK — " + (reasons[0] if reasons else "capture gate satisfied"))
        return 0
    print(
        "CAPTURE GATE NOT SATISFIED — this cycle has not recorded its learning:\n  - "
        + "\n  - ".join(reasons)
        + "\nSee .claude/rules/cycle-discipline.md + failure-is-a-finding.md."
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
