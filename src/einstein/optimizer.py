"""Generic RALPH-style adaptive optimizer.

Problem-agnostic optimization loop that uses the knowledge layer
to inform strategy selection. Each problem provides:
  - score_fn(solution) -> float
  - direction: "minimize" or "maximize"
  - category: problem category (for knowledge-based priors)

The optimizer handles strategy selection, iteration, and learning.
Problem-specific strategies can be registered via add_strategy().
"""

from __future__ import annotations

import time
from collections import defaultdict
from typing import Any, Callable

import numpy as np
from scipy.optimize import minimize

from einstein.knowledge import get_strategy_priors


# ── Built-in strategies (work on any continuous problem) ─────────────────────

def _strategy_hillclimb(
    solution: list[float],
    score_fn: Callable,
    rng: np.random.RandomState,
    is_better: Callable[[float, float], bool],
) -> tuple[list[float], float]:
    """Coordinate-wise perturbation with adaptive step sizes."""
    x = list(solution)
    k = len(x)
    step = rng.choice([0.5, 0.1, 0.01, 0.001])
    step_sizes = [step] * k
    best = score_fn(x)

    for _ in range(60):
        improved = False
        for i in range(k):
            for d in [1, -1]:
                for s in [1.0, 0.5, 0.1, 2.0]:
                    trial = list(x)
                    trial[i] += d * step_sizes[i] * s
                    score = score_fn(trial)
                    if is_better(score, best):
                        best = score
                        x = trial
                        improved = True
                        break
                if improved:
                    break
        if not improved:
            step_sizes = [s * 0.5 for s in step_sizes]
            if max(step_sizes) < 1e-13:
                break
    return x, best


def _strategy_nelder_mead(
    solution: list[float],
    score_fn: Callable,
    rng: np.random.RandomState,
    is_better: Callable[[float, float], bool],
) -> tuple[list[float], float]:
    """Nelder-Mead simplex — good for non-smooth landscapes."""
    trial = [v + rng.randn() * 0.05 for v in solution]
    sign = 1.0  # minimize by default; negate for maximize
    if not is_better(0.0, 1.0):  # maximize mode
        sign = -1.0

    def obj(x):
        return sign * score_fn(list(x))

    res = minimize(obj, trial, method="Nelder-Mead",
                   options={"maxiter": 2000, "xatol": 1e-12, "fatol": 1e-16})
    return list(res.x), score_fn(list(res.x))


def _strategy_lbfgsb(
    solution: list[float],
    score_fn: Callable,
    rng: np.random.RandomState,
    is_better: Callable[[float, float], bool],
) -> tuple[list[float], float]:
    """L-BFGS-B with small perturbation."""
    trial = [v + rng.randn() * 0.1 for v in solution]
    sign = 1.0
    if not is_better(0.0, 1.0):
        sign = -1.0

    def obj(x):
        return sign * score_fn(list(x))

    res = minimize(obj, trial, method="L-BFGS-B",
                   options={"maxiter": 300, "ftol": 1e-16})
    return list(res.x), score_fn(list(res.x))


def _strategy_perturbation(
    solution: list[float],
    score_fn: Callable,
    rng: np.random.RandomState,
    is_better: Callable[[float, float], bool],
) -> tuple[list[float], float]:
    """Random perturbation of subset + hillclimb refinement."""
    k = len(solution)
    trial = list(solution)
    n_perturb = rng.randint(1, min(4, k) + 1)
    indices = rng.choice(k, n_perturb, replace=False)
    sigma = rng.choice([0.3, 0.5, 1.0, 2.0])
    for i in indices:
        trial[i] += rng.randn() * sigma
    return _strategy_hillclimb(trial, score_fn, rng, is_better)


BUILTIN_STRATEGIES: dict[str, Callable] = {
    "hillclimb": _strategy_hillclimb,
    "nelder_mead": _strategy_nelder_mead,
    "lbfgsb": _strategy_lbfgsb,
    "perturbation": _strategy_perturbation,
}


# ── Optimizer ────────────────────────────────────────────────────────────────

class Optimizer:
    """Generic RALPH-style adaptive optimizer.

    Args:
        score_fn: Evaluates a solution, returns a float score.
        direction: "minimize" or "maximize".
        category: Problem category string (for knowledge-based priors).
        verify_fn: Optional exact verifier. Called on candidates before accepting.
    """

    def __init__(
        self,
        score_fn: Callable[[Any], float],
        direction: str = "minimize",
        category: str = "continuous",
        verify_fn: Callable[[Any], float] | None = None,
    ):
        self.score_fn = score_fn
        self.direction = direction
        self.category = category
        self.verify_fn = verify_fn
        self.strategies: dict[str, Callable] = dict(BUILTIN_STRATEGIES)
        self.history: list[dict] = []

        if direction == "minimize":
            self.best_score = float("inf")
            self._is_better = lambda new, old: new < old - 1e-15
        else:
            self.best_score = float("-inf")
            self._is_better = lambda new, old: new > old + 1e-15

        self.best_solution: Any = None

    def add_strategy(self, name: str, fn: Callable) -> None:
        """Register a problem-specific strategy."""
        self.strategies[name] = fn

    def select_strategies(self, max_strategies: int = 5) -> list[str]:
        """Pick strategies for next iteration using knowledge priors + history."""
        priors = get_strategy_priors(self.category)
        prior_map = {name: weight for name, weight in priors}

        # Boost strategies that have worked in recent history
        for record in self.history[-10:]:
            for sr in record.get("strategy_results", []):
                name = sr["name"]
                if sr.get("improved"):
                    prior_map[name] = prior_map.get(name, 1.0) + 3.0

        # Only include strategies we actually have implementations for
        available = [(name, prior_map.get(name, 1.0)) for name in self.strategies]
        available.sort(key=lambda x: x[1], reverse=True)

        return [name for name, _ in available[:max_strategies]]

    def run_iteration(
        self,
        solution: Any,
        strategies: list[str] | None = None,
        seed: int | None = None,
    ) -> dict:
        """Run one optimization iteration with selected strategies.

        Returns dict with best_score, best_solution, strategy_results.
        """
        if strategies is None:
            strategies = self.select_strategies()

        if seed is None:
            seed = int(time.time()) % 100000

        if self.best_solution is None:
            self.best_solution = solution
            self.best_score = self.score_fn(solution)

        results = []
        iter_best_score = self.best_score
        iter_best_solution = self.best_solution

        for name in strategies:
            fn = self.strategies.get(name)
            if fn is None:
                continue

            rng = np.random.RandomState(seed + hash(name) % 10000)
            try:
                t0 = time.time()
                candidate, score = fn(
                    list(solution), self.score_fn, rng, self._is_better,
                )
                dt = time.time() - t0

                improved = self._is_better(score, iter_best_score)

                # Verification gate
                verified = True
                if improved and self.verify_fn is not None:
                    try:
                        exact_score = self.verify_fn(candidate)
                        if abs(score - exact_score) > 1e-4:
                            verified = False
                        else:
                            score = exact_score
                    except Exception:
                        verified = False

                if improved and verified:
                    iter_best_score = score
                    iter_best_solution = candidate

                results.append({
                    "name": name,
                    "score": score,
                    "time": dt,
                    "improved": improved and verified,
                })
            except Exception as e:
                results.append({
                    "name": name,
                    "score": None,
                    "time": 0.0,
                    "improved": False,
                    "error": str(e),
                })

        # Update global best
        if self._is_better(iter_best_score, self.best_score):
            self.best_score = iter_best_score
            self.best_solution = iter_best_solution

        record = {
            "best_score": self.best_score,
            "best_solution": self.best_solution,
            "strategy_results": results,
        }
        self.history.append(record)
        return record
