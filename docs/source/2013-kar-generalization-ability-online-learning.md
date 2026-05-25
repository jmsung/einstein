---
type: source
kind: paper
title: On the Generalization Ability of Online Learning Algorithms for Pairwise Loss Functions
authors: Purushottam Kar, Bharath K. Sriperumbudur, Prateek Jain, H. Karnick
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1305.2505
source_local: ../raw/2013-kar-generalization-ability-online-learning.pdf
topic: general-knowledge
cites:
---

# On the Generalization Ability of Online Learning Algorithms for Pairwise Loss Functions

**Authors:** Purushottam Kar, Bharath K. Sriperumbudur, Prateek Jain, H. Karnick  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1305.2505

## One-line
Tighter, dimension-aware generalization bounds for online learning with pairwise loss functions (metric learning, AUC, ranking), plus a finite-buffer online algorithm with provable all-pairs regret.

## Key claim
Using a "Symmetrization of Expectations" decoupling step, the authors derive Rademacher-complexity-based online-to-batch bounds that improve on Wang et al. (2012): the excess risk over the full ensemble decays as $O(C_d/\sqrt{n} + R_n/n)$ where $C_d=1$ for $L_2$-regularized classes (dimension-independent) and $C_d=\sqrt{\log d}$ for sparse classes — strictly tighter than the $L_\infty$-covering-number bounds with linear $d$ dependence in prior work.

## Method
Pairwise losses $\ell(h,z,z')$ break the martingale structure standard online-to-batch proofs rely on, because the "head" $z_t$ and "tail" $z_\tau$ couple inside $\hat L_t(h)= \tfrac{1}{t-1}\sum_{\tau<t}\ell(h,z_t,z_\tau)$. The fix is *Symmetrization of Expectations*: take an inner $\mathbb E_z$ over the head before symmetrizing tails with ghost samples $\tilde z_\tau$, which restores the sign-flip identity needed to introduce Rademacher variables $\epsilon_\tau$. The bivariate Rademacher complexity $R_n(\mathcal H)=\mathbb E\sup_h \tfrac{1}{n}\sum_\tau \epsilon_\tau h(z,z_\tau)$ is then controlled by an order-reduction trick (lift pairs $(x,x')$ to $\psi(x,x')$) plus strong-convexity duality from Kakade et al. (2008/2012).

## Result
Three deliverables: (1) Theorem 3 — for $B$-bounded losses, $\tfrac{1}{n-1}\sum L(h_{t-1}) \le L(h^*)+ \tfrac{4}{n-1}\sum R_{t-1}(\ell\circ\mathcal H)+\tfrac{R_n}{n-1}+6B\sqrt{\log(n/\delta)/(n-1)}$. (2) Theorem 5 — for $\sigma$-strongly-convex losses, fast rate $\tilde O(C_d^2/n)$ matching first-order Kakade–Tewari up to log factors. (3) Theorem 6 — finite-buffer regret of size $s$ yields an extra $O(C_d/\sqrt{s})$ term, valid for any stream-oblivious buffer policy (FIFO or reservoir sampling). An accompanying algorithm OLP with a new "RS-x" buffer (i.i.d. samples after a repopulation step) gets high-probability all-pairs regret $\tilde O(\sqrt{n}+C_d n/\sqrt{s})$, correcting a flaw in Zhao et al. (2011)'s OAM proof.

## Why it matters here
General background; no direct arena tie. Pairwise-loss generalization theory is adjacent to the agent's optimization-on-finite-samples work but doesn't supply a technique for sphere packing, autocorrelation, or kissing-number problems. The Kakade–Sridharan–Tewari Rademacher / strong-convexity machinery cited here is the more reusable thread if the agent ever needs uniform-convergence rates for a learned surrogate.

## Open questions / connections
- Can stream-*aware* buffer policies (e.g., importance-weighted retention) be analyzed without losing the decoupling?
- The $\sqrt{p}$ vs $\sqrt{\log p}$ gap to Cortes et al. (2010a) for $L_2$-regularized multiple kernel learning — is the looseness in the proof or intrinsic to two-stage MKL?
- Extends Cesa-Bianchi et al. (2001) online-to-batch and Kakade & Tewari (2008) strong-convex rates from first-order to pairwise; natural next step is $k$-th order U-statistic losses.
- RS-x uses $O(s)$ random bits/step vs Vitter RS's $O(\log s)$; RS-x2 implementation recovers $O(\log s)$ via a Binomial-then-permute trick.

## Key terms
Rademacher complexity, pairwise loss, online-to-batch conversion, U-statistic, symmetrization of expectations, reservoir sampling, AUC maximization, metric learning, multiple kernel learning, strong convexity, finite-buffer regret, GIGA / Zinkevich, Kakade-Tewari, martingale decoupling
