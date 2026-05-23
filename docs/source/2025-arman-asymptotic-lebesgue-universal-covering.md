---
type: source
kind: paper
title: On asymptotic Lebesgue's universal covering problem
authors: Andrii Arman, Andriy Bondarenko, Andriy Prymak, Danylo Radchenko
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2512.04023v1
source_local: ../raw/2025-arman-asymptotic-lebesgue-universal-covering.pdf
topic: general-knowledge
cites: 
---

# On asymptotic Lebesgue's universal covering problem

**Authors:** Andrii Arman, Andriy Bondarenko, Andriy Prymak, Danylo Radchenko  ·  **Year:** 2025  ·  **Source:** http://arxiv.org/abs/2512.04023v1

## One-line
Proves that in high dimensions, Jung's ball is an asymptotically optimal universal cover — any set containing a congruent copy of every diameter-1 set must have volume at least $(1-o(1))^n \mathrm{Vol}(J_n)$.

## Key claim
For any universal cover $U \subset \mathbb{E}^n$, $\mathrm{Vol}(U) \geq \exp(-(5/4 + o(1))n\log n) \cdot \mathrm{Vol}(J_n)$, where $J_n$ is Jung's ball of radius $r_n = \sqrt{n/(2n+2)}$. This is tight up to a subexponential factor.

## Method
Probabilistic deletion / coclique construction in a measurable graph. Assume a minimal universal cover $U$ violates the bound; discretize the infinite family of congruent copies of $U$ into a finite family $\mathcal{U}_\varepsilon$ of $\varepsilon$-thickenings using nets on $O(n)$ (Szarek's bound); then construct a random discrete set $X \subset rB^n$ of diameter $\leq 1$ via i.i.d. sampling + edge-deletion (Chernoff + Markov), showing $X$ escapes every member of $\mathcal{U}_\varepsilon$ when $\mathrm{Vol}(U)$ is too small. A general framework (Lemma 5) bounds covering numbers via spherical-cap measure $m(\alpha)$.

## Result
Theorem 1: $\mathrm{Vol}(U) \geq (1-o(1))^n (1/\sqrt{2})^n \mathrm{Vol}(B_n)$ for any universal cover. By Urysohn's inequality, Jung's ball is also asymptotically optimal for mean width and any quermassintegral (via Alexandrov) among convex universal covers. Corollary on Borsuk: partitioning universal covers into diameter-$<1$ pieces yields $b(n) \geq (\sqrt{2}-o(1))^n$, weaker than Schramm–Bourgain–Lindenstrauss's $(\sqrt{3/2}+o(1))^n$ upper bound, so this route cannot improve $b(n)$.

## Why it matters here
General background for discrete-geometry extremal problems involving diameter-1 sets, body of constant width, and covering numbers — touches Borsuk-type partition bounds and Jung-ball machinery that recur in kissing/packing problems. No direct arena-problem tie unless an arena problem reduces to covering diameter-1 sets in high dimensions.

## Open questions / connections
- Closes the asymptotic Lebesgue covering problem (volume) up to subexponential factor; the exact constant in front of $n\log n$ (currently $5/4$) is not yet sharp.
- Confirms that partitioning universal covers cannot beat Schramm / Bourgain–Lindenstrauss for Borsuk's $b(n)$ — rules out a class of approaches.
- Extends Bezdek–Connelly / Makeev (translative case, exact) to congruent covers (asymptotic, sharp).
- Generalizes the deletion method of Arman–Bondarenko–Prymak (illumination, [1]) to a measurable-graph coclique framework — reusable tool.

## Key terms
universal cover, Lebesgue covering problem, Jung's theorem, Jung ball, Borsuk's conjecture, constant width body, diameter-1 set, isodiametric inequality, Urysohn inequality, Schramm, Bourgain-Lindenstrauss, spherical cap measure, Szarek net, deletion method, coclique, Chernoff bound, mean width, quermassintegral, Kahn-Kalai
