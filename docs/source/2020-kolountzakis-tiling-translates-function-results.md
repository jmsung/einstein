---
type: source
kind: paper
title: Tiling by translates of a function: results and open problems
authors: Mihail N. Kolountzakis, Nir Lev
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2009.09410v2
source_local: ../raw/2020-kolountzakis-tiling-translates-function-results.pdf
topic: general-knowledge
cites: 
---

# Tiling by translates of a function: results and open problems

**Authors:** Mihail N. Kolountzakis, Nir Lev  ·  **Year:** 2020  ·  **Source:** http://arxiv.org/abs/2009.09410v2

## One-line
A survey-plus-new-results paper on the structure of tilings $\sum_{\lambda \in \Lambda} f(x-\lambda) = w$ a.e. by translates of an $L^1$ function on $\mathbb{R}$, focusing on density, periodicity, level-zero, and unbounded-density phenomena.

## Key claim
Four new theorems: (1) every level-zero tiling $f+\Lambda$ of bounded density forces $\int f = 0$ and $\Lambda$ relatively dense; (2) non-periodic tilings exist with $f$ supported in arbitrarily sparse sets $\Omega$ (containing arbitrarily long intervals); (3) tilings of unbounded density exist with $\Lambda$ of tempered growth and $f$ Schwartz; (4) in any such unbounded-density Schwartz tiling, $\int f = 0$.

## Method
Fourier-analytic: tiling $\Leftrightarrow$ $\hat f \cdot \hat\delta_\Lambda = w \cdot \delta_0$; the necessary condition $\operatorname{supp}(\hat\delta_\Lambda) \setminus \{0\} \subset \{\hat f = 0\}$ from Wiener's tauberian theorem drives most arguments. New existence proofs use Kurasov–Sarnak crystalline measures plus an interpolation lemma (functions with sparse spectrum can match prescribed values on tempered-growth sets), and a Kargaev implicit-function / Banach fixed-point construction. The level-zero $\int f = 0$ proof uses Ruzsa–Székely convolution quotients; the relatively-dense proof uses Hardy-space ($H^1$) boundary uniqueness.

## Result
- Theorem 1.2: $f+\Lambda$ tiling at level 0 (bounded density, $\Lambda \neq \emptyset$, $f \in L^1$) $\Rightarrow \int f = 0$.
- Theorem 1.3: same hypotheses with $f \neq 0$ $\Rightarrow \Lambda$ relatively dense (in particular $D(\Lambda) > 0$ if it exists).
- Theorem 1.8: a single non-periodic $\Lambda$ of bounded density admits, for any prescribed level $w$ and any $\Omega$ with arbitrarily long intervals, a nonzero $f \in L^1$ with $\operatorname{supp}(f) \subset \Omega$ tiling at level $w$.
- Theorem 1.9 / 5.1: a set $\Lambda \subset \mathbb{R}$ of tempered growth (so $\#(\Lambda \cap (-r,r)) = O(r^3)$) but unbounded density, with $\hat\delta_\Lambda = \delta_0 - \delta_0''/(4\pi^2)$ on $(-1/2, 1/2)$, admits Schwartz tilings at any level.
- Theorem 1.10: in any tempered-growth/unbounded-density Schwartz tiling, $\hat f(0) = 0$.

## Why it matters here
General background on Fourier-analytic tiling and quasicrystal/crystalline-measure machinery; no direct Einstein Arena problem tie, but the interplay of $\hat f$-zero sets, sparse-spectrum interpolation, and Poisson-summation-type identities is the same toolbox that underlies Cohn–Elkies sphere-packing bounds and autocorrelation-uncertainty constructions used on packing/autocorrelation/uncertainty problems.

## Open questions / connections
- Does a bounded-density level-zero tiling always force a uniform density $D(\Lambda)$? Open even though $\Lambda$ is relatively dense.
- If $f \in L^1$ has $\{f \neq 0\}$ of finite measure (or $f = 1_\Omega$ with $\operatorname{mes}(\Omega) < \infty$) and tiles, must $\Lambda$ be periodic?
- Does compact-support $f$ + tempered-growth $\Lambda$ force $\Lambda$ to be a finite union of arithmetic progressions (Theorem 1.5 without bounded density)?
- Lattice-tiling conjecture: every $L^1$ tiling on $\mathbb{R}^d$ admits a lattice translation set (known for finite unions of translated lattices via Skolem–Mahler–Lech and Evertse–Schlickewei–Schmidt).
- Extends Kargaev '82, Leptin–Müller '91, Kolountzakis–Lagarias '96, Kolountzakis–Lev '16, Lev '20; relies on Kurasov–Sarnak '20 crystalline measures.

## Key terms
translational tiling, crystalline measures, quasicrystals, Poisson summation, spectral gap, uncertainty principle, Wiener tauberian theorem, Kargaev implicit function method, Kurasov–Sarnak, tempered growth, bounded density, relatively dense set, Hardy space $H^1$, Ruzsa–Székely, sparse spectrum interpolation, Cohn–Elkies background, Skolem–Mahler–Lech
