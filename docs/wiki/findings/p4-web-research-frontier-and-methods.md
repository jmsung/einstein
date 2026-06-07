---
type: finding
author: agent
drafted: 2026-06-06
question_origin: problem-4
status: answered
related_concepts: [autocorrelation-inequality, equioscillation, lp-duality]
related_problems: [2, 4]
cites:
  - ../problems/4-third-autocorrelation.md
  - ../findings/p4-basin-is-discrete-sign-topology.md
  - https://arxiv.org/abs/2511.02864
  - https://arxiv.org/abs/0907.1379
  - https://github.com/google-deepmind/alphaevolve_repository_of_problems
  - https://ar5iv.labs.arxiv.org/html/1205.0626
---

# P4 web frontier: no published value < 1.4523; method families + untried leads

## Question
After ~15 local/construction methods capped at ~1.4525, what does the external
literature/web offer to beat the arena leader 1.4523043332 (signed autoconvolution
min, Tao Problem 6.4b)?

## Answer (deep web research, 2026-06-06)
- **No published value below 1.4523 exists anywhere.** Chain: Matolcsi–Vinuesa
  1.45810 (n=150 signed step fn, arXiv:0907.1379) → AlphaEvolve 1.4557 (a "quick
  experiment", arXiv:2511.02864 line 1006) → arena 1.4523 (OrganonAgent, **method
  unpublished** — arena threads aren't crawlable). So the arena frontier is ahead
  of the literature; our wall IS the public frontier.
- **No closed-form/proven extremizer.** Tao: "the irregular nature of the
  extremizers is one reason this optimization is difficult by traditional means."
  Damek Davis's meta-analysis [88] tried many optimizers and could NOT beat
  AlphaEvolve (specific optimizers not public).
- **Evaluator caveat:** ThetaEvolve (arXiv:2511.23473) reports AlphaEvolve's
  ThirdAutoCorr evaluator had typos. Our evaluator was triple-verified byte-exact
  vs downloaded arena solutions, so this is not our issue, but worth knowing.

## Method families (record-producing) + adaptable code
1. **Two-sided signed LP–Frank–Wolfe** (the MV/AlphaEvolve method): maximise Σg
   s.t. −M ≤ (f★g) ≤ M (g signed), FW line-search, scale by grid-refinement.
   Code: `github.com/google-deepmind/alphaevolve_repository_of_problems`
   (`autocorrelation_problems.ipynb`: `solve_convolution_lp`,
   `get_good_direction_to_move_into`; for variant b use `max(abs(conv))` and drop
   the nonneg clamp). Our earlier LP was ONE-SIDED — the two-sided polytope is a
   different active-set geometry. Implemented: `scripts/.../two_sided_lp_fw.py`.
   LP cost ~n³ → moderate-n only; lift the best basin to 100k via escape.
2. **Tabu self-avoiding-walk steepest descent** (LABS / merit-factor SOTA,
   `lssOrel`/`lssMAts`; survey arXiv:1205.0626, arXiv:2409.07222): the proven
   algorithm class for fragmented ±1 incompressible optima — DISTINCT from our
   random SA and crossover. Flip the single cell that most reduces C, tabu recent
   flips, self-avoiding-walk restarts, re-polish heights between flips. The
   obstacle is scale: incremental all-flip steepest descent is O(n²)/step, so it
   is moderate-n only; the better P4 basins live at high n.
3. **Construct-don't-search (complementary slackness):** at the optimum the
   autoconvolution is pinned at ±M on an active set; parameterise WHICH lags are
   pinned ±M and solve for f. The one "construct" door not yet tried.
- **Other repos:** `github.com/ajaech/autocorrelation_inequality` (~2000-elt
  optimized vector), `github.com/zkli-math/autoconvolutionHolder` (Boyer–Li
  two-phase SA→gradient + 5× grid-refinement — for the *non-negative* sibling, but
  the refinement scaffold transfers).

## What this rules out / implies
- Searching the web for a ready-made sub-1.4523 recipe is exhausted — none exists.
- The leader/record are at or beyond the published frontier; reaching them needs
  either the specific seed or dedicated compute in the LP-FW + tabu-SAW +
  grid-refinement family (all of which our experiments suggest cap ~1.4525 at the
  scales we can run).

## Next concrete moves (ranked)
1. Two-sided signed LP-FW + grid-refinement, lift best basin to 100k (running).
2. Tabu-SAW steepest descent at moderate n (LABS SOTA), lift best.
3. Active-set/complementary-slackness construction.
4. The seed (sure path).
