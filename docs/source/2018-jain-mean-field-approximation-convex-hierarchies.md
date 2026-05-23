---
type: source
kind: paper
title: "Mean-field approximation, convex hierarchies, and the optimality of correlation rounding: a unified perspective"
authors: Vishesh Jain, Frederic Koehler, Andrej Risteski
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1808.07226
source_local: ../raw/2018-jain-mean-field-approximation-convex-hierarchies.pdf
topic: general-knowledge
cites:
---

# Mean-field approximation, convex hierarchies, and the optimality of correlation rounding: a unified perspective

**Authors:** Vishesh Jain, Frederic Koehler, Andrej Risteski  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1808.07226

## One-line
Unifies two opposite-direction variational approaches to the Ising free energy — mean-field (lower bound) and Sherali-Adams convex hierarchies (upper bound) — showing both have the same tight regime $\|J\|_F^2 = o(n)$, via a single correlation-rounding argument.

## Key claim
For any Ising model on $n$ vertices with interaction matrix $J$, $F - F^* \le 3 n^{2/3} \|J\|_F^{2/3}$, where $F^*$ is the mean-field variational lower bound. This is tight up to constants, removes the $\log^{1/3}$ factor in Jain–Koehler–Mossel 2018, and subsumes Basak–Mukherjee's $o(n)$ result. The same bound yields a $2^{o(n)}$-time approximation scheme for $F$ within $o(n)$ additive error whenever $\|J\|_F^2 = o(n)$, and this regime is Gap-ETH-tight.

## Method
Round the true Gibbs measure (or a Sherali-Adams level-$r$ pseudo-distribution) to a product distribution by **conditioning on a small random set $T$ of coordinates** via the Raghavendra–Tan / Manurangsi–Raghavendra correlation rounding theorem: for $|T| = O(1/\epsilon^2)$, the remaining variables have average $|\text{Cov}(X_i, X_j)| \le \epsilon$. Balance the rounding error $n^2 \epsilon \|J\|_F$ against the level $r$ via Sherali-Adams LP duality. The same machinery, plugged into the SK spin glass with $\beta > 1$, refutes the Allen–O'Donnell–Zhou conjecture by showing $|T| = \Omega(1/\epsilon^2)$ is required (Theorem 1.3).

## Result
Three tight statements: (1) **mean-field error** $F - F^* \le 3 n^{2/3} \|J\|_F^{2/3}$ for Ising; for $k$-MRFs, the tight regime is $\|J\|_F^2 = o(n^{3-k})$. (2) **algorithmic** sub-exponential time approximation of $F$ to $o(n)$ in this regime; matched by Gap-ETH lower bound. (3) **correlation-rounding optimality**: there is an SK-spin-glass family where conditioning on any $t_n \to \infty$ variables leaves $\mathbb{E}|\text{Cov}(X_i,X_j)| \ge C/\sqrt{t_n}$, refuting the conjectured $O(1/\epsilon)$ improvement.

## Why it matters here
General background; no direct arena tie. Touches **LP/SDP hierarchies (Sherali-Adams, SOS)** and **convex relaxation rounding** — relevant if the agent ever attacks discrete CSP-flavored arena problems (extremal graphs, MAX-CUT-style combinatorics) by relaxing through a moment hierarchy. The correlation-rounding lower bound is a cautionary tale for any "condition-on-a-few-variables-to-decorrelate" heuristic.

## Open questions / connections
- Optimal exponent $\alpha$ in $F - F^* \le O(n^{1-\alpha} \|J\|_F^{2\alpha})$ — only $\alpha = 1/3$ proved; values in $(0, 1/3]$ open.
- Is the fRSB phase of SK strictly harder to correlation-round than RS phase? Are spin glasses extremal for the correlation-rounding constant $\kappa^*$?
- How many SA / SOS rounds are needed to compute the SK ground state (the MAX-QP problem dropping the entropy)? Is $\Omega(n)$ required?
- Extends Raghavendra–Tan correlation rounding, Risteski 2016 (Sherali-Adams free-energy bounds), Basak–Mukherjee mean-field universality; uses Aizenman–Lebowitz–Ruelle SK rigor and Wigner semicircle law for the lower bound.

## Key terms
Ising model, free energy, partition function, mean-field approximation, Sherali-Adams hierarchy, sum-of-squares, correlation rounding, Gibbs variational principle, Sherrington-Kirkpatrick spin glass, replica symmetry breaking, Frobenius norm, Gap-ETH, MAX-k-CSP, k-MRF, pseudo-distribution, Parisi formula, total correlation
