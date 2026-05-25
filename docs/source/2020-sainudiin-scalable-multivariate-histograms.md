---
type: source
kind: paper
title: Scalable Multivariate Histograms
authors: Raazesh Sainudiin, Warwick Tucker, Tilo Wiklund
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2012.14847v1
source_local: ../raw/2020-sainudiin-scalable-multivariate-histograms.pdf
topic: author-sweep
cites: 
---

# Scalable Multivariate Histograms

**Authors:** Raazesh Sainudiin, Warwick Tucker, Tilo Wiklund  ·  **Year:** 2020  ·  **Source:** http://arxiv.org/abs/2012.14847v1

## One-line
A distributed (Apache Spark / MapReduce) algorithm for building adaptive multivariate histogram density estimators on tree-based partitions (regular pavings) so they scale to datasets too large for a single machine.

## Key claim
Adaptive histogram estimation over statistical regular pavings (SRPs) — previously a sequential procedure — can be parallelized exactly by (i) splitting all cells exceeding a priority threshold simultaneously, then (ii) backtracking via sibling-merger to recover the canonical sequential path, with no change to the resulting estimator. Demonstrated on $n = 13 \times 10^7$ points in 2D and 10D.

## Method
Partitions are encoded as **regular pavings (RPs)**: binary trees built by recursively bisecting the root box along its first widest coordinate, giving partitions closed under addition/scalar multiplication. **Priority-queued Markov chains (PQMCs)** drive splits: SEB-PQMC (priority = cell count) for data-dense regions and SPC-PQMC (priority = $(1 - \#x_{\rho v}/n)\,\mathrm{vol}(\rho v)$) for carving empty space; the two are run jointly. Distributed implementation tags each data point by its current cell ID (binary path encoding via multi-precision int), uses `countByKey`-style reduces to get cell counts, splits all over-threshold cells in parallel via a point-wise map, and reconstructs the sequential path by merging in least-priority order. Smoothing is chosen by Stone's leave-one-out cross-validation minimizing $J(\tau)$, a near-unbiased estimator of expected $L_2$ loss.

## Result
On a 5-worker Spark cluster (30 GB, 4.4 cores), $n = 1.3 \times 10^8$ points: 2D run in ≈1.79 h with estimated $L_1$ error 0.03; 10D run in ≈5.8 h with $L_1$ error 1.13. The class of RP simple functions is dense in $C(x_\rho, \mathbb{R})$ (Stone–Weierstrass), and SEB-PQMC partitioning is asymptotically $L_1$-consistent (satisfies Lugosi–Nobel conditions).

## Why it matters here
General background; no direct arena tie. Possibly tangential to high-dimensional density estimation / empirical-measure approximations that could appear in sieve-theory or autocorrelation problems, but no current arena problem is a density-estimation task.

## Open questions / connections
- Extends Lugosi–Nobel (1996) data-driven histogram consistency and Sainudiin–Teng (2019) minimum distance histograms to the distributed regime.
- Leaves open: how to handle non-axis-aligned splitting hyperplanes, and whether priority functions beyond count/volume admit the same parallel-then-backtrack trick.
- Connection to dyadic histograms (Klemelä; Lu–Jiang–Wong Bayesian sequential partitioning) — RPs strictly contain complete dyadic trees but restrict to widest-coord splits.

## Key terms
density estimation, regular pavings, statistical regular pavings, priority-queued Markov chain, MapReduce, Apache Spark, adaptive histogram, dyadic partition, leave-one-out cross-validation, Stone-Weierstrass, statistically equivalent blocks, support carving
