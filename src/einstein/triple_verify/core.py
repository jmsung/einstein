"""core.py — dataclasses, tolerance, registry, and dispatcher for triple-verify.

The agreement rule (the disagreement protocol from
`.claude/rules/triple-verify.md`, design in
`docs/wiki/findings/triple-verify-wiring-design.md`):

  - three-way agreement within tolerance → passed=True
  - any pair outside tolerance         → passed=False (two-way mismatch = a bug)

"Within tolerance" is pairwise across all three numbers; a single divergent
pair fails the whole check. Honest-zero over fake-pass.
"""

from __future__ import annotations

import gzip
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

# A scorer takes the loaded solution dict and returns a float score.
Scorer = Callable[[dict], float]

_REPO = Path(__file__).resolve().parents[3]


# ---------------- tolerance ----------------


@dataclass(frozen=True)
class Tolerance:
    """Two-sided agreement band. Two numbers agree iff
    ``|a-b| <= max(abs_tol, rel_tol * max(|a|, |b|))``.
    """

    abs_tol: float = 1e-10
    rel_tol: float = 1e-8

    def agree(self, a: float, b: float) -> bool:
        if a == b:
            return True
        # Non-finite numbers (inf / nan) never "agree" unless bit-identical.
        if not (_finite(a) and _finite(b)):
            return False
        return abs(a - b) <= max(self.abs_tol, self.rel_tol * max(abs(a), abs(b)))


DEFAULT_TOLERANCE = Tolerance()


def _finite(x: float) -> bool:
    return x == x and x not in (float("inf"), float("-inf"))


# ---------------- result ----------------


@dataclass
class TripleVerifyResult:
    """Outcome of one triple-verify run. ``as_dict()`` yields exactly the dict
    that ``auto_submit.try_submit`` gate 2 reads — so the gate logic is
    unchanged; only the *source* of the dict moved from a hardcoded literal to
    this verdict.
    """

    passed: bool
    problem_id: int
    fast: float | None = None
    exact: float | None = None
    cross: float | None = None
    reason: str = ""
    tolerance: Tolerance = field(default_factory=Tolerance)

    def as_dict(self) -> dict:
        d: dict = {"passed": self.passed}
        if self.fast is not None:
            d["fast"] = self.fast
        if self.exact is not None:
            d["exact"] = self.exact
        if self.cross is not None:
            d["cross"] = self.cross
        if self.reason:
            d["note"] = self.reason
        return d


# ---------------- verifier ----------------


@dataclass(frozen=True)
class TripleVerifier:
    """Three scorers + a tolerance for one problem.

    If ``unavailable_reason`` is set, the problem is registered honestly as
    *cannot be verified* — ``verify`` short-circuits to ``passed=False`` with
    that reason (e.g. ``"no_third_check_available"``) instead of running. This
    keeps a problem from being silently passed when its third check doesn't yet
    exist.
    """

    problem_id: int
    fast: Scorer | None = None
    exact: Scorer | None = None
    cross: Scorer | None = None
    tolerance: Tolerance = DEFAULT_TOLERANCE
    unavailable_reason: str | None = None


# ---------------- registry ----------------

_REGISTRY: dict[int, TripleVerifier] = {}


def register(
    problem_id: int,
    *,
    fast: Scorer | None = None,
    exact: Scorer | None = None,
    cross: Scorer | None = None,
    tolerance: Tolerance = DEFAULT_TOLERANCE,
    unavailable_reason: str | None = None,
) -> TripleVerifier:
    """Register (or replace) the triple-verifier for ``problem_id``.

    Either supply all three scorers, or supply ``unavailable_reason`` to record
    an honest can't-verify entry. Returns the stored ``TripleVerifier``.
    """
    if unavailable_reason is None and not (fast and exact and cross):
        raise ValueError(
            f"register(P{problem_id}): need all three scorers (fast, exact, cross) "
            f"or an explicit unavailable_reason"
        )
    v = TripleVerifier(
        problem_id=problem_id,
        fast=fast,
        exact=exact,
        cross=cross,
        tolerance=tolerance,
        unavailable_reason=unavailable_reason,
    )
    _REGISTRY[problem_id] = v
    return v


def get_verifier(problem_id: int) -> TripleVerifier | None:
    return _REGISTRY.get(problem_id)


def registered_ids() -> list[int]:
    return sorted(_REGISTRY)


def clear_registry() -> None:
    """Test seam — drop all registrations."""
    _REGISTRY.clear()


# ---------------- agreement core ----------------


def verify(seed: dict, verifier: TripleVerifier) -> TripleVerifyResult:
    """Run the three scorers on ``seed`` and apply the agreement rule."""
    pid = verifier.problem_id
    tol = verifier.tolerance

    if verifier.unavailable_reason is not None:
        return TripleVerifyResult(
            passed=False, problem_id=pid, reason=verifier.unavailable_reason, tolerance=tol
        )

    numbers: dict[str, float] = {}
    for name, scorer in (
        ("fast", verifier.fast),
        ("exact", verifier.exact),
        ("cross", verifier.cross),
    ):
        assert scorer is not None  # guaranteed by register()
        try:
            numbers[name] = float(scorer(seed))
        except Exception as e:  # a scorer that raises = unverifiable, honest-zero
            return TripleVerifyResult(
                passed=False,
                problem_id=pid,
                reason=f"{name}-check raised {type(e).__name__}: {e}",
                tolerance=tol,
                **{k: v for k, v in numbers.items()},
            )

    fast, exact, cross = numbers["fast"], numbers["exact"], numbers["cross"]
    pairs = {
        "fast/exact": tol.agree(fast, exact),
        "fast/cross": tol.agree(fast, cross),
        "exact/cross": tol.agree(exact, cross),
    }
    diverging = [name for name, ok in pairs.items() if not ok]

    if not diverging:
        reason = "3-way agreement"
    else:
        reason = (
            "disagreement: "
            + ", ".join(f"{p} differ" for p in diverging)
            + f" (fast={fast:.14g}, exact={exact:.14g}, cross={cross:.14g})"
        )

    return TripleVerifyResult(
        passed=not diverging,
        problem_id=pid,
        fast=fast,
        exact=exact,
        cross=cross,
        reason=reason,
        tolerance=tol,
    )


# ---------------- dispatcher ----------------


def _load_seed(path: Path) -> dict:
    """Load a solution JSON (transparently gunzips ``.gz``). Same discipline as
    ``scripts/verify_seed.py``."""
    if not path.is_file():
        raise FileNotFoundError(f"solution not found at {path}")
    raw = gzip.decompress(path.read_bytes()) if path.suffix == ".gz" else path.read_bytes()
    data = json.loads(raw)
    if not isinstance(data, dict):
        raise ValueError(f"solution {path} must be a JSON object, got {type(data).__name__}")
    return data


def run(problem_id: int, solution_path: str | Path) -> TripleVerifyResult:
    """Dispatch entry point read by ``autonomous_loop.py``.

    Loads the solution at ``solution_path``, looks up the registered verifier,
    and returns its verdict. An unregistered problem returns
    ``passed=False, reason="not_registered"`` — never a silent pass.

    ``solution_path`` may carry a ``{"payload": {...}}`` wrapper (the shape
    written by ``verify_seed.py`` / ``json_score_payload`` result files); the
    payload is unwrapped to the bare solution dict the scorers expect.
    """
    verifier = get_verifier(problem_id)
    if verifier is None:
        return TripleVerifyResult(passed=False, problem_id=problem_id, reason="not_registered")
    try:
        seed = _load_seed(Path(solution_path))
    except (FileNotFoundError, ValueError, json.JSONDecodeError) as e:
        return TripleVerifyResult(
            passed=False,
            problem_id=problem_id,
            reason=f"solution load failed: {e}",
            tolerance=verifier.tolerance,
        )
    if "payload" in seed and isinstance(seed["payload"], dict):
        seed = seed["payload"]
    return verify(seed, verifier)
