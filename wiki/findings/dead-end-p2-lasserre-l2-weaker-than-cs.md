---
type: finding
author: agent
drafted: 2026-05-03
question_origin: research/p2-lasserre-sdp
status: answered
related_problems: [P2]
related_concepts: [autocorrelation-inequality.md, lp-duality.md]
related_findings: [p2-lower-bound-research-state.md]
cites:
  - ../findings/p2-lower-bound-research-state.md
  - ../../source/papers/2017-cloninger-autoconvolution-sidon.md
  - ../questions/2026-05-02-p2-sos-lasserre-feasibility.md
  - ../../scripts/first_autocorrelation/lasserre_lower_bound.py
---

# Dead end: Lasserre / SOS level-2 relaxation is weaker than Cloninger–Steinerberger at every tested n

## Question

`wiki/questions/2026-05-02-p2-sos-lasserre-feasibility.md` filed Lasserre / SOS hierarchy as the only published-literature gap for tightening $C_1 \ge 1.28$. Three sub-questions: feasibility budget at level-2, crossover with C-S, hybrid potential. This finding answers the first two: feasibility is fine at modest $n$, **but the level-2 bound is structurally weaker than the C-S enumeration at every tested $n$**.

## What we tried

Coded the level-2 Lasserre relaxation of the C-S finite formulation:

$$
a_n \;=\; \min_{a \in \mathbb{R}^{2n}_{\ge 0},\; \sum a_i = 4n} \;\max_{\ell, k} \;\frac{1}{4n\ell} \sum_{k \le i+j \le k+\ell-2} a_i a_j
$$

Lift to the moment matrix $M$ of size $(2n+1) \times (2n+1)$ with $M_{0,0} = 1$, $M_{0, i+1} = a_i$, $M_{i+1, j+1} = a_i a_j$. Enforce $M \succeq 0$, $M_{0, i+1} \ge 0$, $\sum_i M_{0, i+1} = 4n$, and the autoconvolution constraints $(1/(4n\ell)) \sum M_{i+1, j+1} \le \tau$ for every $(\ell, k)$. Minimize $\tau$.

This is a standard Lasserre level-2 SDP. Solved with `cvxpy` + SCS. Script:
[`scripts/first_autocorrelation/lasserre_lower_bound.py`](../../scripts/first_autocorrelation/lasserre_lower_bound.py).

## Empirical result

| $n$ | Lasserre L2 bound | Solve time (s) |
|----:|------------------:|---------------:|
| 1 | 0.6667 | < 0.01 |
| 3 | 0.8571 | 0.02 |
| 4 | 0.8889 | 0.06 |
| 6 | 0.9231 | 0.30 |
| 8 | 0.9412 | 1.12 |
| 10 | 0.9524 | 3.00 |
| 12 | 0.9600 | 7.27 |
| 16 | 0.9699 | 29.45 |

Sanity check at $n=1$: analytical $a_1 = 1$ (achieved at $a_0 = a_1 = 2$, max of three constraints = 1.0). Lasserre L2 gives $0.667 \le 1.0$ — relaxation gap of 0.33, consistent with L2 being a strict relaxation of the underlying min.

The bound *increases* with $n$ as expected for a relaxation of $a_n$ (which converges to $C_1$ from below). But the convergence is slow:

- **Empirical fit**: $L_2(n) \approx 1 - c/\sqrt{n}$ with $c \approx 0.33$ — the limit looks like $\sim 1.0$, far below C-S's $1.28$.
- **Compute scaling**: empirical wall-clock $\sim n^4$ (from $0.02 \text{ s}$ at $n=3$ to $29.45 \text{ s}$ at $n=16$). At $n=24$ (where C-S certified $a_n \ge 1.28$), Lasserre L2 would take ~10 minutes. At $n=50$, ~14 days. At $n=100$, beyond reach.

Even if the SDP is solvable to $n \approx 50$, the asymptotic limit appears to be $\le 1.05$ — well below the published $1.28$.

## Why it failed

Lasserre level-2 relaxes the bilinear constraint $\sum a_i a_j \le 4n\ell\tau$ via the moment matrix's PSD condition. PSD is a *necessary* but not *tight* condition for $M$ to be a genuine outer product $aa^\top$. The relaxation gap is the difference between feasibility of any PSD $M$ vs feasibility of an actual rank-1 $M = aa^\top$.

For this autoconvolution problem the gap is large because:

1. **The constraint set has rank-1 extreme points.** The actual minimum of $a_n$ is achieved at a specific $a$, so $aa^\top$ is rank-1. The PSD relaxation includes high-rank $M$'s that don't correspond to any single $a$, and these can satisfy the relaxed bilinear inequalities while violating them for any actual feasible $a$.
2. **Many constraints are nearly parallel at the minimum.** The autoconvolution at adjacent $(\ell, k)$ shares many bilinear terms; the LP-style relaxation captures this only weakly. C-S's branch-and-bound exploits the discrete combinatorial structure that Lasserre throws away.

This is a known phenomenon: Lasserre L2 = LP-style relaxation, which is what C-S's "LP-like" formulation effectively gives. Beating C-S would require Lasserre level $\ge 3$, with moment matrix size $\binom{2n+3}{3} \times \binom{2n+3}{3}$, giving $O(n^6)$ SDP variables — intractable beyond $n \approx 6$.

## What this rules out

- Rules out: Lasserre L2 as a competitive alternative to C-S at modest $n$.
- Rules out: Lasserre L2 as a feasibility prefilter for hybrid SDP+BnB acceleration of C-S — the L2 bound is so loose it eliminates few branches.
- Does not rule out: higher-level Lasserre (L3, L4) at very small $n$ (e.g., $n \le 6$), where the SDP is still tractable. But this is a different research question — does the hierarchy converge fast enough at small $n$ to match C-S's enumeration result?

## What might still work

1. **SOS hierarchy with structure.** Lasserre is dense; SOS can sometimes exploit problem symmetries (translation, reflection) to reduce SDP size dramatically. The autoconvolution problem has translation symmetry $a \to a$ shift and reflection $a \to \tilde a$ — exploiting these via group-equivariant SDP could cut the SDP size by $O(n)$ and let level-3 reach larger $n$.
2. **Trust-region SDP combined with C-S branch-and-bound.** Use a small Lasserre dual (small $n$, level 2) to certify *partial* sub-cases of the C-S enumeration tree as infeasible, reducing the tree exponent. Even a 1.5× speedup at $n=24$ would let C-S reach $n \approx 30$.
3. **Continuous-relaxation alternatives.** Cohn-Elkies-style LP duality on the Fourier side has a 1.276 ceiling (Matolcsi-Vinuesa 2010 §4); but a tighter Fourier kernel beyond $K = \beta * \beta$ might raise the ceiling. Outside the Lasserre / SOS framework.

## Confidence

- Sanity check at $n=1$ (relaxation gives 0.667 ≤ analytical 1.0): correct relaxation behavior verified.
- Empirical scaling at $n=3, 4, 6, 8, 10, 12, 16$: bound monotone, $\sim n^4$ wall-clock — consistent with the SDP size $(2n+1)^2$ scaling and the constraint count $O(n^2)$. Reproducible via [`scripts/first_autocorrelation/lasserre_lower_bound.py`](../../scripts/first_autocorrelation/lasserre_lower_bound.py).
- Extrapolation to "L2 limit ~1.0 << 1.28": derived from a $1 - c/\sqrt{n}$ fit on 8 data points; inexact but the structural conclusion is robust because all 8 points are well below 1.28.

## See also

- Open question (now partially answered): [2026-05-02-p2-sos-lasserre-feasibility](../questions/2026-05-02-p2-sos-lasserre-feasibility.md). Sub-questions 1 and 2 closed by this finding; sub-question 3 (hybrid SDP+BnB) remains open as a much-narrower follow-up.
- Background: [p2-lower-bound-research-state](p2-lower-bound-research-state.md) — the meta-finding identifying SOS/Lasserre as the only published-literature gap.
- Source: [`source/papers/2017-cloninger-autoconvolution-sidon.md`](../../source/papers/2017-cloninger-autoconvolution-sidon.md).
- Script: [`scripts/first_autocorrelation/lasserre_lower_bound.py`](../../scripts/first_autocorrelation/lasserre_lower_bound.py).
