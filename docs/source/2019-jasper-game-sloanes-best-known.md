---
type: source
kind: paper
title: "Game of Sloanes: best known packings in complex projective space"
authors: J. Jasper, E. King, D. Mixon
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1907.07848
source_local: ../raw/2019-jasper-game-sloanes-best-known.pdf
topic: general-knowledge
cites:
---

# Game of Sloanes: best known packings in complex projective space

**Authors:** J. Jasper, E. King, D. Mixon  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1907.07848

## One-line
Announces a public leaderboard of best-known line packings in complex projective space $\mathbb{CP}^{d-1}$ (Grassmannian frames), with a survey of the coherence lower bounds used to certify optimality.

## Key claim
For $\Phi=(\varphi_j)_{j=1}^n\in\mathrm{UN}(d,n,\mathbb{F})$, coherence $\mu(\Phi)=\max_{j\neq k}|\langle\varphi_j,\varphi_k\rangle|$ obeys four lower bounds — Bukh–Cox (4), Welch–Rankin (5) $\mu\ge\sqrt{(n-d)/(d(n-1))}$, orthoplex (6) $\mu\ge 1/\sqrt{d}$ for $n>Z(d,\mathbb{F})$, and Levenstein (7) — and the website tabulates putatively optimal $\Phi$ for $3\le d\le 7$, $d+2\le n\le 49$ in $\mathbb{C}^d$.

## Method
Combines (i) Delsarte-style linear programming and Rankin's sphere-embedding to derive the four bounds, (ii) numerical search via Medra–Davidson sequential smooth optimization on the Grassmannian manifold with smooth penalty functions, then (iii) refinement by gradient descent and Tropp–Dhillon–Heath–Strohmer alternating projection. Closed-form "exactification" is attempted on Gram-matrix phases.

## Result
Establishes a Sloane-style table (https://www.math.colostate.edu/~king/GameofSloanes.html) of best-known $\mu(\Phi)$ for complex $d,n$, each annotated with the tightest applicable bound from Thm. 6. Two new putatively optimal closed-form configurations are conjectured: 8 vectors in $\mathbb{C}^3$ obtained by removing one vector from any $\mathrm{ETF}(3,9)$ (Conj. 7), and an explicit 5-vector packing in $\mathbb{C}^3$ with parameters $a=\sqrt{\sqrt{13}+2}+\sqrt{\sqrt{13}-1})/(3\sqrt{3})$ etc. (Conj. 8).

## Why it matters here
Direct background for any Einstein Arena problem cast as line/projective packing or equiangular-tight-frame search — gives the four canonical lower bounds, when each is tight, and the maximal-MUB construction yielding $d(d+1)>Z(d,\mathbb{C})$ vectors at coherence $1/\sqrt{d}$ for prime-power $d$. Complements existing wiki coverage of equiangular lines, LP bounds, and Welch-type inequalities.

## Open questions / connections
- Open Problem 9: generalize Bukh–Cox and Levenstein bounds to subspace packings of dimension $>1$.
- Zauner's conjecture: do $d^2$ vectors saturating Welch–Rankin (SIC-POVMs) exist in every $\mathbb{C}^d$? Open beyond finitely many dimensions.
- Three-point SDP bounds (Bachoc–Vallentin, de Laat–Vallentin) likely sharpen the LP bounds — unexplored for complex line packings.
- Contact-graph + algebraic-geometry techniques (used for $n=6$ in $\mathbb{RP}^3$) may exactify more numerical entries.

## Key terms
Grassmannian frame, coherence, equiangular tight frame, Welch–Rankin bound, Bukh–Cox bound, orthoplex bound, Levenstein bound, mutually unbiased bases, Zauner conjecture, SIC-POVM, Delsarte linear programming, complex projective packing, Tammes problem, Naimark complement, projective t-design
