---
type: source
kind: paper
title: "Wanted: Floating-Point Add Round-off Error instruction"
authors: Marat Dukhan, Richard Vuduc, Jason Riedy
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1603.00491v1
source_local: ../raw/2016-dukhan-wanted-floating-point-add-round-off.pdf
topic: general-knowledge
cites:
---

# Wanted: Floating-Point Add Round-off Error instruction

**Authors:** Marat Dukhan, Richard Vuduc, Jason Riedy  ·  **Year:** 2016  ·  **Source:** http://arxiv.org/abs/1603.00491v1

## One-line
Proposes a new hardware instruction FPADDRE that returns the round-off error of a floating-point add, collapsing the 6-instruction error-free addition (EFT) of Knuth/Dekker down to 2 independent instructions.

## Key claim
A hardware FPADDRE instruction (paired with FPADD) would cut double-double addition latency by up to 55% and lift throughput by up to 103%, yielding up to 2× end-to-end speedup on compensated Horner, compensated dot product, and double-double GEMM — without changing IEEE-754 semantics.

## Method
Architectural proposal + simulation study. The authors define FPADDRE as a variant of FPADD that emits the trailing (normally discarded) bits of the rounded sum, so $a+b = \mathrm{FPADD}(a,b) + \mathrm{FPADDRE}(a,b)$ exactly. They simulate it on Intel Skylake/Haswell, AMD Steamroller, and Xeon Phi (Knights Corner) by substituting an instruction of identical latency/throughput (e.g. `min(a,b)` or `fma(a,a,b)`) — correct numerics are sacrificed but control flow and timing are preserved. Microbenchmarks and three application kernels (compensated Horner, compensated dot product, DDGEMM inner kernel) are profiled with and without the simulated instruction.

## Result
Compared to Knuth's 6-instruction TwoSum, FPADDRE-based EFT uses 2 instructions in 1 latency slot (vs. 6 in 5). Measured speedups across the four architectures: compensated Horner −13%…−29% latency; compensated dot product +29%…+95% throughput (cache-resident); DDGEMM micro-kernel +28%…+93%, shrinking the DDGEMM-vs-DGEMM penalty from 35–69× down to 14–24×. A symmetric instruction FPMULRE is also sketched as a cheaper alternative to FMA for the multiplication EFT.

## Why it matters here
General background; no direct arena tie. Relevant only as context for the project's mpmath/double-double polish steps on float-precision-critical problems (P5, P6, P11, P14, P17) — it explains why software double-double is currently 30–60× slower than DP and clarifies that the bottleneck is the EFT instruction count, not the algorithm. Does not change any current technique choice.

## Open questions / connections
- Would FPADDRE/FPMULRE actually appear in a future x86 or ARM ISA? (Paper is a proposal, not a deployment.)
- Connects to Ogita–Rump–Oishi FPADD3 and Demmel–Nguyen reproducible summation — alternative routes to the same speedup that don't require new hardware.
- Open: software-only tricks (better SIMD scheduling, AVX-512 mask tricks) that approximate the FPADDRE win on current chips for our mpmath polish pipelines.

## Key terms
floating-point round-off error, FPADDRE, error-free transformation, TwoSum, Dekker, Knuth, double-double arithmetic, compensated Horner scheme, compensated dot product, fused multiply-add, FMA, reproducible summation, DDGEMM, high-precision arithmetic
