---
type: source
kind: paper
title: "Phase Retrieval: An Overview of Recent Developments"
authors: Kishore Jaganathan, Yonina C. Eldar, B. Hassibi
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1510.07713
source_local: ../raw/2015-jaganathan-phase-retrieval-overview-recent.pdf
topic: general-knowledge
cites:
---

# Phase Retrieval: An Overview of Recent Developments

**Authors:** Kishore Jaganathan, Yonina C. Eldar, B. Hassibi  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1510.07713

## One-line
Survey of modern algorithms and uniqueness theory for recovering a signal from the magnitude of its Fourier (or short-time Fourier) transform, emphasizing sparsity priors, mask-based measurements, and STFT redundancy.

## Key claim
Phase retrieval — generically ill-posed in 1D with up to $2^N$ non-equivalent solutions — becomes well-posed (up to trivial ambiguities) under three regimes: (i) sparse signals with aperiodic support, (ii) two generic masks giving $M \geq 2N$ Fourier magnitudes, and (iii) STFT magnitude with sufficient short-time overlap ($L < W \leq N/2$). TSPR provably recovers most $O(N^{1/2-\epsilon})$-sparse signals and is robust for $O(N^{1/4-\epsilon})$-sparse signals.

## Method
Three algorithmic families are reviewed: (1) **Alternating projections** (Gerchberg–Saxton, Fienup HIO) — non-convex, often trap in local minima; (2) **Semidefinite lifting** ($X = xx^*$, replace $\mathrm{rank}(X)$ with $\mathrm{trace}(X)$) giving PhaseLift and its $\ell_1$-regularized sparse / STFT variants (STliFT); (3) **Combinatorial/greedy** methods — TSPR uses Turnpike-style reconstruction of support from pairwise-distance set $B = \{n : a[n] \neq 0\}$, then SDP on the restricted support; GESPAR runs 2-opt support swaps with damped Gauss–Newton inner solves.

## Result
For 1D sparse phase retrieval: collision-free autocorrelation suffices for $k \neq 6$ (Ranieri); $k^2 - k + 1$ Fourier-magnitude measurements suffice (Ohlsson–Eldar); aperiodic-support signals are almost-surely identifiable (Jaganathan). For STFT: non-vanishing signals are uniquely recoverable up to global phase when $L = 1$, $2 \leq W \leq N/2$, $\gcd(W-1, N) = 1$; sparse signals with $< \min\{W-L, L\}$ consecutive zeros are recoverable when $L < W \leq N/2$. Numerical simulations: GESPAR recovers $N=6400$ signals up to $k \approx 57$; TSPR up to $k \approx 53$; HIO far worse.

## Why it matters here
General background; no direct arena tie. The lifting / trace-relaxation machinery here is the same technical scaffolding used in Cohn–Elkies-style LP/SDP bounds (sphere packing, kissing number), and the "rank-1 PSD constraint + linear measurements" pattern recurs in autocorrelation problems — relevant as methodology cross-reference for P1, P14, P17, and any autocorrelation/extremal-sequence problem where the SDP relaxation is loose.

## Open questions / connections
- How tight is the SDP/trace-norm relaxation when the rank-1 primal is unique — extends the dead-end finding `sdp-relaxation-uselessness` (P1) into a structural question about when lifting preserves vs destroys the optimum.
- Turnpike (reconstructing an integer set from its pairwise distance multiset) — directly applicable to any autocorrelation-uniqueness question in arena problems.
- Minimum number of masks / measurements for unique + robust recovery remains open in full generality; analog of "how much structure must we add to the LP/SDP to close the gap."

## Key terms
phase retrieval, Fourier magnitude, autocorrelation, PhaseLift, semidefinite relaxation, trace-norm minimization, GESPAR, TSPR, Gerchberg-Saxton, Fienup HIO, STFT, sparse recovery, Turnpike problem, collision-free autocorrelation, lifting, Wirtinger flow, compressed sensing, Hayes uniqueness, Candes, Eldar
