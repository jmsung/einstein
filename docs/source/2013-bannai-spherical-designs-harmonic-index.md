---
type: source
kind: paper
title: Spherical designs of harmonic index t
authors: E. Bannai, T. Okuda, M. Tagami
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1308.5101
source_local: ../raw/2013-bannai-spherical-designs-harmonic-index.pdf
topic: general-knowledge
cites:
---

# Spherical designs of harmonic index t

**Authors:** E. Bannai, T. Okuda, M. Tagami  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1308.5101

## One-line
Introduces "harmonic index $t$-designs" — finite point sets on $S^{n-1}$ that annihilate every degree-$t$ harmonic polynomial — and proves a Fisher-type lower bound on their size plus a construction from lower-dimensional spherical designs.

## Key claim
Any harmonic index $t$-design $X \subset S^{n-1}$ satisfies $|X| \ge 1 + \frac{1}{c_{n,t}}\left[\binom{n+t-1}{t} - \binom{n+t-3}{t-2}\right]$, where $c_{n,t} = -\min_{[-1,1]} Q_{n,t}(x)$ and $Q_{n,t}$ is the normalized Gegenbauer polynomial; equality forces $X$ to be a two-distance / equiangular configuration.

## Method
Uses the reproducing-kernel addition formula for $\mathrm{Harm}_t(S^{n-1})$: setting $F(s) = c_{n,t} + Q_{n,t}(s) \ge 0$ on $[-1,1]$ and double-counting $\sum_{x,y \in X} F(\langle x,y\rangle)$ gives the Fisher-type bound. The construction lifts a spherical $t$-design $X$ on $S^{n-2}$ to $S^{n-1}$ by placing it on a parallel sphere at height $r$, where $r$ is a root of $Q_{n,t}$; orthogonal-basis decomposition of $\mathrm{Harm}_t(S^{n-1})$ from Andrews–Askey–Roy ensures the harmonic-sum vanishes. Combined with Bondarenko–Radchenko–Viazovska, this yields $A(n,t) = O(t^{n-2})$.

## Result
Tight examples: $A(2,t)=2$ via two unit vectors at angle $j\pi/(2e)$, $A(n,2)=n$ via an orthonormal basis (an antipodal half cross-polytope), and the first nontrivial computer-verified case $A(3,4)=5$ realized by a regular 5-gon lifted to $S^2$ at radius $r=\sqrt{30}/35$ or $\sqrt{525\pm70\sqrt{30}}/35$. Notable small designs exceeding the bound only loosely: 6 vertices of half-icosahedron form a harmonic index 8- and 14-design, $E_8$'s 120 antipodal points form a harmonic index 10-design (Fisher bound 672), and 60 vertices of the 600-cell form a harmonic index 58-design (Fisher bound 900).

## Why it matters here
General background for design-theoretic lower bounds via reproducing kernels; the Gegenbauer/LP framework is the same machinery underlying Cohn–Elkies sphere-packing bounds and Delsarte-style kissing-number bounds relevant to arena problems in sphere packing, kissing numbers, and equiangular-line / two-distance set constructions. Tight harmonic index designs coincide with equiangular line configurations, tying into Lemmens–Seidel and Musin two-distance bounds.

## Open questions / connections
- Tight harmonic index designs hardly exist for general $(n,t)$ because the Fisher bound exceeds the absolute equiangular-lines bound $n(n+1)/2$ — full classification of $(n,t)$ admitting tight designs is open.
- Whether the $O(t^{n-2})$ upper bound on $A(n,t)$ is tight; gap from Fisher bound $\Theta(t^{n-1})$ for usual designs is dimensional.
- Why exotic small designs (icosahedron half, $E_8$ half, 600-cell half) realize huge index $t$ — connection to invariant theory / harmonic Molien series of finite reflection groups deserves systematic study.

## Key terms
spherical design, harmonic index design, Gegenbauer polynomial, Fisher-type inequality, reproducing kernel, Harm_t, equiangular lines, two-distance set, Delsarte LP method, Bondarenko-Radchenko-Viazovska, E8 root system, 600-cell, icosahedron, Bannai, Seymour-Zaslavsky
