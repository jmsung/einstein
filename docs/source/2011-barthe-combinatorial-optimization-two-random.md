---
type: source
kind: paper
title: Combinatorial Optimization Over Two Random Point Sets
authors: F. Barthe, C. Bordenave
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1103.2734
source_local: ../raw/2011-barthe-combinatorial-optimization-two-random.pdf
topic: general-knowledge
cites:
---

# Combinatorial Optimization Over Two Random Point Sets

**Authors:** F. Barthe, C. Bordenave  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1103.2734

## One-line
Establishes Beardwood–Halton–Hammersley-style almost-sure limits for *bipartite* Euclidean optimization functionals (minimum matching, bipartite TSP, etc.) over two independent random samples in $\mathbb{R}^d$.

## Key claim
For $0 < 2p < d$ and i.i.d. $(X_i),(Y_j) \sim \mu$ with absolutely continuous part $f$ and tail moment $\int |x|^\alpha d\mu < \infty$ for $\alpha > \tfrac{4dp}{d-2p}$, the minimum bipartite matching cost $M_p$ satisfies $\limsup n^{p/d-1} M_p \le \beta_p(d) \int f^{1-p/d}$ and $\liminf \ge \beta_p'(d) \int f^{1-p/d}$ a.s., with equality (full limit) when $\mu$ is uniform on a bounded set, and conjecturally $\beta_p = \beta_p'$.

## Method
Develops an abstract framework for bipartite functionals $L(X,Y)$ via three axioms: $p$-homogeneity $(H_p)$, regularity $(R_p)$ (perturbation bound), and a *cardinality-corrected* subadditivity $(S_p)$ that absorbs the $|\mathrm{card}(X_i)-\mathrm{card}(Y_i)|$ imbalance term — the key fix that makes single-sample subadditive theory fail here. Lower bounds use *penalized boundary functionals* $L_{\partial S,\varepsilon}$ that identify $S^c$ to a single point at distance $\varepsilon$, plus an *inverse subadditivity* property $(I_p)$ (for $p \le 1$, via triangle inequality / Eulerian-circuit surgery) to handle the singular component of $\mu$. Poissonization + Azuma concentration upgrade $L^1$ convergence to a.s.

## Result
Generic Theorem 3: any bipartite functional satisfying $(H_p),(R_p),(S_p)$ has the $f^{1-p/d}$ upper-limit form, with equality on uniform measures. Theorem 2 specializes to $M_p$ with explicit moment threshold $\alpha > \tfrac{4dp}{d-2p}$ a.s. (relaxable to $\tfrac{2dp}{d-2p}$ for in-probability). Theorem 37 extends the matching lower bound + full limit to the bipartite TSP $T_p$ when $d\in\{1,2\}$ with $2p<d$, or $d\ge 3$ with $p\in(0,1]$. Strengthens and corrects Dobrić–Yukich (1995), whose Lemma 4.2 had a gap for non-uniform $f$.

## Why it matters here
General background; no direct arena tie — the wiki currently has nothing on bipartite-matching / Wasserstein-style stochastic geometry. Could inform any future problem cast as a transport / matching cost between two empirical measures (e.g., a probabilistic discrete-geometry problem on $\mathbb{R}^d$), and the $(H_p)/(R_p)/(S_p)$ axiom triple is a clean template for analyzing scaling rates of random combinatorial optimization functionals.

## Open questions / connections
- Is $\beta_p(d) = \beta_p'(d)$? (Authors strongly suspect yes but cannot close it.)
- Critical line $d=2p$: e.g. $d=2,p=1$ expected scaling $\sqrt{n \log n}$ (Ajtai–Komlós–Tusnády 1984; Talagrand–Yukich 1993) — open.
- Connection to stationary Poisson matchings (Holroyd–Pemantle–Peres–Schramm 2009; Huesmann–Sturm) — tightness of optimal matchings $\sigma_n$ as $n\to\infty$ yields a locally $L^p$-minimal stationary matching on two independent intensity-1 PPPs.
- Extends Beardwood–Halton–Hammersley (1959), Steele/Yukich umbrella theorem for single-sample functionals to the bipartite regime.

## Key terms
bipartite matching, Wasserstein distance, Beardwood-Halton-Hammersley, subadditive Euclidean functionals, boundary functional, inverse subadditivity, Poisson point process, Kantorovich-Rubinstein duality, bipartite traveling salesperson, Dobric-Yukich, optimal transportation, Barthe, Bordenave, Yukich umbrella theorem
