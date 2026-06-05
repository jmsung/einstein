---
type: question
author: agent
asked_by: tao
drafted: 2026-06-04
status: open
related_problems: [2]
---

# P2 headroom — Tao: what degree of freedom remains past v²@n=90000, and what is the obstruction OrganonAgent removed that we didn't?

1. **What is the single obstruction that pinned us at 1.5028610916 while OrganonAgent reached 1.5028609074?**
   Why it matters: name the one phenomenon, per Tao's first heuristic. Candidate obstructions are mutually exclusive enough to be falsifiable: (a) *resolution* — n=90000 was a measured sweet spot and 120k/150k were *shallower*, so the win may need a non-block-repeat refinement at the SAME n; (b) *β-ceiling* — our cascade stopped at 1e14, and the smooth-max may still be over-relaxed at the floor; (c) *support topology* — our stored v3 seed has 90000/90000 nonzero cells (NOT sparse), so the v²-exact-zeros mechanism may be inactive in the actual winning seed, meaning the real lever is cluster *positions*, not sparsity. A good answer designs one experiment per candidate that distinguishes them.

2. **Our resolution sweep showed n=90000 beats 120k/150k (which were shallower). Is the sweet spot an artifact of L-BFGS converging too fast on smoother large-n landscapes, and would a longer/restarted low-β phase at n≥120k unlock a deeper basin than 90k?**
   Why it matters: the recipe note says larger n "paradoxically converges to shallower minima because L-BFGS converges faster." If true, the cure is more low-β exploration *time* at large n, not abandoning large n. A good answer is a controlled run: n=120000, low-β=1e6, max_iter ≥ 9000 (3× the 90k recipe), history_size 300, measuring whether the deeper basin appears with more exploration budget.

3. **Is there a multi-scale (dyadic) structure in the 69-cluster support whose finest scale is below the n=90000 grid spacing — i.e. is the optimum genuinely band-unlimited, so the right move is adaptive (non-uniform) grid refinement on the active clusters rather than uniform n?**
   Why it matters: B3 proved the optimum is high-frequency (18,193 non-trivial cells, low-freq regularizer strictly hurts). If the comb-spike clusters need sub-grid resolution that uniform 90k can't represent, an adaptive mesh concentrating points on the 69 clusters could expose DOF that uniform large-n wastes. A good answer measures the finest active cluster width in grid units and states whether it is grid-spacing-limited.
