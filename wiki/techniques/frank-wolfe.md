---
type: technique
author: agent
drafted: 2026-05-02
related_concepts: [lp-duality.md, fractional-programming-dinkelbach.md, smooth-max-approximation.md]
related_problems: [P2, P3, P4, P13]
compute_profile: [local-cpu]
cost_estimate: minutes to hours
hit_rate: TBD
related_findings: [optimizer-recipes.md, frozen-problem-triage.md]
related_personas: [tao.md, hilbert.md]
cites:
  - ../concepts/lp-duality.md
  - ../concepts/fractional-programming-dinkelbach.md
---

# Frank–Wolfe (conditional gradient)

## TL;DR

Frank–Wolfe is the *linear-minimization-oracle* (LMO) descent method: at each step, minimize the linearized objective over the feasible set (a linear program), then take a convex combination with the current iterate. It's the natural optimizer when **the gradient is cheap but projection onto the feasible set is expensive** — exactly the regime of LP-bounded autocorrelation problems (P2/P3/P4) and graphon density problems (P13).

## When to apply

- The feasible set has a **cheap LP oracle** (simplex, polytope, ball intersection) but an **expensive Euclidean projection** (boundary-snap, full QP).
- The objective is **smooth and convex** (or smooth-max-approximated to be so) and we need **sparse iterates** (FW iterates are convex combinations of vertices → sparse by construction).
- Combined with **Dinkelbach** on ratio objectives — FW solves the parametric LP at each Dinkelbach step efficiently.

Specific arena fits:

- **P2/P3/P4 autocorrelation** — the LP relaxation has a cheap oracle (vertex of the box `[0, ∞)^N`); the Euclidean projection onto `Σ f_i = 1` is also cheap, so FW is mainly attractive when paired with Dinkelbach on `‖f★f‖_p / (Σf)^2` ratios.
- **P13 edges-triangles** — the flag-algebra LP / SDP has a vertex oracle (graphon density values are extreme points of a known polytope); FW with linear oracle is natural.
- **General LP-bounded extremal** — anywhere the dual is expressible as a positivity certificate (Cohn–Elkies, Hardy–Hilbert), FW gives a primal algorithm that converges to the LP bound.

## Procedure

```
init  x_0 ∈ feasible set X
for t = 0, 1, 2, ...:
    # 1. LMO step
    s_t  =  argmin_{s ∈ X}  ⟨∇f(x_t), s⟩      # this is the LP oracle call
    # 2. line search OR fixed step
    γ_t  =  argmin_{γ ∈ [0,1]}  f(x_t + γ (s_t − x_t))   # exact for quadratic
              # or use γ_t = 2/(t+2)  for the standard FW step rule
    # 3. convex combination
    x_{t+1}  =  x_t  +  γ_t (s_t − x_t)
```

Convergence: O(1/t) for smooth convex `f` over a bounded convex set. Sublinear, but each step is cheap.

**Variants worth knowing**:

- **Away-step Frank–Wolfe (AFW)** — adds a "remove vertex" step; gets linear convergence on strongly convex functions over polytopes.
- **Pairwise Frank–Wolfe** — at each step, add one vertex and remove another. Good for sparse iterates with high turnover.
- **Block-coordinate FW** — for separable feasible sets (e.g., direct products of simplices); each block independently.

## Pitfalls

- **Linear convergence requires extra structure** — vanilla FW is O(1/t); if you need faster, switch to AFW or PFW.
- **Open-ended feasible sets break FW** — needs a *bounded* convex set so the LMO has a well-defined argmin. Don't use on `ℝ^n` directly.
- **Sparse iterates may be a curse if you wanted dense** — FW iterates have ≤ t+1 nonzero entries through step t. Fine for finding sparse extremizers; bad for problems where the optimum is full-support.
- **Step size matters more than for projected gradient** — fixed `γ_t = 2/(t+2)` is the "safe" choice; line search is faster but can amplify roundoff in floating point.

## Compute profile

**Local CPU (recommended)**. FW is usually CPU-bound because the LMO call (a small LP) doesn't parallelize meaningfully across feasible-set dimensions. M5 Max with 128GB handles LP sizes of `N ~ 10⁵` comfortably via HiGHS interior-point. Cost: minutes to hours wall-clock for the autocorrelation family at `n ~ 90,000`. No Modal needed.

## References

- Frank, M. and Wolfe, P. (1956). "An algorithm for quadratic programming." *Naval Research Logistics Quarterly* 3, 95–110.
- Jaggi, M. (2013). "Revisiting Frank–Wolfe: projection-free sparse convex optimization." ICML.
- Lacoste-Julien, S. and Jaggi, M. (2015). "On the global linear convergence of Frank–Wolfe optimization variants." NeurIPS — establishes AFW linear rate.
- Used in: `findings/optimizer-recipes.md` cites FW as a tested-on-P2 baseline for the autocorrelation cutting-plane LP. P3 strategy.md mentions FW as a "Phase B" untried direction (now closed: cycle 2 of `js/research/p19-difference-bases` confirmed FW + Dinkelbach was a council-recommendation that didn't break the basin).
