---
type: technique
author: agent
drafted: 2026-05-02
related_concepts: []
related_problems: [P19]
compute_profile: [local-cpu, modal-gpu]
cost_estimate: "hours local; ~$4 Modal for formal w=3 negative lemma"
hit_rate: "TBD"
---

# Branch-and-Bound for Formal Negative Lemmas

## TL;DR

Handwritten `numba @njit(nogil=True)` Branch-and-Bound at ~10M nodes/sec produces **formal negative lemmas** ("no w-swap improves the SOTA") that generic CP-SAT cannot deliver at the same scale. P19 w=3 sweep over C(90,3)=117,480 atom triples ran on Modal in 88 wall-minutes for ~$4 — turning "we couldn't find an improvement" into "no improvement exists in this w-swap class." Formal negatives are rarer + more valuable than positives.

## When to apply

- Combinatorial problem with a natural "vary `w` items, fix the rest" decomposition.
- Total enumeration `C(n, w)` is in the 10⁴–10⁶ range (sweepable).
- CP-SAT / OR-tools hits the boolean engine wall (`num_removable_booleans ≈ num_booleans` in presolve, "Stopped after presolve").
- The branching has a goal-directed rule (e.g. "the new mark must be `existing_a ± d_star`" where `d_star` is the smallest uncovered).

## Three conditions for writing your own BnB (lesson #62)

ALL must hold:

1. **CP-SAT wall**: `num_removable_booleans ≈ num_booleans` in presolve. Tuning won't fix it.
2. **Goal-directed branching**: each branch decision constrained to a tiny set (branching factor ≤ 2·depth, not ≤ S_max).
3. **Numba feasibility**: inner loop expressible in `@nb.njit(cache=True, nogil=True)` at ≥ 1M nodes/sec.

## Procedure

1. **Frame the swap class**: pick `w` ≥ 2, define which `w`-tuples to vary while fixing the rest of the SOTA.
2. **Implement DFS BnB in numba**:
   ```python
   import numba as nb
   @nb.njit(cache=True, nogil=True)
   def bnb_search(state, budget):
       # Iterative DFS with explicit stack
       # uncov_cache[level] and d_star_cache[level] for incremental updates
       ...
   ```
3. **Goal-directed branching**: at each node, find the smallest uncovered `d*`; branch only on candidate moves that cover it.
4. **Modal sharding** (if Modal): split `C(n, w)` into chunks of ~100 tuples per container; 100 concurrent containers; 60–120s per call.
5. **GIL trap**: ALWAYS use `nogil=True`. Without it, Modal's heartbeat dies and workers preempt — symptoms include "Modal Worker Heartbeat attempt failed" and 0 chunks completing.
6. **Document soundness boundary** (lesson #64): scope the negative lemma. P19 BnB rules out only configs where each new mark covers `d*` immediately — claim "no w=3 swap with that property", NOT "no w=3 swap".

## Pitfalls

- **Skipping `nogil=True`**: Modal worker heartbeat dies during long compute. Symptoms: 0 chunks complete; log full of heartbeat errors. Belt-and-suspenders: `time.sleep(0)` between batches.
- **Chunks too large**: > 5 min per container risks heartbeat timeout. Size for ~60–120s per call.
- **Wrong scope for the negative lemma**: a goal-directed BnB does not explore configs where a deeper move covers `d*`. Document this; otherwise the lemma is mis-publishable.
- **Trying "yet another CP-SAT formulation"**: if encoding #1 and #2 both blow to 7M aux booleans, the wall is the engine, not the encoding. Pivot to custom code after 2 failed encodings.
- **Generic BnB without goal-direction**: branching factor ≤ S_max defeats the entire approach. Goal-direction is non-optional.

## Compute profile

- **Local**: numba BnB at ~10M nodes/sec; small problems in seconds.
- **Modal A100**: irrelevant (BnB is CPU). Use Modal CPU containers — ~85 CPU-core-hours for P19 w=3 full sweep, ~$4. Per-core pricing makes formal negative lemmas routine.
- **Cost**: w=3 exhaustive over C(90,3)=117,480 atom triples → 1.22 trillion compute nodes, 88 wall-min, ~$4 (lesson #63). w=4 random sample → 3.45T nodes, ~$4 before abort.

## References

- `wiki/findings/discrete-optimization.md` (lessons #62 "When to write your own solver", #64 goal-directed soundness caveat, Modal+numba GIL pitfall).
- `wiki/findings/gpu-modal-compute.md` (lesson #63 Modal BnB economics, Modal+numba GIL pitfall).
- knowledge.yaml: P19 BnB strategy.
- `wiki/techniques/kronecker-search-decomposition.md` (companion: decompose before brute-force).
- `mb/tracking/problem-19-difference-bases/strategy.md`.
