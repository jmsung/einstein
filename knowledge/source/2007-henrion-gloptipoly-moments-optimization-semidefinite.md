---
type: source
kind: paper
title: "GloptiPoly 3: moments, optimization and semidefinite programming"
authors: D. Henrion, J. Lasserre, Johan Löfberg
year: 2007
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/0709.2559
source_local: ../raw/2007-henrion-gloptipoly-moments-optimization-semidefinite.pdf
topic: general-knowledge
cites:
---

# GloptiPoly 3: moments, optimization and semidefinite programming

**Authors:** D. Henrion, J. Lasserre, Johan Löfberg  ·  **Year:** 2007  ·  **Source:** https://arxiv.org/abs/0709.2559

## One-line
A Matlab toolbox that parses Generalized Problems of Moments (GPM) with polynomial data and solves them via a hierarchy of SDP relaxations whose optimal values converge to the global optimum.

## Key claim
Any GPM with polynomial objective, semialgebraic support constraints, and linear moment constraints across multiple measures can be cast as a monotone hierarchy of SDP relaxations (Lasserre hierarchy), with global-optimality certificates available when the moment matrix admits a flat extension and finite atomic support extraction.

## Method
Lasserre's moment-SDP hierarchy: variables become moments $y_\alpha = \int x^\alpha\, d\mu_k(x)$ of unknown measures $d\mu_k$ supported on basic semialgebraic sets $K_k = \{g_{ik}(x) \ge 0\}$; truncated moment + localizing matrices give PSD constraints whose feasibility implies a representing measure. Object-oriented Matlab classes (`mpol`, `meas`, `mom`, `supcon`, `momcon`, `msdp`) build the relaxation; SeDuMi or any YALMIP-interfaced SDP solver solves it. Explicit monic-monomial moment substitutions collapse equality constraints (e.g., $x_i^2 = 1$ in Max-Cut) before SDP assembly.

## Result
Demonstrated on: (i) six-hump camel back unconstrained min $= -1.0316$ with two atoms extracted at order-3 relaxation; (ii) non-convex QP from [3, §4.4] reaching global $-4$ at order-4 relaxation (lower bounds $-6, -5.69, -4.07, -4$); (iii) rational min of $(x^2-x)/(x^2+2x+1) = -1/3$ at $x \approx 0.5$ via the $\int h_0\, d\mu = 1$ trick; (iv) double-integrator minimum-time optimal control, where degree-16 test functions push the lower bound to $3.4991$ vs analytic $3.5$. Max-Cut AW29 substitution reduces 5005 moments to 465 in a 130×130 matrix vs 220×220 without substitution.

## Why it matters here
GloptiPoly/Lasserre hierarchy is the canonical SDP-relaxation engine for polynomial optimization and is directly invokable for any Einstein Arena problem cast as polynomial extremization on a semialgebraic set — autocorrelation inequalities, discrete-geometry packings with polynomial distance constraints, and any problem where the wiki's `findings/sdp-relaxation-uselessness` dead-end might be revisited with the right monomial substitution or rational reformulation. Connects to existing wiki entries on SDP relaxation, moment-SDP duality, and the LP/SDP hierarchy compute-routing question (RAM-bound large LP/SDP → Modal per [compute-router.md](../../.claude/rules/compute-router.md)).

## Open questions / connections
- When does flat-extension / atom-extraction succeed for arena problems? — `findings/three-way-local-optimality-proof` is the closest analogue; do any P1/P15/P16 configurations admit moment-SDP certificates?
- Rational minimization via the $\int h_0\, d\mu = 1$ normalization (Jibetean–de Klerk) — applicable to autocorrelation-ratio problems (P14, P17)?
- Lasserre hierarchy convergence is asymptotic under Archimedean conditions; what is the practical relaxation-order cliff for arena polynomial degrees in the 6–16 range?
- Moment-substitution gains (5005→465) suggest a general preprocessing pass — is there a wiki-worthy substitution-discipline note for any equality of the form (monic monomial = polynomial)?

## Key terms
Generalized Problem of Moments, Lasserre hierarchy, semidefinite programming, SDP relaxation, moment matrix, localizing matrix, polynomial optimization, semialgebraic set, GloptiPoly, SeDuMi, YALMIP, flat extension, atom extraction, rational minimization, occupation measure, optimal control, Henrion, Lasserre, Löfberg
