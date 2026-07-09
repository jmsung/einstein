"""triple_verify — per-problem 3-way score verification for the auto-submit gate.

Axiom A1 (`.claude/rules/axioms.md`) requires every trusted score to agree
across three *different kinds* of evidence before it can feed an arena
submission:

  1. fast local evaluator   (the optimization-loop scorer)
  2. exact / independent reimplementation   (a different code path)
  3. cross-check            (analytical bound / different method / higher precision)

`auto_submit.try_submit` gate 2 reads a dict `{"passed": bool, ...}`. Until this
package landed, `autonomous_loop.py` hardcoded `{"passed": False}`, making the
whole auto-submit chain a no-op. This package produces a real verdict.

Public API:

    from einstein import triple_verify
    result = triple_verify.run(problem_id, solution_path)   # -> TripleVerifyResult
    gate_dict = result.as_dict()                            # -> {"passed", "fast", ...}

A `problem_id` with no registration returns ``passed=False,
reason="not_registered"`` — never a silent pass. See
``knowledge/wiki/findings/triple-verify-wiring-design.md`` for the design.
"""

from __future__ import annotations

# Import per-problem registration modules for their import-time side effects.
# Each module calls register(...) at import; the problems/ package handles the
# fan-out import. (Empty in Goal 1; populated in Goal 2.)
from . import problems as _problems  # noqa: F401  (side-effect import)
from .core import (
    DEFAULT_TOLERANCE,
    Tolerance,
    TripleVerifier,
    TripleVerifyResult,
    clear_registry,
    get_verifier,
    register,
    registered_ids,
    run,
    run_payload,
    verify,
)

__all__ = [
    "DEFAULT_TOLERANCE",
    "Tolerance",
    "TripleVerifier",
    "TripleVerifyResult",
    "clear_registry",
    "get_verifier",
    "register",
    "registered_ids",
    "run",
    "run_payload",
    "verify",
]
