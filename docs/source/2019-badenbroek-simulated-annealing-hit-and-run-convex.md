---
type: source
kind: paper
title: Simulated annealing with hit-and-run for convex optimization: rigorous complexity analysis and practical perspectives for copositive programming
authors: Riley Badenbroek, Etienne de Klerk
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1907.02368v1
source_local: ../raw/2019-badenbroek-simulated-annealing-hit-and-run-convex.pdf
topic: general-knowledge
cites: 
---

# Simulated annealing with hit-and-run for convex optimization: rigorous complexity analysis and practical perspectives for copositive programming

**Authors:** Riley Badenbroek, Etienne de Klerk  ·  **Year:** 2019  ·  **Source:** http://arxiv.org/abs/1907.02368v1

## One-line
Rigorous polynomial-time complexity proof for Kalai–Vempala simulated annealing using Abernethy–Hazan's entropic-barrier temperature schedule, plus practical heuristics tested on copositive programming.

## Key claim
With temperature update $T_k = (1 - \tfrac{1}{\alpha\sqrt{\vartheta}}) T_{k-1}$ for $\alpha > 1 + 1/\sqrt{\vartheta}$ (where $\vartheta$ is the entropic barrier's complexity parameter, $\vartheta \le n + o(n)$), Algorithm 2 returns a near-optimal solution to $\min_{x \in K} \langle c, x \rangle$ in $m = O^*(\sqrt{\vartheta})$ phases with high probability, using only a membership oracle.

## Method
Markov-chain simulated annealing over Boltzmann distributions $\propto e^{\langle \theta, x \rangle}$ on a convex body $K$, with hit-and-run sampling (Smith 1984) using directions drawn from $N(0, \widehat{\Sigma}(\theta_{k-1}))$ where $\widehat{\Sigma}$ is the empirically estimated covariance of the previous Boltzmann. Mixing analysis transports the body via $\Sigma(\theta_0)^{-1/2}$ to near-isotropic position, then applies Rudelson-style $L^2$-divergence bounds between consecutive Boltzmanns. Heuristic Algorithm 3 reuses centered samples as hit-and-run directions (skipping explicit covariance estimation), chains walks instead of restarting, and uses previous-iteration sample mean as the warm start.

## Result
Theorem 9/Corollary 10 give an explicit hit-and-run path length $\ell = \tilde{O}(n^3)$ per phase guaranteeing total-variation distance $\le q$ to the target Boltzmann. Appendix A gives numerical evidence that for the Euclidean unit ball $B^n$, $\vartheta = (n+1)/2$. Numerical experiments on doubly-nonnegative cone (sizes $m \in \{5,10,15,20\}$, $n = m(m+1)/2$) show the heuristic $N = \ell = n\sqrt{n}$ suffices for final gap $\sim \bar{\epsilon}/p$; ten random extreme-ray $6\times 6$ doubly-nonnegative matrices were strictly separated from the completely-positive cone via copositive program (19), but the Ellipsoid method needed $\sim 10^3$ oracle calls vs $\sim 10^7$ for Algorithm 3.

## Why it matters here
General background on membership-oracle convex optimization; the entropic barrier's $\vartheta \le n + o(n)$ and the conjecture $\vartheta = (n+1)/2$ for $B^n$ are relevant context for SDP/LP-bound work on sphere packing and kissing-number problems. The practical takeaway — hit-and-run covariance/mean estimation is impractical in high dimensions and cutting-plane methods dominate — is a cautionary note for any sampling-based optimizer in the arena's LP/SDP families.

## Open questions / connections
- Is $\vartheta < n$ for any convex body? Required for Abernethy–Hazan schedule (4) to beat Kalai–Vempala's $O^*(\sqrt{n})$ schedule (needs $\vartheta < n/16$).
- Prove the numerical conjecture $\vartheta_{B^n} = (n+1)/2$ analytically.
- Generating separating cuts from the completely-positive cone for general doubly-nonnegative $Y$ remains open (Berman–Dür–Shaked-Monderer 2015); only specific structures (e.g., $5\times 5$ Burer–Dong) are solved.

## Key terms
simulated annealing, hit-and-run sampling, Boltzmann distribution, entropic barrier, self-concordant barrier, complexity parameter, convex optimization, membership oracle, Kalai-Vempala, Abernethy-Hazan, copositive programming, doubly nonnegative cone, completely positive cone, isotropic position, total variation distance, ellipsoid method, Bubeck-Eldan, interior point method
