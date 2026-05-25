---
type: source
kind: paper
title: Density of Spherically Embedded Stiefel and Grassmann Codes
authors: Renaud-Alexandre Pitaval, Lu Wei, O. Tirkkonen, C. Hollanti
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1607.03132
source_local: ../raw/2016-pitaval-density-spherically-embedded-stiefel.pdf
topic: general-knowledge
cites:
---

# Density of Spherically Embedded Stiefel and Grassmann Codes

**Authors:** Renaud-Alexandre Pitaval, Lu Wei, O. Tirkkonen, C. Hollanti  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1607.03132

## One-line
Derives bounds on the packing density of codes in complex Stiefel/Grassmann manifolds (and the unitary group) under the chordal distance from their Euclidean embedding, and shows density is *not* a one-to-one function of minimum distance.

## Key claim
For Grassmann/Stiefel codes with chordal distance, the kissing radius $\varrho$ (and hence density) is *not* determined by the minimum distance $\delta$ alone — two codes with equal $\delta$ can have different densities. Bounds: $\underline{\varrho}(\delta) \le \varrho \le \bar{\varrho}(\delta)$ with explicit closed forms; e.g. for the Grassmannian, $\underline{\varrho}^2 = \tfrac{p}{2}(1 - \sqrt{1-\delta^2/p})$ and $\bar{\varrho}^2 = \tfrac{1}{2}(\lceil\delta^2\rceil - \sqrt{\lceil\delta^2\rceil - \delta^2})$. Spherically embedded Stiefel/Grassmann codes asymptotically achieve *higher* density than their image spherical codes as $n \to \infty$.

## Method
Two ingredients: (i) **volume of a metric ball** — small-radius approximation via tangent-space ball (using the exact volume scaling induced by the spherical embedding from Nash's theorem) plus large-radius **hyperspherical-cap approximation** justified by a volume-comparison theorem; (ii) **kissing radius bounds** — formulate min/max of $\sum \sin^2(\theta_i/2)$ subject to $\sum \sin^2 \theta_i = \delta^2$ on principal angles, solved via Lagrange multipliers (lower bound: spread equally over all $p$ angles) and mean-value-theorem contradiction (upper bound: concentrate on $\lceil \delta^2 \rceil$ angles at $\pi/2$). Asymptotic ball volume comes from a CLT on the chordal distance as linear statistics of random-matrix eigenvalues (Borel-style Gaussianity of sphere coordinates).

## Result
Closed-form bounds $\underline{\varrho}, \bar{\varrho}$ on the kissing radius give matching lower/upper bounds on code density. Volume-comparison theorem: normalized ball volume in $V_{n,p}^{\mathbb{C}}$ or $G_{n,p}^{\mathbb{C}}$ converges (as $n,p \to \infty$ with $n-2p$ fixed) to the normalized cap volume in the embedding sphere, with $\mathrm{erf}$-form asymptotic $\mu(B(r)) \to \tfrac{1}{2} - \tfrac{1}{2}\mathrm{erf}(\sqrt{np}(1 - r^2/(2p)))$ for Stiefel. Yields refined Hamming bounds improving prior Grassmann bounds (Barg–Nogin, Henkel) and extending Han–Rosenthal's unitary-group bound to all Stiefel manifolds.

## Why it matters here
General background; no direct arena tie. Closest links: provides volume-of-metric-ball machinery and kissing-vs-minimum-distance dissociation relevant to any Grassmannian/Stiefel packing problem on the arena; could inform density-based bound calculations for subspace-packing variants if they arise. Adds a worked example where "max min-distance ≠ max density" — a useful counterpoint to the wiki's default Cohn–Elkies/sphere-packing intuition.

## Open questions / connections
- Stiefel upper bound on kissing radius is not proved in full generality (only matches unitary group as a lower bound); generalizing $\max_Y d^2(I_{n,p}, M_Y) = \bar{\varrho}$ is open.
- Geodesic between two arbitrary Stiefel points has no known closed form (Remark 1) — blocks direct mid-distance computation.
- Extends Conway–Hardin–Sloane (1996) Grassmannian packings and Bachoc–Ben-Haim–Litsyn (2008) bounds; complements LP bounds of Bachoc (2006) and Creignou–Diet (2008).
- Suggests density (not min-distance) as the right MIMO precoding criterion — separates "packing objective" from "coding-distance objective".

## Key terms
Grassmann manifold, Stiefel manifold, unitary group, chordal distance, kissing radius, packing density, Hamming bound, hyperspherical cap, principal angles, volume comparison theorem, MIMO precoding, spherical embedding, two-point homogeneous space, Nash embedding, random matrix CLT
