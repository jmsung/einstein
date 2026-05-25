---
type: source
kind: paper
title: Exact hyperplane covers for subsets of the hypercube
authors: James Aaronson, Carla Groenland, Andrzej Grzesik, Tom Johnston, Bartłomiej Kielak
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2010.00315
source_local: ../raw/2020-aaronson-exact-hyperplane-covers-subsets.pdf
topic: general-knowledge
cites:
---

# Exact hyperplane covers for subsets of the hypercube

**Authors:** James Aaronson, Carla Groenland, Andrzej Grzesik, Tom Johnston, Bartłomiej Kielak  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2010.00315

## One-line
Generalizes the Alon–Füredi hyperplane-cover theorem: how many hyperplanes are needed to cover $\{0,1\}^n$ while exactly missing a prescribed subset $S$.

## Key claim
For $|S| \in \{2,3\}$, $\mathrm{ec}(\{0,1\}^n \setminus S) = n-1$; for $|S|=4$ it is $n-1$ or $n-2$ depending on whether a hyperplane hits exactly 3 points of $S$; globally $2^{n-2}/n^2 \le \mathrm{ec}(n) \le 2^{n+1}/n$.

## Method
Lower bounds use the Alon–Füredi corollary (any $m<n$ hyperplanes missing some vertex miss $\ge 2^{n-m}$ vertices) plus a probabilistic/union-bound argument over the $\le 2^{n^2}$ possible intersection patterns of $\{0,1\}^n$. Upper bounds use explicit "merge-coordinates" hyperplanes of the form $\{x : (x_1+\dots+x_a)/a + \dots = \alpha\}$ to inductively reduce dimension, plus a Hamming-sphere cover via the hypercube's total domination number ($\le 2^{n+1}/n$). Small cases ($n \le 7$) are handled by exhaustive computer search.

## Result
$\mathrm{ec}(n,k) = n + \Theta_k(1)$: specifically $n - \log_2(k) \le \mathrm{ec}(n,k) \le n - 2k + \mathrm{ec}(2k,k)$. The size-4 case is fully characterized by 2-dimensional subcube structure. Single-layer-minus-a-point has $\mathrm{ec} = \min(i, n-i)$. The global $\mathrm{ec}(n)$ scales as $\Theta(2^n/\mathrm{poly}(n))$.

## Why it matters here
General background on hypercube combinatorics and hyperplane-cover extremal problems; informs the polynomial-method / Combinatorial-Nullstellensatz toolkit used implicitly across discrete-geometry problems. No direct Einstein Arena problem tie, but the intersection-pattern counting and Hamming-sphere cover arguments are reusable templates.

## Open questions / connections
- Problem 1: Is $\mathrm{ec}(n,k) \le n + C$ for some absolute $C$ once $n \ge n_0(k)$? (Wagner's NN counterexample disproved a stronger product conjecture.)
- Problem 2: Minimum $|S|$ hitting every $d$-dimensional (not necessarily axis-aligned) subcube of $\{0,1\}^n$ — related to Alon–Krech–Szabó's Turán-in-hypercube bounds $\log_2(d)/2^{d+2} \le g(n,d)/2^n \le 1/(d+1)$.
- Tightening the $2^{n-2}/n^2$ lower bound; Noga Alon's parity refinement gives $\ge 2^n/n^2$.

## Key terms
Alon-Füredi, hyperplane cover, exact cover number, hypercube, intersection patterns, Combinatorial Nullstellensatz, total domination number, Hamming sphere, axis-aligned subcube, polynomial method, Turán-type, Clifton-Huang k-cover
