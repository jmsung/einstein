---
type: source
kind: paper
title: A geometrical approach to computing free-energy landscapes from short-ranged potentials
authors: Miranda C. Holmes-Cerfon, S. Gortler, M. Brenner
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1210.5451
source_local: ../raw/2012-holmescerfon-geometrical-approach-computing-free-energy.pdf
topic: general-knowledge
cites:
---

# A geometrical approach to computing free-energy landscapes from short-ranged potentials

**Authors:** Miranda C. Holmes-Cerfon, S. Gortler, M. Brenner  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1210.5451

## One-line
Shows that in the short-range limit, the free-energy landscape of $n$ interacting particles reduces to a union of geometric manifolds (rigid sphere-packing "corners" joined by floppy modes) plus one sticky parameter $\kappa$, and computes the full landscape for $n \le 8$.

## Key claim
As the interaction range $\epsilon \to 0$ with depth $C$ tuned so $\kappa = \lim_{\epsilon\to 0} e^{-\beta C U_0}/(d\sqrt{c\beta C U''(0)})$ is finite, the equilibrium measure concentrates on the stratified manifold of bond-constraint sets $\{y_k(x)=0\}$, with partition function $z_\alpha = \kappa^m \int_{\Omega^Q_\alpha} h_\alpha(x) I(x)\sqrt{|\bar g_\alpha|}\,dx$ where $h_\alpha = \prod_i \lambda_i^{-1/2}$ depends only on geometry. Floppy/rigid ratios $Z_1/Z_0$ and $Z_2/Z_1$ are nearly $n$-independent ($\approx 7$–$8$ and $\approx 4.5$–$4.7$ for $n=6,7,8$), implying clusters "melt explosively" rather than incrementally.

## Method
Distinguished asymptotic limit ($\epsilon\to 0$, $C\to\infty$) of the Gibbs measure for overdamped Langevin dynamics, evaluated via Laplace's method after splitting configuration space into fast (constraint) and slow (manifold) coordinates. Builds on Arkus–Brenner–Manoharan enumeration of rigid sphere packings with $\ge 3n-6$ contacts; floppy modes obtained by breaking bonds and walking the null space of the rigidity matrix $M=(\nabla y_1,\dots,\nabla y_m, t_1,\dots,t_6)^T$, then projecting back to the constraint variety via Newton's method. Two-dimensional manifolds are parameterized by boundary tracing, interior point generation, and a Floater-style convex-combination triangulation in the quotient space $\Omega_\alpha/SE(3)$.

## Result
Complete enumeration of $0$-, $1$-, $2$-dimensional manifolds for $n=5,6,7,8$: e.g. for $n=8$, $13$ rigid clusters, $75$ one-dim modes, $281$ two-dim modes with $Z_0=4.9\times 10^4$, $Z_1=3.96\times 10^5$, $Z_2=1.87\times 10^6$. Derives a coupled Fokker–Planck hierarchy on the stratified manifold with "sticky" boundary conditions $\kappa_i \partial_t u = \mathrm{div}_i \kappa_i \mathrm{grad}_i u - \nabla u\cdot\hat n$, shown self-adjoint between forward and backward equations. Brownian-dynamics simulations with Morse potential ($\rho=30$, $E=8.5$, $\kappa\approx 16$) reproduce predicted occupation probabilities and transition rate matrices.

## Why it matters here
General background; no direct arena tie. Closest contact is to **sphere-packing enumeration** (Arkus et al. rigid $n$-sphere clusters with $\ge 3n-6$ contacts) which is conceptually adjacent to P1-style sphere-packing density problems — the floppy-mode / rigidity-matrix machinery could inform how to characterize the local basin geometry of dense packing optima, especially the "basin rigidity" theme already in the wiki.

## Open questions / connections
- Are all floppy manifolds topologically discs (not higher-genus or non-orientable)? Conjectured but unproven for general $n,p$.
- Does the list of rigid $n$-sphere clusters from Arkus et al. omit any rigid configurations with $< 3n-6$ contacts? (Open at the time.)
- Do the near-constant ratios $Z_{p+1}/Z_p$ persist for $n \ge 9$ and $p \ge 3$? Would imply universal cluster-melting behavior.
- Extends sticky-sphere limit literature (Baxter 1968; Stell) to a full geometric/dynamical framework.

## Key terms
sticky sphere limit, rigid sphere packings, floppy modes, Arkus-Brenner-Manoharan enumeration, Fokker-Planck on manifolds, rigidity matrix, stratified manifold, free energy landscape, quotient space SE(3), Holmes-Cerfon, Floater triangulation, colloidal clusters, $3n-6$ contacts, basin rigidity
