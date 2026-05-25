---
type: source
kind: paper
title: FI-modules and stability for representations of symmetric groups
authors: Thomas Church, J. Ellenberg, B. Farb
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1204.4533
source_local: ../raw/2012-church-fi-modules-stability-representations-symmetric.pdf
topic: general-knowledge
cites:
---

# FI-modules and stability for representations of symmetric groups

**Authors:** Thomas Church, J. Ellenberg, B. Farb  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1204.4533

## One-line
Introduces FI-modules — functors from the category of finite sets with injections to $k$-modules — as a unifying framework that converts "representation stability" for sequences of $S_n$-representations into a single finite-generation property, with broad applications across topology, combinatorics, and algebraic geometry.

## Key claim
For any finitely generated FI-module $V$ over a field of characteristic 0, the characters $\chi_{V_n}$ of the $S_n$-representations $V_n$ are eventually polynomial in the cycle-counting functions $X_i(\sigma) = \#\{i\text{-cycles in }\sigma\}$: there exist $r, N$ and a character polynomial $P(X_1,\ldots,X_r)$ with $\chi_{V_n}(\sigma) = P(X_1,\ldots,X_r)(\sigma)$ for all $n \geq N$. In particular $\dim V_n$ is eventually polynomial in $n$, with degree bounded by the weight of $V$.

## Method
Define the category FI of finite sets + injections; an FI-module is a functor $V:\text{FI}\to k\text{-Mod}$, yielding a sequence $V_n$ of $S_n$-representations with compatible maps. The Noetherian property (Thm 1.3: sub-FI-modules of f.g. FI-modules are f.g. when $\mathbb{Q}\subset k$) plus invariants — *weight* (highest $S_n$-irrep partition appearing) and *stability degree* (when the sequence stabilizes) — give effective bounds on $r$ and $N$. The richer FI♯-modules (allowing partial injections) are nearly semisimple: polynomial-bounded dimension forces *exact* polynomial dimension for all $n\geq 0$ (Thm 1.7).

## Result
Concrete corollaries proved by exhibiting finite generation: (i) $\dim H^i(\text{Conf}_n(M);\mathbb{Q})$ is polynomial of degree $\leq i$ in $n$ for $n\geq 2i$ on any connected oriented manifold of $\dim \geq 3$; example: $\chi_{H^2(\text{Conf}_n(\mathbb{R}^2);\mathbb{Q})} = \binom{X_1}{2} + \binom{X_1}{3} + 3\binom{X_1}{4} - \binom{X_1}{2}X_2 + \binom{X_2}{2} - X_3 - X_4$ for all $n\geq 0$. (ii) Multivariate diagonal coinvariant graded pieces $R^{(r)}_J(n)$ have $\dim = P^{(r)}_J(n)$ polynomial of degree $\leq |J|$ for large $n$ (resolves growth-rate question for $r>2$). (iii) Tautological ring $R^j(\mathcal{M}_{g,n})$, Albanese cohomology $H^i_{\text{Alb}}(I_n^1;\mathbb{Q})$ and $H^i_{\text{Alb}}(IA_n;\mathbb{Q})$ all have eventually-polynomial dimensions (degree $\leq 3i$ for the Torelli cases). (iv) Murnaghan's stability of Kronecker coefficients $g_{\lambda,\mu}^{\nu}$ falls out as f.g. of $V(\lambda)\otimes V(\mu)$.

## Why it matters here
General background; no direct arena tie — none of the 23 Einstein Arena problems are about $S_n$-representation stability or configuration-space cohomology. Possible thin connection: the *eventually-polynomial-in-$n$* paradigm could inform meta-analysis of how solution-quality scales with problem size in families (e.g., sphere packing in $\mathbb{R}^d$ across $d$, or Sidon-set growth), but this is speculative — the paper's machinery is representation-theoretic, not optimization-theoretic.

## Open questions / connections
- Problem 1.10/1.12: explicit formulas for $R^{(r)}_J(n)$ characters when $r > 2$ remain unknown; FI-module theory bounds degree but is non-constructive.
- Specifying the polynomials in Theorem 1.5 for specific FI-modules (e.g., $H^i_{\text{Alb}}(I_n^1)$ for $i\geq 3$) is open — Noetherian-derived bounds are not effective.
- Connection to Deligne's category $\text{Rep}(S_t)$: can a finite-type object specialize to a f.g. FI-module? (Raised re: Ren–Schedler invariant differential operators.)
- Extended by Church–Ellenberg–Farb–Nagpal [CEFN] to arbitrary Noetherian rings; by Wilson to other Weyl groups (FI$_W$); by Sam–Snowden to twisted commutative algebras.

## Key terms
FI-module, representation stability, character polynomial, symmetric group $S_n$, configuration space cohomology, diagonal coinvariant algebra, tautological ring, Torelli group, Noetherian category, Murnaghan stability, Kronecker coefficients, Church-Farb, eventually polynomial dimension, finitely generated functor
