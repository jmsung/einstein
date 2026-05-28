"""fanout.py — K-attempt orchestrator (Goal 1).

Given (problem, K, bandit, rng, runner), build K `AttemptContext`s, invoke
`runner` for each, and return a `FanoutResult` with all K outcomes plus the
winner index. The arena verifier (via the runner's returned `score`) picks
the winner — never internal heuristics.

K-pull Thompson semantics (confirmed in Goal 0):
  K independent θ draws from the SAME Beta posterior per arm; argmax per
  draw. Collisions allowed and informative — when one arm dominates the
  posterior, K pulls on that arm is the optimal play under probability
  matching. We reject any "exclusion" variant within a single fanout.

Determinism contract:
  Two `run_fanout` calls with identical (problem, k, bandit-state, runner,
  seeded rng) produce identical `FanoutResult.attempts` and `winner_index`.
  Per-attempt RNGs are derived from the shared rng deterministically.

Portability:
  This module is domain-agnostic. Math-specific bits (optimizer dispatch,
  arena verifier, problem schema) live behind the `runner` callable. If
  another archetype wants K-attempt fanout, the same `run_fanout` works.
"""

from __future__ import annotations

import concurrent.futures
import random
from concurrent.futures import Executor, ThreadPoolExecutor
from dataclasses import dataclass
from typing import Callable, Literal, Protocol

from einstein.bandit.thompson import PickResult, ThompsonSampler


class _Problem(Protocol):
    """Duck type for `autonomous_loop.Problem`. Enough for the runner to
    route dispatch; fanout itself doesn't read any fields."""

    problem_id: int
    score_current: float | None


_RAND_INT_MAX = 2**31 - 1


# ---------------- attempt context + result ----------------


@dataclass(frozen=True)
class AttemptContext:
    """What `runner` receives for one attempt.

    `technique` and `pick_note` are None when the bandit found no matching
    arm for the category — the runner decides fallback (council, manifest
    dispatch, skip).

    `rng` is a per-attempt `random.Random` seeded deterministically from
    the shared rng passed to `run_fanout`. Use it for any per-attempt
    seeded operation (the actual optimizer's seed, sub-trial draws, etc.)
    so the cycle stays reproducible.
    """

    problem: _Problem
    attempt_index: int  # 1-indexed (matches inner_attempt's `attempt_index`)
    technique: str | None
    pick_note: str | None
    rng: random.Random


@dataclass(frozen=True)
class AttemptResult:
    """What `runner` returns. All K of these are recorded in cycle-log."""

    index: int  # 1-indexed; matches AttemptContext.attempt_index
    technique: str | None
    score: float | None  # None when the attempt did not complete
    exit: str  # "ok" | "no-arm" | "timeout" | "dispatch-failed" | "no-manifest-entry" | …
    notes: str
    pick_note: str | None  # echoes AttemptContext.pick_note for cycle-log capture


AttemptRunner = Callable[[AttemptContext], AttemptResult]
"""Signature: runner(ctx) -> AttemptResult."""


# ---------------- result ----------------


@dataclass(frozen=True)
class FanoutResult:
    """K attempts + the winner index (None when none completed)."""

    attempts: tuple[AttemptResult, ...]
    winner_index: int | None  # index into `attempts`; None if no `exit == 'ok'`

    @property
    def winner(self) -> AttemptResult | None:
        if self.winner_index is None:
            return None
        return self.attempts[self.winner_index]

    @property
    def k_completed(self) -> int:
        """Number of attempts with `exit == 'ok'`."""
        return sum(1 for a in self.attempts if a.exit == "ok")

    @property
    def pick_notes(self) -> list[str | None]:
        """The K bandit audit strings, for the cycle-log row (Goal 3)."""
        return [a.pick_note for a in self.attempts]


# ---------------- orchestration ----------------


def _pick_winner(
    attempts: tuple[AttemptResult, ...],
    *,
    score_direction: Literal["min", "max"],
) -> int | None:
    """Argmin / argmax of `score` over completed attempts. Stable on ties:
    earliest attempt wins (caller can interpret 'first to finish')."""
    best_index: int | None = None
    best_score: float | None = None
    for a in attempts:
        if a.exit != "ok" or a.score is None:
            continue
        if best_score is None:
            best_index, best_score = a.index - 1, a.score  # attempts is 0-indexed
            continue
        if score_direction == "min" and a.score < best_score:
            best_index, best_score = a.index - 1, a.score
        elif score_direction == "max" and a.score > best_score:
            best_index, best_score = a.index - 1, a.score
    return best_index


def _timeout_attempt_result(ctx: AttemptContext, seconds: float) -> AttemptResult:
    """Fabricated result when `runner(ctx)` exceeds the per-attempt timeout."""
    return AttemptResult(
        index=ctx.attempt_index,
        technique=ctx.technique,
        score=None,
        exit="timeout",
        notes=f"per-attempt timeout exceeded ({seconds}s)",
        pick_note=ctx.pick_note,
    )


def run_fanout(
    problem: _Problem,
    *,
    k: int,
    bandit: ThompsonSampler,
    category: str,
    rng: random.Random,
    runner: AttemptRunner,
    score_direction: Literal["min", "max"] = "min",
    per_attempt_timeout_seconds: float | None = None,
    executor: Executor | None = None,
) -> FanoutResult:
    """Run K parallel attempts; return all results + winner index.

    Args:
        problem: passed to the runner via `AttemptContext.problem`. Fanout
            itself reads no fields.
        k: number of attempts. Must be >= 1.
        bandit: Thompson sampler. K independent `pick(category, rng=rng)`
            calls produce K independent draws from the same posterior;
            collisions are allowed and informative.
        category: bandit category for arm masking (e.g. "circle-packing").
        rng: seeded `random.Random`. The bandit picks AND the per-attempt
            RNG derivation both consume from this stream — same seed →
            same K attempts.
        runner: callable that executes one attempt. Injected so tests don't
            spin up the optimizer dispatch.
        score_direction: "min" (default; codebase convention) or "max".
        per_attempt_timeout_seconds: when set (Goal 4), each `runner(ctx)`
            call runs in a `ThreadPoolExecutor` worker and is given at most
            this many seconds; on timeout, the result becomes
            `AttemptResult(exit="timeout", score=None, ...)` with the
            technique + pick_note preserved. Soft timeout — Python can't
            kill a running thread, so the runner keeps consuming CPU in the
            background, but the cycle moves on. None = sequential, no thread
            overhead (pre-Goal-4 behavior).
        executor: test seam for Goal 4. When timeout is set and `executor`
            is None, a fresh `ThreadPoolExecutor(max_workers=k)` is created
            and shut down `wait=False` after collection.

    Returns:
        FanoutResult — K attempts in submission-index order (NOT completion
        order — Goal 3 needs `attempts[i]` to align with `chosen_techniques[i]`).
        `winner_index` = the best `exit == "ok"` attempt (None if none).

    Raises:
        ValueError on invalid k or score_direction.
    """
    if k < 1:
        raise ValueError(f"K must be >= 1, got {k}")
    if score_direction not in ("min", "max"):
        raise ValueError(f"score_direction must be 'min' or 'max', got {score_direction!r}")

    # 1. Sample K AttemptContexts deterministically from the shared rng.
    #    Done before any threading so technique picks stay reproducible.
    ctxs: list[AttemptContext] = []
    for i in range(1, k + 1):
        # Per-attempt rng derived BEFORE the bandit pick — determinism test pins.
        attempt_seed = rng.randint(0, _RAND_INT_MAX)
        attempt_rng = random.Random(attempt_seed)
        pick: PickResult | None = bandit.pick(category, rng=rng)
        ctxs.append(
            AttemptContext(
                problem=problem,
                attempt_index=i,
                technique=pick.technique if pick is not None else None,
                pick_note=pick.note() if pick is not None else None,
                rng=attempt_rng,
            )
        )

    # 2. Run the K attempts. Sequential when no timeout; threaded otherwise.
    if per_attempt_timeout_seconds is None:
        results: list[AttemptResult] = [runner(ctx) for ctx in ctxs]
    else:
        owns_executor = executor is None
        ex = executor or ThreadPoolExecutor(max_workers=max(1, k))
        try:
            futures = [ex.submit(runner, ctx) for ctx in ctxs]
            results = []
            for ctx, fut in zip(ctxs, futures):
                try:
                    results.append(fut.result(timeout=per_attempt_timeout_seconds))
                except concurrent.futures.TimeoutError:
                    # Dead thread keeps running in background — Python can't
                    # cancel it. Side-channels that the runner writes to AFTER
                    # this point are harmless: winner_index is computed over
                    # exit=="ok" attempts only, so a late write into
                    # `payloads_by_index` from a timed-out thread can never
                    # be read.
                    results.append(_timeout_attempt_result(ctx, per_attempt_timeout_seconds))
        finally:
            if owns_executor:
                ex.shutdown(wait=False)

    attempts = tuple(results)
    winner_index = _pick_winner(attempts, score_direction=score_direction)
    return FanoutResult(attempts=attempts, winner_index=winner_index)


__all__ = [
    "AttemptContext",
    "AttemptResult",
    "AttemptRunner",
    "FanoutResult",
    "run_fanout",
]
