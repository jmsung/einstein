# Uncertainty Principle Push — Optimization Trajectory

## Session: 2026-04-18

### Goal
Push P9 Uncertainty Principle (Upper Bound) score as low as possible.
Target: 0.001 → 0.0001.

### Starting State
- Arena #1: alpha_omega_agents at 0.2688 (k=19, grid-based roots)
- Our previous best: JSAgent at 0.3182 (k=14, rank #11)
- minImprovement: 1e-05

### Key Discovery: poly_eval evaluator
The grid-based `fast_evaluate` was broken for k≥19 (spurious sign changes at high x).
Built `poly_eval.py`: mpmath polynomial construction + numpy.roots companion matrix.
- ~0.3s at k=19, ~2s at k=28, ~8s at k=50, ~13s at k=60
- Verified to match hybrid evaluator to ~1e-12

### Optimization Trajectory

| Time  | k  | Score       | Method | Notes |
|-------|---:|-------------|--------|-------|
| 00:04 | 19 | 0.11775     | CMA-ES 200 evals from alpha_omega grid | First CMA run — 2x improvement |
| 00:15 | 19 | 0.02715     | CMA-ES 2000 evals | 10x improvement over arena #1 |
| 00:27 | 20 | 0.02670     | CMA-ES from grid insert | |
| 00:47 | 23 | 0.01986     | CMA-ES 3000 evals from grid insert chain | First sub-0.02 |
| 01:20 | 20 | 0.02588     | CMA-ES round 3 | |
| 01:21 | 21 | 0.02593     | CMA-ES 2 rounds | |
| 02:21 | 30 | 0.01989     | CMA-ES from k=19→k=30 buildup | |
| 02:58 | 25 | 0.01909     | CMA-ES 3000 evals from k=23 insert | |
| 03:11 | 26 | 0.01916     | Aggressive climb CMA | |
| 03:36 | 27 | 0.01855     | Aggressive climb CMA | |
| 04:04 | 28 | 0.01746     | Aggressive climb CMA | |
| 04:35 | 29 | 0.01669     | Aggressive climb CMA | |
| 04:30 | 50 | 0.00131     | CMA-ES 732 evals from Laguerre zeros | **BREAKTHROUGH: sub-0.002** |
| 05:09 | 30 | 0.01590     | Aggressive climb CMA | |
| 05:44 | 31 | 0.01705     | Aggressive climb CMA (regression) | |
| 05:57 | 25 | 0.01873     | NM+LBFGSB 5-round polish | |
| 09:25 | 50 | 0.00131     | Verified final | **Global best** |

### Key Insights
1. **alpha_omega's grid roots leave massive room for CMA-ES** — their k=19 at 0.269 became 0.027 with CMA
2. **Higher k = lower scores** — k=50 reached 0.00131 vs k=30's 0.01590
3. **Laguerre polynomial zeros are excellent starting points** — well-spaced, finite scores at all k
4. **CMA-ES needs 500+ evals at high k to find good basins** — k=50 found 0.0197 at eval 224 but 0.00131 at eval 732
5. **Incremental climb (insert + CMA) gives steady improvement** but direct high-k is faster for breakthroughs
6. **Verification critical at high k** — k=40 CMA score didn't match verified score

### Active Optimization Processes
- k=50 deep polish (CMA + NM + CMA from 0.00131)
- k=60 CMA from Laguerre zeros (at 0.033, still dropping)
- k=70 CMA from Laguerre zeros (just started)
- Aggressive climb (at k=37)
- LBFGSB climb (at k=28)

### Files
- `src/einstein/uncertainty/poly_eval.py` — fast correct evaluator
- `scripts/uncertainty/optimize_poly.py` — CMA-ES optimizer
- `scripts/uncertainty/aggressive_climb.py` — incremental k-climbing with CMA
- `scripts/uncertainty/fast_climb.py` — k-climbing with L-BFGS-B
- `results/up_k*.json` — all saved solutions (gitignored)

### Solution Archive (best per k)
Results are in `results/` (gitignored). Key solutions:
- `up_k50_0.0013095237.json` — global best, k=50, verified
- `up_k30_0.0159033727.json` — best from incremental climb
- `up_k25_0.0187313400.json` — best polished k=25
- `up_k23_0.0198566208.json` — first sub-0.02 solution
