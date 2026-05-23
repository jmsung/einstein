---
type: source
kind: paper
title: On eigenfunctions and maximal cliques of Paley graphs of square order
authors: S. Goryainov, V. Kabanov, L. Shalaginov, A. Valyuzhenich
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1801.00438
source_local: ../raw/2018-goryainov-eigenfunctions-maximal-cliques-paley.pdf
topic: general-knowledge
cites:
---

# On eigenfunctions and maximal cliques of Paley graphs of square order

**Authors:** S. Goryainov, V. Kabanov, L. Shalaginov, A. Valyuzhenich  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1801.00438

## One-line
Constructs a new family of maximal cliques in Paley graphs $P(q^2)$ via norm-$1$ ovals, and uses them to build eigenfunctions whose support meets the weight-distribution lower bound.

## Key claim
For odd prime power $q$, the norm-$1$ subgroup $Q = \langle \omega \rangle$ of order $q+1$ in $\mathbb{F}_{q^2}^*$ splits as $Q_0 \cup Q_1$ (even/odd powers of $\omega = \beta^{q-1}$); then (i) if $q \equiv 1 \pmod 4$, $Q_0$ and $Q_1$ are maximal cocliques of size $(q+1)/2$ in $P(q^2)$, and (ii) if $q \equiv 3 \pmod 4$, $Q_0 \cup \{0\}$ and $Q_1 \cup \{0\}$ are maximal cliques of size $(q+3)/2$. The associated $\pm 1$ indicator on $Q_0,Q_1$ is an eigenfunction for a non-principal eigenvalue of $P(q^2)$ with support exactly $q+1$, matching the weight-distribution bound.

## Method
Identify $\mathbb{F}_{q^2}$ with the points of the affine plane $A(2,q)$; the norm-$1$ kernel $Q$ then forms an oval (no three collinear) by Qvist's theorem. Adjacency in $P(q^2)$ is read off via "quadratic vs non-quadratic" line slopes, and the multiplicative action of $T_Q$ on $Q$ gives transitive symmetry used to classify tangents/secants. Maximality is proved by counting tangents/secants through any candidate extension vertex and contradicting Qvist's $0$-or-$2$ tangent dichotomy.

## Result
Two infinite families of maximal cliques of size $(q+1)/2$ ($q \equiv 1 \pmod 4$) or $(q+3)/2$ ($q \equiv 3 \pmod 4$) in $P(q^2)$, distinct from Baker–Ebert–Hemmeter–Woldar (1996) per exhaustive computer search. The $\pm 1$-on-$Q_0/Q_1$ function is an eigenfunction for $\theta_2 = (-1-q)/2$ (case $q \equiv 1$) or $\theta_1 = (-1+q)/2$ (case $q \equiv 3$) with $|\mathrm{Supp}(f)| = q+1$, proving the weight-distribution lower bound is tight for $P(q^2)$.

## Why it matters here
General background; no direct arena tie. Most relevant as machinery for extremal-graph / association-scheme problems where Delsarte LP bounds, eigenfunction supports, or Paley-graph clique numbers appear — e.g. cross-pollination for any arena problem involving strongly regular graphs or finite-field combinatorial constructions.

## Open questions / connections
- The gap between $(q+3)/2$ and $q$ for maximal-clique sizes in $P(q^2)$ remains empty — are there cliques of intermediate size?
- Exhaustive search confirms there are *other* maximal cliques of the same size beyond Baker et al. and this family — full classification open.
- Extends the Valyuzhenich / Vorob'ev–Mogilnykh program (Hamming, Johnson graphs) of minimum-support eigenfunctions to Paley graphs of square order; analogous tightness for other strongly regular graphs is open.

## Key terms
Paley graph, maximal clique, eigenfunction, weight-distribution bound, Delsarte bound, strongly regular graph, affine plane, oval, Qvist's theorem, finite field, norm map, quadratic residue
