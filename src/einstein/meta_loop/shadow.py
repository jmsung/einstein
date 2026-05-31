"""meta_loop.shadow — A/B harness for proposals (Goal 5).

Per `docs/wiki/findings/meta-loop-design-from-literature.md` § evaluation:

  Self-attribution is asymmetric (AHE result, 89% of regressions unforeseen).
  Shadow A/B is the regression-foresight gap-filler — fork two worktrees,
  apply the proposal to arm A, run N inner cycles in each arm, compare
  outcome deltas. Promotion requires A wins by a threshold + human sign-off.

Pipeline per proposal (when `requires_shadow=True`):

  1. Create two worktrees:
       cb-shadow-<id>-A on a branch derived from the proposal's diff
       cb-shadow-<id>-B on the current commit (control)
  2. In each arm, run N inner cycles via `cycle_runner(arm_path)`.
  3. Parse each arm's resulting cycle-log; compute per-arm metric tuples.
  4. Compute Δ = A - B on each metric.
  5. Append a row to `mb/logs/meta-shadow-runs.md`.
  6. Cleanup: `git worktree remove` both arms.
  7. Return ShadowResult — Δ + promotion recommendation (still human-gated).

This module exposes pure helpers that are unit-testable (delta computation,
worktree spec construction, the orchestration with an injected cycle_runner).
Actual N-cycle execution is expensive; the harness here is *the contract* —
firing it on a real run is operator-initiated, not in unit tests.
"""

from __future__ import annotations

import datetime as dt
import logging
import re
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from . import diagnose
from .proposals import Proposal, ProposalType

log = logging.getLogger("meta_loop.shadow")


# ---------------- specs ----------------


@dataclass(frozen=True)
class WorktreeSpec:
    """One arm of a shadow A/B run."""

    arm: str  # "A" | "B"
    path: Path
    branch: str

    def __post_init__(self) -> None:
        if self.arm not in ("A", "B"):
            raise ValueError(f"arm must be 'A' or 'B', got {self.arm!r}")


def make_arms(proposal: Proposal, *, worktree_parent: Path) -> tuple[WorktreeSpec, WorktreeSpec]:
    """Build the two arm specs. Branch names embed the proposal id."""
    a = WorktreeSpec(
        arm="A",
        path=worktree_parent / f"cb-shadow-{proposal.id}-A",
        branch=f"meta-shadow/{proposal.id}/A",
    )
    b = WorktreeSpec(
        arm="B",
        path=worktree_parent / f"cb-shadow-{proposal.id}-B",
        branch=f"meta-shadow/{proposal.id}/B",
    )
    return a, b


# ---------------- runner contract ----------------


@dataclass
class RunResult:
    ok: bool
    stdout: str = ""
    stderr: str = ""
    returncode: int = 0


Runner = Callable[[list[str], Path | None, str | None], RunResult]
"""Signature: runner(args, cwd, stdin) -> RunResult."""


def _default_runner(args: list[str], cwd: Path | None, stdin: str | None) -> RunResult:
    try:
        proc = subprocess.run(
            args,
            cwd=cwd,
            input=stdin,
            capture_output=True,
            text=True,
            timeout=900,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError) as e:
        return RunResult(ok=False, stderr=str(e), returncode=-1)
    return RunResult(
        ok=proc.returncode == 0,
        stdout=proc.stdout,
        stderr=proc.stderr,
        returncode=proc.returncode,
    )


# ---------------- worktree setup + apply + cleanup ----------------


def setup_worktree(
    spec: WorktreeSpec,
    *,
    repo_root: Path,
    base_branch: str = "HEAD",
    runner: Runner | None = None,
) -> RunResult:
    """`git worktree add <path> -b <branch> <base>`."""
    r = runner or _default_runner
    return r(
        ["git", "worktree", "add", str(spec.path), "-b", spec.branch, base_branch],
        repo_root,
        None,
    )


def apply_proposal_to_worktree(
    proposal: Proposal,
    spec: WorktreeSpec,
    *,
    runner: Runner | None = None,
) -> RunResult:
    """Apply the proposal's diff/body to the arm's worktree.

    Per-type behavior:

    - `NEW_QUESTION` — write `proposed_diff` to `target_path` as a fresh file.
    - `CODE_EDIT` — *graduate* the draft. `target_path` is
      `scripts/proposed/<slug>.py` by schema; in the shadow arm we write
      the body to `scripts/<slug>.py` AND add stub manifest entries under
      every problem id cited in the body, so the per-problem dispatcher
      can pick the tool up during the B-arm cycles. The draft path
      `scripts/proposed/` stays empty post-apply (Goal 4 invariant). See
      `_apply_code_edit_graduation` for the details.
    - other types — unified diff via `git apply`.
    """
    r = runner or _default_runner
    if proposal.type == ProposalType.CODE_EDIT.value:
        return _apply_code_edit_graduation(proposal, spec, r)
    if proposal.type == ProposalType.NEW_QUESTION.value:
        target = spec.path / proposal.target_path
        if target.exists():
            return RunResult(
                ok=False,
                stderr=(
                    f"target_path={proposal.target_path!r} already exists in worktree "
                    f"{spec.path}; refusing to overwrite"
                ),
                returncode=-1,
            )
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(proposal.proposed_diff)
        add = r(["git", "add", proposal.target_path], spec.path, None)
        if not add.ok:
            return add
        return r(
            ["git", "commit", "-m", f"shadow({spec.arm}): apply {proposal.id}"],
            spec.path,
            None,
        )
    apply_r = r(
        ["git", "apply", "--whitespace=nowarn"],
        spec.path,
        proposal.proposed_diff,
    )
    if not apply_r.ok:
        return apply_r
    add = r(["git", "add", proposal.target_path], spec.path, None)
    if not add.ok:
        return add
    return r(
        ["git", "commit", "-m", f"shadow({spec.arm}): apply {proposal.id}"],
        spec.path,
        None,
    )


# ---- code_edit graduation helpers ----------------------------------------


# Parse `- problems: ['P14', 'P12']` from the draft body's cite block. The
# body shape is set by `code_edit._render_draft_body`; keep this regex in
# sync with that template.
_CITE_PROBLEMS_RE = re.compile(
    r"^- problems:\s*\[(.+?)\]\s*$",
    re.MULTILINE,
)


def _parse_problem_ids_from_body(body: str) -> list[str]:
    """Extract `['P14', 'P12']` from the draft's cite block.

    Returns sorted, deduplicated problem ids. Empty list if no cite block
    is present (e.g. a hand-edited draft) — the apply step still writes
    the script but skips the manifest wire in that case.
    """
    m = _CITE_PROBLEMS_RE.search(body)
    if not m:
        return []
    raw = m.group(1)
    ids = re.findall(r"P\d+", raw)
    return sorted(set(ids))


def _problem_id_int(pid: str) -> int | None:
    m = re.fullmatch(r"P(\d+)", pid)
    return int(m.group(1)) if m else None


def _stub_manifest_entry(slug: str, *, script_path: str) -> str:
    """Render the YAML lines for a stub optimizer entry under a problem.

    Indented to live under `<id>: optimizers:` per the existing
    `optimizer_manifest.yaml` shape. Result is a string with a leading
    newline so it can be appended idempotently.
    """
    py_id = slug.replace("-", "_")
    return (
        f"    # autosynth-stub (shadow B-arm only): see tool-autosynthesis-design.md\n"
        f"    {py_id}:\n"
        f"      script: {script_path}\n"
        f"      cli_args: []\n"
        f"      timeout_seconds: 60\n"
        f"      result_file: results/proposed/{slug}_result.json\n"
        f"      result_parser: json_score_payload\n"
    )


def _apply_code_edit_graduation(
    proposal: Proposal,
    spec: WorktreeSpec,
    r: Runner,
) -> RunResult:
    """Graduate the draft into `scripts/` + wire stub manifest entries.

    Steps:
      1. Refuse if `scripts/<slug>.py` already exists (graduation collision).
      2. Write the body to `scripts/<slug>.py`.
      3. Parse problem_ids from the body's cite block.
      4. For each problem id with a block in `optimizer_manifest.yaml`,
         append a stub optimizer entry under its `optimizers:` mapping.
      5. `git add` both paths; commit.

    The manifest wire is *additive*: existing entries are untouched. If a
    problem block isn't present in the manifest, that id is silently
    skipped (the cycle still runs; the strategy_picker just won't see the
    new tool for that problem). Logged via stdout so the operator can see
    which problems got wired.
    """
    slug = Path(proposal.target_path).stem
    graduated = spec.path / "scripts" / f"{slug}.py"
    if graduated.exists():
        return RunResult(
            ok=False,
            stderr=f"scripts/{slug}.py already exists in worktree; refusing to graduate",
            returncode=-1,
        )
    graduated.parent.mkdir(parents=True, exist_ok=True)
    graduated.write_text(proposal.proposed_diff)
    paths_to_add = [f"scripts/{slug}.py"]

    # Manifest wire (best-effort additive).
    manifest_path = spec.path / "src" / "einstein" / "optimizer_manifest.yaml"
    if manifest_path.is_file():
        body = manifest_path.read_text()
        wired = _wire_manifest(
            body=body,
            problem_ids=_parse_problem_ids_from_body(proposal.proposed_diff),
            slug=slug,
            script_path=f"scripts/{slug}.py",
        )
        if wired != body:
            manifest_path.write_text(wired)
            paths_to_add.append("src/einstein/optimizer_manifest.yaml")

    add = r(["git", "add", *paths_to_add], spec.path, None)
    if not add.ok:
        return add
    return r(
        ["git", "commit", "-m", f"shadow({spec.arm}): graduate {proposal.id} ({slug})"],
        spec.path,
        None,
    )


def _wire_manifest(*, body: str, problem_ids: list[str], slug: str, script_path: str) -> str:
    """Append a stub optimizer entry under each cited problem id.

    Linear pass — no regex backtracking. Splits the manifest into top-level
    blocks keyed on `^\\d+:` headers, finds each cited block, locates its
    `  optimizers:` line, and appends the stub at the end of that block's
    optimizer mapping. Idempotent: if `py_id:` already appears in the
    block, leave it alone.

    Returns the (possibly unchanged) body. Skips problem ids whose block
    isn't present in the manifest (cycle still runs; strategy_picker just
    won't see the new tool for that problem).
    """
    py_id = slug.replace("-", "_")
    entry = _stub_manifest_entry(slug, script_path=script_path)
    targets = {_problem_id_int(p) for p in problem_ids}
    targets.discard(None)
    if not targets:
        return body

    # Split on top-level `^\d+:` headers. Each segment starts with either
    # the preamble (before any header) or `<n>:` block.
    lines = body.splitlines(keepends=True)
    # Identify the start line of each top-level block.
    block_starts: list[int] = []  # indices into `lines`
    block_ids: list[int | None] = []  # parsed `n` for each block, or None for preamble
    block_starts.append(0)
    block_ids.append(None)  # preamble (lines before first `\d+:` header)
    for i, line in enumerate(lines):
        m = re.match(r"^(\d+):\s*$", line.rstrip("\n"))
        if m and i > 0:
            block_starts.append(i)
            block_ids.append(int(m.group(1)))
    # Also handle the case where line 0 is a header (no preamble).
    if lines and re.match(r"^(\d+):\s*$", lines[0].rstrip("\n")):
        block_ids[0] = int(re.match(r"^(\d+):\s*$", lines[0].rstrip("\n")).group(1))

    # Walk each block; if target + not already wired, append the stub
    # right before the next block starts.
    out_segments: list[str] = []
    for bi, start in enumerate(block_starts):
        end = block_starts[bi + 1] if bi + 1 < len(block_starts) else len(lines)
        segment = "".join(lines[start:end])
        n = block_ids[bi]
        if n in targets and f"\n    {py_id}:" not in ("\n" + segment):
            # Append the stub at the end of this block (before the trailing
            # blank line(s)). The entry is indented to live under
            # `<n>: optimizers:`.
            trimmed = segment.rstrip("\n")
            trailing = segment[len(trimmed) :]
            segment = trimmed + "\n" + entry + trailing
        out_segments.append(segment)
    return "".join(out_segments)


def remove_worktree(
    spec: WorktreeSpec,
    *,
    repo_root: Path,
    runner: Runner | None = None,
) -> RunResult:
    """`git worktree remove --force <path>`."""
    r = runner or _default_runner
    res = r(
        ["git", "worktree", "remove", "--force", str(spec.path)],
        repo_root,
        None,
    )
    # On a stale worktree where git lost track, fall back to rm -rf
    if not res.ok and spec.path.exists():
        try:
            shutil.rmtree(spec.path)
            res = RunResult(ok=True, stdout=f"fallback rm -rf {spec.path}")
        except OSError as e:
            res = RunResult(ok=False, stderr=str(e), returncode=-1)
    return res


# ---------------- delta computation ----------------


@dataclass(frozen=True)
class ArmMetrics:
    """Per-arm metric tuple computed from that arm's cycle-log rows.

    `tool_invoked_cycles` is populated only when `compute_arm_metrics` is
    called with a `tool_slug` — the count of cycles whose notes mention
    the slug (case-insensitive). For `code_edit` shadow runs this is the
    key promotion signal (Goal 5).
    """

    cycles: int
    score_changed_cycles: int
    findings_added: int
    concepts_added: int
    dead_ends_added: int
    tokens_in: int = 0  # placeholder — not parsed yet
    tokens_out: int = 0
    tool_invoked_cycles: int = 0

    def per_cycle(self, attr: str) -> float:
        if self.cycles == 0:
            return 0.0
        return getattr(self, attr) / self.cycles


@dataclass(frozen=True)
class MetaArmMetrics:
    """Per-arm meta-layer metrics — read from the arm's meta-proposals audit log.

    Goal 4 of `js/feat/recursive-meta`: the cycle-log metrics on `ArmMetrics`
    don't move enough on `meta_self_edit` shadow runs (an edit that quiets a
    proposer looks identical to one that breaks it). The meta-layer signals
    below are what distinguishes the two — they read from the audit log the
    gate chain writes to, not from cycle-log.

    See `docs/wiki/findings/recursive-meta-design.md` § "What shadow A/B wins
    means for the meta layer". The Goodhart counter-measure remains the
    dead-end-non-regression check on the cycle-log side (`ShadowDelta.a_wins`).
    """

    proposals_emitted: int
    proposals_accepted: int
    proposals_rejected: int
    proposals_queued: int
    proposals_shadow_pending: int

    @property
    def gate_pass_rate(self) -> float:
        if self.proposals_emitted == 0:
            return 0.0
        return (self.proposals_accepted + self.proposals_queued) / self.proposals_emitted


def parse_meta_arm_metrics(audit_log_path: Path) -> MetaArmMetrics:
    """Count audit-log rows by decision to build per-arm meta metrics.

    Uses meta_gate._parse_audit_log under the hood so the row format stays
    in one place. Returns all-zeros if the audit log is missing or empty —
    silent rather than throwing, because shadow runs may legitimately
    produce no proposals.
    """
    # Local import to avoid circular module-load (meta_gate → propose → meta_loop)
    from .meta_gate import _parse_audit_log

    rows = _parse_audit_log(audit_log_path)
    if not rows:
        return MetaArmMetrics(0, 0, 0, 0, 0)
    return MetaArmMetrics(
        proposals_emitted=len(rows),
        proposals_accepted=sum(1 for r in rows if r["decision"] == "accepted"),
        proposals_rejected=sum(1 for r in rows if r["decision"] == "rejected"),
        proposals_queued=sum(1 for r in rows if r["decision"] == "queued"),
        proposals_shadow_pending=sum(1 for r in rows if r["decision"] == "shadow-pending"),
    )


@dataclass(frozen=True)
class ShadowMetaDelta:
    """A/B delta on meta-layer signals — pair to ShadowDelta for meta_self_edit."""

    arm_a: MetaArmMetrics
    arm_b: MetaArmMetrics

    @property
    def emit_rate_delta(self) -> int:
        return self.arm_a.proposals_emitted - self.arm_b.proposals_emitted

    @property
    def gate_pass_rate_delta(self) -> float:
        return self.arm_a.gate_pass_rate - self.arm_b.gate_pass_rate

    @property
    def queued_delta(self) -> int:
        return self.arm_a.proposals_queued - self.arm_b.proposals_queued


def _safe_int(s: str) -> int:
    """Pull the leading integer out of a cell like '1 (`dead-end-foo.md`)'."""
    if not s:
        return 0
    s = s.strip()
    digits = []
    for ch in s:
        if ch.isdigit():
            digits.append(ch)
        elif digits:
            break
    return int("".join(digits)) if digits else 0


def compute_arm_metrics(
    rows: list[diagnose.CycleRow],
    *,
    tool_slug: str | None = None,
) -> ArmMetrics:
    """Aggregate per-arm metrics from parsed cycle-log rows.

    `tool_slug` (Goal 4 of `js/feat/tool-autosynthesis`): if provided,
    count cycles whose `notes` mention the slug (case-insensitive). This
    becomes the `tool_invoked_cycles` field — the citation-grounded
    promotion signal for `code_edit` shadow runs.
    """
    if not rows:
        return ArmMetrics(0, 0, 0, 0, 0)
    findings = sum(_safe_int(r.findings_added) for r in rows)
    concepts = sum(_safe_int(r.concepts_added) for r in rows)
    # Dead-ends approximated by the count of "dead-end" outcomes
    dead_ends = sum(1 for r in rows if "dead-end" in r.outcome.lower())
    tool_invoked = 0
    if tool_slug:
        slug_low = tool_slug.lower()
        tool_invoked = sum(1 for r in rows if slug_low in (r.notes or "").lower())
    return ArmMetrics(
        cycles=len(rows),
        score_changed_cycles=sum(1 for r in rows if r.score_changed),
        findings_added=findings,
        concepts_added=concepts,
        dead_ends_added=dead_ends,
        tool_invoked_cycles=tool_invoked,
    )


@dataclass(frozen=True)
class ShadowDelta:
    """Result of one A/B comparison."""

    arm_a: ArmMetrics
    arm_b: ArmMetrics

    # Per-cycle deltas (A - B) on each metric
    @property
    def score_changed_delta(self) -> float:
        return self.arm_a.per_cycle("score_changed_cycles") - self.arm_b.per_cycle(
            "score_changed_cycles"
        )

    @property
    def findings_delta(self) -> float:
        return self.arm_a.per_cycle("findings_added") - self.arm_b.per_cycle("findings_added")

    @property
    def concepts_delta(self) -> float:
        return self.arm_a.per_cycle("concepts_added") - self.arm_b.per_cycle("concepts_added")

    @property
    def dead_ends_delta(self) -> float:
        return self.arm_a.per_cycle("dead_ends_added") - self.arm_b.per_cycle("dead_ends_added")

    def a_wins(
        self, *, min_findings_delta: float = 0.0, min_score_changed_delta: float = 0.0
    ) -> bool:
        """A wins iff A is non-worse on score-change and strictly better on
        any of findings/concepts, with neither regression of either dead-ends
        relative to B.

        Trivial default thresholds — caller can tighten.
        """
        if self.score_changed_delta < min_score_changed_delta:
            return False
        # Strict improvement on findings or concepts (any positive Δ)
        positive_signal = self.findings_delta > min_findings_delta or self.concepts_delta > 0
        # Avoid regressing on dead-ends (more dead-ends = more failed attempts,
        # but it's neutral if score also moved — only flag when score didn't move)
        not_worse_on_dead_ends = self.dead_ends_delta <= 0
        return positive_signal and not_worse_on_dead_ends


# ---------------- shadow log ----------------


SHADOW_LOG_HEADER = (
    "| timestamp_utc | proposal_id | n_cycles | A_score_chg | A_findings "
    "| A_concepts | B_score_chg | B_findings | B_concepts | "
    "Δ_findings_per_cycle | a_wins | reason |\n"
    "|---|---|---|---|---|---|---|---|---|---|---|---|\n"
)


def _ensure_shadow_log_header(path: Path) -> None:
    if path.is_file():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("# meta-shadow runs\n\n" + SHADOW_LOG_HEADER)


def append_shadow_log(
    path: Path,
    *,
    timestamp: dt.datetime,
    proposal: Proposal,
    n_cycles: int,
    delta: ShadowDelta,
    a_wins: bool,
    reason: str,
) -> None:
    _ensure_shadow_log_header(path)
    row = (
        f"| {timestamp.strftime('%Y-%m-%dT%H:%M:%SZ')} "
        f"| {proposal.id} | {n_cycles} "
        f"| {delta.arm_a.score_changed_cycles} | {delta.arm_a.findings_added} "
        f"| {delta.arm_a.concepts_added} "
        f"| {delta.arm_b.score_changed_cycles} | {delta.arm_b.findings_added} "
        f"| {delta.arm_b.concepts_added} "
        f"| {delta.findings_delta:.3f} "
        f"| {'yes' if a_wins else 'no'} "
        f"| {reason} |\n"
    )
    with path.open("a") as fh:
        fh.write(row)


# ---------------- orchestration ----------------


@dataclass
class ShadowResult:
    proposal_id: str
    n_cycles: int
    delta: ShadowDelta | None = None
    a_wins: bool = False
    reason: str = ""
    error: str | None = None
    cleaned_up: bool = False


CycleRunner = Callable[[Path, int], list[diagnose.CycleRow]]
"""run_n_cycles(arm_path, n) -> list of CycleRow rows produced."""


DEFAULT_CYCLE_RUNNER_TIMEOUT_SECONDS = 14400  # 4h — fits N=10 at observed ~12 min/cycle


def _with_env(os_mod, key: str, value: str, fn):
    """Run ``fn()`` with ``os_mod.environ[key] = value``; restore prior state.

    Used by `run_shadow` to mark each arm's cycle_runner subprocess via
    inherited env vars (Goal 9 of js/feat/research-synthesis). os_mod is
    injected so tests can verify the env was set/cleared correctly.
    """
    prior = os_mod.environ.get(key)
    os_mod.environ[key] = value
    try:
        return fn()
    finally:
        if prior is None:
            os_mod.environ.pop(key, None)
        else:
            os_mod.environ[key] = prior


def default_cycle_runner(
    arm_path: Path,
    n: int,
    *,
    timeout_seconds: int = DEFAULT_CYCLE_RUNNER_TIMEOUT_SECONDS,
    env: dict[str, str] | None = None,
) -> list[diagnose.CycleRow]:
    """Shell out to scripts/autonomous_loop.py inside the arm worktree.

    Captures the cycle-log rows that get APPENDED during this run by
    snapshotting the cycle-log size before/after and parsing the delta.

    Heavy: each cycle is an LLM call. Real use is operator-initiated;
    unit tests stub this.

    On `subprocess.TimeoutExpired`: subprocess is killed, but we still parse
    whatever rows the autonomous_loop appended before being killed and return
    them. Without this, a single slow arm crashes the whole shadow run + we
    lose all in-flight work to the `cleanup=True` finally-block.

    Goal 9 of js/feat/research-synthesis: ``env`` is merged over
    ``os.environ`` so the caller can set per-arm env vars (e.g.
    ``EINSTEIN_SHADOW_ARM=A``) that the inner agent's sidecar writes pick up.
    Without it, both arms' citation records are indistinguishable in the
    shared sidecar and the promotion gate can't measure per-arm counts.
    """
    import os as _os

    cycle_log = arm_path / "docs" / "agent" / "cycle-log.md"
    rows_before = diagnose.parse_cycle_log(cycle_log)
    before_ids = {r.cycle_id for r in rows_before}

    full_env = _os.environ.copy()
    if env:
        full_env.update(env)

    try:
        proc = subprocess.run(
            [
                "uv",
                "run",
                "python",
                "scripts/autonomous_loop.py",
                "--max-problems",
                str(n),
            ],
            cwd=arm_path,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
            check=False,
            env=full_env,
        )
        if proc.returncode != 0:
            log.warning(
                "autonomous_loop in %s exited %d; stderr: %s",
                arm_path,
                proc.returncode,
                proc.stderr[-500:],
            )
    except subprocess.TimeoutExpired:
        log.warning(
            "autonomous_loop in %s timed out after %ds; returning partial rows",
            arm_path,
            timeout_seconds,
        )

    rows_after = diagnose.parse_cycle_log(cycle_log)
    return [r for r in rows_after if r.cycle_id not in before_ids]


def run_shadow(
    proposal: Proposal,
    *,
    repo_root: Path,
    n_cycles: int = 10,
    worktree_parent: Path | None = None,
    cycle_runner: CycleRunner,
    git_runner: Runner | None = None,
    shadow_log: Path | None = None,
    cleanup: bool = True,
    clock: Callable[[], dt.datetime] | None = None,
) -> ShadowResult:
    """Run a full shadow A/B comparison. Returns ShadowResult.

    Args:
        proposal: must have requires_shadow=True; this isn't enforced here
            (the gate chain handles routing) but logged.
        cycle_runner: REQUIRED — runs N cycles in one arm and returns the
            parsed cycle-log rows that arm produced. The real implementation
            shells out to scripts/autonomous_loop.py; tests inject a stub.
        cleanup: when True, `git worktree remove` both arms after the run.
            Set False to keep the worktrees for human inspection.
    """
    now = (clock or (lambda: dt.datetime.now(dt.timezone.utc)))()
    parent = worktree_parent or repo_root.parent

    arm_a, arm_b = make_arms(proposal, worktree_parent=parent)
    result = ShadowResult(proposal_id=proposal.id, n_cycles=n_cycles)

    runner = git_runner or _default_runner
    try:
        # Setup both arms from current HEAD
        s = setup_worktree(arm_a, repo_root=repo_root, runner=runner)
        if not s.ok:
            result.error = f"setup A failed: {s.stderr.strip()}"
            return result
        s = setup_worktree(arm_b, repo_root=repo_root, runner=runner)
        if not s.ok:
            result.error = f"setup B failed: {s.stderr.strip()}"
            return result
        # Apply proposal to A only
        a = apply_proposal_to_worktree(proposal, arm_a, runner=runner)
        if not a.ok:
            result.error = f"apply to A failed: {a.stderr.strip()}"
            return result
        # Run N cycles in each arm. Goal 9 of js/feat/research-synthesis:
        # set EINSTEIN_SHADOW_ARM in os.environ so the cycle_runner
        # subprocess inherits it; inner_agent_output.append_citation_record
        # tags each sidecar record with the arm letter. This lets the
        # downstream promotion gate compute per-arm citation counts from
        # the shared sidecar JSONL after cleanup deletes the arm cycle-logs.
        import os as _os

        rows_a = _with_env(
            _os, "EINSTEIN_SHADOW_ARM", "A", lambda: cycle_runner(arm_a.path, n_cycles)
        )
        rows_b = _with_env(
            _os, "EINSTEIN_SHADOW_ARM", "B", lambda: cycle_runner(arm_b.path, n_cycles)
        )
        # For code_edit proposals, count cycles that mention the tool slug.
        # The B-arm has the tool wired into its manifest; A-arm is control.
        tool_slug: str | None = None
        if proposal.type == ProposalType.CODE_EDIT.value:
            tool_slug = Path(proposal.target_path).stem
        delta = ShadowDelta(
            arm_a=compute_arm_metrics(rows_a, tool_slug=tool_slug),
            arm_b=compute_arm_metrics(rows_b, tool_slug=tool_slug),
        )
        result.delta = delta
        result.a_wins = delta.a_wins()
        result.reason = (
            f"Δfindings/cycle={delta.findings_delta:.3f}, "
            f"Δscore_changed/cycle={delta.score_changed_delta:.3f}"
        )
        if shadow_log is not None:
            append_shadow_log(
                shadow_log,
                timestamp=now,
                proposal=proposal,
                n_cycles=n_cycles,
                delta=delta,
                a_wins=result.a_wins,
                reason=result.reason,
            )
    finally:
        if cleanup:
            for arm in (arm_a, arm_b):
                rm = remove_worktree(arm, repo_root=repo_root, runner=runner)
                if not rm.ok:
                    log.warning("cleanup %s failed: %s", arm.path, rm.stderr)
            result.cleaned_up = True
    return result


__all__ = [
    "ArmMetrics",
    "CycleRunner",
    "MetaArmMetrics",
    "RunResult",
    "Runner",
    "ShadowDelta",
    "ShadowMetaDelta",
    "ShadowResult",
    "WorktreeSpec",
    "append_shadow_log",
    "apply_proposal_to_worktree",
    "compute_arm_metrics",
    "default_cycle_runner",
    "make_arms",
    "parse_meta_arm_metrics",
    "remove_worktree",
    "run_shadow",
    "setup_worktree",
]
