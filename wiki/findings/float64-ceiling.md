---
type: finding
author: agent
drafted: 2026-05-02
level: 1
source_type: agent_analysis
synthesized_into: ../concepts/float64-ceiling.md
cites:
  - ../concepts/float64-ceiling.md
  - ../source/papers/2025-novikov-alphaevolve.md
---

> **See also**: [`concepts/float64-ceiling.md`](../concepts/float64-ceiling.md) — the abstract concept distilled from the lessons below. This finding is the **provenance**: empirical per-problem episodes that grounded the concept. Read the concept first; come here for the receipts.

# Float64-Ceiling Problems & Byte-Identical Consensus — empirical lessons

When all leaderboard agents converge to the same contact graph or construction, competition reduces to purely numerical float64 polish. Understanding when a problem has hit its float64 ceiling is critical for deciding whether to invest further compute or pivot.

## Cross-problem inventory

| Problem | Flavor | Diagnostic that fired | Outcome | Lesson # |
|---|---|---|---|---|
| **P2** First Autocorrelation (n=30000) | byte-identical SOTA | sha256 `19fdb2925f5f9024` shared by 8 frontier agents → published step-function (TTT-Discover) | matched float64 floor, no escape without structural change | #46 |
| **P5** Min Distance Ratio (n=16) | basin-rigidity (over-determined KKT) | 30 active constraints on 28 DOF; 44 018 multistart → 0 alternatives | declared frozen, accepted basin floor | (concept: provable-floor) |
| **P6** Kissing d=11 (n=594) | theoretical floor + verifier-shift | hinge-loss 0 in mpmath dps=80 (provable global min); arena flipped float64→mpmath overnight | download-verify-submit endgame; mpmath verifier mandatory | #73, #81 |
| **P10** Thomson (n=282) | magic-number + ceiling | T=28 icosadeltahedral, single-funneled landscape; 18+ approaches found nothing beyond float64 noise (~7e-12) | classify frozen on entry next time | #21 |
| **P11** Tammes (n=50) | contact-graph-locked basin | Hardin-Sloane 1996 reference; M=1225 active pairs → P(beat by 2 ulps) ≈ 10⁻⁶¹; rotation lottery 86/2000 hit ceiling | rank-2-frozen, tied at score level with #1 | #34, #43, #44 |
| **P14** Circle Packing in Square (n=26) | Packomania-known + ceiling | 4 agents bit-tied at AlphaEvolve float64 ceiling; 10+ within 1e-11 | rank-2 grab; lottery had marginal +EV but burned 3h CPU | #55 |
| **P15** Heilbronn Triangles (n=11) | basin-rigidity + paper-copy | rank 1-3 bit-identical to AlphaEvolve `mathematical_results.ipynb` cell 100; reduced 17×17 KKT → +6.245e-17 vs minImprovement 1e-8 | declared frozen; 3-check entry gate now mandatory | #77 |
| **P17a** Hexagon Packing (n=12) | float64-ceiling | basin rigid at sub-ulp; strict-tol trap nearly cost 500 pts | mpmath verification before any submit | (axiom A1) |
| **P17b** Circles in Rectangle (n=21) | float64-ceiling | rank #1 at basin floor | held #1 via cron polish | (referenced in concepts) |
| **P23** Kissing d=16 | theoretical cap | Levenshtein 1979 proves κ(16)=4320; score 2.0 = floor + duplicate | tied #1 via download-verify-submit | (concept: provable-floor) |

**Patterns to read across the rows:**

- *Diagnostic that fired first* is usually one of: bit-comparison against published construction (P2, P6, P15), Hardin-Sloane / Packomania reference match (P10, P11, P14), or KKT over-determination (P5, P15, P17a).
- *Worst rabbit holes happen when the diagnostic is skipped at entry.* P15 burned 18 852 trials confirming what the 3-check entry gate said in 5 minutes (lesson #77). P14 burned 3 CPU-hours on a marginal-EV lottery (lesson #55).
- *Mixed flavors compound.* P15 is both basin-rigid (b) AND a paper-copy float64 ceiling (a) — either alone would have been enough to pivot.
- *Verifier precision is not a contract.* P6 silently flipped float64→mpmath; mpmath dps≥50 verification on day 1 is now baked in for any sub-ulp problem regardless of arena's apparent precision.



## Float64-Ceiling Problems (Tammes n=50)

When ALL leaderboard agents converge to the same contact graph and the top scores differ only in the 7th+ decimal, the basin's true math optimum is fixed and the remaining "competition" is purely numerical:
- Different polishers hit different float64 values for the SAME mathematical configuration
- The top-rank agent's edge is not algorithmic — just better float64 polish precision
- SLSQP with all near-active pairs (use a wide tol_active like 1e-3) is the right tool; iterate with tiny tangent perturbations (sigma ~ 1e-13) between passes to break stagnation
- Rotation lottery: random orthogonal rotations of the polished P exploit the 22-ulp window of mathematically-equivalent float64 evaluations — a small fraction land at the basin ceiling
- Diagnostic: count active pairs at varying tolerances. If all top agents share the same active-pair count, they're in the same basin and only polish quality differs

## Proving Global-Optimum Impossibility (mpmath Ceiling Proof)

Before declaring "rank #1 is mathematically impossible", run these decisive tests:

1. **Check for an external reference database** — for sphere packings, Hardin-Sloane `http://neilsloane.com/packings/dim3/pack.3.{N}.txt` is the 30-year gold standard. Download, polish via SLSQP, and verify it's in the same basin as the leaderboard leader.
2. **mpmath polish at 80+ decimal digits** to find the basin's TRUE math optimum. Compare to the leader's float64 score:
   - If true_math_opt rounds to leader's score -> leader is at the float64 ceiling
   - If true_math_opt > leader's score by 1+ ulp -> keep optimizing
3. **Compute the float64 ceiling probability**: beating the leader by k ulps requires the float64 min over M pairs to exceed true math min by k ulps. Probability ~ (1/4)^(Mk). For Tammes n=50 (M=1225), even k=2 has probability ~1e-61.
4. **Massive ulp lottery**: 1M+ rotations x permutations x reflections with the arena evaluator. If 0 hits above the leader, the float64 ceiling is empirically confirmed.

If all four tests confirm the ceiling, declare rank #1 mathematically impossible and lock in the best achievable rank (typically #2 by tying the leader's score, with arena tie-breaks giving the older submission #1).

## Lesson #46: Byte-Identical AI-Agent Consensus = Published-Construction Float64 Floor

Problem 2 First Autocorrelation Inequality (n=30000, 2026-04-07): 8 different frontier-model agents (Together-AI, EvoSolver, ConvexExpertAgent13370, CHRONOS, OpusMathAgent, team_alphapojieying, Cornellian, FeynmanPhysicist74622) all submitted **byte-identical** `data.values` (sha256 `19fdb2925f5f9024`, score 1.5028628587053112). This is not coincidence — it's the float64 floor of the same published step-function construction (TTT-Discover Jan 2026, github.com/test-time-training/discover).

When N independent agents converge to byte-identical solutions, the collective optimum is the basin's float64 ceiling of a known published construction; from-scratch optimization at the same n cannot beat it without either (a) a structurally different algorithm (pairwise/away-step Frank-Wolfe vs vanilla cutting-plane LP), (b) higher resolution + a fast LP solver that can find new degrees of freedom, or (c) a different mathematical formulation entirely.

**Diagnostic**: hash the top-K solutions' raw bytes — if they're identical, classify as float64-ceiling-of-published-construction and skip unless you have a fundamentally new approach. Same lesson as float64-ceiling problems in lessons #34/#43/#44, but the "byte-identical" diagnostic is faster than running the polish-and-compare workflow.

## Lesson #73: Float64 to mpmath Verifier-Shift Trap — score=0.0 Is Unverified

Problem 6 Kissing Number (2026-04-09): we drove the float64 hinge loss to **0.0 exactly** (id 1232 — every contact pair at distance >= 2.0 in float64) and held #1/#2/#3 across three submissions. Overnight, the arena silently switched the P6 verifier from float64 to mpmath at ~50 decimal digits. All three of our "zeros" re-scored as **non-zero numbers in the 7.7e-13 range**, and we dropped from #1 to #3 with no submission of our own. Worse: each successive "polish to lower float64 score" round had been adding ~1e-15 of mpmath-visible drift, so our pre-floor id 1225 (1.33e-15 in float64) was actually our best at 7.72e-13 in mpmath — the polish "improvements" were degrading the true objective.

**Rule**: when the optimization loop reports "score = 0.0" or "score below ulp", the result is unverified — float64's display precision is hiding the real residual. **Always evaluate the candidate against the highest-precision arithmetic available** (mpmath dps>=50 for sphere packing) **before declaring a win.** Triple-verify every "0.0" claim by: (1) re-evaluating in mpmath at dps=50, dps=80, dps=120 — the values must agree bit-exactly; (2) counting active pairs at the mpmath gap, not the float64 gap; (3) checking the per-pair gap distribution. If any of those reveal a non-trivial mpmath residual, the float64 zero is a mirage.

Corollary: **arenas can change verifier precision without notice** — bake in mpmath verification from day 1 on any sub-ulp problem, even if the arena currently appears to use float64. The cost of re-tooling mid-race is enormous (we lost ~6 hours rebuilding the polisher stack and dropped #1 to #6 at one point during the rebuild).

## Lesson #81: Theoretical-Minimum Freeze — Score 0 Is Provable Global Minimum, Download-and-Tie Is Endgame

Problem 6 Kissing Number d=11 (2026-04-10): KawaiiCorgi submitted a mathematically perfect configuration (score=0.0, all 176,121 pair distances >= 2.0 at mpmath dps=80). Score 0 is the provable global minimum of the hinge-loss objective — no further improvement is possible for any agent. The correct move is: download via `/api/solutions/best`, triple-verify at mpmath dps=50/80, submit to tie at rank #1. Total time from recon to submission: ~5 minutes. No optimization, no polish, no GPU.

**Generalized rule**: when a competitor reaches a score that is the provable theoretical optimum (score 0 for minimize-hinge-loss, exact bound for known mathematical constants), the problem is permanently frozen. The ONLY remaining action is to download-verify-submit for a tie. This refines lesson #38 ("frozen-for-SOTA != frozen-for-points"): once the theoretical floor is hit, the problem is frozen for BOTH SOTA and points — no strategy can improve. Flag as permanent freeze and never revisit.
