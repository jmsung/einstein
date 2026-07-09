---
type: source
kind: paper
title: "TPU v4: An Optically Reconfigurable Supercomputer for Machine Learning with Hardware Support for Embeddings"
authors: N. Jouppi, George Kurian, Sheng Li, Peter C. Ma, R. Nagarajan, Lifeng Nai, Nishant Patil, Suvinay Subramanian, Andy Swing, Brian Towles, C. Young, Xiaoping Zhou, Zongwei Zhou, David A. Patterson
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2304.01433
source_local: ../raw/2023-jouppi-tpu-optically-reconfigurable-supercomputer.pdf
topic: general-knowledge
cites:
---

# TPU v4: An Optically Reconfigurable Supercomputer for Machine Learning with Hardware Support for Embeddings

**Authors:** N. Jouppi, George Kurian, Sheng Li, Peter C. Ma, R. Nagarajan, Lifeng Nai, Nishant Patil, Suvinay Subramanian, Andy Swing, Brian Towles, C. Young, Xiaoping Zhou, Zongwei Zhou, David A. Patterson  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2304.01433

## One-line
Describes Google's TPU v4 ML supercomputer, whose optical circuit switches (OCSes) reconfigure a 4096-chip 3D torus interconnect on the fly, and whose SparseCore accelerates embedding lookups for recommendation models.

## Key claim
TPU v4 outperforms TPU v3 by $2.1\times$ at $2.7\times$ better perf/Watt and scales to 4096 chips ($\sim 10\times$ aggregate); OCS-driven topology reconfiguration (including twisted $k\times k\times 2k$ 3D tori) improves all-to-all throughput by $1.31\times$–$1.63\times$ over regular tori while costing $<5\%$ of system capex and $<3\%$ of system power. SparseCore accelerates embeddings $5\times$–$7\times$ at $\sim 5\%$ die area.

## Method
Systems/architecture paper, not mathematical. Uses 3D MEMS-mirror OCSes as a "plugboard" between $4^3$ electrically-cabled blocks; 48 OCSes wire 64 blocks into a $16^3 = 4096$-chip 3D torus. Topology choice draws on Camarero-Martinez-Beivide twisted-torus lattice graphs to improve bisection bandwidth without recabling. SparseCore is a dataflow "sea of cores" with 16 SIMD tiles + cross-channel units over a 128 TiB globally addressable HBM space.

## Result
4096-chip TPU v4 supercomputer sustains $\sim 60\%$ of peak FLOPS/s on LLM training (PaLM 540B: $57.8\%$ over 50 days). Bisection bandwidth scales as $N^{2/3}$ for the 3D torus vs $N^{1/2}$ for the 2D torus on TPU v3, giving $2$–$4\times$ ratio at fixed $N$. Twisted tori chosen by 40% of $\geq 4^3$-chip jobs in production. Versus contemporaries: $1.2\times$–$1.7\times$ faster and $1.3\times$–$1.9\times$ lower power than A100; $4.3\times$–$4.5\times$ faster than Graphcore IPU Bow; $\sim 20\times$ lower CO2e than typical on-premise DSAs.

## Why it matters here
General background; no direct arena tie. Relevant only as compute-substrate context — TPU v4 / 3D-torus reasoning could inform [compute-router](knowledge/wiki/techniques/compute-router.md) decisions when considering TPU-class accelerators, but the Einstein Arena workloads use local workstation + Modal A100/H100, not TPU pods.

## Open questions / connections
- Does the $N^{2/3}$ vs $N^{1/2}$ bisection-bandwidth scaling argument carry over to MPI-style all-reduce workloads we'd want to run on Modal multi-GPU?
- Twisted-torus lattice graphs (Camarero-Martinez-Beivide; Sequin's doubly-twisted tori) are graph-theoretic objects — any tangential interest for arena's extremal-graph or discrete-geometry problems?
- Embedding-table sharding strategies (column/row/table) are orthogonal to math optimization, but the underlying "low arithmetic intensity, bisection-bandwidth-bound" framing is the dual of our compute-router classification.

## Key terms
TPU v4, optical circuit switch, OCS, MEMS, 3D torus, twisted torus, Camarero-Martinez-Beivide, bisection bandwidth, SparseCore, embedding lookup, DLRM, all-to-all, all-reduce, PaLM, LLM training, supercomputer interconnect, compute routing
