---
type: source
kind: paper
title: A new lower bound for the kissing number in 19 dimensions
authors: B. Ho
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2603.10425
source_local: ../raw/2026-ho-new-lower-bound-kissing.pdf
topic: general-knowledge
cites:
---

# A new lower bound for the kissing number in 19 dimensions

**Authors:** B. Ho  ·  **Year:** 2026  ·  **Source:** https://arxiv.org/abs/2603.10425

## One-line
Improves the kissing number lower bound in 19 dimensions to $k(19) \geq 11948$ by constructing an explicit nonlinear binary code of size 1280 with minimum distance 5 inside a 5-punctured extended Golay code.

## Key claim
$k(19) \geq 11948$, improving the previous Cohn–Li bound of $11692$ by exactly 256 (= 1280 − 1024).

## Method
Cohn–Li's odd-sign construction reduces the problem to finding a binary code of length 19, minimum distance ≥ 5, inside a 5-punctured extended binary Golay code (dim 12, $|D|=4096$). Author exhibits an explicit chain $M \leq K \leq D$ with $|M|=64$, $|K/M|=16$, $|D/K|=4$, and observes the 21 forbidden low-weight ($\text{wt} \in \{3,4\}$) words of $D$ lie in exactly five nonzero $M$-cosets of $K$, whose images in $K/M \cong \mathbb{F}_2^4$ form the connection set $\Sigma=\{e_1,e_2,e_3,e_4,e_1{+}e_2{+}e_3{+}e_4\}$ of the Clebsch graph. The sum-free set $\Sigma$ is itself a 5-coclique in $\text{Cay}(\mathbb{F}_2^4,\Sigma)$, which lifts to a 320-word code in $K$ and then quadruples via the four $K$-cosets in $D$ to a 1280-word code $A$.

## Result
Theorem 1: $k(19) \geq 11948 = 10668 + 1280$. The construction is fully explicit — six generators $m_i$ for $M$, four coset reps $s_i$ for $K/M$, two coset reps $r_i$ for $D/K$ — and every claim is a finite enumeration over the 4096 words of $D$. Min-distance witness: $s_2$ and $s_3+r_1$ differ by the weight-5 word $\{1,7,12,13,14\}$.

## Why it matters here
Direct hit for arena kissing-number problems: shows that *nonlinear* codes inside a Golay-punctured ambient can beat the best linear subcode, via a Cayley-graph coclique lift — a transferable technique pattern (low-weight forbidden differences → connection set → coclique → coset union lift) for any odd-sign / antipodal construction whose forbidden differences concentrate in few cosets. Augments existing wiki content on Cohn–Li and 5-shortened $S(5,8,24)$ Steiner-system constructions.

## Open questions / connections
- Same coset-quotient + Cayley-graph machinery may extend to dims 17, 18, 20, 21 (Cohn–Li's other dims) — does the forbidden-differences set there also concentrate in a Cayley graph with a large sum-free coclique?
- The Clebsch graph has independence number exactly 5; is there a *non-Cayley* coclique-style argument in a different ambient quotient that gives more than 5?
- Can the 1280-word $A$ be enlarged by relaxing linearity further, e.g. by searching cocliques in $\Gamma|_D$ directly rather than via the $K/M$ quotient (4096-vertex graph search)?
- GPT-5.4 Pro was credited in the discovery — example of AI-assisted combinatorial-construction search worth studying for the agent's own methodology.

## Key terms
kissing number, dimension 19, extended binary Golay code, 5-punctured Golay code, Steiner system S(5,8,24), Cohn-Li odd-sign construction, Clebsch graph, Cayley graph, coclique lift, coset chain, binary code minimum distance 5, sum-free set, nonlinear code construction, sphere packing, Viazovska, Conway-Sloane
