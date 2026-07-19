---
type: source
kind: paper
title: Fast Extra Gradient Methods for Smooth Structured Nonconvex-Nonconcave Minimax Problems
authors: Sucheol Lee, Donghwan Kim
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2106.02326
source_local: ../raw/2021-lee-fast-extra-gradient-methods.pdf
topic: general-knowledge
cites:
---

# Fast Extra Gradient Methods for Smooth Structured Nonconvex-Nonconcave Minimax Problems

**Authors:** Sucheol Lee, Donghwan Kim  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2106.02326

## One-line
Proposes FEG, the first explicit first-order method achieving accelerated $O(1/k^2)$ squared-gradient-norm rate for smooth nonconvex-nonconcave minimax problems under negative comonotonicity.

## Key claim
For $L$-Lipschitz, $\rho$-comonotone saddle-gradient $F$ with $\rho > -1/(2L)$, FEG satisfies $\|Fz_k\|^2 \leq \frac{4\|z_0 - z^*\|^2}{(1/L + 2\rho)^2 k^2}$ — first $O(1/k^2)$ rate in the nonconvex-nonconcave regime, and 27/4× tighter constant than EAG-V in the monotone case ($\rho = 0$).

## Method
Combines two prior ideas: (i) the two-time-scale extragradient EG+ of Diakonikolas–Daskalakis–Jordan, and (ii) the Halpern/anchoring technique of EAG (Yoon–Ryu). The update reuses $Fz_k$ in the $z_{k+1}$ step (atypical for extragradient methods) — this reuse is what handles negative comonotonicity. Step sizes $\alpha_k = 1/L$, $\beta_k = 1/(k+1)$, $\rho_k = \rho$ are constants except for the anchoring weight. Analysis uses a nonincreasing potential $V_k = a_k \|Fz_k\|^2 - b_k \langle Fz_k, z_0 - z_k\rangle$. A backtracking variant FEG-A removes the need to know $L, \rho$; a stochastic variant S-FEG handles noisy gradients but only stays stable if noise variance decays as $O(1/k)$.

## Result
Three regimes for $L$-Lipschitz $F$: (1) negative comonotone with $\rho \in (-1/(2L), 0)$: first ever $O(1/k^2)$ rate (vs EG+'s $O(1/k)$), and widens convergence region from $\rho > -1/(8L)$ to $\rho > -1/(2L)$. (2) monotone ($\rho = 0$): rate constant 4 vs EAG-V's 27 vs EAG-C's 260; only 4× the known lower bound $\Omega(1/k^2)$. (3) $\rho$-cocoercive with $L < 1/(2\rho)$: beats explicit Halpern even per gradient call. Lemma 8.1 also constructs a smooth $L$-Lipschitz (non-comonotone) example where no first-order method in the span class can drive $\|Fz_k\|$ below $\sqrt{2LR}$ — extra structure beyond Lipschitz is unavoidable.

## Why it matters here
General background; no direct arena tie. The Einstein Arena problems are continuous optimization (sphere packing, autocorrelation, kissing) rather than saddle-point games, so FEG is unlikely to be a drop-in. But the anchoring/Halpern acceleration trick + potential-function proof template could inform any iteration where progress is measured in squared gradient norm (e.g., gradient-based polish in P5/P6/P14/P17 precision-critical problems where last-iterate squared-gradient control matters more than ergodic average).

## Open questions / connections
- Extends Yoon–Ryu EAG ($O(1/k^2)$ for monotone) to the negative-comonotone regime; sharpens the constant in the monotone case from 27 to 4 — leaves the lower-bound–upper-bound gap at exactly 4×.
- Authors leave open: structurally weaker conditions than weak-MVI / negative comonotonicity that still permit accelerated rates, and a class of methods beyond span-of-past-gradients that could handle the worst-case Lipschitz-only example in Lemma 8.1.
- Stochastic S-FEG only stable under $\sigma_k^2 = O(1/k)$ noise decay; constant-noise stability via step-size adaptation (analogous to Devolder's analysis of Nesterov) is open.

## Key terms
extragradient method, anchoring, Halpern iteration, negative comonotonicity, cohypomonotonicity, weak Minty variational inequality, monotone operator, cocoercive, saddle-point problem, nonconvex-nonconcave minimax, squared gradient norm, accelerated first-order method, backtracking line-search, potential function analysis, GAN optimization
