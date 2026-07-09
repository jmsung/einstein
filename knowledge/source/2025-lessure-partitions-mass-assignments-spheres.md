---
type: source
kind: paper
title: Partitions of mass assignments with spheres and wedges
authors: Deron Lessure, Pablo Sober'on
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2507.06919
source_local: ../raw/2025-lessure-partitions-mass-assignments-spheres.pdf
topic: general-knowledge
cites:
---

# Partitions of mass assignments with spheres and wedges

**Authors:** Deron Lessure, Pablo Sober'on  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2507.06919

## One-line
Extends three classical mass-partition theorems (Stone–Tukey spheres, Takahashi–Soberón parallel hyperplanes, Uno–Kawano–Kano axis-parallel wedges) from $\mathbb{R}^k$ to the mass-assignment setting, where measures are continuously assigned to $k$-dimensional subspaces of $\mathbb{R}^d$ and one is free to choose the subspace.

## Key claim
For $1 \le k \le d$: (1) $d+1$ mass assignments on $k$-affine subspaces admit a $k$-subspace $L$ and a sphere in $L$ bisecting all of them, with $k-1$ directions of $L$ prescribable, and $d+1$ is optimal; (2) the same count works for two parallel hyperplanes bounding a slab; (3) $d$ mass assignments to vertical 2-planes in $\mathbb{R}^d$ admit a vertical plane with an axis-parallel wedge bisecting all of them.

## Method
Topological: each problem reduces to finding zeros of a $(\mathbb{Z}_2)^{d-k+1}$-equivariant continuous map $f : S^d \times V_{d-k}(\mathbb{R}^d) \to \mathbb{R}^d \times \mathbb{R}^{d-1} \times \cdots \times \mathbb{R}^k$ on a product of a sphere and a Stiefel manifold. A new Borsuk–Ulam-type theorem (Theorem 2.1) is proved via Bárány's complementary-pivoting / Musin-style homotopy argument with a model map $g$ having a single equivariant orbit of zeros. Spherical partitions are encoded by lifting $\mathbb{R}^d \hookrightarrow \mathbb{R}^{d+1}$ then applying inversion $\sigma(x) = x/\|x\|^2$ (hyperplanes ↔ spheres); parallel-hyperplane partitions use a parabolic lift; the wedge result uses a planar down-wedge degree argument on $S^{d-2}$.

## Result
Theorems 1.2, 1.4, 1.6 establish the bisection counts above. Optimality (Claim 3.1): $d+2$ projected radial measures around a regular simplex with barycenter cannot all be sphere-bisected on any $k$-subspace — the argument uses only convexity, so it also pins down optimality of the parallel-hyperplane version. Corollary 1.3 gives a concrete instance: any 4 families of generic non-vertical lines in $\mathbb{R}^3$ admit a vertical circle splitting each family in half by "goes around / doesn't".

## Why it matters here
General background; no direct arena tie. Mass-partition / Borsuk–Ulam machinery is adjacent to discrete-geometry problems (kissing, packing, point-configuration extremals) but the arena's existing problems are not framed as bisection problems, so this paper is reference-shelf material for topological-combinatorics techniques rather than an immediate solver.

## Open questions / connections
- Extends Schnider's ham-sandwich for mass assignments [Sch20] and Soberón–Takahashi's parallel-hyperplane partition [ST23] to spheres, slabs, and wedges in the mass-assignment regime.
- Whether the wedge theorem extends past $d=2$-style wedges to higher-dimensional axis-parallel cones, or to more than $d$ assignments under symmetry assumptions, is open.
- Whether prescribing $k-1$ directions can be replaced by prescribing other geometric constraints (curvature, tangency) while keeping the $d+1$ count.

## Key terms
mass assignment, ham sandwich theorem, Borsuk–Ulam, Stiefel manifold, equivariant map, $(\mathbb{Z}_2)^k$ action, Stone–Tukey sphere partition, Takahashi–Soberón parallel hyperplanes, axis-parallel wedge, Fadell–Husseini index, inversion lift, mass partition optimality
