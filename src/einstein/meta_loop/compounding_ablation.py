"""Blank-slate Cold-vs-Warm knowledge-compounding ablation harness.

Pre-registration: docs/agent/ablations/2026-06-26-knowledge-compounding-preregistration.md
This module is §10.3 (per-arm session launcher) + §10.4 (run driver).

The causal test the paper still owes: does the *read -> solve -> write-back ->
reuse* loop itself make the agent better across a sequence of fresh problems?
Two arms, identical in everything except the memory loop:

- **Cold (control):** memory wiped between problems; every problem solved from an
  empty KB, from scratch.
- **Warm (treatment):** writes one lesson after each problem and may read its own
  accumulated lessons before later problems; the KB grows across the sequence.

Both start blank (empty KB), neither submits to the arena, neither gets a
warm-*start* seed (pre-reg §5). v1 holds web search and personas OFF for both
(pre-reg §11) so the only thing that varies is the memory loop.

Like `ablation.py` (the 3-arm knowledge-access experiment), this is the *harness,
not the run*: real execution spawns a fresh Claude Code session per
(problem, arm, seed) — autonomous self-execution from inside one session would
defeat the control. The harness defines the arms, builds + threads the run KB,
enforces the sanity invariants (pre-reg §9), and is driven by an injected
`solve_fn` so it is fully testable; a production runner supplies a `solve_fn`
that launches the session described by `SessionSpec`.

Reuses metric primitives from `ablation.py` (climb_rate, cycles_to_fraction_of_floor,
dead_ends_avoided) and `trajectory.TrajectoryPoint`.
"""

from __future__ import annotations

import enum
import hashlib
import json
import statistics
from collections.abc import Callable, Sequence
from dataclasses import dataclass, field
from pathlib import Path

from einstein.meta_loop.ablation import dead_ends_avoided, is_firewalled
from einstein.meta_loop.trajectory import TrajectoryPoint

# ---------------- arms (the one independent variable: the memory loop) ----------------


class Arm(enum.Enum):
    COLD = "cold"
    WARM = "warm"


@dataclass(frozen=True)
class ArmConfig:
    """What an arm may do with memory. Everything NOT here is identical between
    arms (base model, tools, solver code, compute budget, problem statement).
    `allow_web` / `allow_personas` are held at the SAME value for both arms in v1
    (pre-reg §11) — they are recorded, not varied."""

    arm: Arm
    read_kb: bool  # may read accumulated lessons before a problem
    write_kb: bool  # persists a lesson after a problem (carried to later problems)
    allow_web: bool = False  # §11: OFF for both arms in v1
    allow_personas: bool = False  # §11: OFF for both arms in v1

    @property
    def label(self) -> str:
        return self.arm.value


ARM_CONFIGS: dict[Arm, ArmConfig] = {
    Arm.COLD: ArmConfig(Arm.COLD, read_kb=False, write_kb=False),
    Arm.WARM: ArmConfig(Arm.WARM, read_kb=True, write_kb=True),
}


def arms_isolated() -> bool:
    """One-variable invariant: the arms differ ONLY in the memory loop.

    Web access and persona access must be identical across arms (held constant),
    and the (read_kb, write_kb) memory-loop pair must differ between them. Guards
    against a config edit silently turning this into a multi-variable experiment.
    """
    configs = list(ARM_CONFIGS.values())
    webs = {c.allow_web for c in configs}
    personas = {c.allow_personas for c in configs}
    memory = {(c.read_kb, c.write_kb) for c in configs}
    return len(webs) == 1 and len(personas) == 1 and len(memory) == len(configs)


# ---------------- run KB (the persistence layer that compounds) ----------------


@dataclass
class RunKB:
    """A run's accumulated-lesson directory. Warm reads+writes it across the
    problem sequence; Cold's is wiped before every problem so it is always empty.

    A lesson is one markdown file (pre-reg §3: <=1 page per problem capturing the
    operator/parameterization that worked, dead-ends to skip, transferable
    structure). Lessons are ordered by write index so reads are deterministic.
    """

    root: Path

    def __post_init__(self) -> None:
        self.root = Path(self.root)
        self.root.mkdir(parents=True, exist_ok=True)

    def _lessons(self) -> list[Path]:
        return sorted(self.root.glob("lesson-*.md"))

    def wipe(self) -> None:
        for f in self._lessons():
            f.unlink()

    def is_empty(self) -> bool:
        return not self._lessons()

    def lesson_count(self) -> int:
        return len(self._lessons())

    def write_lesson(self, problem_id: str, text: str) -> Path:
        idx = self.lesson_count()
        path = self.root / f"lesson-{idx:03d}-{problem_id}.md"
        path.write_text(text)
        return path

    def read_lessons(self, *, max_chars: int | None = None) -> list[str]:
        """Accumulated lessons in write order, capped to `max_chars` total so
        both arms get an equal max context (pre-reg §12 token-budget mitigation).
        The cap drops whole lessons from the end, never truncates one mid-file."""
        out: list[str] = []
        total = 0
        for f in self._lessons():
            t = f.read_text()
            if max_chars is not None and total + len(t) > max_chars:
                break
            out.append(t)
            total += len(t)
        return out

    def state_hash(self) -> str:
        """Stable hash of the KB contents — recorded before/after each problem so
        the audit trail proves Cold stayed empty and Warm grew (pre-reg §10 schema
        kb_state_hash_before/after)."""
        h = hashlib.sha256()
        for f in self._lessons():
            h.update(f.name.encode())
            h.update(f.read_bytes())
        return h.hexdigest()[:16]


# Empty-KB hash sentinel (sha256 of nothing), for asserting Cold is empty.
EMPTY_KB_HASH = hashlib.sha256().hexdigest()[:16]


# ---------------- problem + run matrix ----------------


@dataclass(frozen=True)
class Problem:
    """One frozen problem from config/ablation_problems.yaml (pre-reg §6)."""

    problem_id: str
    n: int
    sequence_index: int
    reference_optimum: float
    statement: str
    minimize: bool = False  # all current families maximize
    family: str = "equal_circles_in_unit_square"  # scorer key (ablation_packing.families)


@dataclass(frozen=True)
class RunSpec:
    """One run to execute: (problem, arm, seed). Ordered for Warm threading —
    within a (seed, arm) block the problems run in sequence_index order so the
    Warm KB accumulates along the sequence."""

    problem_id: str
    arm: Arm
    seed: int
    sequence_index: int

    @property
    def label(self) -> str:
        return f"{self.problem_id}-{ARM_CONFIGS[self.arm].label}-seed{self.seed}"


def build_run_matrix(problems: Sequence[Problem], seeds: Sequence[int]) -> list[RunSpec]:
    """Full (problem x arm x seed) matrix, grouped seed -> arm -> sequence so each
    (seed, arm) runs the problem sequence contiguously in order (required for the
    Warm KB to thread across problems 1..L)."""
    ordered = sorted(problems, key=lambda p: p.sequence_index)
    return [
        RunSpec(p.problem_id, arm, seed, p.sequence_index)
        for seed in seeds
        for arm in Arm
        for p in ordered
    ]


# ---------------- session launcher (§10.3) ----------------


@dataclass(frozen=True)
class SessionSpec:
    """The fresh-session configuration a production runner consumes to launch one
    (problem, arm, seed) Claude Code session with the right tool set and KB
    access. The harness builds it; the runner executes it."""

    problem_id: str
    arm: Arm
    seed: int
    statement: str
    allow_web: bool
    allow_personas: bool
    run_kb_readable: bool
    run_kb_path: str | None
    accumulated_lessons: tuple[str, ...]


def build_session_spec(
    problem: Problem,
    arm: Arm,
    seed: int,
    *,
    run_kb: RunKB | None,
    max_lesson_chars: int | None = None,
) -> SessionSpec:
    """Build the launch spec for one cell. Warm gets read access to its run KB and
    the accumulated lessons (capped); Cold gets neither. Web/personas come from
    the (constant-in-v1) arm config."""
    cfg = ARM_CONFIGS[arm]
    lessons: tuple[str, ...] = ()
    kb_path: str | None = None
    if cfg.read_kb and run_kb is not None:
        lessons = tuple(run_kb.read_lessons(max_chars=max_lesson_chars))
        kb_path = str(run_kb.root)
    return SessionSpec(
        problem_id=problem.problem_id,
        arm=arm,
        seed=seed,
        statement=problem.statement,
        allow_web=cfg.allow_web,
        allow_personas=cfg.allow_personas,
        run_kb_readable=cfg.read_kb,
        run_kb_path=kb_path,
        accumulated_lessons=lessons,
    )


# ---------------- the solve callback (injected; a real session in production) ----------------


@dataclass(frozen=True)
class SolveResult:
    """What one session returns after solving one problem. In production this is
    parsed from the session transcript + result artifact; in tests it is a
    synthetic fixture."""

    trajectory: list[TrajectoryPoint]
    score_coldinit: float  # first-evaluation score (the per-run cold baseline)
    score_final: float
    lesson_text: str | None  # the lesson to persist (both arms may produce one;
    #                          Cold's is discarded — reflection effort equalized)
    attempted_techniques: set[str] = field(default_factory=set)
    wall_clock_s: float = 0.0


# (problem, arm_config, seed, session_spec) -> SolveResult
SolveFn = Callable[[Problem, ArmConfig, int, SessionSpec], SolveResult]


# ---------------- dependent variable (§8) ----------------


def gap_closed(
    score_coldinit: float, score_final: float, score_optimum: float, *, minimize: bool
) -> float:
    """Primary DV (pre-reg §8): fraction of the start->optimum gap closed.

    `(final - coldinit) / (optimum - coldinit)` (signs flipped for minimize),
    clamped to [0, 1]. 1.0 = reached the reference optimum; 0 = no progress. If
    the gap is non-positive (cold-init already at/over the reference), returns
    0.0 — there was no room to show learning on that run.
    """
    denom = (score_coldinit - score_optimum) if minimize else (score_optimum - score_coldinit)
    if denom <= 0:
        return 0.0
    num = (score_coldinit - score_final) if minimize else (score_final - score_coldinit)
    return max(0.0, min(1.0, num / denom))


# ---------------- run record (§10 schema) ----------------


@dataclass(frozen=True)
class RunRecord:
    """One (problem, arm, seed) result — the JSON record schema in pre-reg §10."""

    problem_id: str
    arm: str
    seed: int
    sequence_index: int
    score_coldinit: float
    score_final: float
    score_optimum_ref: float
    gap_closed: float
    cycles: int
    wall_clock_s: float
    trajectory: list[tuple[int, float]]
    lessons_written: int
    lessons_read: int
    dead_ends_avoided: int
    kb_state_hash_before: str
    kb_state_hash_after: str

    def to_dict(self) -> dict:
        return {
            "problem_id": self.problem_id,
            "arm": self.arm,
            "seed": self.seed,
            "sequence_index": self.sequence_index,
            "score_coldinit": self.score_coldinit,
            "score_final": self.score_final,
            "score_optimum_ref": self.score_optimum_ref,
            "gap_closed": self.gap_closed,
            "cycles": self.cycles,
            "wall_clock_s": self.wall_clock_s,
            "trajectory": [{"cycle": c, "best_verified": s} for c, s in self.trajectory],
            "lessons_written": self.lessons_written,
            "lessons_read": self.lessons_read,
            "dead_ends_avoided": self.dead_ends_avoided,
            "kb_state_hash_before": self.kb_state_hash_before,
            "kb_state_hash_after": self.kb_state_hash_after,
        }


class SanityViolation(RuntimeError):
    """Raised when a pre-reg §9 manipulation check fails — the run is void."""


# ---------------- driver (§10.4) ----------------


def run_arm_sequence(
    arm: Arm,
    seed: int,
    problems: Sequence[Problem],
    solve_fn: SolveFn,
    run_kb: RunKB,
    *,
    known_dead_ends: set[str] | None = None,
    max_lesson_chars: int | None = None,
) -> list[RunRecord]:
    """Run one arm's full problem sequence for one seed, threading the run KB.

    Warm: KB starts empty (start of run), grows by one lesson per problem, is read
    before each later problem. Cold: KB wiped before every problem, so it is
    provably empty at each problem start. Enforces the pre-reg §9 sanity checks
    per cell and raises `SanityViolation` on any breach.
    """
    cfg = ARM_CONFIGS[arm]
    known_dead_ends = known_dead_ends or set()
    ordered = sorted(problems, key=lambda p: p.sequence_index)

    run_kb.wipe()  # empty at start of run (pre-reg §3: both arms start blank)
    records: list[RunRecord] = []

    for problem in ordered:
        # Cold: memory wiped between problems -> empty KB at each problem start.
        if not cfg.read_kb:
            run_kb.wipe()
            if not run_kb.is_empty():
                raise SanityViolation(f"Cold KB not empty at start of {problem.problem_id}")

        hash_before = run_kb.state_hash()
        spec = build_session_spec(
            problem, arm, seed, run_kb=run_kb, max_lesson_chars=max_lesson_chars
        )
        lessons_read = len(spec.accumulated_lessons)

        result = solve_fn(problem, cfg, seed, spec)

        # Warm persists a lesson; Cold's reflection is discarded (effort equalized).
        lessons_written = 0
        if cfg.write_kb and result.lesson_text:
            run_kb.write_lesson(problem.problem_id, result.lesson_text)
            lessons_written = 1
        hash_after = run_kb.state_hash()

        gc = gap_closed(
            result.score_coldinit,
            result.score_final,
            problem.reference_optimum,
            minimize=problem.minimize,
        )
        records.append(
            RunRecord(
                problem_id=problem.problem_id,
                arm=arm.value,
                seed=seed,
                sequence_index=problem.sequence_index,
                score_coldinit=result.score_coldinit,
                score_final=result.score_final,
                score_optimum_ref=problem.reference_optimum,
                gap_closed=gc,
                cycles=len(result.trajectory),
                wall_clock_s=result.wall_clock_s,
                trajectory=[(p.cycle_id, p.best_score) for p in result.trajectory],
                lessons_written=lessons_written,
                lessons_read=lessons_read,
                dead_ends_avoided=dead_ends_avoided(result.attempted_techniques, known_dead_ends),
                kb_state_hash_before=hash_before,
                kb_state_hash_after=hash_after,
            )
        )

    # Warm manipulation check (pre-reg §9): KB grew >=1 lesson per problem and was
    # read on later problems (lessons_read increases along the sequence).
    if cfg.write_kb:
        if run_kb.lesson_count() < len(ordered):
            raise SanityViolation(
                f"Warm KB grew {run_kb.lesson_count()} lessons for {len(ordered)} problems"
            )
        reads = [r.lessons_read for r in records]
        if len(reads) > 1 and max(reads) == 0:
            raise SanityViolation("Warm never reused a lesson — manipulation failed")

    return records


def run_matrix(
    problems: Sequence[Problem],
    seeds: Sequence[int],
    solve_fn: SolveFn,
    kb_root_for: Callable[[Arm, int], Path],
    *,
    known_dead_ends: set[str] | None = None,
    max_lesson_chars: int | None = None,
) -> list[RunRecord]:
    """Run the full (seed x arm x problem-sequence) matrix. `kb_root_for(arm, seed)`
    returns a distinct KB directory per (arm, seed) cell so runs never share a KB."""
    out: list[RunRecord] = []
    for seed in seeds:
        for arm in Arm:
            kb = RunKB(kb_root_for(arm, seed))
            out.extend(
                run_arm_sequence(
                    arm,
                    seed,
                    problems,
                    solve_fn,
                    kb,
                    known_dead_ends=known_dead_ends,
                    max_lesson_chars=max_lesson_chars,
                )
            )
    return out


# ---------------- config loader ----------------


def load_problems(config_path: str | Path) -> list[Problem]:
    """Load the frozen problem set (config/ablation_problems.yaml) into `Problem`s,
    reading each problem's statement file. `minimize` is derived from the config's
    top-level `minimize` flag (False for circle packing)."""
    import yaml

    config_path = Path(config_path)
    data = yaml.safe_load(config_path.read_text())
    minimize = bool(data.get("minimize", False))
    family = str(data.get("family", "equal_circles_in_unit_square"))
    repo_root = config_path.resolve().parent.parent  # config/ -> repo root
    problems: list[Problem] = []
    for p in data["problems"]:
        stmt_path = repo_root / p["statement_file"]
        statement = stmt_path.read_text() if stmt_path.exists() else ""
        problems.append(
            Problem(
                problem_id=p["id"],
                n=int(p["n"]),
                sequence_index=int(p["sequence_index"]),
                reference_optimum=float(p["reference_optimum"]),
                statement=statement,
                minimize=minimize,
                family=family,
            )
        )
    return problems


# ---------------- logging (§10.5) ----------------


def append_record(record: RunRecord, results_path: str | Path) -> None:
    """Append one run record as a JSON line (the §10 schema). The run log is
    append-only — one line per (problem, arm, seed) — so a crashed batch keeps the
    records it already produced (no cherry-picking; cycle-discipline rule)."""
    results_path = Path(results_path)
    results_path.parent.mkdir(parents=True, exist_ok=True)
    with results_path.open("a") as fh:
        fh.write(json.dumps(record.to_dict()) + "\n")


def load_records(results_path: str | Path) -> list[dict]:
    """Read the append-only JSONL run log back into dicts."""
    results_path = Path(results_path)
    if not results_path.exists():
        return []
    return [json.loads(line) for line in results_path.read_text().splitlines() if line.strip()]


# ---------------- analysis (§10.6) ----------------


def _pooled_stdev(records: list[dict]) -> float:
    """Pooled per-cell stdev of gap_closed: sqrt(mean of per-(problem,arm) cell
    variances). The §9 decision rules compare effect sizes against this."""
    cells: dict[tuple[str, str], list[float]] = {}
    for r in records:
        cells.setdefault((r["problem_id"], r["arm"]), []).append(r["gap_closed"])
    variances = [statistics.pvariance(v) for v in cells.values() if len(v) >= 2]
    if not variances:
        return 0.0
    return statistics.fmean(variances) ** 0.5


def mean_gap_closed(records: list[dict], arm: str) -> float:
    vals = [r["gap_closed"] for r in records if r["arm"] == arm]
    return statistics.fmean(vals) if vals else 0.0


@dataclass(frozen=True)
class DeltaK:
    """Per-problem Warm-minus-Cold advantage at sequence position k (pre-reg §9 H2)."""

    sequence_index: int
    problem_id: str
    warm_mean: float
    cold_mean: float
    delta: float


def delta_k_trend(records: list[dict]) -> list[DeltaK]:
    """Δ_k = mean gap_closed(Warm, k) − mean gap_closed(Cold, k), per problem,
    ordered by sequence position. The slope of this is the compounding signal."""
    by_seq: dict[int, dict[str, list[float]]] = {}
    pid_of: dict[int, str] = {}
    for r in records:
        si = r["sequence_index"]
        by_seq.setdefault(si, {}).setdefault(r["arm"], []).append(r["gap_closed"])
        pid_of[si] = r["problem_id"]
    out: list[DeltaK] = []
    for si in sorted(by_seq):
        warm = by_seq[si].get("warm", [])
        cold = by_seq[si].get("cold", [])
        wm = statistics.fmean(warm) if warm else 0.0
        cm = statistics.fmean(cold) if cold else 0.0
        out.append(DeltaK(si, pid_of[si], wm, cm, wm - cm))
    return out


def _slope(xs: list[float], ys: list[float]) -> float:
    """Least-squares slope of ys vs xs (0.0 if degenerate)."""
    n = len(xs)
    if n < 2:
        return 0.0
    mx = statistics.fmean(xs)
    my = statistics.fmean(ys)
    denom = sum((x - mx) ** 2 for x in xs)
    if denom == 0:
        return 0.0
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys, strict=True)) / denom


@dataclass(frozen=True)
class Decision:
    supported: bool
    detail: str


@dataclass(frozen=True)
class AnalysisReport:
    n_records: int
    warm_mean: float
    cold_mean: float
    pooled_stdev: float
    delta_k: list[DeltaK]
    delta_slope: float
    h1: Decision  # level effect — knowledge helps
    h2: Decision  # slope effect — it compounds


def analyze(records: list[dict]) -> AnalysisReport:
    """Compute the pre-reg §9 H1/H2 decisions from the run log.

    H1 (level): supported iff mean gap_closed(Warm) exceeds Cold by MORE than the
    pooled per-cell stdev (clear separation, not overlap).
    H2 (slope/compounding): supported iff Δ_k trends upward — positive least-squares
    slope of Δ_k vs k AND later-third mean Δ exceeds first-third mean Δ by more than
    the pooled stdev. H2 is the headline ("compounds").
    """
    warm_mean = mean_gap_closed(records, "warm")
    cold_mean = mean_gap_closed(records, "cold")
    pooled = _pooled_stdev(records)
    dks = delta_k_trend(records)

    h1_gap = warm_mean - cold_mean
    h1 = Decision(
        supported=h1_gap > pooled and pooled >= 0,
        detail=f"warm−cold={h1_gap:+.4f} vs pooled_stdev={pooled:.4f} "
        f"→ {'separation' if h1_gap > pooled else 'overlap'}",
    )

    seqs = [d.sequence_index for d in dks]
    deltas = [d.delta for d in dks]
    slope = _slope([float(s) for s in seqs], deltas)
    # first-third vs later-third (L=6 → {0,1} vs {4,5}); generalizes by thirds.
    third = max(1, len(dks) // 3)
    first_mean = statistics.fmean(deltas[:third]) if deltas else 0.0
    later_mean = statistics.fmean(deltas[-third:]) if deltas else 0.0
    trend_up = later_mean - first_mean > pooled
    h2 = Decision(
        supported=slope > 0 and trend_up,
        detail=f"Δ_k slope={slope:+.4f}; later-third Δ̄={later_mean:+.4f} vs "
        f"first-third Δ̄={first_mean:+.4f} (need Δ>{pooled:.4f}) "
        f"→ {'compounding' if (slope > 0 and trend_up) else 'no compounding'}",
    )
    return AnalysisReport(
        n_records=len(records),
        warm_mean=warm_mean,
        cold_mean=cold_mean,
        pooled_stdev=pooled,
        delta_k=dks,
        delta_slope=slope,
        h1=h1,
        h2=h2,
    )


# ---------------- transcript auditor (§10.7) ----------------


@dataclass(frozen=True)
class AuditReceipt:
    """Pass/fail receipt for one session's tool-call targets (pre-reg §9, §10.7)."""

    arm: str
    passed: bool
    forbidden_hits: list[str]


def audit_session(
    targets: list[str], *, arm: Arm, allow_web: bool, own_kb_root: str | None
) -> AuditReceipt:
    """Audit one session's tool-call targets for forbidden retrieval.

    Flags, for every target the session reached:
    - the **answer key** (reuses `ablation.is_firewalled` — leaderboard, this
      repo, any solution/SOTA dump) — forbidden for BOTH arms;
    - a **web URL** when web is off for the arm (v1: off for both) — the session
      must reason from the statement + (Warm) its own lessons, not the internet;
    - a **cross-arm / foreign run-kb path** — a Cold session touching any run-kb,
      or a Warm session touching a run-kb that is not its own.

    `own_kb_root` is the run's own KB dir (None for Cold). A run-kb reference is a
    target containing 'run-kb' or 'lesson-' that does not start with own_kb_root.
    """
    hits: list[str] = []
    for t in targets:
        low = t.lower()
        if is_firewalled(t):
            hits.append(f"answer-key:{t}")
            continue
        if not allow_web and ("://" in low or low.startswith("www.")):
            hits.append(f"web:{t}")
            continue
        is_kb_ref = "run-kb" in low or "/lesson-" in low or low.startswith("lesson-")
        if is_kb_ref:
            if own_kb_root is None or not t.startswith(own_kb_root):
                hits.append(f"foreign-kb:{t}")
    return AuditReceipt(arm=arm.value, passed=not hits, forbidden_hits=hits)
