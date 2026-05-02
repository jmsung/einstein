---
type: finding
author: agent
drafted: 2026-05-02
level: 1
source_type: agent_analysis
cites:
  - knowledge.yaml
---

# Equioscillation Traps & Larger-n Escape

Equioscillation traps occur when a solution is locked by many simultaneously-active constraints forming a balanced stress network. For discretized-function problems, increasing the resolution (larger n) can shatter these traps. For fixed-geometry problems, equioscillation is genuinely unbeatable.

## Lesson #34: Max-Min Triangle-Area Problems Are Equioscillation Traps

Problem 16 (Heilbronn Convex n=14): the SOTA is locked by 16-21 simultaneously-active triangles forming a balanced stress network. Random isotropic perturbation strictly DECREASES score (confirmed across 6 independent agents). LSE soft-min Adam, SLSQP epigraph polish, CMA-ES, null-space walks at the genuine slack dimensions, and ~5000 multistart trials all converge to <= SOTA.

The right diagnostic is **count active triples** (within 1e-12 of the min) — capybara's 20 active triples is structurally distinct from the 6-way AlphaEvolve tied group's 16-17. Distinct-basin solutions exist (we found one with 21 active triples) but they sit slightly BELOW capybara's float64 score. Treat any equioscillation maximin problem with 15+ active constraints as basin-locked from the start.

## Lesson #36: Hull Saturation Diagnostic for Heilbronn-Convex

All top n=14 solutions have **10 hull + 4 interior** structure, not 14 hull or 8 hull. This is structural, not accidental. When tackling a Heilbronn-convex problem at any n, check the SOTA's hull/interior split first — the right parameterization is `arc_length(hull) + interior_positions`, not `14 free points`.

SierpinskiAgent2083 confirmed this independently: concentric regular polygons cap at 0.02123, well below SOTA — the optimum REQUIRES asymmetric placement.

## Lesson #51: Larger-n Escape — Piecewise-Constant Equioscillation Basins Shattered by Re-Optimizing at Larger n

Problem 4 Third Autocorrelation (2026-04-08): 9 top agents (including 3 byte-identical at 1.4540379299619) were stuck at a piecewise-constant n=400 Chebyshev equioscillation basin (400/799 conv positions active — the textbook KKT fingerprint of "the optimum for THIS n"). Going to n=1600 via block-repeat + 1e-6 * sigma Gaussian noise + L-BFGS smooth-max (beta cascade 1e4 -> 1e10) immediately dropped the score by 4.7e-4, crossing `minImprovement = 1e-4` on the FIRST bigger n. Cascading through n in {3200, 6400, 12800, 25600, 51200, 100000} kept adding improvements (each ~halving the previous gain) until hitting the continuous limit at ~1.4525212, a **total delta of 1.52e-3 — 15x minImprovement**. JSAgent jumped from off-leaderboard to #1, pushing the tied trio to #2/#3/#4.

**The key insight**: block-repeat PRESERVES the score exactly (piecewise-constant upsampling), so simple upsampling does nothing — the unlock comes from the *perturbation* that breaks the piecewise-constant constraint and lets gradient descent find new basin structure at the finer resolution.

**Generalized rule**: for any discretized-function problem where top agents cluster at a single n with high active-constraint count (active >= ~n -> Chebyshev equioscillation), test n in {4n, 16n, 64n} with block-repeat + noise + L-BFGS before labeling "frozen at theoretical bound". The smooth-max loss is `LSE_beta(f*f * dx) / (sum(f) * dx)^2` with beta cascaded 1e4 -> 1e10; FFT conv via `torch.fft.rfft/irfft` makes n=100k tractable on CPU in ~5 min. Triple-verify with `np.convolve` + `scipy.fftconvolve` + manual loop before submission.

This refines lesson #11 ("different resolutions give different basins") with a concrete mechanism and a universal warm-start recipe for equioscillation traps. **Contrast with lesson #49**: P15 Heilbronn Triangles *is* truly frozen (over-determined KKT basin, no DoF slack); P4 looked the same on the surface but the DoF-to-active-constraint ratio was actually slack-rich at larger n.

## Lesson #52: "Frozen — 3-Way Tie at Theoretical Bound" Labels Must Be Tested, Not Trusted

The MB problem-evaluation for P4 said "Frozen. 3-way tie at likely theoretical bound." The tie was REAL (byte-identical n=400 piecewise-constant basin floor) but the "theoretical bound" framing was wrong — it was the n=400 discretization bound, not the continuous bound. From recon to #1 submission took ~1 hour.

**New rule**: any "Frozen" label on a downloadable-solution problem where top agents all use the same n must be stress-tested with the larger-n escape recipe (lesson #51) before writing it off. The 15-minute test:
1. Download SOTA via `/api/solutions/best`
2. Count active conv positions — if >= n/2, it's likely equioscillation-locked at THIS n
3. Upsample via block-repeat to 4n with tiny noise
4. Run L-BFGS smooth-max beta in {1e4, 1e5, 1e6}
5. If score drops by more than one tenth of `minImprovement`, escalate to full n cascade

Only after this test fails can "frozen" be confirmed.

**Scope**: applies to any problem whose solution is a discretized function (autocorrelation inequalities, Erdos overlap, flat polynomials with variable n) — NOT to fixed-dimensional geometric problems like Heilbronn Triangles where n is the count of points in a fixed region (lesson #49 still applies there).

## Lesson #94: Larger-n Escape Requires Parameterization Change When exp(v) Peak-Locks

Problem 2 First Autocorrelation (2026-04-15): lesson #51's larger-n escape recipe worked on P4 (exp(v) + beta cascade), but on P2 the same recipe peak-locked at delta~5.25e-8 regardless of n (30k to 300k). The unlock was **changing parameterization from f=exp(v) to f=v^2** (lesson #93), which escapes peak-locking by allowing exact zeros and changing gradient geometry. Combined with ultra-low-beta exploration at n=90000 (3x block-repeat sweet spot), achieved delta=1.23e-6 (#1).

**Refinement to lesson #51**: the larger-n escape has TWO independent levers: (1) increase n (more DOF), and (2) change parameterization (different landscape). If increasing n alone doesn't break through, the bottleneck is the parameterization, not the resolution. Test {exp(v), v^2, max(v,0)} at the best n before concluding the problem is frozen.

## Lesson #49: Heilbronn-Style Over-Determined KKT Basins Are Unbeatable When `minImprovement >> ulp Headroom`

Problem 15 Heilbronn Triangles n=11 (2026-04-08): the arena SOTA 0.036529889880030156 is the bit-exact AlphaEvolve Figure 26 construction from arXiv:2511.02864 section 6.48 (four arena agents tied at the same float64 value or 1 ulp below under a D3 isometry). Structural diagnostics from a 30-second scrape already tell the full story — **if you see >= k * (shape DoF) active triples at float64 equality, stop**.

For P15: 17 active triples, 8 effective shape DoF after D1 symmetry and boundary incidences -> over-determined by ~1 constraint -> SierpinskiAgent2083's first-order LP on the 17 tight triples returned `delta_min = 0` (no feasible ascent direction exists), CHRONOS's KKT Obstruction Theorem classifies it as a rigid local max. mpmath 60-digit Newton on the reduced 17x17 system confirmed the basin's true-math ceiling is +6.245e-17 above the float64 score — 1.6e8 times smaller than `minImprovement = 1e-8`.

Our total search effort: **18,852 trials** across multistart (6740, 12 init strategies), CMA-ES (1612), and basin-hopping (10,500, 8 hop types including teleport_1/2/3, boundary_swap, large_perturb) — **zero improvements over the CHRONOS basin, and every cold-start strategy capped 9%+ below SOTA**.

This refines lesson #10 ("check minImprovement feasibility first"): when the gap between local headroom and `minImprovement` exceeds ~5 orders of magnitude AND 3+ agents sit on byte-identical SOTA, the problem is frozen — declare it and pivot without running long searches.

The 30-second diagnostic is:
1. Arena_score parity against the top-1 downloaded solution
2. Count active triples / pairs at rel_tol 1e-9
3. Count effective DoF after symmetry and boundary constraints
4. If active > DoF + 0, basin is KKT-locked and further local search is wasted compute

Do NOT submit: matching = rank #(tied_count + 1) = 0 pts under 4/2/1 medal scoring.

**Contrast with lesson #51**: not every byte-identical tie is a true bound — P4's was the discretization bound, not the continuous one. The differentiator is the DoF vs active-constraint ratio: P15 is over-determined at fixed n, so larger n still hits the same KKT trap (2D geometric points in a fixed region); P4's discretization is itself the DoF, so increasing n opens new structure.
