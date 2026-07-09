---
type: source
kind: paper
title: Variants of the Erdős-Szekeres and Erdős-Hajnal Ramsey problems
authors: D. Mubayi
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1609.07670
source_local: ../raw/2016-mubayi-variants-erd-s-szekeres-erd.pdf
topic: general-knowledge
cites:
---

# Variants of the Erdős-Szekeres and Erdős-Hajnal Ramsey problems

**Authors:** D. Mubayi  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1609.07670

## One-line
Improves polynomial bounds on ordered Ramsey numbers for squared paths and establishes tower-height bounds for hypergraph Ramsey numbers involving tight paths.

## Key claim
$r(P_n^2, P_n^2) < c \cdot n^{19.487}$ (vastly improving the prior $cn^{256}$ bound), and for $k \geq 3$, $\mathrm{twr}_{k-2}(n^c) < r_k(k+1, P_n) < \mathrm{twr}_{k-2}(n^{62})$, pinning down the correct tower height.

## Method
Uses Ramsey multiplicity bounds — specifically the Flag Algebra result $\alpha(4) > 0.00119583$ (Niess, Sperfeld) giving $\log_2(1/\alpha(4)) < 9.7434$ — combined with a pigeonhole argument on the "middle pair" of monochromatic $K_4$ copies, plus induction. For the hypergraph results, introduces an ordered **broom** structure $B_{a,m}^k$ (tight path + fan) to load the induction hypothesis, then applies the standard Erdős-Rado pigeonhole stepping up from $k=3$.

## Result
Theorem 2: $r(P_n^2, P_n^2) < cn^{19.487}$. Theorem 4: $r_3(4, P_n) < n^{21}$ and tower bounds for general $k$. Theorem 9: $r_k(k+1, t; P_n) < \mathrm{twr}_{t-2}(cn^{2k})$, improving the trivial tower-$t{-}1$ bound to tower-$t{-}2$. Theorem 10: linear bounds $r_k(k+1, 3; P_n) \leq 16n$ and $2n-2 \leq r_3(4, 3; P_n) \leq 3n - 4$, plus $r_4(5, 4; P_n) \geq 2^{n-2} + 1$.

## Why it matters here
General background; no direct arena tie. Ordered Ramsey machinery (broom induction, Ramsey multiplicity coupled to bound improvements) is a technique pattern potentially relevant to extremal-graph arena problems, but no current arena problem directly invokes ordered $P_n^\ell$ Ramsey bounds.

## Open questions / connections
- Conjecture 8: $r_k(k+1, t; P_n) < \mathrm{twr}_{t-2}(n^{c'})$ for all $3 \leq t \leq k$ — tower height matching the Erdős-Hajnal pattern but with shift $t-2$ instead of $t-1$.
- Is $r_3(s, P_n)$ polynomial for all fixed $s \geq 4$? (Settled only for $s = 4$ here.)
- Determine the tower growth rate of $r_k(s, t; P_n)$ for $s > k+1$ — no conjecture yet offered.
- Extends Mubayi-Suk [15] from unordered cliques to ordered tight paths; constructions from that work fail in the ordered setting.

## Key terms
ordered Ramsey numbers, Erdős-Szekeres theorem, Erdős-Hajnal conjecture, tight path, squared path, Ramsey multiplicity, flag algebras, monochromatic K4 density, broom hypergraph, tower function, Erdős-Rado stepping-up, hypergraph Ramsey
