---
type: source
kind: paper
title: Last Iterate is Slower than Averaged Iterate in Smooth Convex-Concave Saddle Point Problems
authors: Noah Golowich, S. Pattathil, C. Daskalakis, A. Ozdaglar
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2002.00057
source_local: ../raw/2020-golowich-last-iterate-slower-than.pdf
topic: general-knowledge
cites:
---

# Last Iterate is Slower than Averaged Iterate in Smooth Convex-Concave Saddle Point Problems

**Authors:** Noah Golowich, S. Pattathil, C. Daskalakis, A. Ozdaglar  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2002.00057

## One-line
Proves the last iterate of the Extragradient (EG) algorithm on smooth convex-concave saddle-point problems converges at $O(1/\sqrt{T})$, quadratically slower than the $O(1/T)$ rate of its averaged iterate, and shows this rate is tight.

## Key claim
For smooth convex-concave min-max problems, EG's last iterate satisfies $\sqrt{\mathrm{Ham}_f(z^{(T)})} = O(1/\sqrt{T})$ and primal-dual gap $= O(1/\sqrt{T})$; a matching $\Omega(1/\sqrt{T})$ lower bound holds for all 1-stationary canonical linear iterative (1-SCLI) algorithms whose inversion polynomial has degree $\le k-1$, establishing a *quadratic separation* between last and averaged iterates.

## Method
Upper bound: monotone-operator analysis of EG under first-order ($L$-Lipschitz $F$) and second-order ($\Lambda$-Lipschitz $\partial F$) smoothness, using a potential that tracks $\|F(z^{(t)})\|^2$ and PSD inequalities (Lemmas 11, 17, 18) to show Hamiltonian descent. Lower bound: restrict to bilinear $f(x,y)=x^\top My+b_1^\top x+b_2^\top y$ with $M=\nu I$, reduce the 1-SCLI iteration to a scalar polynomial $q_0(\nu i)$ acting on $b$, then invoke a Chebyshev-polynomial extremal argument (Lemmas 13, 14) improving on Nemirovsky / Arjevani-Shamir bounds to get the $\nu^2 |q_0(\nu i)|^{2t} \gtrsim L^2/(tk^2)$ lower bound.

## Result
Theorem 10 (upper): EG with constant step $\eta < 1/(L+\Lambda D)$-style condition gives $\|F(z^{(T)})\|, \mathrm{Gap}_f(z^{(T)}) = O(LD/\sqrt{T})$. Theorem 9 (lower, for 1-SCLIs with $N(A)$ a degree-$\le k-1$ polynomial): $\mathrm{IC}(\mathcal{A}, \mathcal{L}_{\mathrm{Ham}}; T) \ge L^2 D^2/(20Tk^2)$ and $\mathrm{IC}(\mathcal{A}, \mathcal{L}_{\mathrm{Gap}}; T) \ge LD^2/(k\sqrt{20T})$. The inverse-linear $k$-dependence is shown tight (Proposition 15). Proximal Point obtains the same $O(1/\sqrt{T})$ last-iterate rate (Theorem 20, Appendix C).

## Why it matters here
General background; no direct arena tie — none of the 23 Einstein Arena problems are saddle-point / min-max optimization. Marginally relevant only as background for *convergence-rate lower bounds via polynomial extremal arguments* (Chebyshev tricks), a technique family that occasionally appears in LP/SDP-bound analyses for sphere packing.

## Open questions / connections
- Does the $O(1/\sqrt{T})$ last-iterate rate extend to OGDA and other monotone-VI methods beyond EG? (Followed up in subsequent literature.)
- Can the inverse-linear $k$ dependence be improved for $T > 1$, or is it tight at all $T$?
- Extends Nemirovski (2004) / Ouyang–Xu (2019) $\Omega(1/T)$ averaged-iterate lower bounds via the SCLI / CLI framework of Arjevani–Shamir (2016), Azizian et al. (2019), Ibrahim et al. (2019).

## Key terms
extragradient, EG algorithm, saddle point, convex-concave, last iterate convergence, averaged iterate, primal-dual gap, Hamiltonian, monotone variational inequality, 1-SCLI lower bound, Chebyshev polynomial, proximal point algorithm
