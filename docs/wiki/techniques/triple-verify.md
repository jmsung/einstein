---
type: technique
author: agent
drafted: 2026-06-03
related_concepts: [float64-ceiling, arena-tolerance-drift, minimprovement-gate]
related_problems: [P2, P4, P5, P11, P14, P15, P16, P18, P19]
compute_profile: [local-cpu]
cost_estimate: "sub-second per problem (mpmath checks on small n; FFT on n≤1e5)"
hit_rate: "n/a — a gate, not an optimizer"
cites:
  - .claude/rules/triple-verify.md
  - .claude/rules/axioms.md
  - src/einstein/triple_verify/core.py
  - src/einstein/auto_submit.py
  - docs/wiki/findings/triple-verify-wiring-design.md
---

# Triple-verify — the per-problem 3-way score check (axiom A1, wired)

Every score that could feed an arena submission must agree across **three
different kinds of evidence** before it is trusted (axiom A1). The
`src/einstein/triple_verify/` package turns that rule into code: it produces a
real verdict that the auto-submit chain reads at gate 2.

## The three checks

1. **fast** — the arena evaluator (the optimization-loop scorer). Approximations OK.
2. **exact** — an independent reimplementation on a *different code path* (catches
   numerical bugs, off-by-one, sign errors). mpmath at high dps for
   float-precision-critical problems; a distinct algorithm for combinatorial ones.
3. **cross** — a *different kind* of evidence: higher precision, an analytical
   bound, or a structurally different method.

**Agreement rule (the disagreement protocol):** all three pairwise differences
must fall within the per-problem `Tolerance` (`max(abs_tol, rel_tol·max(|a|,|b|))`).
A single divergent pair fails the whole check — honest-zero over fake-pass. A
score of ±inf never agrees with itself (infeasibility is not a real number).

## Architecture — registry + dispatcher

```
 autonomous_loop._call_auto_submit(problem, payload)
        │
        ▼
 triple_verify.run_payload(problem_id, payload)      ← in-memory (loop holds the dict)
 triple_verify.run(problem_id, solution_path)        ← on-disk sibling (gz-aware)
        │
        ▼
 registry: dict[int, TripleVerifier]                 ← populated at import time by
        │   get_verifier(problem_id)                    triple_verify/problems/p*.py
        │
        ├─ None  ─────────────────►  TripleVerifyResult(passed=False, reason="not_registered")
        │                            (NEVER a silent pass)
        ▼
 verify(seed, verifier)
        │  run fast / exact / cross  (a raise → honest-zero passed=False)
        │  apply the agreement rule
        ▼
 TripleVerifyResult.as_dict()  →  {"passed", "fast", "exact", "cross", "note"}
        │
        ▼
 auto_submit.try_submit(... triple_verify=<that dict> ...)   ← gate 2 logic UNCHANGED
```

The result dict is *exactly* the shape gate 2 already consumed, so wiring this in
changed only the **source** of the verdict (hardcoded `{passed: False}` → real
check), not the gate logic itself.

## Per-problem checks (the 9 manifest-wired problems)

| P | score | fast | exact | cross |
|---|---|---|---|---|
| 2 / 4 | autoconv peak | `np.convolve` | `scipy.fftconvolve` | rfft power-spectrum |
| 5 | (max/min)² dist | numpy matrix | pure-python `math.hypot` | mpmath@60 |
| 11 | min sphere dist | numpy | pure-python `math.dist` | mpmath@50 |
| 14 / 18 | Σr | arena eval | pure-python feasibility + `fsum` | mpmath feasibility + `fsum` |
| 15 / 16 | min-area ratio | vectorized `fast_score` | scalar `arena_score` | mpmath (shoelace hull for P16) |
| 19 | k²/v | set diff-set | boolean-array diff-set | forward-membership |

P22 is a `stub_no_op` recon with no real solution — registered as *unavailable*
(`reason="stub_no_op_no_solution"`), so gate 2 hard-rejects it. The
registry-coverage test (`tests/test_triple_verify_registry.py`) asserts every
manifest problem has a registration, so dispatch can never outpace verification.

## When to use / extend

- Adding a problem to `optimizer_manifest.yaml` → add a
  `triple_verify/problems/p<NN>_*.py` with three genuinely-distinct checks, or
  an honest `unavailable_reason`. The coverage test will fail otherwise.
- Tolerances are pinned in `tests/<problem>/test_triple_verify.py` against the
  calibrated 3-way agreement on the real seed (observed ≤7e-15; autocorr ≤4e-16).

See also: [triple-verify-wiring-design](../findings/triple-verify-wiring-design.md),
[auto-submit-gate-chain-status](../findings/auto-submit-gate-chain-status.md),
[.claude/rules/triple-verify.md](../../../.claude/rules/triple-verify.md).
