---
type: finding
author: agent
drafted: 2026-05-02
level: 1
source_type: agent_analysis
cites:
  - reference/2025-novikov-alphaevolve.md
  - knowledge.yaml
---

# Frozen Problem Triage & Entry Gates

Decision frameworks for determining when a problem is frozen (no further improvement possible) and when to stop investing compute. Includes the 3-check entry gate, stopping conditions, and EV calculus for lottery-vs-fallback decisions.

## Lesson #9: Some Problems Are Mathematically Frozen

Problem 1 (Erdos overlap) has a minImprovement of 1e-6 but the best local improvement from SOTA is 1e-10. The leaderboard is effectively frozen. No amount of compute helps — a new mathematical approach is needed. Check arena discussions before investing time.

## Lesson #10: Check minImprovement Feasibility First

Before optimizing, check if the gap between SOTA and what local refinement can achieve is larger than minImprovement. If not, the problem is frozen for local methods.

## Lesson #21: Magic-Number Configurations Are Frozen — Skip Immediately

Problem 10 (Thomson n=282): n=282 is an icosadeltahedral magic number (T=28, chiral icosahedral symmetry I) with a single-funneled energy landscape. The putative global minimum has stood 20+ years in the Wales Cambridge database. 18+ optimization approaches including GPU A100 massive search (2000 hops, 112 restarts) found zero improvement beyond float64 noise (7e-12). When a problem instance sits at a known magic number, classify as frozen immediately and move on.

## Lesson #55: Lottery-vs-Rank-2-Fallback EV Calculus

Problem 14 Circle Packing in a Square (n=26, 2026-04-08): the leaderboard shows 4 agents at the AE float64 ceiling and 10+ in the same basin within 1e-11. Branch chose a "lottery bet" — 10-approach breadth search for a novel basin (~5% prior, +3 pts on success), with rank-#2 fallback (~95% probability after the breadth confirms ceiling, +2 pts). Expected value = 0.05 * 3 + 0.95 * 2 = 2.05 pts, vs 2.0 pts for skipping the lottery and going straight to fallback. The lottery had marginal positive EV but burned ~3 hours of CPU and produced zero novel basins.

**Decision rule** for "should I run the lottery?":

- **Skip lottery (go straight to rank-2 grab)** when: (a) the basin is a known canonical/published mathematical optimum (Packomania, Hardin-Sloane, AE-published with bit-tied agents), AND (b) the basin's float64 ceiling is locked (see lessons #34, #43, #44, #46), AND (c) the n is small/fixed (no resolution-escape via lesson #51), AND (d) the contact graph is over-determined (see lesson #49).
- **Run lottery (full breadth search)** when: (a) the SOTA is recent and not yet well-replicated across agents, OR (b) the problem has structural slack (DoF > active constraints), OR (c) the SOTA is at a non-canonical n (try larger-n escape, lesson #51), OR (d) there is reason to believe an alternative topology exists (e.g., pocket swaps, asymmetric basins).
- **Hybrid (run a 30-min smoke test only)** when uncertain: try the cheapest 2-3 approaches (multistart + topology-mutate + warm-start polish), then commit to either the lottery or the fallback.

For P14 n=26, all four "skip" criteria held — the optimal play would have been to skip the lottery entirely and go straight to the rank-2 grab in ~5 minutes. Lesson cost: ~3 hours of CPU. The reusable side benefit was a library of 10 packing-search scripts now available for future packing problems where the lottery DOES make sense.

## Lesson #60: Stopping Condition "10+ Approaches Exhausted" Applied in Practice — P2 Closeout

The CLAUDE.md protocol says "Only stop when ... 10+ distinct approaches exhausted with zero improvement". P2 hit 19 distinct approaches across Phase A (16) + Phase B (B1 KM LP, B2 Sidon warmstart, B3 Fourier L-BFGS + scipy.linprog rerun) and was closed out with no submission.

Decision signals that correctly triggered closeout: (a) all 3 council-recommended untried approaches independently failed for different reasons (solver scaling, wrong basin, wrong DoF), (b) the only remaining theoretical avenue (full Fejer-Riesz SDP) is O(n^2) variables and infeasible beyond n ~ 200 where resolution ceiling is already above SOTA, (c) commercial SDP/QP solver + multi-day dev = uncertain payoff vs +0 team points if tied in the 8-wide cluster.

**Rule**: when the ONLY remaining approaches require either (i) commercial solvers that aren't in the stack or (ii) multi-day dev with uncertain payoff, and the team is already in a comfortable lead, close out. Don't chase tail approaches on a problem the team doesn't need.

**Contrast with P4** (lesson #51/52): P4 was closed to closeout after 9 agents tied, but a 15-minute larger-n escape test would have found a 1.52e-3 improvement. P2 passed the larger-n test (Phase A's exp(v) cascade already reached n=90000 with delta=-6.54e-8, below the 1e-7 gate) — so closeout here is not premature, it's the residue of a genuinely locked problem.

## Lesson #70: Session Saturation Signal — 8+ Structurally Distinct Zero-Gain Attempts Means Pivot

Problem 13 Edges vs Triangles (2026-04-09): after the bounded-L-BFGS + boundary-snap + BH-chain pipeline reached -0.71170918806610, **9 consecutive distinct exploration scripts** (push_l multistart, push_m scipy L-BFGS-B, push_n scallop-transfer, push_o Euler-Lagrange optimality sweep, push_p snap-BH chain rerun, push_q Snell refraction, push_r cusp-cross, push_s BIPOP-CMA-ES, push_t Council 5 left-cluster hypothesis) **all produced zero improvement**. Each was a structurally distinct attempt (different local minimizer, different perturbation, different hypothesis), not parameter sweeps of the same script.

**Rule**: when 8+ structurally distinct attempts in the same session yield zero gain, the basin is the session attractor and further work in the same parameterization is wasted compute. The right next move is one of: (a) a qualitatively different parameterization (e.g., drop the per-row Turan assumption and search free 20-simplex rows), (b) a precision-level escalation (GPU float64 polish), (c) a larger-n cascade analogous to lesson #51 (block-repeat the discretization to break piecewise-constant artifacts). Continuing to spam more "different" scripts at the same parameterization does nothing.

**Diagnostic**: count the number of attempts since the last improvement — if `attempts_since_last_gain >= 8` AND each attempt was structurally distinct (not just a re-seed), declare saturation, write a parked-branch resumption note listing what was tried, and pivot.

**Distinct from lesson #29** ("12+ approaches with <2% of target -> pivot") which is about cross-session basin-locking; this lesson is about within-session attractor recognition and prevents wasting hours on the diminishing tail of the same parameterization.

## Lesson #95: 111+ Multi-Paradigm Experiments Across 22 Sessions = Definitive Stopping Condition for Discretized-Function Problems

Problem 1 Erdos Minimum Overlap (2026-04-17): across 22 autonomous sessions, 111+ structurally distinct experiments spanning every known optimization paradigm (gradient: Adam/L-BFGS/subgradient/torch autograd; combinatorial: mass transport/basin hopping/SA/DE/CEM; convex relaxation: SDP/SLP/SOCP; parametric: Fourier/B-spline/sigmoid/piecewise; constructive: Legendre/Haar/spectral/equioscillation) plus additional methods (nullspace perturbation search, different-n interpolation, large-neighborhood search, Cross-Entropy Method) all converge on the same verdict: the SOTA sits at a Remez-optimal equioscillation point where max local improvement is ~1e-10, vs minImprovement=1e-6 (ratio 1:10,000).

Key findings across sessions 4-15 (the diminishing-returns tail):
- **SDP relaxation**: Shor lifting at n=30-80 gives bounds 0.93-0.97 vs true optimum 0.38 — factor 2.5x too loose. Useless for any bilinear minimax problem where the quadratic relaxation is inherently non-tight.
- **Subgradient/bundle methods**: converge to same 1e-10 plateau as mass transport — non-smooth methods offer no advantage over smooth here.
- **Torch autograd**: sigmoid/direct/Fourier parameterizations all fail due to normalization sensitivity (values pushed outside [0,1], returning inf).
- **SLP confirms Remez optimality**: zero descent direction from SOTA, perturbed SOTA, and Fourier-constructed starts.
- **N-sweep 27 values (100-1200)**: SOTA only feasible at n=600; resampling to any other n produces infeasible solutions (normalization constraint violation).
- **Batch PyTorch Adam 64 diverse starts**: best 0.38089 (gap 1.7e-5); even diverse cold starts can't find a better basin.
- **Basin hopping**: 50+ random starts + population search — no undiscovered basins.
- **Three-way local-optimality proof**: (1) PyTorch LBFGS float64 zero gradient, (2) CMA-ES sigma collapse to 1e-15, (3) Remez exchange zero iterations at 437 active shifts.
- **Nullspace perturbation**: 50K zero-sum random perturbation trials — 0 improvements (sessions 11+).
- **Cross-Entropy Method**: 200 pop, 100 gens, two sigma scales — 0 improvements from SOTA.
- **Different-n interpolation**: 12 resolutions from n=300-1200 via cubic spline — all worse, n=600 uniquely optimal.
- **Arena community**: 20 discussion threads, 80+ replies, 8+ independent agents all confirm same plateau.

**Stopping rule**: when a discretized-function problem has been attacked by 60+ experiments covering all 5 paradigm families (gradient, combinatorial, relaxation, parametric, constructive), AND the best local improvement is 4+ orders of magnitude below minImprovement, AND the Remez exchange algorithm reports zero exchanges needed (equioscillation optimality), permanently close the problem. Further compute is wasted — the gap is a mathematical open question, not an optimization question. This refines lesson #70 (session saturation at 8+ attempts) into a cross-session definitive stopping condition: 60+ across 5 paradigms is the exhaustive closure standard. **Update (session 22, FINAL)**: sessions 5-22 added 50+ more experiments (including coord descent with exact 1D minimax, Hessian eigenspace exploration, Frank-Wolfe, random subspace search, and 4 recon-only sessions) yielding zero new insights beyond confirming the three-way optimality proof. Diminishing returns set in hard after session 4 (~60 experiments). **Auto-solve retry cap**: 4 sessions is sufficient for any problem that hits the three-way optimality proof (zero gradient + CMA collapse + Remez equioscillation). Sessions 5-22 on P1 were wasted compute — the verdict was clear at session 4.

## Lesson #77: Problem-Entry Gate — 3-Check Tie-and-Paper Test

Problem 15 Heilbronn Triangles n=11 closeout (2026-04-09): the entire branch confirmed what a 3-check, ~5-minute entry-gate diagnostic could have told us before launching 18,852 trials. The three checks, in order:

### Check 1: Tie-Multiplicity Gate

After scraping `/api/solutions/best?problem_id=N&limit=20`, count how many distinct agents are bit-tied (or within 1 ulp) at the top float64 score. If `K_tied >= N_medal_slots` (N=3 for 3/2/1 scoring, N=4 for 4/2/1 scoring), matching the SOTA gives rank #(K_tied + 1) = 0 pts.

**Decision**: do NOT optimize unless you have a concrete plan to strictly beat SOTA by `>= minImprovement`. Matching a crowded top is worth zero under every arena scoring scheme. For P15: K_tied=4 at 0.036529889880030156, N=4 under 4/2/1 medal scoring -> matching = rank #5 = 0 pts. Known before any optimization started, but the branch kept going anyway and burned ~18k trials confirming what the gate said upfront.

### Check 2: Paper-Copy Detection

Compute sha256 or bit-compare the SOTA `data` field against every published AI-discovered construction for the problem (AlphaEvolve results repo, AlphaEvolve repository of problems, OpenAI/DeepMind math repos, arXiv preprints). If it matches bit-for-bit, the incumbent is a copy-paste from the paper — not an optimization result — and local polish has zero headroom because the paper's authors already polished to the float64 ceiling of their own construction.

For P15: CHRONOS/AlphaEvolve/Euclid's rank 1-3 entries are bit-identical to `alphaevolve_results/mathematical_results.ipynb` cell 100 (B.9) from `google-deepmind/alphaevolve_results`, i.e. arXiv:2511.02864 section 6.48 Figure 26. This is detectable in 10 seconds with a diff against the public notebook.

### Check 3: mpmath-Ceiling Quick Check

If the first two gates say "don't bother", but you still want to verify the basin is at the float64 ceiling before closing the problem out, run a ~60-digit mpmath Newton on the reduced KKT system (only the active constraints + Lagrange multipliers, not the full epigraph). The reduced system size for a geometry problem is `(shape DoF) + 1` variables, so <= 20 for most small-n problems, which converges in 2-3 Newton iterations at dps=60. Compare the true-math score to the float64 SOTA: if `delta < minImprovement / 1e6`, the basin is at the float64 ceiling and polish-based improvement is mathematically impossible — pivot.

For P15: reduced 17x17 system, converged in 2 iters, delta = +6.245e-17 vs `minImprovement = 1e-8` -> ratio of 1.6e8, impossible.

### Composite Rule

The three checks gate a hard-no-submit + hard-no-compute verdict. Run them BEFORE any multistart / CMA-ES / basin-hopping. Each check is cheap: ~10s for tie scrape, ~30s for paper diff, ~2min for mpmath Newton. If all three fire together (K_tied >= N_slots AND SOTA is paper-copy AND mpmath headroom < minImprovement / 1e6), declare frozen and close the branch without further work. Refines lesson #49 with a concrete entry-gate recipe; refines lesson #34 ("equioscillation traps") by converting it into a 5-minute decision gate rather than a post-hoc diagnosis after exhausting search.
