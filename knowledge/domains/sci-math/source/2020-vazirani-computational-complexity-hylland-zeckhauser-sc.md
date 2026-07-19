---
type: source
kind: paper
title: Computational Complexity of the Hylland-Zeckhauser Scheme for One-Sided Matching Markets
authors: V. Vazirani, M. Yannakakis
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2004.01348
source_local: ../raw/2020-vazirani-computational-complexity-hylland-zeckhauser-sc.pdf
topic: general-knowledge
cites:
---

# Computational Complexity of the Hylland-Zeckhauser Scheme for One-Sided Matching Markets

**Authors:** V. Vazirani, M. Yannakakis  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2004.01348

## One-line
Partial resolution of the long-open complexity of the Hylland–Zeckhauser (HZ) one-sided matching-market equilibrium: poly-time for bivalued utilities, irrational + disconnected equilibria in general, membership in FIXP.

## Key claim
Three results: (1) a combinatorial **strongly polynomial-time** algorithm for HZ with $0/1$ (and more generally bivalued $\{a_i,b_i\}$) utilities; (2) an explicit 4-agent/4-good instance with **only irrational equilibria** and **disconnected** equilibrium set — ruling out PPAD membership and any convex-programming formulation; (3) HZ equilibrium computation is in the class **FIXP**. FIXP-hardness is left open.

## Method
For (1): combine bipartite perfect-matching / Gallai–Edmonds-style vertex-cover decomposition with a *Simplified DPSV* primal-dual price-raising algorithm for the linear Fisher submarket on the over-demanded side; equivalence under affine $u' = s\cdot u + h$ lifts the unit case to bivalued. For (2): solve the HZ KKT/complementarity system on a 4×4 instance, reducing to a cubic $7y^2-y-4=0$ (and a parallel cubic giving $y=\tfrac{1+\sqrt{113}}{14}$), yielding two disconnected irrational equilibria. For (3): construct an explicit straight-line program (algebraic Brouwer map using $+,-,\times,/,\min,\max$) over a compact domain whose fixed points are exactly HZ equilibria — price-update step pushes excess demand toward $0$, bundle-update steps swap mass between optimal/suboptimal triples until KKT (Type A–D bundle classification) holds.

## Result
Strongly polynomial algorithm for $0/1$ and bivalued HZ via Algorithm 10 (perfect matching + Simplified DPSV). Example 18: agents with utilities forcing prices $p_1=0$, $p_2=1-y^2$, $p_3=1+y$, $p_4=2(1-y^2)-y$ where $7y^2-y-4=0$, plus a second disconnected equilibrium with $r_4=5-6y^2$ and $y=(1+\sqrt{113})/14$ — both irrational, both fractional perfect matchings, agents spend exactly $\$1$. Corollary 19: no convex program for HZ. Theorem 27: HZ $\in$ FIXP.

## Why it matters here
General background on fixed-point complexity classes (PPAD vs FIXP) and the *irrational-equilibrium / disconnected-feasible-set* obstruction to convex programming — relevant as a cautionary template when the agent considers SDP/convex-LP relaxations for arena problems whose true optimum may be algebraic-irrational with multiple disconnected basins (cf. basin-rigidity findings, $\sqrt{\cdot}$-valued optima in P11/P15/P16). No direct arena tie to a specific problem.

## Open questions / connections
- Is HZ FIXP-hard? (left open; would settle complexity tightly).
- Does the $\{0,\tfrac12,1\}$ trivalued case always admit rational equilibria? Conjectured non-trivial; possibly intractable.
- Efficient approximation algorithms for HZ equilibria; extension to two-sided / endowment / constrained pseudo-markets [EMZ19a/b].
- Connects to FIXP membership program for Arrow–Debreu under Leontief / PLC / CES utilities [Yan13, GMV16, GMVY17, CPY17] and to the PPAD-completeness of SPLC Fisher markets [VY11].

## Key terms
Hylland-Zeckhauser, one-sided matching market, FIXP, PPAD, Brouwer fixed point, irrational equilibrium, disconnected equilibria, convex program obstruction, linear Fisher market, DPSV primal-dual, bivalued utilities, Nash equilibrium, Vazirani, Yannakakis
