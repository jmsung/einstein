---
type: source
kind: paper
title: Nonlinear large deviation bounds with applications to traces of Wigner matrices and cycles counts in Erd\"os-Renyi graphs
authors: F. Augeri
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1810.01558
source_local: ../raw/2018-augeri-nonlinear-large-deviation-bounds.pdf
topic: general-knowledge
cites:
---

# Nonlinear large deviation bounds with applications to traces of Wigner matrices and cycles counts in Erd\"os-Renyi graphs

**Authors:** F. Augeri  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1810.01558

## One-line
Sharpens Chatterjee–Dembo nonlinear large deviation bounds by removing the second-order smoothness requirement, enabling LDPs at much smaller speeds and pushing sparse Erdős–Rényi cycle-count upper tails down to the $n^{-1/2}$ threshold.

## Key claim
For $X \sim \mu$ with $\Lambda_\mu$ essentially smooth and $f$ measurable with low-complexity "subgradient set" $W$, $\log P(f(X)\notin V_\delta(\{I\le r\})) \le -r + \log|D_{\delta/2}| + \log(\kappa L D/\delta \vee 1) + 2$, with no smoothness terms — only a covering-number error from a $\delta/2D$-net of $W$.

## Method
Convex-analysis approach via Legendre duality: tilt measures $\mu_y = e^{\langle\lambda,x\rangle - \Lambda_\mu(\lambda)}d\mu$ indexed by barycenter $y=\nabla\Lambda_\mu(\lambda)$, then a non-asymptotic Varadhan lemma controls $\log\int e^f d\mu$ by $\sup\{f-\Lambda_\mu^*\} + \log|D_\delta|+\delta$. For applications, truncation reduces $f$ to a low-rank-gradient surrogate (e.g. truncated trace $\mathrm{tr}_{[k]}Y^d$) whose Hilbert–Schmidt covering numbers are controlled by $O(nk\log n)$. Lower bounds via Jensen on the tilted measure $\mu_y$.

## Result
Three applications: (1) mean-field Ising partition function is accurate as soon as $\mu_{A_n}\Rightarrow\delta_0$ and $n^{-1}\mathrm{tr}A_n^2$ stays bounded, strengthening Basak–Mukherjee; (2) full LDP for $n^{-1}\mathrm{tr}(X/\sqrt n)^d$ of Wigner matrices with sharp sub-Gaussian entries at speed $n^{1+d/2}$ with rate $J_d(x)=(\beta/4)(x-C_{d/2})^{2/d}$ for $x\ge C_{d/2}$ (even $d$), $(\beta/4)|x|^{2/d}$ (odd $d$), giving universality across the class; (3) upper-tail LDP for cycle counts $X_{C_d}$ in $G(n,p)$ valid down to $p\gg n^{-1/2}$ (up to log factors), improving Cook–Dembo for triangles.

## Why it matters here
General background; no direct arena tie. Closest relevance is methodological: convex-analysis / Legendre-dual machinery for tightening counting / large-deviation bounds, which is structurally analogous to LP-bound and Cohn–Elkies-style dual-feasibility arguments used in packing/autocorrelation problems on the wiki.

## Open questions / connections
- Can the covering-number error term be tightened further to remove the residual log factors at $p\sim n^{-1/2}$ for cycle counts?
- How does the universality class (sharp sub-Gaussian) extend — e.g. to super-Gaussian tails where heavy-tail / planted-clique strategies dominate (cf. Augeri's earlier arXiv:1605.03894)?
- Extends Chatterjee–Dembo [11], Eldan's Gaussian-mean-width framework [19], Yan's compactly supported generalization [37]; counterexample by Šileikis–Warnke [35] to the DeMarco–Kahn conjecture sits in the same upper-tail landscape.

## Key terms
nonlinear large deviations, Chatterjee-Dembo, Legendre transform, essentially smooth convex function, mean-field Ising, Wigner matrix trace LDP, sharp sub-Gaussian, sparse Erdős–Rényi, cycle count upper tail, Gaussian mean-width, covering number, convex concentration, Augeri, Eldan
