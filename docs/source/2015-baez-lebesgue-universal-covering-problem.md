---
type: source
kind: paper
title: The Lebesgue universal covering problem
authors: J. Baez, Karine Bagdasaryan, P. Gibbs
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1502.01251
source_local: ../raw/2015-baez-lebesgue-universal-covering-problem.pdf
topic: general-knowledge
cites:
---

# The Lebesgue universal covering problem

**Authors:** J. Baez, Karine Bagdasaryan, P. Gibbs  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1502.01251

## One-line
Constructs a new smallest-known convex universal cover for the plane — a convex set containing an isometric copy of every diameter-1 subset — shaving $2.2 \cdot 10^{-5}$ off Hansen's 1992 bound.

## Key claim
The least area $a$ of a convex universal cover satisfies $a \le 0.8441153$ (refined by Egan to $0.844115297128419\ldots$), improving Hansen's $a \le 0.844137708398$; combined with Brass–Sharifi's lower bound this gives $0.832 \le a \le 0.8441153$. The paper also corrects Hansen's area-removed claim from $6 \cdot 10^{-18}$ to $8.4541 \cdot 10^{-21}$.

## Method
Start from Pál's regular hexagon (side $1/\sqrt{3}$, inscribed circle of diameter 1) and rotate a second congruent hexagon by $30° + \sigma$ to obtain a tilted intersection (a near-dodecagon when $\sigma=0$). Three reductions are layered: (1) remove two opposite "corner" triangles using a parallel-tangent-lines argument (any diameter-1 set fits in three adjacent or three alternating triangles); (2) trim arc-bounded slivers using Vrećica's extension of any diameter-1 set to a constant-width-1 curve, which must touch each hexagon side at a unique point; (3) remove a curved region $WXY$ near a corner via a three-case symmetry argument over which triangles the curve enters, requiring constraints $\angle WYL > 90°$ and $\angle MWY > 90°$. Optimal slant $\sigma \approx 1.2944°$ found numerically (Java + Mathematica at 2000-digit precision).

## Result
Explicit construction with area $\le 0.8441153$; Egan's high-precision verification gives $0.844115297128419059$ at $\sigma = 1.294389444703601012°$, with $\angle WYL \approx 90.00593°$ and $\angle MWY \approx 122.9277°$. Recursive distance formula $x_{i+1} = 2x_i^2 / (\sqrt{3}x_i + \sqrt{1 - 2\sqrt{3}x_i - x_i^2})$ from $x_0 = 1 - \sqrt{3}/2$ gives the sliver-area sequence: $a_2 \approx 3.75 \cdot 10^{-11}$, $a_3 \approx 8.45 \cdot 10^{-21}$, $a_4 \approx 4.29 \cdot 10^{-40}$ — exposing Hansen's $10^3$-magnitude arithmetic error.

## Why it matters here
General background for the agent's discrete-geometry / packing problem family: an exemplar of a long-running "shave-the-corners" optimization where computer-assisted high-precision arithmetic (Mathematica at 2000 dps) finally beat hand calculation, and where a published bound contained an undetected arithmetic error for 23 years — concrete cautionary tale aligned with the triple-verify axiom. The recursive $x_i$ construction and the constant-width-extension trick (Vrećica) are reusable techniques for any "smallest convex set containing all X" formulation.

## Open questions / connections
- Closing the gap $0.832 \le a \le 0.8441153$: lower bound (Brass–Sharifi via shape-alignment) and upper bound improvements are both wide open.
- Dropping convexity (Duff 1980): how much smaller can a non-convex universal cover be?
- Whether the slant-angle reduction technique generalizes to higher-dimensional Lebesgue covers or to other "universal" containment problems.

## Key terms
Lebesgue universal covering, convex cover, diameter-1 set, constant width curve, Vrećica extension, Pál hexagon, Sprague reduction, Hansen reduction, regular dodecagon inscription, slant angle optimization, Brass-Sharifi lower bound, plane geometry, high-precision arithmetic verification, triple-verify, Baez, Egan
