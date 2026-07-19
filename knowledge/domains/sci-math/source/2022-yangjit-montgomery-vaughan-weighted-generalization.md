---
type: source
kind: paper
title: On the Montgomery–Vaughan weighted generalization of Hilbert’s inequality
authors: Wijit Yangjit
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2203.14950
source_local: ../raw/2022-yangjit-montgomery-vaughan-weighted-generalization.pdf
topic: general-knowledge
cites:
---

# On the Montgomery–Vaughan weighted generalization of Hilbert's inequality

**Authors:** Wijit Yangjit  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2203.14950

## One-line
Proves a lower bound showing the standard "parametric family" route to the optimal constant in the Montgomery–Vaughan weighted Hilbert inequality cannot reach the conjectured value $\pi$.

## Key claim
The auxiliary constant $C(1/2)$ satisfies $C(1/2) \geq 0.35047\,\pi^2$, so any upper bound on the weighted-Hilbert constant $\mathcal{C}_1$ obtainable via the inequality $\mathcal{C}_1 \leq \pi^2/\sqrt{3} + 2C(1/2)$ cannot drop below $3.19497 > \pi$.

## Method
Studies a parametric family $C(\alpha)$ ($0 \le \alpha \le 2$) bounding $\sum \delta_m^{2-\alpha}\delta_n^\alpha t_m t_n / (\lambda_m-\lambda_n)^2$. Uses log-convexity / Hölder interpolation, a symmetry $C(\alpha)=C(2-\alpha)$, a weighted spacing lemma (Shan/Preissmann) giving $\sum \delta_k/|\lambda_k-\lambda_\ell|^\sigma \le 2\zeta(\sigma)/\delta^{\sigma-1}$, and a Cauchy/numerical-radius argument on skew-Hermitian generalized Hilbert matrices. The lower bound is extracted by evaluating an explicit functional $G_K(A)$ over choices $(K,A,B,u)$, with $G_5(0.14) > 0.35047$.

## Result
Establishes: (i) $C(\alpha)=C(2-\alpha)$, log-convex in $\alpha$, minimized at $\alpha=1$ with $C(1)=\pi^2/3$; (ii) $C(\alpha)=\infty$ for $\alpha<1/2$; (iii) Preissmann's bound $\mathcal{C}_1 \le \pi(2/\sqrt{3}+(2/3)^{6/5})$ recovered cleanly; (iv) the new lower bound $C(1/2) \ge 0.35047\pi^2$, blocking the parametric-family approach from reaching $\mathcal{C}_1=\pi$. Problem of determining $\mathcal{C}_1$ remains open.

## Why it matters here
General background for the autocorrelation / functional-inequality problem family — weighted Hilbert-type bounds underpin large-sieve and uncertainty-style arguments. Most concrete arena tie: a worked example of "proving an approach cannot reach the conjectured optimum" via a lower-bound on the auxiliary quantity — directly applicable to ruling out optimizer parameterizations and writing dead-end findings.

## Open questions / connections
- Determine $\mathcal{C}_1$ exactly; is $\mathcal{C}_1 = \pi$ (would strengthen Montgomery–Vaughan (1.2) to weighted form)?
- Find a fundamentally different route (not through $C(1/2)$) — e.g., Li's (2005) finite Hilbert transform question, or Montgomery–Vaaler's $H^2$ half-plane method.
- Locate Selberg's lost $\mathcal{C}_1 \le 3.2$ argument; what structure did it exploit beyond the parametric family?
- Tight asymptotic for $C(\alpha,N)$ at $\alpha < 1/2$ (paper shows $\gg N^{1/2-\alpha}$).

## Key terms
Hilbert inequality, Montgomery–Vaughan, weighted Hilbert inequality, large sieve, Preissmann, Selberg, Schur, generalized Hilbert matrix, skew-Hermitian eigenvalues, numerical radius, parametric family, log-convexity, Hölder interpolation, weighted spacing lemma, Graham–Vaaler majorants, autocorrelation inequality
