---
type: source
kind: paper
title: Extremizers for adjoint Fourier restriction on hyperboloids: the higher dimensional case
authors: Emanuel Carneiro, Diogo Oliveira e Silva, Mateus Sousa, Betsy Stovall
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1809.05698v1
source_local: ../raw/2018-carneiro-extremizers-adjoint-fourier-restriction.pdf
topic: general-knowledge
cites: 
---

# Extremizers for adjoint Fourier restriction on hyperboloids: the higher dimensional case

**Authors:** Emanuel Carneiro, Diogo Oliveira e Silva, Mateus Sousa, Betsy Stovall  ·  **Year:** 2018  ·  **Source:** http://arxiv.org/abs/1809.05698v1

## One-line
Proves that maximizers exist for the non-endpoint, Lorentz-invariant $L^2 \to L^p$ adjoint Fourier restriction inequality on the $d$-dimensional hyperboloid $\mathbb{H}^d$ when $d \geq 3$.

## Key claim
For $d \geq 3$ and $\frac{2(d+2)}{d} < p < \frac{2(d+1)}{d-1}$, extremizers of the Strichartz–type estimate $\|T(f)\|_{L^p(\mathbb{R}^{d+1})} \leq \mathbf{H}_{d,p} \|f\|_{L^2(\mathbb{H}^d)}$ exist; moreover, every extremizing sequence converges in $L^2(\mathbb{H}^d)$ to an extremizer modulo Lorentz boosts and space-time modulations, after passing to a subsequence.

## Method
Bilinear restriction theory: the authors set up a hybrid dyadic decomposition of frequency space into "caps" (elliptic regime, $r \leq 1$) and "sectors" (conic regime, $1 < r \leq N$), interpolating between paraboloid and cone geometry. Bilinear extension estimates on separated regions, combined with an annular Littlewood–Paley decoupling derived from mixed-norm Strichartz, yield a refined Strichartz inequality (Theorem 4) that localizes mass to a single cap/sector. Concentration-compactness machinery from the precursor [3, Section 6] then upgrades this to strong convergence of an extremizing sequence.

## Result
Theorem 1: extremizers exist on $\mathbb{H}^d$ for all $d \geq 3$ throughout the open admissible range $\frac{2(d+2)}{d} < p < \frac{2(d+1)}{d-1}$. The bilinear estimates (Proposition 3) yield exponents $N^{-2d/s} r^{2(d/s' - (d+2)/p)}$ (caps) and $N^{-2(d-1)/s} r^{2(d-1)/s' - 2(d+1)/p}$ (sectors) for $s < 2$ arbitrarily close to $2$, and the refined Strichartz controls $\|T(f_N)\|_{L^p}^p$ by a supremum of single-region contributions times $\|f_N\|_{L^2}^{p(1-\gamma)}$. Endpoint cases $(d,p) = (2,4), (2,6), (3,4), (1,6)$ — where $p$ is even and extremizers are known not to exist — remain excluded.

## Why it matters here
General background; no direct arena tie. Fourier restriction / Strichartz extremizers and bilinear restriction theory are not currently mapped to any of the 23 Einstein Arena problems in `knowledge/wiki/problems/_inventory.md` — closest neighbors would be functional-inequality / uncertainty problems, but this paper's machinery (Lorentz boosts on hyperboloids, Klein–Gordon dispersive estimates) does not align with sphere packing, autocorrelation, or extremal graph problems in scope.

## Open questions / connections
- Endpoint existence at $p = \frac{2(d+1)}{d-1}$ for $d \geq 3$ remains open (proof requires the strict inequality).
- Quilodrán [13] handles a different endpoint ($d=4$, $L^2 \to L^4$ on the one-sheeted hyperboloid); the gap between even-integer endpoints and the open range is the recurring theme.
- Extends Carneiro–Oliveira e Silva–Sousa [3] from $d \in \{1,2\}$ (convolution / even-$p$ structure) to $d \geq 3$ (bilinear).
- Bilinear "cap vs sector" decomposition could in principle be reused for other surfaces with mixed elliptic/conic curvature regimes.

## Key terms
adjoint Fourier restriction, hyperboloid, Strichartz inequality, Klein–Gordon equation, extremizers, bilinear restriction, Lorentz boost, concentration-compactness, refined Strichartz, Littlewood–Paley decoupling, cap-sector decomposition, Carneiro Oliveira-e-Silva Sousa Stovall
