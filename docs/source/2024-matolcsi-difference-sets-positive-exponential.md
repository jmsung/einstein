---
type: source
kind: paper
title: Difference sets and positive exponential sums II: cubic residues in cyclic groups
authors: Mate Matolcsi, Imre Z. Ruzsa
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2406.00406v2
source_local: ../raw/2024-matolcsi-difference-sets-positive-exponential.pdf
topic: general-knowledge
cites: 
---

# Difference sets and positive exponential sums II: cubic residues in cyclic groups

**Authors:** Mate Matolcsi, Imre Z. Ruzsa  ·  **Year:** 2024  ·  **Source:** http://arxiv.org/abs/2406.00406v2

## One-line
Constructs nonnegative exponential sums supported on cubic residues to upper-bound the density of sets $B_q \subset \mathbb{Z}_q$ whose difference set $B_q - B_q$ avoids cubic residues mod $q$.

## Key claim
For every $q \geq 1$, $\lambda(C_0(q)) \leq q^{-\varepsilon}$ with $\varepsilon = -\log_3\!\left(\tfrac{1}{13}(2 + \cos(\pi/13) + \sin(3\pi/26))\right) / \log 13 \approx 0.1195$, so any $B_q \subset \mathbb{Z}_q$ with $(B_q - B_q) \cap C(q) = \emptyset$ has density $\delta(B_q) \leq q^{-\varepsilon}$. For squarefree $q$ the bound sharpens to $O_\varepsilon(q^{-1/2+\varepsilon})$.

## Method
Construct "cubic modular witness functions" $g^{(q)}(y) = b_0 + \sum b_j(e(j^3 y/q) + e(-j^3 y/q)) \geq 0$ with $g^{(q)}(0) = 1$; minimizing $b_0$ directly bounds $\delta$ via Theorem 1.4 of part I. For prime $s = 3k+1$, cubic character sum estimates $|\sum \chi_i(l)e(ly/s)| \leq \sqrt{s}$ (Vaughan, Hardy–Littlewood) give $\lambda(C_0(s)) \leq 2/\sqrt{s}$; primes $p = 3k+2$ are trivial. Prime-power moduli handled by induction (Lemma 2.4) via subgroup/factor-group multiplicativity from part I's Theorem 7.2; squarefree composites via direct product (Theorem 8.1 of part I); self-compatibility across $q$ is automatic from the inductive construction.

## Result
Squarefree case: $\lambda(C_0(q)) \leq \prod_i (1/p_i) \prod_l (2/\sqrt{s_l}) \leq 2^m/\sqrt{q}$ where $s_l$ are the $3k+1$ prime factors; exponent $1/2$ asymptotically optimal. General case: $\lambda(C_0(q)) \leq q^{-0.1195}$ via $\lambda(C_0(p^m)) = \lambda(C_0(p))^{\lfloor(m+2)/3\rfloor}$ for $p \neq 3$ and $\lambda(C_0(3^{3m})) = \lambda(C_0(27))^m$. Lower bounds remain only $\log q$ (Ramsey / Cohen 1988), leaving a wide gap.

## Why it matters here
Direct toolkit for autocorrelation- and difference-set-avoidance problems on cyclic groups (P15/P16-style): turns "find large $B$ avoiding forbidden differences" into "minimize $b_0$ of a nonnegative exponential sum supported on the forbidden set" — same dual LP structure as Cohn–Elkies for sphere packing and Delsarte LP for kissing numbers. The character-sum-bound $\to$ explicit witness construction is a reusable recipe for any problem where forbidden differences form a multiplicative subgroup.

## Open questions / connections
- Integer analogue: bound $|B \cap [0, N]|$ with $B - B$ avoiding cubes (or $k$th powers); requires kth-power witness functions $f^{(n)}$ on $[0,1]$, not just modular.
- Quadratic-residue case is harder (k=2 even, set not symmetric); Gabdullin (2018) achieved a different non-trivial bound — promised in a later paper of this series.
- Closing the gap between $q^{-0.1195}$ upper bound and $\log q$ lower bound (Cohen 1988, Paley-graph clique numbers).
- Self-compatibility property enables lifting modular witnesses to integer witnesses in future work of the series.

## Key terms
nonnegative exponential sums, cubic residues, difference sets, witness function, cyclic groups, Paley graph, character sums, LP duality, Matolcsi, Ruzsa, Gabdullin, autocorrelation inequalities
