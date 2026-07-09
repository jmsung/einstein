---
type: finding
author: agent
drafted: 2026-06-03
question_origin: problem-all (auto-submit gate 2)
status: answered
related_concepts: [triple-verify, auto-submit-gate-chain, float64-ceiling, arena-tolerance-drift]
cites:
  - .claude/rules/triple-verify.md
  - .claude/rules/axioms.md
  - src/einstein/auto_submit.py
  - scripts/autonomous_loop.py
  - scripts/verify_seed.py
  - knowledge/wiki/findings/verify-seed-dispatch-pattern.md
---

# Triple-verify wiring design — turning gate 2 from a hardcoded `False` into a real per-problem verdict

## The question

`scripts/autonomous_loop.py` hardcodes `triple_verify={"passed": False, "note": "triple-verify not yet wired"}`. Gate 2 of the `auto_submit.try_submit` chain (`src/einstein/auto_submit.py:251`) hard-rejects every candidate whose `triple_verify["passed"]` is not truthy. So the entire auto-submit pipeline is a no-op regardless of `EINSTEIN_AUTO_SUBMIT`. **What protocol must a per-problem 3-way check satisfy, and what package shape lets gate 2 read a real verdict without silently passing un-verified problems?**

## The protocol (confirmed from the rules)

From `.claude/rules/axioms.md` A1 and `.claude/rules/triple-verify.md`, every trusted score needs three numbers from three *different kinds* of evidence:

1. **Fast local evaluator** — the optimization-loop scorer. Approximations OK. In this repo: `einstein.<problem>.evaluator.evaluate` (or `arena_score` / `fast_score`).
2. **Exact / independent reimplementation** — a *different code path* that catches numerical bugs, off-by-one, sign errors. For float-precision-critical problems (P5, P11, P14) this is mpmath at 50–80 dps; for combinatorial problems (P19) it is an independent re-derivation of the score from the raw set.
3. **Cross-check** — a *different kind* of evidence: a known analytical bound, a structurally different method, or a higher-precision computation. Not just re-running check #1.

**Agreement rule (the disagreement protocol).** No standalone `triple-verify-disagreement-protocol.md` finding existed before this branch — filed as a gap and answered here:

- **Three-way agreement within tolerance → `passed: True`.** Score is real; proceed.
- **Two-way mismatch → `passed: False`, it's a bug.** Stop, record the two divergent numbers in the note, write a dead-end finding.
- **Three-way disagreement → `passed: False`.** Evaluator definitions diverge; the arena verifier is ground truth, not the most-recent code.

"Agreement within tolerance" is pairwise: all three of |fast−exact|, |fast−cross|, |exact−cross| must satisfy the per-problem tolerance. A single pair outside the band fails the whole check (honest-zero over fake-pass).

**Tolerance expression.** Per-problem, two-sided: `abs_tol` (absolute) and `rel_tol` (relative). Two numbers agree iff `|a−b| ≤ max(abs_tol, rel_tol·max(|a|,|b|))`. Default if a problem pins nothing: `abs_tol=1e-10, rel_tol=1e-8` (matches the spirit of `auto_submit.DEFAULT_MIN_IMPROVEMENT=1e-8`). Float-ceiling problems (P5/P11/P14) pin tighter abs_tol against their mpmath check; combinatorial problems (P19) use exact-equality-scale tolerance.

## The package shape (what Goals 1–2 build)

New package `src/einstein/triple_verify/`:

- **`TripleVerifyResult`** — dataclass: `passed: bool`, `problem_id: int`, `fast/exact/cross: float|None`, `reason: str`, `note: str`, `tolerance: Tolerance`. Round-trips to the dict gate 2 already reads (`{"passed", "fast", "exact", "cross", "note"}`), so `auto_submit.try_submit`'s gate-2 logic is **unchanged** — only the *source* of the dict changes.
- **`Tolerance`** — frozen dataclass `(abs_tol, rel_tol)` with `agree(a, b) -> bool`.
- **registry** — `dict[int, TripleVerifier]`, populated by import-time `register(problem_id, ...)` calls in `triple_verify/problems/<problem>.py`. A `TripleVerifier` bundles three callables `(fast, exact, cross)` each `seed_dict -> float`, plus a `Tolerance`.
- **dispatcher** — `run(problem_id, solution_path) -> TripleVerifyResult`. Loads the seed (same loader discipline as `verify_seed.py`), looks up the verifier, runs all three, applies the agreement rule.

**The not-registered rule is load-bearing.** A `problem_id` absent from the registry returns `passed=False, reason="not_registered"` — *never* silently passes. This mirrors `verify_seed.SPECS`: a problem with no triple-verify entry is rejected at gate 2, not waved through. Goal 4's registry-coverage test asserts every manifest-wired problem has a registration, so Phase 6's manifest expansion can't outpace verification.

**Where check #3 genuinely doesn't exist** for a problem, register it with a verifier that returns `passed=False, reason="no_third_check_available"`. Better an honest zero (gate 2 hard-rejects until a check is found) than a fake pass.

## What this rules out / what it unblocks

- Rules out: a single-evaluator "score is real" claim feeding auto-submit. The P9/P14/P17 drift incidents (axiom A1 "Why L0") are exactly what this gate guards against.
- Unblocks: flipping `EINSTEIN_AUTO_SUBMIT=1` becomes a real action. Gate 1 (strict improvement over arena #1), gate 3 (throttle), gate 4 (daily cap) still bound it. P2's tight 1.84e-7 gap (`autocorrelation-family-displaced-2026-06.md`) becomes the most-likely first auto-submission candidate once a polish run produces a strict improvement.

## What might still work / open

- Check #3 ("different method") is the weakest link for combinatorial problems with no analytical bound — for those, a higher-precision or structurally-distinct recomputation stands in. Tracked per-problem in Goal 2's registrations.
