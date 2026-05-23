---
type: source
kind: paper
title: The Kakeya conjecture on local fields of positive characteristic
authors: Alejo Salvatore
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2202.11344
source_local: ../raw/2022-salvatore-kakeya-conjecture-local-fields.pdf
topic: general-knowledge
cites:
---

# The Kakeya conjecture on local fields of positive characteristic

**Authors:** Alejo Salvatore  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2202.11344

## One-line
Proves the Kakeya conjecture (Hausdorff dimension $n$) for Besicovitch-type sets in the local field $\mathbb{F}_q((t))^n$, extending Arsovski's $p$-adic result to positive characteristic via Lubin–Tate theory.

## Key claim
Every $c$-Kakeya set in $\mathbb{F}_q((t))^n$ has Hausdorff dimension exactly $n$ (Theorem 1), and the Kakeya maximal conjecture holds with $\|\mathcal{K}_\delta \phi\|_{L^n(S^{n-1}(A))} \lesssim_{n,q} k^{n+2} \|\phi\|_{L^n(A^n)}^n$ where $\delta = q^{-k}$ (Theorem 4).

## Method
Adapts Dvir's polynomial method (find low-degree polynomial vanishing on a discretized Kakeya set, contradict via line structure) to the local-field setting. The key innovation: replace Arsovski's $p^k$-th roots of unity (unavailable in char $p$) with the roots $\Lambda_k$ of the iterated additive polynomial $f^{\circ k}$ where $f(X) = tX + X^q$ — a Lubin–Tate construction giving a totally ramified extension $L/K$ whose Galois action realizes $R = A/t^k A$ as an $A$-module acting on $\Lambda_k$ by power series $[a]_f$. A discrete-valuation analogue of Schwartz–Zippel (Lemma 7) replaces the classical degree argument.

## Result
For any $(\varepsilon, \nu)$-Kakeya set in $\mathbb{F}_q[[t]]^n$, the number of radius-$q^{-k}$ balls needed to cover it is at least $\binom{\lfloor \frac{\nu\varepsilon}{kn} q^{k-1}\rfloor + n}{n}$ (Theorem 3). This implies (via $q$-adic decomposition) $\dim_H(E) = n$ for all $c$-Kakeya sets, and via a random-rotation distributional estimate it yields the maximal conjecture with explicit polynomial-in-$k$ dependence (analogous to expected log-loss in the real case).

## Why it matters here
General background; no direct arena tie. The polynomial method and Lubin–Tate / additive-polynomial machinery are far from the optimization-heavy arena problems, though the polynomial method itself appears tangentially in discrete-geometry contexts (e.g., extremal incidence bounds) that touch problems like P1 sphere packing or kissing-number LPs.

## Open questions / connections
- Extends Arsovski 2021 ($p$-adic Kakeya) to all non-archimedean local fields — completes the local-field Kakeya picture.
- Real-case Kakeya conjecture ($n \geq 3$) remains open; best bounds $d(3) \geq 5/2 + \varepsilon_0$ (Katz–Zahl 2019), $d(4) \geq 3.059$ (Katz–Zahl 2021).
- Whether the method-of-multiplicities refinement (Dvir–Kopparty–Saraf–Sudan) gives improved constants in the local-field setting.

## Key terms
Kakeya conjecture, Besicovitch set, Hausdorff dimension, local fields, positive characteristic, $\mathbb{F}_q((t))$, polynomial method, Dvir, Arsovski, Lubin–Tate theory, additive polynomial, Schwartz–Zippel lemma, Kakeya maximal operator, totally ramified extension, formal group law
