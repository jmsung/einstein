---
type: source
kind: paper
title: Faster Arbitrary-Precision Dot Product and Matrix Multiplication
authors: Fredrik Johansson
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1901.04289
source_local: ../raw/2019-johansson-faster-arbitrary-precision-dot-product.pdf
topic: general-knowledge
cites:
---

# Faster Arbitrary-Precision Dot Product and Matrix Multiplication

**Authors:** Fredrik Johansson  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1901.04289

## One-line
Treats the entire dot product as one atomic GMP-limb-level operation with a fixed-point accumulator, yielding 2–4× speedups for arbitrary-precision real/complex floating-point and ball arithmetic in the Arb library.

## Key claim
A single-pass arbitrary-precision dot product implemented on raw GMP limb arrays costs only 20–30 cycles/term (float) and 40–50 cycles/term (ball) up to 128-bit precision — roughly 2× faster than MPFR and 3–4× faster than naive `arb_addmul` loops — while a scaled-integer block matrix-multiplication algorithm gives up to 16× speedup over classical multiplication at $N=1000$, $p=3392$ bits, with entrywise-optimal accuracy preserved.

## Method
A two-pass dot-product algorithm: pass 1 scans all terms to determine accumulator exponent, working precision, and exceptional cases; pass 2 writes each $m_i m'_i$ product directly into a two's-complement fixed-point limb accumulator (sized $p + \text{extend} + \text{padding}$ bits), with a separate `prad`-bit (30-bit) radius accumulator for ball error propagation. The matrix algorithm splits $A$ into column blocks $A_s$ and $B$ into row blocks $B_s$, applies row/column diagonal scaling matrices $E_s, F_s$ so $(E_s A_s)(B_s F_s)$ has bounded integer height $h \approx 1.25\min(p,\max(p_A,p_B))+192$, multiplies over $\mathbb{Z}$ via FLINT (classical/Strassen/multimodular with 60-bit primes), then unscales. Radius products $|A|R_B$ and $R_A(|B|+R_B)$ are computed via the analogous block strategy over `double`.

## Result
At $p=128$ bits the ball dot product reaches ~50 cycles/term (4.2× over `addmul`, 2× over MPFR); at $p=212$ both the approx and ball versions beat QD quad-double by ~2×. Ball-arithmetic error propagation adds only ~20 cycles/term constant overhead. For uniform $1000\times1000$ real matrices the block algorithm is 5.3× faster than classical Arb at $p=53$ and 16× faster at $p=3392$; for ill-scaled Pascal-like matrices the block strategy degrades and classical dot-products win for $p\le128$. Downstream: Newton-based series inversion, $\exp$/$\sin$/$\cos$ on power series, characteristic polynomial, and linear solves all gain 2–5× from Arb 2.14→2.15.

## Why it matters here
General background; no direct arena tie — but mpmath/Arb-style arbitrary-precision arithmetic is the workhorse for the project's ulp-polish stage on float-precision-critical problems (P5, P6, P11, P14, P17 per `.claude/rules/triple-verify.md`), so any wisdom about *where* arbitrary-precision cost dominates (atomic dot products good; sequential per-op multiply-add bad) and *which* operations vectorize over GMP limbs is relevant when tuning the local-CPU compute-router path. Suggests that mpmath polish loops written as explicit dot products (rather than per-term `+= a*b`) realize substantial constant-factor speedups for free.

## Open questions / connections
- Could a Horner-scheme polynomial evaluation be made atomic in the same way, removing per-step overhead in evaluators that compute $\sum a_i x^i$ (used in modular-form / theta-series style approaches to P11)?
- Block matrix multiplication via scaled integers loses the "discard negligible limbs" optimization that classical dot products keep — what's the right hybrid for non-uniformly-scaled matrices like Pascal-type Gram matrices arising in sphere-packing LP bounds?
- Hansen–Smith preconditioning is 3–6× slower than direct LU in ball arithmetic but stable for ill-conditioned systems — relevant when solving rank-deficient LP-bound systems where LU loses $O(N)$ digits.

## Key terms
arbitrary-precision arithmetic, ball arithmetic, midpoint-radius interval, fixed-point accumulator, GMP limb, MPFR, Arb library, FLINT, multimodular reconstruction, Strassen multiplication, Hansen-Smith preconditioning, QR algorithm verification, mpmath polish, Johansson
