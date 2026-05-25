---
type: source
kind: paper
title: Bootstrap percolation and the geometry of complex networks
authors: Elisabetta Candellero, N. Fountoulakis
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1412.1301
source_local: ../raw/2014-candellero-bootstrap-percolation-geometry-complex.pdf
topic: general-knowledge
cites:
---

# Bootstrap percolation and the geometry of complex networks

**Authors:** Elisabetta Candellero, N. Fountoulakis  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1412.1301

## One-line
Identifies a sharp critical initial-infection rate $p_c(N) \sim N^{-1/(2\alpha)}$ for $r$-neighbor bootstrap percolation on Krioukov et al.'s hyperbolic random geometric graph model of complex networks.

## Key claim
For the hyperbolic random graph $G(N;\alpha,\nu)$ with $1/2 < \alpha < 1$ (power-law exponent $2\alpha+1 \in (2,3)$), activation threshold $r \geq 2$, and edge-retention probability $\rho \in (0,1]$: (i) if $p(N) N^{1/(2\alpha)} \to \infty$ then $|A_f|/N$ stays bounded away from 0 a.a.s.; (ii) if the limit is a positive constant, this holds with positive probability; (iii) if $p(N) N^{1/(2\alpha)} \to 0$, then $|A_f| = |A_0|$ a.a.s. The phenomenon is robust to constant-probability random edge deletion.

## Method
Exploits a dense "core" of vertices with type $t_v \geq R/2$ (near the circumference of radius $R/2\alpha$ in the native hyperbolic representation), which forms a clique by triangle inequality and survives Bernoulli edge-percolation as $G(N_0,\rho)$. Partitions the disk $D_R$ into homocentric bands $B_i$ with radii defined by the recursion $t_i = \lambda t_{i-1} - 2\ln(\ldots)$ where $\lambda = 2\alpha - 1$, and runs an inductive "black-block" argument: angular blocks on circle $C_i$ are black if covered by $\geq r$ disks of radius $R$ centered on vertices of the previous band. Concentration via Chernoff and Hoeffding-Azuma bounded-differences inequalities controls the propagation.

## Result
Theorem 1.2 establishes the sharp threshold $p_c(N) \asymp N^{-1/(2\alpha)}$. Corollary 1.3: $G(N;\alpha,\nu,\rho)$ has a giant component for all $\rho > 0$ (robust giant). Theorem 1.4: the $r$-core has linear size a.a.s. for every $r \geq 2$ and $\rho \in (0,1]$. The hyperbolic-law-of-cosines Lemma 2.1 yields the adjacency characterization $\theta_{u,v} < 2(1\pm\varepsilon)\exp\tfrac{1}{2}(t_u+t_v-R)$, recovering the Chung-Lu rank-1 kernel $\kappa(u,v) \propto e^{t_u/2}e^{t_v/2}/N$.

## Why it matters here
General background; no direct arena tie. The hyperbolic-plane construction (curvature $-\alpha^2$ disk, native representation, exponential type distribution) is a useful template for parameterizing power-law structures and for sphere-packing-adjacent geometric reasoning, but none of the 23 arena problems involve bootstrap percolation or complex-network degree distributions.

## Open questions / connections
- Extends Amini-Fountoulakis [AF14] result on Chung-Lu power-law graphs to the geometric (hyperbolic) setting where local clustering survives.
- Leaves open the regime $\alpha = 1/2$ (boundary of power-law exponent 2) and $\alpha \geq 1$ (no giant component, sublinear largest component per [BFM15]).
- Connects to Gugelmann-Panagiotou-Peter [GPP12] (degree sequence, clustering coefficient) and Kiwi-Mitsche [KM15] (second-largest component polylogarithmic in supercritical regime).

## Key terms
bootstrap percolation, hyperbolic random graph, Krioukov model, Chung-Lu model, power-law degree distribution, giant component, $r$-core, activation threshold, hyperbolic law of cosines, native representation, Chernoff bound, Hoeffding-Azuma inequality, inhomogeneous random graph, edge percolation robustness
