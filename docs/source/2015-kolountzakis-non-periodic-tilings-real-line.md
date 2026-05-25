---
type: source
kind: paper
title: On non-periodic tilings of the real line by a function
authors: Mihail N. Kolountzakis, Nir Lev
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1505.06833
source_local: ../raw/2015-kolountzakis-non-periodic-tilings-real-line.pdf
topic: general-knowledge
cites:
---

# On non-periodic tilings of the real line by a function

**Authors:** Mihail N. Kolountzakis, Nir Lev  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1505.06833

## One-line
Constructs a positive Schwartz function on $\mathbb{R}$ that tiles the line by translations along a non-periodic discrete set, settling an open question about whether unbounded-support tiling functions force periodic translation sets.

## Key claim
**Theorem 1.1:** there exists a positive $f \in L^1(\mathbb{R})$ (in fact Schwartz class) and a bounded-density discrete set $\Lambda$ — an arbitrarily small perturbation of $\mathbb{Z}$ — such that $\sum_{\lambda \in \Lambda} f(x-\lambda) = 1$ a.e. yet $\Lambda$ is **not** a finite union of periodic sets. **Theorem 1.2 (complement):** if $\Lambda$ has finite local complexity (successive gaps take only finitely many values), then any $L^1$ tiling forces $\Lambda$ periodic. **Theorem 1.3:** every $\ell^1(\mathbb{Z})$ tiling of $\mathbb{Z}$ is periodic.

## Method
Builds $\Lambda = \{n + \alpha(n) : n \in \mathbb{Z}\}$ as a perturbation of $\mathbb{Z}$ via a self-contained re-proof of Kargaev's spectral-gap construction: solve $f + Rf = g$ for a prescribed gap-supported $g$ using the Banach contractive mapping theorem on a small ball in $C(I)$ with the non-linear operator $R$ in (2.3) — avoiding the infinite-dimensional implicit function theorem of prior presentations. Then $\widehat{\delta_\Lambda} = \widehat{\delta_\mathbb{Z}} - F'$ inherits a spectral gap $(-a,a)$, and choosing $\widehat{f}$ supported in $(-a,a)$ with $\widehat{f}(0)=1$ forces tiling by Poisson summation. For Theorems 1.2/1.3, a strengthened Fourier-analytic necessary condition $\mathrm{supp}(\widehat{\delta_\Lambda}) \subset \{\widehat{f}=0\} \cup \{0\}$ (Theorem 4.1, using Wiener's Tauberian theorem to remove prior smoothness/compact-support hypotheses) is combined with Helson's theorem and an Iosevich–Kolountzakis result that finite-local-complexity sets with a spectral gap are periodic.

## Result
Non-periodic tilings of $\mathbb{R}$ by an $L^1$ function exist iff the support is unbounded — sharpening the Lagarias–Wang / Kolountzakis–Lagarias periodicity theorems which required compact support. The dichotomy is clean: unbounded support **and** unbounded local complexity are both necessary for non-periodicity; either alone forces a periodic translation set. The constructed $\alpha(n) \to 0$ with $\sum \alpha(n)^2 < \infty$, and $\sup |\alpha(n)|$ can be made arbitrarily small.

## Why it matters here
General background for autocorrelation / uncertainty-principle problems where spectral gaps and Poisson-summation-style constraints govern admissible configurations; the Wiener-Tauberian-based "support of $\widehat{\delta_\Lambda} \subset \{\widehat{f}=0\}\cup\{0\}$" lemma is a general tool for converting tiling/packing constraints into Fourier-support constraints, relevant to any problem cast as a translation-sum identity. No direct arena tie to a specific numbered problem in the wiki's current inventory.

## Open questions / connections
- Does every function-tiling translation set $\Lambda$ admit an *alternative* periodic translation set $\Lambda'$ (function-version of the periodic tiling conjecture)? The construction's $f$ tiles both $\Lambda$ and $\mathbb{Z}$.
- Can Theorem 1.1 be strengthened to $f = 1_\Omega$ for some unbounded $\Omega \subset \mathbb{R}$ of finite measure tiling non-periodically?
- Extends Lagarias–Wang (1996), Kolountzakis–Lagarias (1996), Leptin–Müller (1991); leans on Kargaev (1982) spectral-gap sets, Helson, and Iosevich–Kolountzakis (2013).

## Key terms
tiling by translations, spectral gap, Kargaev construction, finite local complexity, Poisson summation, periodic tiling conjecture, Wiener Tauberian theorem, Helson theorem, bounded density, pseudo-measure, Banach contractive mapping, autocorrelation
