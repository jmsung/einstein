"""AlphaEvolve-style evolve engine — Goal 4 of js/feat/evolve-and-measure.

The loop that actually *climbs* on problems with genuine open headroom:

    champion  →  mutate-K  →  triple-verify each  →  promote best iff STRICTLY
    better  →  repeat

This is AlphaEvolve/FunSearch's shape (already published — not our novelty); our
contribution is the rigor around it: the champion only ever moves on a
triple-verified strict improvement, and the engine is *gated* to problems the
Goal-1 classifier calls ``stuck`` (open headroom, no certificate). Running it on
a solved-at-floor problem would burn LLM spend chasing a proven floor — the
exact waste this branch exists to stop.

Design — pure core, injected edges:

- ``mutator(champion, k, rng) -> list[payload]`` is the LLM mutate-K step,
  injected so tests are deterministic and the engine has no claude dependency.
- ``verify_fn(payload) -> float | None`` is the score gate: the triple-verified
  score, or ``None`` when verification fails (a candidate that can't be
  triple-verified is not a candidate). ``triple_verify_score_fn`` builds the
  production one from the registry.
- The promotion rule (``strict_improvement``) and selection (``select_best``)
  are pure and exhaustively tested.

Reuse: selection mirrors ``parallel.fanout``'s best-of-K argmin/argmax; the
score gate is ``triple_verify``; the production K-evaluation can be driven by
``run_fanout`` + the Thompson bandit (each mutation operator an arm) when the
loop turns the engine on — the engine core stays agnostic to how the K
candidates were produced.
"""

from __future__ import annotations

import random
from dataclasses import dataclass, field
from typing import Callable

from einstein.meta_loop.trajectory import Classification, ProblemClassification

# A solution payload — the per-problem param dict auto_submit / verifiers read.
Payload = dict
Mutator = Callable[["Champion", int, random.Random], list[Payload]]
VerifyFn = Callable[[Payload], "float | None"]


@dataclass(frozen=True)
class Champion:
    """The current best triple-verified solution for one problem."""

    score: float
    payload: Payload


@dataclass(frozen=True)
class GenerationResult:
    """Outcome of one evolve generation (one mutate-K → verify → select round)."""

    generation: int
    champion: Champion  # champion AFTER this generation (unchanged if no promote)
    promoted: bool
    best_candidate_score: float | None  # best verified candidate this generation
    n_candidates: int  # mutants proposed
    n_verified: int  # mutants that triple-verified


# ---------------- promotion rule ----------------


def strict_improvement(
    candidate: float, champion_score: float, *, minimize: bool, min_improvement: float = 0.0
) -> bool:
    """True iff ``candidate`` strictly beats ``champion_score`` by > the margin.

    ``min_improvement`` (default 0.0 = bit-strict) guards against promoting on
    float noise; pass the problem's arena ``minImprovement`` to require a
    submission-meaningful gain.
    """
    if minimize:
        return candidate < champion_score - min_improvement
    return candidate > champion_score + min_improvement


def select_best(
    scored: list[tuple[Payload, float | None]], *, minimize: bool
) -> tuple[Payload, float] | None:
    """Best (payload, score) over candidates that verified (score is not None).

    Ties resolve to the earliest candidate (stable) — mirrors fanout's
    earliest-wins convention. Returns None when nothing verified.
    """
    best: tuple[Payload, float] | None = None
    for payload, score in scored:
        if score is None:
            continue
        if best is None:
            best = (payload, score)
            continue
        if (minimize and score < best[1]) or (not minimize and score > best[1]):
            best = (payload, score)
    return best


# ---------------- one generation (pure) ----------------


def evolve_step(
    champion: Champion,
    candidates: list[Payload],
    verify_fn: VerifyFn,
    *,
    minimize: bool,
    min_improvement: float = 0.0,
    generation: int = 1,
) -> GenerationResult:
    """Verify K candidates, select the best, promote iff strictly better.

    Pure: ``candidates`` are pre-generated and ``verify_fn`` is injected. The
    champion is replaced ONLY on a strict improvement; otherwise it is returned
    unchanged (the AlphaEvolve invariant — the champion is monotone).
    """
    scored = [(c, verify_fn(c)) for c in candidates]
    n_verified = sum(1 for _, s in scored if s is not None)
    best = select_best(scored, minimize=minimize)

    if best is None:
        return GenerationResult(
            generation=generation,
            champion=champion,
            promoted=False,
            best_candidate_score=None,
            n_candidates=len(candidates),
            n_verified=0,
        )

    best_payload, best_score = best
    promote = strict_improvement(
        best_score, champion.score, minimize=minimize, min_improvement=min_improvement
    )
    new_champion = Champion(score=best_score, payload=best_payload) if promote else champion
    return GenerationResult(
        generation=generation,
        champion=new_champion,
        promoted=promote,
        best_candidate_score=best_score,
        n_candidates=len(candidates),
        n_verified=n_verified,
    )


# ---------------- the loop ----------------


@dataclass
class EvolveRun:
    """Full evolve run: the final champion + per-generation history."""

    final_champion: Champion
    generations: list[GenerationResult] = field(default_factory=list)

    @property
    def improved(self) -> bool:
        return any(g.promoted for g in self.generations)

    @property
    def total_promotions(self) -> int:
        return sum(1 for g in self.generations if g.promoted)


def evolve(
    champion: Champion,
    *,
    generations: int,
    k: int,
    mutator: Mutator,
    verify_fn: VerifyFn,
    rng: random.Random,
    minimize: bool,
    min_improvement: float = 0.0,
) -> EvolveRun:
    """Run ``generations`` rounds of mutate-K → verify → promote-iff-better.

    Deterministic under a seeded ``rng`` *given a deterministic mutator* — the
    same seed reproduces the same run (the reproducibility the test plan asks
    for). The champion threads forward across generations and only ever moves on
    a strict, triple-verified improvement.
    """
    history: list[GenerationResult] = []
    current = champion
    for gen in range(1, generations + 1):
        candidates = mutator(current, k, rng)
        result = evolve_step(
            current,
            candidates,
            verify_fn,
            minimize=minimize,
            min_improvement=min_improvement,
            generation=gen,
        )
        history.append(result)
        current = result.champion
    return EvolveRun(final_champion=current, generations=history)


# ---------------- the gate ----------------


def should_evolve(pc: ProblemClassification) -> bool:
    """Gate: evolve ONLY problems classified ``stuck`` (open headroom, no cert).

    - ``solved-at-floor`` → a certificate proves the floor; climbing is waste.
    - ``improving`` → the existing loop is already climbing; don't pre-empt.
    - ``unknown`` → not enough signal to justify LLM spend.
    Only ``stuck`` has the profile the engine is built for: real headroom and no
    proof we're at the floor.
    """
    return pc.classification is Classification.STUCK


# ---------------- triple-verify score adapter ----------------


def triple_verify_score_fn(problem_id: int) -> VerifyFn:
    """Build the production ``verify_fn`` from the triple-verify registry.

    Returns a callable that triple-verifies a payload and yields the agreed
    score iff all three checks agree, else ``None``. An unregistered problem (no
    verifier) yields ``None`` for every candidate — the engine simply never
    promotes, which is the honest behavior (we can't trust an unverifiable gain).
    """
    from einstein.triple_verify.core import get_verifier, verify

    def _score(payload: Payload) -> float | None:
        verifier = get_verifier(problem_id)
        if verifier is None:
            return None
        result = verify(payload, verifier)
        if not result.passed:
            return None
        # The agreed score: prefer exact, fall back to fast (they agree on pass).
        return result.exact if result.exact is not None else result.fast

    return _score
