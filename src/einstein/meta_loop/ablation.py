"""3-arm knowledge ablation harness — Goal 6 of js/feat/evolve-and-measure.

The publishable experiment: does the *curated knowledge base* actually help, or
would web search (or nothing) do as well? Three arms, cold-start, N seeds:

- **A — curated wiki**: may read `docs/wiki/` (our distilled KB); no web.
- **B — web search (firewalled)**: may web-search, but firewalled from the
  literal answer key — the arena leaderboard, this repo, and any solution dump;
  no wiki.
- **C — model-only**: no wiki, no web — the model's training only.

The experiment varies **reasoning support**, not **answer access**: every arm
gets the problem statement and every arm is firewalled from the answer key. The
difference between arms is *where the reasoning help comes from*.

This module is the harness, not the run. Like the surgical-removal protocol,
execution requires fresh cold-start agent sessions (autonomous self-execution
would defeat the control); the harness defines the arms, *enforces and verifies*
the firewall, builds the N-seed run matrix, and measures results
(climb-rate / dead-ends-avoided / cycles-to-X%-of-floor) with a distributional
comparison across seeds. Trajectory measurement reuses Goal 1
(`einstein.meta_loop.trajectory`).
"""

from __future__ import annotations

import enum
import statistics
from dataclasses import dataclass
from urllib.parse import urlparse

from einstein.meta_loop.trajectory import TrajectoryPoint

# ---------------- arms ----------------


class Arm(enum.Enum):
    CURATED_WIKI = "A"
    WEB_SEARCH = "B"
    MODEL_ONLY = "C"


@dataclass(frozen=True)
class ArmConfig:
    """What an arm may read. All arms get the problem statement; all are
    firewalled from the answer key (the firewall is unconditional)."""

    arm: Arm
    allow_wiki: bool
    allow_web: bool

    @property
    def label(self) -> str:
        return f"{self.arm.value}-{self.arm.name.lower()}"


ARM_CONFIGS: dict[Arm, ArmConfig] = {
    Arm.CURATED_WIKI: ArmConfig(Arm.CURATED_WIKI, allow_wiki=True, allow_web=False),
    Arm.WEB_SEARCH: ArmConfig(Arm.WEB_SEARCH, allow_wiki=False, allow_web=True),
    Arm.MODEL_ONLY: ArmConfig(Arm.MODEL_ONLY, allow_wiki=False, allow_web=False),
}


def arms_isolated() -> bool:
    """Sanity invariant: the three arms differ in knowledge access (no two arms
    expose the same (wiki, web) pair). Guards against a config edit silently
    collapsing the experiment."""
    pairs = {(c.allow_wiki, c.allow_web) for c in ARM_CONFIGS.values()}
    return len(pairs) == len(ARM_CONFIGS)


# ---------------- firewall (the answer-key guarantee) ----------------


class FirewallViolation(RuntimeError):
    """Raised when an arm tries to reach the answer key (leaderboard / this repo
    / a solution dump). Arm B's web access must pass through `assert_allowed`."""


# The arena (leaderboard + solutions) and this project's own repos.
FIREWALL_DENY_HOSTS = (
    "einsteinarena.com",
    "raw.githubusercontent.com",
)
# Substrings that mark the answer key regardless of host: this repo's slug, the
# leaderboard, or a solution/results dump.
FIREWALL_DENY_SUBSTRINGS = (
    "jmsung/einstein",
    "leaderboard",
    "/solutions/",
    "solution-best",
)
# Local paths that are the answer key when an arm reads the filesystem.
FIREWALL_DENY_PATH_MARKERS = (
    "/mb/problems/",
    "/results/",
    "docs/wiki/problems/",  # problem pages carry SOTA scores
)


def _host_blocked(host: str) -> bool:
    host = host.lower()
    return any(host == h or host.endswith("." + h) for h in FIREWALL_DENY_HOSTS)


def is_firewalled(target: str) -> bool:
    """True iff `target` (a URL or local path) hits the answer key.

    Blocks: the arena host(s), any URL/path containing this repo's slug, the
    leaderboard, a solution dump, or local SOTA-bearing paths. Everything else
    (arxiv, wikipedia, general math references) is allowed — the arm may still
    *reason*, it just can't read the answer.
    """
    low = target.lower()
    if any(sub in low for sub in FIREWALL_DENY_SUBSTRINGS):
        return True
    if any(marker in low for marker in FIREWALL_DENY_PATH_MARKERS):
        return True
    host = urlparse(target).netloc
    if host and _host_blocked(host):
        return True
    return False


def assert_allowed(target: str) -> None:
    """Raise `FirewallViolation` if `target` is the answer key; else return."""
    if is_firewalled(target):
        raise FirewallViolation(f"firewall: '{target}' is the answer key — blocked for arm B")


def firewall_verified(probe_urls: list[str]) -> bool:
    """Verify the firewall blocks every known answer-key probe (test-plan item:
    'B web-search firewall verified — no leaderboard/repo/solution leak')."""
    return all(is_firewalled(u) for u in probe_urls)


# Canonical answer-key probes — the firewall must block ALL of these.
ANSWER_KEY_PROBES = (
    "https://einsteinarena.com/problems/difference-bases",
    "https://einsteinarena.com/leaderboard",
    "https://github.com/jmsung/einstein/blob/main/docs/wiki/problems/19-difference-bases.md",
    "https://raw.githubusercontent.com/jmsung/einstein/main/README.md",
    "/Users/x/projects/einstein/mb/problems/19-difference-bases/solutions/solution-best.json",
    "docs/wiki/problems/2-first-autocorrelation.md",
)


# ---------------- N-seed run matrix ----------------


@dataclass(frozen=True)
class RunSpec:
    """One cold-start run to execute manually: (problem, arm, seed)."""

    problem_id: int
    arm: Arm
    seed: int

    @property
    def label(self) -> str:
        return f"P{self.problem_id}-{ARM_CONFIGS[self.arm].label}-seed{self.seed}"


def build_run_matrix(problem_ids: list[int], seeds: list[int]) -> list[RunSpec]:
    """The full (problem × arm × seed) matrix of cold-start runs to execute.

    Ordered problem → arm(A,B,C) → seed for legible batch scheduling.
    """
    return [RunSpec(pid, arm, seed) for pid in problem_ids for arm in Arm for seed in seeds]


# ---------------- measurement ----------------


def climb_rate(trajectory: list[TrajectoryPoint], *, minimize: bool) -> float:
    """Total verified improvement per cycle over the run (signed; >0 = climbing).

    Improvement = (first_best − last_best) for minimize, negated for maximize,
    divided by the number of cycles spanned. 0.0 for a flat or <2-point curve.
    """
    if len(trajectory) < 2:
        return 0.0
    first, last = trajectory[0].best_score, trajectory[-1].best_score
    span = trajectory[-1].cycle_id - trajectory[0].cycle_id
    if span <= 0:
        return 0.0
    gain = (first - last) if minimize else (last - first)
    return gain / span


def cycles_to_fraction_of_floor(
    trajectory: list[TrajectoryPoint],
    *,
    start: float,
    floor: float,
    fraction: float,
    minimize: bool,
) -> int | None:
    """Cycle id at which the running-best first closes `fraction` of the gap from
    `start` to the known `floor`. None if never reached (the honest 'didn't get
    there' — never silently 0).
    """
    gap = (start - floor) if minimize else (floor - start)
    if gap <= 0:
        return None  # already at/over the floor, or floor mis-specified
    target = start - fraction * gap if minimize else start + fraction * gap
    for pt in trajectory:
        reached = (pt.best_score <= target) if minimize else (pt.best_score >= target)
        if reached:
            return pt.cycle_id
    return None


def dead_ends_avoided(attempted_techniques: set[str], known_dead_ends: set[str]) -> int:
    """Count of known dead-end techniques the arm did NOT re-run.

    The curated-wiki arm should avoid more (it has the dead-end findings); the
    model-only arm re-grinds them. This is the metric that most directly tests
    'does the knowledge base help' — measured against `docs/wiki/findings/`.
    """
    return len(known_dead_ends - attempted_techniques)


# ---------------- distributional comparison ----------------


@dataclass(frozen=True)
class ArmSummary:
    """Across-seed distribution of climb-rate for one arm on one problem."""

    arm: Arm
    n_seeds: int
    mean_climb_rate: float
    median_climb_rate: float
    stdev_climb_rate: float


def summarize_arm(arm: Arm, climb_rates: list[float]) -> ArmSummary:
    if not climb_rates:
        return ArmSummary(arm, 0, 0.0, 0.0, 0.0)
    return ArmSummary(
        arm=arm,
        n_seeds=len(climb_rates),
        mean_climb_rate=statistics.fmean(climb_rates),
        median_climb_rate=statistics.median(climb_rates),
        stdev_climb_rate=statistics.stdev(climb_rates) if len(climb_rates) > 1 else 0.0,
    )


def rank_arms(climb_rates_by_arm: dict[Arm, list[float]]) -> list[ArmSummary]:
    """Per-arm summaries ranked by mean climb-rate (best first).

    The headline: if A (curated) ranks above B (web) above C (model-only), the
    knowledge base helps. If A ≈ B, web search suffices — the honest negative
    result the branch is prepared to report.
    """
    summaries = [summarize_arm(arm, rates) for arm, rates in climb_rates_by_arm.items()]
    summaries.sort(key=lambda s: s.mean_climb_rate, reverse=True)
    return summaries
