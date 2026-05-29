"""meta_loop.queue — review + apply surface for meta_self_edit queue entries.

The `meta_self_edit` gate chain (Goal 3) writes accepted-by-every-gate
candidates to `mb/meta-self-edit-queue/<ts>-<sha>.md` rather than applying
them to the working tree. This module is the human-driven review surface
for that queue.

Two operations:

- `list_queue(queue_dir)` — render queue entries as a human-readable summary.
- `apply_queue_entry(queue_id, ...)` — extract the diff from a queue entry,
  `git apply` it to the working tree, commit, and move the queue file to
  `<queue_dir>-resolved/`.

The `apply` op is **human-initiated only** — there is no auto-merge code
path. Per `docs/wiki/findings/recursive-meta-design.md` § "Revert path",
the queue entry references the pre-edit snapshot so a revert is a
`git apply --reverse` plus restoring the snapshot.

Queue file format (set by `meta_gate.evaluate_meta_self_edit_post_shadow`):

    # meta_self_edit candidate <proposal_id>

    - proposer_id: `<id>`
    - target_path: `scripts/meta_loop.py`
    - evidence_cycles: N
    - shadow: a_wins=True, findings_delta=…, p=…
    - snapshot: `<path>`
    - revert recipe: …

    ## Rationale
    …

    ## Proposed diff

    ```diff
    --- a/scripts/meta_loop.py
    +++ b/scripts/meta_loop.py
    @@ …
    ```
"""

from __future__ import annotations

import datetime as dt
import logging
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

log = logging.getLogger("meta_loop.queue")


# ---------------- queue entry parsing ----------------


_FRONT_FIELD_RE = re.compile(r"^- ([a-z_]+):\s*`?([^`\n]+)`?\s*$", re.MULTILINE)
_DIFF_FENCE_RE = re.compile(r"```diff\n(.*?)\n```", re.DOTALL)


@dataclass(frozen=True)
class QueueEntry:
    """One parsed queue file."""

    queue_id: str  # filename stem (e.g. "20260528t130000-abcdef01")
    queue_path: Path
    proposal_id: str
    proposer_id: str
    target_path: str
    snapshot_path: str
    diff: str
    rationale: str


def parse_queue_entry(path: Path) -> QueueEntry:
    """Parse a queue markdown file into a QueueEntry. Raises on malformed input."""
    text = path.read_text()
    # `# meta_self_edit candidate <id>` header
    title_match = re.search(r"^# meta_self_edit candidate (\S+)", text, re.MULTILINE)
    if not title_match:
        raise ValueError(f"queue file {path} missing title header")
    proposal_id = title_match.group(1)
    # Field rows — strip backticks from values
    fields = dict(_FRONT_FIELD_RE.findall(text))
    target_path = fields.get("target_path", "")
    snapshot_path = fields.get("snapshot", "")
    proposer_id = fields.get("proposer_id", "")
    # Rationale: the lines between ## Rationale and the next ##
    rationale_match = re.search(
        r"^## Rationale\s*\n(.*?)(?=^##\s|\Z)", text, re.MULTILINE | re.DOTALL
    )
    rationale = rationale_match.group(1).strip() if rationale_match else ""
    # Diff body — within ```diff fence
    diff_match = _DIFF_FENCE_RE.search(text)
    if not diff_match:
        raise ValueError(f"queue file {path} missing ```diff fence")
    diff = diff_match.group(1).strip() + "\n"
    return QueueEntry(
        queue_id=path.stem,
        queue_path=path,
        proposal_id=proposal_id,
        proposer_id=proposer_id,
        target_path=target_path,
        snapshot_path=snapshot_path,
        diff=diff,
        rationale=rationale,
    )


def list_queue(queue_dir: Path) -> list[QueueEntry]:
    """List all queue entries; oldest first by filename."""
    if not queue_dir.is_dir():
        return []
    out: list[QueueEntry] = []
    for p in sorted(queue_dir.iterdir()):
        if not p.is_file() or p.suffix != ".md":
            continue
        try:
            out.append(parse_queue_entry(p))
        except ValueError:
            log.warning("skipping malformed queue file: %s", p)
    return out


def render_queue(entries: list[QueueEntry]) -> str:
    """Render queue entries as a short human-readable list."""
    if not entries:
        return "no meta_self_edit queue entries\n"
    lines = [f"{len(entries)} queue entry(ies):\n"]
    for i, e in enumerate(entries, 1):
        lines.append(
            f"  [{i}] {e.queue_id}  proposal={e.proposal_id}  "
            f"target={e.target_path}  proposer={e.proposer_id or '(unset)'}"
        )
        if e.rationale:
            short = (e.rationale[:120] + "…") if len(e.rationale) > 120 else e.rationale
            lines.append(f"      rationale: {short.splitlines()[0]}")
        lines.append(f"      snapshot: {e.snapshot_path}")
    return "\n".join(lines) + "\n"


# ---------------- apply ----------------


@dataclass
class GitRunResult:
    ok: bool
    stdout: str = ""
    stderr: str = ""
    returncode: int = 0


GitRunner = Callable[[list[str], Path, str | None], GitRunResult]


def _default_git_runner(args: list[str], cwd: Path, stdin: str | None) -> GitRunResult:
    try:
        proc = subprocess.run(
            ["git", *args],
            cwd=cwd,
            input=stdin,
            capture_output=True,
            text=True,
            timeout=60,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError) as e:
        return GitRunResult(ok=False, stderr=str(e), returncode=-1)
    return GitRunResult(
        ok=proc.returncode == 0,
        stdout=proc.stdout,
        stderr=proc.stderr,
        returncode=proc.returncode,
    )


@dataclass
class ApplyResult:
    queue_id: str
    ok: bool
    commit_sha: str | None = None
    error: str | None = None
    moved_to: Path | None = None


def apply_queue_entry(
    queue_id: str,
    *,
    queue_dir: Path,
    resolved_dir: Path,
    repo_root: Path,
    git_runner: GitRunner | None = None,
    now: dt.datetime | None = None,
) -> ApplyResult:
    """Apply a queue entry's diff to the working tree.

    - Locates `queue_dir/<queue_id>.md`; parses it.
    - `git apply` the embedded diff, `git add` the target_path, `git commit`.
    - Moves the queue file to `resolved_dir/<queue_id>.md` (so the next list
      doesn't show resolved entries).

    On any failure, the queue file is left in place and an error is returned —
    no partial state.
    """
    runner = git_runner or _default_git_runner
    now = now or dt.datetime.now(dt.timezone.utc)
    queue_path = queue_dir / f"{queue_id}.md"
    if not queue_path.exists():
        return ApplyResult(queue_id=queue_id, ok=False, error=f"no queue entry at {queue_path}")
    try:
        entry = parse_queue_entry(queue_path)
    except ValueError as e:
        return ApplyResult(queue_id=queue_id, ok=False, error=str(e))

    apply_r = runner(["apply", "--whitespace=nowarn"], repo_root, entry.diff)
    if not apply_r.ok:
        return ApplyResult(
            queue_id=queue_id, ok=False, error=f"git apply failed: {apply_r.stderr.strip()}"
        )
    add = runner(["add", entry.target_path], repo_root, None)
    if not add.ok:
        return ApplyResult(
            queue_id=queue_id, ok=False, error=f"git add failed: {add.stderr.strip()}"
        )
    commit_msg = (
        f"meta-loop(meta_self_edit): apply queue {queue_id}\n\n"
        f"proposal: {entry.proposal_id}\n"
        f"proposer: {entry.proposer_id}\n"
        f"target: {entry.target_path}\n"
        f"snapshot: {entry.snapshot_path}\n"
    )
    commit = runner(["commit", "-m", commit_msg], repo_root, None)
    if not commit.ok:
        return ApplyResult(
            queue_id=queue_id, ok=False, error=f"git commit failed: {commit.stderr.strip()}"
        )
    sha_r = runner(["rev-parse", "HEAD"], repo_root, None)
    sha = sha_r.stdout.strip() if sha_r.ok else None

    # Move queue file to resolved dir
    resolved_dir.mkdir(parents=True, exist_ok=True)
    dest = resolved_dir / queue_path.name
    queue_path.rename(dest)
    return ApplyResult(queue_id=queue_id, ok=True, commit_sha=sha, moved_to=dest)


__all__ = [
    "ApplyResult",
    "GitRunResult",
    "GitRunner",
    "QueueEntry",
    "apply_queue_entry",
    "list_queue",
    "parse_queue_entry",
    "render_queue",
]
