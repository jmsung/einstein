---
type: source
kind: paper
title: Modular SIMD arithmetic in Mathemagix
authors: J. Hoeven, Grégoire Lecerf, G. Quintin
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1407.3383
source_local: ../raw/2014-hoeven-modular-simd-arithmetic-mathemagix.pdf
topic: general-knowledge
cites:
---

# Modular SIMD arithmetic in Mathemagix

**Authors:** J. Hoeven, Grégoire Lecerf, G. Quintin  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1407.3383

## One-line
Survey and SIMD-vectorized implementation of modular integer arithmetic (Barrett, Montgomery, floating-point) in the Mathemagix C++ system, applied to FFT, integer/polynomial/matrix products.

## Key claim
Hand-vectorized branch-free modular arithmetic on SSE 4.2 / AVX 2 yields near-theoretical speedups (≈4–8×) over scalar code and lets Mathemagix's modular FFT outperform NTL, FLINT, LinBox, and GMP on polynomial, integer, and small-matrix products — sometimes by an order of magnitude.

## Method
Rewrite Barrett's and Montgomery's reductions, plus the floating-point inverse approach, in branch-free form so they vectorize cleanly across SSE/AVX intrinsics. Combine with a vectorized truncated Fourier transform (TFT) over prime fields $\mathbb{F}_p$ with $p-1$ divisible by a large power of two ($p=k\cdot 2^l+1$), splitting size-$l$ TFT into an outer transform over $K^{n_1}$ (vector lanes) and inner transform over $K$. C++ template "implementation variants" select the best algorithm per modulus bit-size $m$ vs register width $n$.

## Result
For $p=469762049=7\cdot 2^{26}+1$, AVX FFT of size $2^{20}$ runs in ~6.8 ms vs ~32 ms scalar (~5× speedup); modular sum drops from ~2.4 cycles (scalar) to ~0.16 (AVX 2) at $m\le 31$. Polynomial product at degree $2^{20}$ over this prime: 60 ms (Mathemagix AVX) vs 580 ms (NTL), 610 ms (FLINT). Integer matrix product at $32\cdot 2^{15}$-bit entries: 13 s vs 140 s (GMP/LinBox). Branch-free Barrett with $\beta=2^{n-2}$ and parameters $s=\max(r-2,0), t=n+1$ achieves bound-tightening factor $h=1$ (no correction loop).

## Why it matters here
General background; no direct arena tie. Potentially relevant if any Einstein Arena problem reduces to large-integer or polynomial matrix arithmetic over $\mathbb{F}_p$ (e.g., LP/SDP solvers with exact rationals, number-theoretic verifications), in which case Mathemagix-style modular FFT could replace mpmath for exact reductions.

## Open questions / connections
- Could AVX-512 (post-2014) push these speedups further, especially for $m=63,64$ where 64-bit lane width currently limits gains?
- Automatic generation of FFTW3-style codelets for SIMD modular FFT remains open.
- Hardware $8\times 8$ transpose for 32-bit integers would close the remaining gap on small-size FFTs.

## Key terms
modular arithmetic, Barrett reduction, Montgomery reduction, SIMD, SSE, AVX, FMA, truncated Fourier transform, TFT, FFT, Kronecker substitution, three-prime FFT, polynomial multiplication, integer matrix product, Mathemagix, finite field $\mathbb{F}_p$, branch-free reduction, vectorization
