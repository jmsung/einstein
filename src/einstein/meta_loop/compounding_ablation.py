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
    """One problem from an ablation config (e.g. config/ablation_problems.yaml, or a
    transfer config that mixes families — pre-reg §6, §0b)."""

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
    replicate: int = 0  # within-cell repeat index for variance reduction; 0 = first/only.
    #                     The production solve_fn folds this into the cold-init seed, so
    #                     replicates draw independent starts that are SHARED across arms —
    #                     each replicate stays a paired Cold/Warm comparison.


def _cap_lessons(lessons: tuple[str, ...], max_chars: int | None) -> tuple[str, ...]:
    """Cap a lesson list to `max_chars` total by dropping whole lessons from the end
    (never truncating one), matching RunKB.read_lessons' equal-max-context policy."""
    if max_chars is None:
        return tuple(lessons)
    out: list[str] = []
    total = 0
    for t in lessons:
        if total + len(t) > max_chars:
            break
        out.append(t)
        total += len(t)
    return tuple(out)


def load_frozen_kb(kb_root: str | Path, *, max_chars: int | None = None) -> tuple[str, ...]:
    """Load a frozen KB_A (a prior family-A Warm run's lesson directory) as a fixed
    lesson tuple for a cross-family warm-transfer arm. The directory is read-only here
    — the transfer arm never writes back into it, keeping A's lessons the ONE variable."""
    return tuple(RunKB(Path(kb_root)).read_lessons(max_chars=max_chars))


def build_session_spec(
    problem: Problem,
    arm: Arm,
    seed: int,
    *,
    run_kb: RunKB | None,
    max_lesson_chars: int | None = None,
    replicate: int = 0,
    frozen_kb_lessons: tuple[str, ...] | None = None,
) -> SessionSpec:
    """Build the launch spec for one cell. Warm gets read access to its run KB and
    the accumulated lessons (capped); Cold gets neither. Web/personas come from
    the (constant-in-v1) arm config. `replicate` indexes the within-cell repeat used
    for variance reduction; it changes only the cold-init draw, identically for both
    arms, so each replicate is still a paired Cold/Warm comparison.

    `frozen_kb_lessons` (cross-family transfer design, pre-reg §0b): a FROZEN KB_A from
    a different family, prepended ahead of any within-run lessons for KB-reading arms.
    For a pure transfer cell (run_kb empty) the warm arm's knowledge IS exactly KB_A —
    the one manipulated variable. None → unchanged within-family behavior."""
    cfg = ARM_CONFIGS[arm]
    lessons: tuple[str, ...] = ()
    kb_path: str | None = None
    if cfg.read_kb:
        within = tuple(run_kb.read_lessons(max_chars=None)) if run_kb is not None else ()
        if run_kb is not None:
            kb_path = str(run_kb.root)
        frozen = tuple(frozen_kb_lessons) if frozen_kb_lessons else ()
        lessons = _cap_lessons(frozen + within, max_lesson_chars)
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
        replicate=replicate,
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
    replicates: int = 1  # within-cell repeats averaged into gap_closed (1 = legacy behavior).
    gap_closed_std: float = 0.0  # stdev of per-replicate gap_closed (0 when replicates==1).
    gap_closed_reps: tuple[float, ...] = ()  # per-replicate gaps, for transparency/re-analysis.

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
            "replicates": self.replicates,
            "gap_closed_std": self.gap_closed_std,
            "gap_closed_reps": list(self.gap_closed_reps),
        }


class SanityViolation(RuntimeError):
    """Raised when a pre-reg §9 manipulation check fails — the run is void."""


# ---------------- driver (§10.4) ----------------


def cyclic_order(problems: Sequence[Problem], seed: int) -> list[str]:
    """Counterbalanced run order (pre-reg v2 §5): cyclic rotation k = seed mod L of
    the sequence_index-ascending order. Over any L consecutive seeds each problem
    visits each position 0…L-1 exactly once (a Latin square), so "lessons banked
    before a problem" is decoupled from the problem's difficulty."""
    ids = [p.problem_id for p in sorted(problems, key=lambda p: p.sequence_index)]
    k = seed % len(ids)
    return ids[k:] + ids[:k]


def run_arm_sequence(
    arm: Arm,
    seed: int,
    problems: Sequence[Problem],
    solve_fn: SolveFn,
    run_kb: RunKB,
    *,
    known_dead_ends: set[str] | None = None,
    max_lesson_chars: int | None = None,
    order: list[str] | None = None,
    skip_done: set[str] | None = None,
    on_record: Callable[[RunRecord], None] | None = None,
    replicates: int = 1,
) -> list[RunRecord]:
    """Run one arm's problem sequence for one seed, threading the run KB.

    `order` (list of problem_ids) sets the run order; None → sequence_index order.
    Warm: KB grows one lesson per problem, read before each later problem. Cold:
    KB wiped before every problem (provably empty at each start). Enforces the §9
    sanity checks; raises `SanityViolation` on a breach.

    Resume (crash-resilience, pre-reg v2 §9): `skip_done` is the set of problem_ids
    already completed in a prior (interrupted) run — they are NOT re-solved and the
    KB is NOT wiped at start (Warm reuses the lessons already persisted on disk).
    `on_record` is called after each problem so records are durable per-cell.

    `replicates` (variance reduction): solve each cell this many times with
    independent cold-inits and record the MEAN of the per-replicate gap_closed,
    cutting per-cell DV noise ~1/√replicates. Exactly one lesson (the first
    replicate's) is persisted, so Warm's one-lesson-per-problem KB invariant and the
    banked-count semantics are unchanged. replicates=1 reproduces legacy behavior.
    """
    cfg = ARM_CONFIGS[arm]
    known_dead_ends = known_dead_ends or set()
    skip_done = skip_done or set()
    by_id = {p.problem_id: p for p in problems}
    ordered = (
        [by_id[pid] for pid in order]
        if order is not None
        else sorted(problems, key=lambda p: p.sequence_index)
    )
    resuming = bool(skip_done)

    if not resuming:
        run_kb.wipe()  # fresh start: empty at start of run (pre-reg §3)
    records: list[RunRecord] = []

    for problem in ordered:
        if problem.problem_id in skip_done:
            continue  # completed in a prior run; (Warm) its lesson is already on disk

        # Cold: memory wiped between problems -> empty KB at each problem start.
        if not cfg.read_kb:
            run_kb.wipe()
            if not run_kb.is_empty():
                raise SanityViolation(f"Cold KB not empty at start of {problem.problem_id}")

        hash_before = run_kb.state_hash()
        # Variance reduction: run `replicates` independent solves of this cell, each
        # with its own cold-init (shared across arms via spec.replicate), and average
        # the per-replicate gap_closed. The DV is mean-OF-gaps — each gap uses its own
        # cold-init, which is NOT the same as the gap of the mean scores.
        rep_results: list[SolveResult] = []
        rep_gaps: list[float] = []
        spec = None
        for r in range(max(1, replicates)):
            spec = build_session_spec(
                problem,
                arm,
                seed,
                run_kb=run_kb,
                max_lesson_chars=max_lesson_chars,
                replicate=r,
            )
            res_r = solve_fn(problem, cfg, seed, spec)
            rep_results.append(res_r)
            rep_gaps.append(
                gap_closed(
                    res_r.score_coldinit,
                    res_r.score_final,
                    problem.reference_optimum,
                    minimize=problem.minimize,
                )
            )
        lessons_read = len(spec.accumulated_lessons)  # identical across replicates

        # Persist exactly ONE lesson (first replicate's) so Warm keeps one lesson per
        # problem — banked-count semantics and the §9 manipulation check are unchanged.
        primary = rep_results[0]
        lessons_written = 0
        if cfg.write_kb and primary.lesson_text:
            run_kb.write_lesson(problem.problem_id, primary.lesson_text)
            lessons_written = 1
        hash_after = run_kb.state_hash()

        k = len(rep_gaps)
        gc = sum(rep_gaps) / k
        gc_std = (sum((g - gc) ** 2 for g in rep_gaps) / (k - 1)) ** 0.5 if k > 1 else 0.0
        techniques: set[str] = set()
        for rr in rep_results:
            techniques |= rr.attempted_techniques
        rec = RunRecord(
            problem_id=problem.problem_id,
            arm=arm.value,
            seed=seed,
            sequence_index=problem.sequence_index,
            score_coldinit=sum(rr.score_coldinit for rr in rep_results) / k,
            score_final=sum(rr.score_final for rr in rep_results) / k,
            score_optimum_ref=problem.reference_optimum,
            gap_closed=gc,
            cycles=len(primary.trajectory),
            wall_clock_s=sum(rr.wall_clock_s for rr in rep_results),
            trajectory=[(p.cycle_id, p.best_score) for p in primary.trajectory],
            lessons_written=lessons_written,
            lessons_read=lessons_read,
            dead_ends_avoided=dead_ends_avoided(techniques, known_dead_ends),
            kb_state_hash_before=hash_before,
            kb_state_hash_after=hash_after,
            replicates=k,
            gap_closed_std=gc_std,
            gap_closed_reps=tuple(rep_gaps),
        )
        records.append(rec)
        if on_record is not None:
            on_record(rec)  # durable now, so a later crash keeps this cell

    # Warm manipulation check (pre-reg §9): after the sequence the KB holds one
    # lesson per problem (skipped ones already on disk), and lessons were reused.
    if cfg.write_kb:
        if run_kb.lesson_count() < len(ordered):
            raise SanityViolation(
                f"Warm KB has {run_kb.lesson_count()} lessons for {len(ordered)} problems"
            )
        reads = [r.lessons_read for r in records]
        if len(reads) > 1 and max(reads) == 0:
            raise SanityViolation("Warm never reused a lesson — manipulation failed")

    return records


@dataclass(frozen=True)
class TransferRecord:
    """One cross-family transfer cell result (pre-reg §0b). The warm-transfer arm
    carries a FROZEN KB_A from family A; the cold arm carries nothing. The ONE
    variable is KB_A's presence — `kb_a_hash` pins which frozen KB was injected."""

    family_a: str
    family_b: str
    problem_id: str
    arm: str  # "cold" | "warm_transfer"
    seed: int
    score_coldinit: float
    score_final: float
    gap_closed: float
    gap_closed_reps: tuple[float, ...]
    lessons_read: int
    kb_a_hash: str
    wall_clock_s: float


def _transfer_cell(
    problem: Problem,
    arm: Arm,
    seed: int,
    solve_fn: SolveFn,
    run_kb: RunKB,
    *,
    frozen: tuple[str, ...] | None,
    max_lesson_chars: int | None,
    replicates: int,
    family_a: str,
    family_b: str,
    kb_a_hash: str,
) -> TransferRecord:
    """Replicate-averaged solve of one family-B cell. Cold and warm-transfer share the
    (seed, replicate) cold-init draw, so the comparison is paired on identical starts."""
    cfg = ARM_CONFIGS[arm]
    run_kb.wipe()
    rep_results: list[SolveResult] = []
    rep_gaps: list[float] = []
    spec = None
    for r in range(max(1, replicates)):
        spec = build_session_spec(
            problem,
            arm,
            seed,
            run_kb=run_kb,
            max_lesson_chars=max_lesson_chars,
            replicate=r,
            frozen_kb_lessons=frozen,
        )
        res = solve_fn(problem, cfg, seed, spec)
        rep_results.append(res)
        rep_gaps.append(
            gap_closed(
                res.score_coldinit,
                res.score_final,
                problem.reference_optimum,
                minimize=problem.minimize,
            )
        )
    k = len(rep_gaps)
    return TransferRecord(
        family_a=family_a,
        family_b=family_b,
        problem_id=problem.problem_id,
        arm="warm_transfer" if arm is Arm.WARM else "cold",
        seed=seed,
        score_coldinit=sum(r.score_coldinit for r in rep_results) / k,
        score_final=sum(r.score_final for r in rep_results) / k,
        gap_closed=sum(rep_gaps) / k,
        gap_closed_reps=tuple(rep_gaps),
        lessons_read=len(spec.accumulated_lessons),
        kb_a_hash=kb_a_hash,
        wall_clock_s=sum(r.wall_clock_s for r in rep_results),
    )


def run_transfer_experiment(
    family_a_problems: Sequence[Problem],
    family_b_problems: Sequence[Problem],
    seeds: Sequence[int],
    solve_fn: SolveFn,
    *,
    results_dir: str | Path,
    max_lesson_chars: int | None = None,
    replicates: int = 1,
    on_record: Callable[[TransferRecord], None] | None = None,
) -> dict:
    """Cross-family transfer experiment (pre-reg §0b PRIMARY design).

    Phase 1: build+freeze KB_A by running family A WARM (per seed) — `run_arm_sequence`
    threads the within-A KB. Phase 2: for each family-B problem, run COLD (control, no
    KB) vs WARM-TRANSFER (frozen KB_A), paired on the shared cold-init. Distance is the
    finding: near (Heilbronn→Tammes) vs far (Heilbronn→autocorrelation). Returns the
    records + the per-seed KB_A hashes for audit. solve_fn is injected, so the whole
    orchestration is testable with a mock (no LLM)."""
    results_dir = Path(results_dir)
    fam_a = family_a_problems[0].family if family_a_problems else "?"
    fam_b = family_b_problems[0].family if family_b_problems else "?"
    records: list[TransferRecord] = []
    kb_a_hashes: dict[int, str] = {}
    for seed in seeds:
        kb_a = RunKB(results_dir / f"kb-a-seed{seed}")
        run_arm_sequence(
            Arm.WARM,
            seed,
            family_a_problems,
            solve_fn,
            kb_a,
            max_lesson_chars=max_lesson_chars,
            replicates=replicates,
        )
        frozen = tuple(kb_a.read_lessons(max_chars=max_lesson_chars))
        kb_a_hash = kb_a.state_hash()
        kb_a_hashes[seed] = kb_a_hash
        for problem in sorted(family_b_problems, key=lambda p: p.sequence_index):
            for arm, frozen_for_arm in ((Arm.COLD, None), (Arm.WARM, frozen)):
                kb_dir = results_dir / f"kb-b-{arm.value}-{problem.problem_id}-seed{seed}"
                rec = _transfer_cell(
                    problem,
                    arm,
                    seed,
                    solve_fn,
                    RunKB(kb_dir),
                    frozen=frozen_for_arm,
                    max_lesson_chars=max_lesson_chars,
                    replicates=replicates,
                    family_a=fam_a,
                    family_b=fam_b,
                    kb_a_hash=kb_a_hash,
                )
                records.append(rec)
                if on_record is not None:
                    on_record(rec)
    return {"records": records, "family_a": fam_a, "family_b": fam_b, "kb_a_hashes": kb_a_hashes}


@dataclass(frozen=True)
class HeadroomResult:
    """One cold-solve probe of a family instance (pre-reg §3 headroom screen)."""

    family: str
    problem_id: str
    seed: int
    gap_closed: float
    in_band: bool


def headroom_probe(
    problems: Sequence[Problem],
    solve_fn: SolveFn,
    seeds: Sequence[int],
    *,
    results_dir: str | Path,
    band: tuple[float, float] = (0.2, 0.8),
    replicates: int = 1,
) -> dict:
    """Cold-solve each instance and screen for genuine headroom (pre-reg §3).

    A family is eligible for the transfer experiment only if a from-scratch (cold) solve
    closes a MIDDLING fraction of the gap — too easy (gap→1: cold already nails it, no
    room to show transfer) or too hard (gap→0: nothing learns) both kill the signal. We
    keep families whose median cold gap_closed sits in `band` (default [0.2, 0.8]). Used
    per-model to pick model-matched difficulty (§0c). solve_fn injected → testable."""
    lo, hi = band
    results_dir = Path(results_dir)
    out: list[HeadroomResult] = []
    for seed in seeds:
        for problem in problems:
            kb = RunKB(results_dir / f"probe-{problem.problem_id}-seed{seed}")
            kb.wipe()
            gaps: list[float] = []
            for r in range(max(1, replicates)):
                spec = build_session_spec(problem, Arm.COLD, seed, run_kb=kb, replicate=r)
                res = solve_fn(problem, ARM_CONFIGS[Arm.COLD], seed, spec)
                gaps.append(
                    gap_closed(
                        res.score_coldinit,
                        res.score_final,
                        problem.reference_optimum,
                        minimize=problem.minimize,
                    )
                )
            gc = sum(gaps) / len(gaps)
            out.append(HeadroomResult(problem.family, problem.problem_id, seed, gc, lo <= gc <= hi))
    by_family: dict[str, list[float]] = {}
    for r in out:
        by_family.setdefault(r.family, []).append(r.gap_closed)
    eligible = {f: (lo <= statistics.median(g) <= hi) for f, g in by_family.items()}
    return {"results": out, "eligible": eligible, "band": band}


# --- Solve-rate screen (the efficiency-DV reframe) --------------------------------------
# The §3 gap-band screen assumes a smooth difficulty knob (gap ∈ [0.2,0.8]). For
# solve-or-don't problems at a fixed budget, cold outcomes are bimodal (gap ≈ 0 or ≈ 1),
# so the band barely exists. The right instrument is then the SOLVE RATE across seeds:
# keep instances cold solves SOME-but-not-all of the time (room for warm to lift it), and
# measure whether warm-transfer raises the solve-rate / lowers time-to-solve. This matches
# the pre-reg's post-#4 pivot of the DV to efficiency (timeout-rate / wall / time-to-target).


def is_solved(gap: float, threshold: float = 0.5) -> bool:
    """A cell 'solved' the instance if it closed >= `threshold` of the gap. With bimodal
    (≈0/≈1) outcomes, 0.5 cleanly separates a real solve from no-progress/failed."""
    return gap >= threshold


@dataclass(frozen=True)
class SolveRateResult:
    """Per-instance cold solve-rate across seeds (the efficiency-screen unit)."""

    family: str
    problem_id: str
    n_seeds: int
    solve_rate: float  # fraction of seeds whose cold cell solved (gap >= threshold)
    mean_wall_s: float
    in_band: bool  # solve_rate sits in the intermediate band → room for warm to lift it


def solve_rate_screen(
    problems: Sequence[Problem],
    solve_fn: SolveFn,
    seeds: Sequence[int],
    *,
    results_dir: str | Path,
    solve_threshold: float = 0.5,
    band: tuple[float, float] = (0.2, 0.8),
    replicates: int = 1,
) -> dict:
    """Screen by COLD solve-rate across seeds (the efficiency reframe — see note above).

    Keep instances whose cold solve-rate sits in `band` (default [0.2, 0.8]): the agent
    sometimes solves and sometimes doesn't, so there is genuine room for warm-transfer to
    raise the rate. solve_rate ≈ 1 (always solves cold) or ≈ 0 (never) have no headroom.
    Needs >= ~5 seeds to estimate a rate. solve_fn injected → testable."""
    lo, hi = band
    results_dir = Path(results_dir)
    per_seed: dict[str, list[tuple[float, float]]] = {}  # problem_id -> [(gap, wall)]
    fam_of: dict[str, str] = {}
    for seed in seeds:
        for problem in problems:
            fam_of[problem.problem_id] = problem.family
            kb = RunKB(results_dir / f"solverate-{problem.problem_id}-seed{seed}")
            kb.wipe()
            gaps: list[float] = []
            walls: list[float] = []
            for r in range(max(1, replicates)):
                spec = build_session_spec(problem, Arm.COLD, seed, run_kb=kb, replicate=r)
                res = solve_fn(problem, ARM_CONFIGS[Arm.COLD], seed, spec)
                gaps.append(
                    gap_closed(
                        res.score_coldinit,
                        res.score_final,
                        problem.reference_optimum,
                        minimize=problem.minimize,
                    )
                )
                walls.append(res.wall_clock_s)
            per_seed.setdefault(problem.problem_id, []).append(
                (sum(gaps) / len(gaps), sum(walls) / len(walls))
            )
    results: list[SolveRateResult] = []
    for pid, gw in per_seed.items():
        rate = sum(1 for g, _ in gw if is_solved(g, solve_threshold)) / len(gw)
        mean_wall = sum(w for _, w in gw) / len(gw)
        results.append(
            SolveRateResult(fam_of[pid], pid, len(gw), rate, mean_wall, lo <= rate <= hi)
        )
    eligible = {
        r.problem_id: r.in_band for r in sorted(results, key=lambda x: (x.family, x.problem_id))
    }
    return {"results": results, "eligible": eligible, "band": band, "threshold": solve_threshold}


def transfer_solve_rates(records: Sequence[TransferRecord], *, threshold: float = 0.5) -> dict:
    """Cold vs warm-transfer solve-rate per family-B target (the efficiency DV under reframe
    A). For each (family_b, arm), the fraction of cells that solved. A positive
    warm−cold delta is the transfer effect; report it per family (near vs far)."""
    by: dict[tuple[str, str], list[bool]] = {}
    for rec in records:
        by.setdefault((rec.family_b, rec.arm), []).append(is_solved(rec.gap_closed, threshold))
    fams = sorted({fb for fb, _ in by})
    out = {}
    for fb in fams:
        cold = by.get((fb, "cold"), [])
        warm = by.get((fb, "warm_transfer"), [])
        cr = sum(cold) / len(cold) if cold else 0.0
        wr = sum(warm) / len(warm) if warm else 0.0
        out[fb] = {
            "cold_solve_rate": cr,
            "warm_solve_rate": wr,
            "delta": wr - cr,
            "n_cold": len(cold),
            "n_warm": len(warm),
        }
    return out


def run_matrix(
    problems: Sequence[Problem],
    seeds: Sequence[int],
    solve_fn: SolveFn,
    kb_root_for: Callable[[Arm, int], Path],
    *,
    known_dead_ends: set[str] | None = None,
    max_lesson_chars: int | None = None,
    replicates: int = 1,
) -> list[RunRecord]:
    """Run the full (seed x arm x problem-sequence) matrix. `kb_root_for(arm, seed)`
    returns a distinct KB directory per (arm, seed) cell so runs never share a KB.
    `replicates` averages each cell over that many independent solves (variance
    reduction; see run_arm_sequence)."""
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
                    replicates=replicates,
                )
            )
    return out


# ---------------- config loader ----------------


def load_problems(config_path: str | Path) -> list[Problem]:
    """Load a problem set into `Problem`s. `minimize` and `family` come from the
    top-level config but may be overridden PER PROBLEM (so one transfer config can list
    both family-A and family-B problems — pre-reg §0b). The statement comes from
    `statement_file` (relative to the repo root) or an inline `statement` key."""
    import yaml

    config_path = Path(config_path)
    data = yaml.safe_load(config_path.read_text())
    top_minimize = bool(data.get("minimize", False))
    top_family = str(data.get("family", "equal_circles_in_unit_square"))
    repo_root = config_path.resolve().parent.parent  # config/ -> repo root
    problems: list[Problem] = []
    for p in data["problems"]:
        if p.get("statement_file"):
            stmt_path = repo_root / p["statement_file"]
            statement = stmt_path.read_text() if stmt_path.exists() else ""
        else:
            statement = str(p.get("statement", ""))
        problems.append(
            Problem(
                problem_id=p["id"],
                n=int(p["n"]),
                sequence_index=int(p["sequence_index"]),
                reference_optimum=float(p["reference_optimum"]),
                statement=statement,
                minimize=bool(p.get("minimize", top_minimize)),
                family=str(p.get("family", top_family)),
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


def paired_deltas(records: list[dict]) -> list[tuple[str, int, float, int]]:
    """Pair Warm/Cold by (problem_id, seed): returns (problem_id, seed, Δ, banked)
    where Δ = gap_closed(Warm) − gap_closed(Cold) (paired by the shared cold-init)
    and `banked` = lessons in the Warm KB when the problem was reached
    (= its position in that seed's counterbalanced order)."""
    warm = {(r["problem_id"], r["seed"]): r for r in records if r["arm"] == "warm"}
    cold = {(r["problem_id"], r["seed"]): r for r in records if r["arm"] == "cold"}
    out: list[tuple[str, int, float, int]] = []
    for key, w in warm.items():
        c = cold.get(key)
        if c is not None:
            out.append((key[0], key[1], w["gap_closed"] - c["gap_closed"], int(w["lessons_read"])))
    return out


def _within_problem_slope(pairs: list[tuple[str, int, float, int]]) -> float:
    """Fixed-effect slope of Δ on `banked`, controlling for the problem: center Δ
    and banked within each problem (removes the difficulty effect), pool, OLS slope.
    This is the pre-reg v2 §7 H2 statistic — accumulation isolated from difficulty.
    Needs banked to vary within a problem (guaranteed by counterbalanced order)."""
    by_p: dict[str, list[tuple[float, int]]] = {}
    for pid, _seed, d, b in pairs:
        by_p.setdefault(pid, []).append((d, b))
    xs: list[float] = []
    ys: list[float] = []
    for vals in by_p.values():
        if len(vals) < 2:
            continue
        mb = statistics.fmean(b for _d, b in vals)
        md = statistics.fmean(d for d, _b in vals)
        for d, b in vals:
            xs.append(b - mb)
            ys.append(d - md)
    return _slope(xs, ys)


def _bootstrap_ci(items, stat, *, n_boot: int = 2000, seed: int = 12345):
    """Point estimate + percentile 95% bootstrap CI of `stat(items)` (seeded →
    reproducible). Resamples `items` with replacement."""
    import random

    point = stat(items)
    n = len(items)
    if n == 0:
        return point, 0.0, 0.0
    rng = random.Random(seed)
    boots = sorted(stat([items[rng.randrange(n)] for _ in range(n)]) for _ in range(n_boot))
    return point, boots[int(0.025 * n_boot)], boots[int(0.975 * n_boot)]


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
    delta_slope: float  # descriptive Δ-vs-sequence-position (confounded by difficulty)
    mean_delta: float
    mean_delta_ci: tuple[float, float]
    banked_slope: float  # within-problem Δ-vs-banked (the §7 compounding statistic)
    banked_slope_ci: tuple[float, float]
    h1: Decision  # level effect — knowledge helps
    h2: Decision  # compounding — within-problem Δ rises with lessons banked


def analyze(records: list[dict]) -> AnalysisReport:
    """Compute the pre-reg v2 §7 H1/H2 decisions from the run log.

    Both use the PAIRED Δ = gap_closed(Warm) − gap_closed(Cold) (same cold-init):
    - **H1 (level):** mean Δ > 0 with a 95% bootstrap CI excluding 0.
    - **H2 (compounding):** the within-problem slope of Δ on lessons-banked is
      positive with a 95% bootstrap CI excluding 0. Counterbalanced order makes
      banked vary within each problem, so this isolates accumulation from
      difficulty. (`delta_slope`, the Δ-vs-sequence-position trend, is reported
      descriptively but is confounded by difficulty — not the decision.)
    """
    warm_mean = mean_gap_closed(records, "warm")
    cold_mean = mean_gap_closed(records, "cold")
    pooled = _pooled_stdev(records)
    dks = delta_k_trend(records)
    pairs = paired_deltas(records)
    deltas = [d for _pid, _s, d, _b in pairs]

    # H1 — paired mean Δ, bootstrap CI excludes 0
    mean_delta, d_lo, d_hi = _bootstrap_ci(deltas, lambda v: statistics.fmean(v) if v else 0.0)
    h1 = Decision(
        supported=mean_delta > 0 and d_lo > 0,
        detail=f"mean Δ={mean_delta:+.4f}, 95% CI [{d_lo:+.4f}, {d_hi:+.4f}] "
        f"→ {'knowledge helps' if (mean_delta > 0 and d_lo > 0) else 'inconclusive'}",
    )

    # H2 — within-problem Δ-vs-banked slope, bootstrap CI excludes 0 and positive
    banked_slope, s_lo, s_hi = _bootstrap_ci(pairs, _within_problem_slope)
    h2 = Decision(
        supported=banked_slope > 0 and s_lo > 0,
        detail=f"within-problem Δ-vs-banked slope={banked_slope:+.4f}, "
        f"95% CI [{s_lo:+.4f}, {s_hi:+.4f}] "
        f"→ {'compounding' if (banked_slope > 0 and s_lo > 0) else 'no compounding'}",
    )

    # descriptive (confounded) Δ-vs-sequence-position trend, for context only
    delta_slope = _slope([float(d.sequence_index) for d in dks], [d.delta for d in dks])

    return AnalysisReport(
        n_records=len(records),
        warm_mean=warm_mean,
        cold_mean=cold_mean,
        pooled_stdev=pooled,
        delta_k=dks,
        delta_slope=delta_slope,
        mean_delta=mean_delta,
        mean_delta_ci=(d_lo, d_hi),
        banked_slope=banked_slope,
        banked_slope_ci=(s_lo, s_hi),
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
