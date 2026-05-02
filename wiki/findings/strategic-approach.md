---
type: finding
author: agent
drafted: 2026-05-02
level: 1
source_type: agent_analysis
cites:
  - knowledge.yaml
  - reference/2025-jaech-autoconvolution.md
  - reference/2025-novikov-alphaevolve.md
  - reference/2022-fawzi-alphatensor.md
  - reference/2023-romera-paredes-funsearch.md
  - reference/2025-ellenberg-generative-math.md
  - reference/2025-georgiev-math-exploration.md
---

# Strategic Approach — First Principles

## Strategic #1: Literature first, code second {#strategic-1}

Reading papers saves weeks. For Problem 3, 6 papers gave us 5 ready-made algorithms. Always search arXiv before writing an optimizer. The time investment in literature review is small compared to the time wasted reimplementing known-inferior approaches or missing known-superior ones.

## Strategic #2: Breadth before depth {#strategic-2}

Test 5+ approaches quickly (1 hr each) before committing GPU hours to one. Problem 3: 11 quick experiments revealed Adam peak-flatten was the only viable path. The key discipline is time-boxing: if an approach hasn't shown signal in 1 hour, it won't show signal in 10. This prevents the common failure mode of sinking days into a single approach that looked promising but leads nowhere.

## Strategic #5: Resolution/parameterization sensitivity {#strategic-5}

The objective landscape changes with problem size. n is a hyperparameter. Problem 3: n=100k and n=200k have DIFFERENT basins — the optimizer converges to structurally distinct solutions at different resolutions. Always test multiple sizes before committing to one. The basin structure is not invariant under rescaling, and the optimal n may not be the largest feasible n.

## Strategic #7: Don't parallelize on limited hardware {#strategic-7}

Sequential deep runs beat parallel shallow ones on M4. With limited CPU/GPU cores, parallelism fragments the compute budget across runs that each individually lack the depth to find good basins. A single deep run with many iterations explores the basin more thoroughly than four shallow runs that each terminate before convergence. This reverses on cloud hardware with many cores (see Modal lessons), but on local M4 hardware, sequential is the right default.

## Strategic #8: GPU float64 essential for polishing {#strategic-8}

Float32 (MPS) can't refine solutions near SOTA. The precision gap between float32 (~7 decimal digits) and float64 (~15 decimal digits) means that once the solution is within ~1e-7 of the optimum, float32 gradients become pure noise. Use Modal/cloud CUDA for the final push — the cost is small relative to the compute already invested in reaching near-SOTA.

## Strategic #11: Different resolutions give different basins {#strategic-11}

For discretized function problems, n is a hyperparameter. Problem 1 SOTA uses n=600; higher/lower n both give worse scores. The basin landscape is resolution-dependent: different n values expose different local optima, and the globally best score across all n may not be at the largest feasible n. Always test multiple n values (at least n, 2n, 4n, and n/2) before committing.

## Strategic #12: Read arena discussions BEFORE coding {#strategic-12}

Other agents post structural insights, failed approaches, and technique hints in arena discussions. Problem 12: discussions revealed SOTA is a 4-flip local optimum, coding theory (PSL-optimal binary codes) as an alternative approach, and run-length structure (37 runs, max 6) of the best solution. This intel would have saved hours of redundant SA experiments. The discussions are effectively free reconnaissance — reading them costs minutes and can redirect hours of wasted effort.

## #14: A problem that LOOKS like domain X may actually be domain Y {#lesson-14}

Problem 7 looks like analytic number theory (Selberg sieve, Mobius function) but is actually a linear program. Arena discussions from CHRONOS revealed this. Don't assume the domain from the problem name — read discussions first, then decide the approach. The cost of starting with the wrong mathematical framework is enormous: not just wasted implementation time, but the optimizer itself may be fundamentally wrong for the true problem structure. LP solvers on an LP beat number-theoretic methods on an LP, regardless of how number-theoretic the problem statement sounds.

## #94: Lean proof problems are a different game — tactic fluency, not compute {#lesson-94}

The arena introduced Lean 4 proof problems (evaluationMode = "proof") starting with P21. These are fundamentally different from optimization: binary scoring (0 or 1), no minImprovement, no basins, no polish. The bottleneck is Lean 4 tactic fluency. For sum/product identities, the pattern is straightforward: `induction n with | zero => simp | succ n ih => rw [sum_range_succ, ...]; ring`. Keep a template submission script (`scripts/lean_proof/submit_p21.py`) for quick turnaround on new Lean problems. Expect future problems to require more sophisticated tactics (omega, decide, norm_num, custom lemmas, or multi-step forward proofs).

## #93: Open knowledge sharing as competitive advantage {#lesson-93}

When your techniques are publicly cited (Together.ai blog) and your solutions are downloadable via the API, secrecy has negative ROI — competitors already have your data. Pivoting to full technique transparency (publishing methodology, failures, structural insights across all 18 problems) creates community goodwill and citation value while costing nothing competitively. The key filter: share techniques and parameters freely, omit infrastructure specifics (compute platform, costs, automation). Publishing also forces a thorough review that catches stale rankings (6 corrected) and validates technique descriptions against the actual codebase.

## #95: Prune tooling that embeds a retired project framing {#lesson-95}

When the project mission shifts (competitive ranking to open knowledge), proactively remove features that embed the old framing rather than leaving them as dead code. update_status.py accumulated 360+ lines of medal-table computation, chart generation, Plotly dashboards, and history tracking that served the competitive framing — all dead weight once the mission changed. Removing them cut the script from 604 to ~240 lines, making it easier to maintain and clearer in purpose. General rule: if a feature's only justification was the old mission, delete it in the same branch that acknowledges the mission shift. Stale features mislead future contributors about what the project values.
