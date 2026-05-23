---
type: source
kind: paper
title: Note on the Theorem of Balog, Szemerédi, and Gowers
authors: Christian Reiher, Tomasz Schoen
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2308.10245v2
source_local: ../raw/2023-reiher-note-theorem-balog-szemer.pdf
topic: general-knowledge
cites: 
---

# Note on the Theorem of Balog, Szemerédi, and Gowers

**Authors:** Christian Reiher, Tomasz Schoen  ·  **Year:** 2023  ·  **Source:** http://arxiv.org/abs/2308.10245v2

## One-line
Sharpens the Balog–Szemerédi–Gowers (BSG) theorem so that a set $A$ with energy $E(A) \ge |A|^3/K$ contains a structured subset $A'$ of size essentially $K^{-1/2}|A|$ — the largest possible up to a $(1-\varepsilon)$ factor — while keeping $|A'-A'| \le O_\varepsilon(K^4|A'|)$.

## Key claim
**Theorem 1.2.** For every $K \ge 1$, $\varepsilon \in (0, 1/2)$, and additive set $A$ with $E(A) \ge |A|^3/K$, there exists $A' \subseteq A$ with $|A'| \ge (1-\varepsilon)K^{-1/2}|A|$ and $|A'-A'| \le 2^{33}\varepsilon^{-9}K^4|A'|$. The $K^{-1/2}$ size factor is essentially optimal (shown by the $G^n$ "at most one nonzero coordinate" example, where any larger $A'$ forces $|A'-A'| \gtrsim \varepsilon^2|G|^2$).

## Method
Split $A-A$ into "popular" differences $P$ (representation count $\ge K^{-1/2}|A|$) and "rare" differences $Q$, then handle each case separately. In the popular case (Lemma 3.1), pick a difference $d^*$ whose translate $A_{d^*} = A \cap (A+d^*)$ has heavy overlap, then prune to $A'$ via a double-counting/popularity argument — yielding the stronger bound $O_\varepsilon(K^3|A'|)$. In the rare case (Lemma 3.2), apply a weighted sum-extraction lemma (Lemma 2.2) to pick an index set $I$ optimizing the trade-off between $\sum x_i$ and $|I|$, then run a graph-theoretic BSG-style argument (Lemma 2.1) on the relation $R = \{(a_1,a_2): a_1-a_2 \in Q'\}$ to extract paths of length 4 representing $A'-A'$.

## Result
For every $\varepsilon \in (0, 1/2)$, the BSG theorem holds with $|A'| \ge (1-\varepsilon)K^{-1/2}|A|$ and $|A'-A'| \le 2^{33}\varepsilon^{-9}K^4|A'|$. The popular-difference subcase achieves the better $|A'-A'| \le 2^{10}\varepsilon^{-4}K^3|A'|$. The doubling exponent $4$ cannot be lowered below $\log 4/\log(27/16) \approx 2.649$ (Shao, via $\{x \in \mathbb{Z}^d: \|x\| \le R\}$ examples).

## Why it matters here
General background for extremal-combinatorics / additive-energy problems; provides the tightest known size-vs-doubling trade-off in BSG, relevant if any Einstein Arena problem reduces to extracting a low-doubling subset from a high-energy set. No direct arena tie among the current 23 problems, but the energy↔structure machinery underlies many discrete-geometry and combinatorics arguments.

## Open questions / connections
- Can the doubling exponent $4$ be reduced toward the $\approx 2.649$ lower bound from Shao's examples?
- Can the stronger $O_\varepsilon(K^3|A'|)$ bound from the popular-difference case (Lemma 3.1) be extended to the rare-difference case (Lemma 3.2) as well?
- Extends Schoen's 2015 $O(K^4|A'|)$ bound by upgrading the size factor from $\Omega(|A|/K)$ to the optimal $(1-\varepsilon)K^{-1/2}|A|$.

## Key terms
Balog-Szemerédi-Gowers theorem, additive energy, difference set, doubling constant, additive combinatorics, Cauchy-Schwarz, popular differences, Plünnecke-Ruzsa, sum-product, Schoen, Gowers, Reiher, structured subset extraction
