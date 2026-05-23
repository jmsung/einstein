---
type: source
kind: paper
title: Efficient implementation of elementary functions in the medium-precision range
authors: Fredrik Johansson
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1410.7176v2
source_local: ../raw/2014-johansson-efficient-implementation-elementary-functions.pdf
topic: general-knowledge
cites: 
---

# Efficient implementation of elementary functions in the medium-precision range

**Authors:** Fredrik Johansson  ·  **Year:** 2014  ·  **Source:** http://arxiv.org/abs/1410.7176v2

## One-line
A new implementation of $\exp, \sin, \cos, \log, \arctan$ for variable precision up to ~4096 bits, achieving 3×–30× speedup over MPFR with rigorous error bounds.

## Key claim
At precisions of 32–4096 bits, table-based argument reduction combined with an improved rectangular-splitting Taylor evaluation yields 3× (cos) to 30× (atan) speedup over MPFR 3.1.2, with proved error bounds of $\leq 2$ ulp internally and $\leq 10 \cdot 2^{-w}$ overall.

## Method
Uses table-based argument reduction (bipartite lookup tables for $\exp(i/2^r)$, $\sin/\cos$, $\log$, $\arctan$ values) plus Smith's rectangular splitting to evaluate Taylor series in $O(\sqrt{N})$ full multiplications. Key innovation: collects several consecutive denominators $1/(2k+1)$ or $1/k!$ into a single machine-word LCM $v_k$, replacing most $(n\times 1)$-word divisions with cheaper $(n\times 1)$-word multiplications. All arithmetic uses GMP's low-level `mpn` layer in fixed-point format to avoid floating-point overhead.

## Result
Benchmarks on Intel i7-2600S: at 53-bit precision, ~0.2–0.4 µs per function (within 10× of `libm`); at 113-bit (quad), 0.6–1.1 µs, comparable to QD library and ~5–20× faster than MPFR; at 1024 bits, 2–7 µs vs MPFR's 6–30 µs. Lookup tables total ~237 KiB (L2-cache-resident). Error analysis is verified by exhaustive symbolic execution over all allowed $N < 300$.

## Why it matters here
General background; no direct arena tie. Could marginally inform any Einstein Arena problem requiring high-precision mpmath polish (P5, P6, P11, P14, P17) — Arb (the library this implements) is a faster alternative to mpmath for ~100–4096 bit fixed-point work, relevant to the [[compute-router]] decision when local CPU mpmath is the bottleneck.

## Open questions / connections
- At 1–2 limb precision, minimax + Horner still beats rectangular splitting — gap to fixed-precision libraries (libquadmath, QD) remains.
- Progressive precision reduction in Taylor tail terms (term $k$ contributes less) not exploited; could halve cost of high-order multiplications.
- GMP lacks a "high half of $(n\times n)$ product" primitive; would give ~2× speedup if available.

## Key terms
elementary functions, arbitrary precision, MPFR, Arb library, rectangular splitting, Smith's algorithm, Taylor series evaluation, argument reduction, lookup tables, fixed-point arithmetic, GMP mpn, interval arithmetic, ball arithmetic, Johansson, medium precision, rigorous error bounds
