---
type: source
kind: paper
title: "A new asymptotic enumeration technique: the Lovasz Local Lemma"
authors: Linyuan Lu, Laszlo A. Szekely
year: 2009
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/0905.3983v4
source_local: ../raw/2009-lu-new-asymptotic-enumeration-technique.pdf
topic: general-knowledge
cites:
---

# A new asymptotic enumeration technique: the Lovasz Local Lemma

**Authors:** Linyuan Lu, Laszlo A. Szekely  ·  **Year:** 2009  ·  **Source:** http://arxiv.org/abs/0905.3983v4

## One-line
Uses the lopsided Lovász Local Lemma (LLL) with negative dependency graphs over the space of random perfect matchings of $K_{2n}$ and $K_{N,N'}$ to derive matching upper/lower bounds for asymptotic enumeration of permutations, Latin rectangles, and regular/degree-constrained graphs by girth.

## Key claim
A negative dependency graph can be constructed in the random-matching space of $K_{2n}$ (and $K_{N,N'}$) where canonical events $A_M$ are extensions of partial matchings $M$ to perfect matchings, with edges between conflicting partial matchings. Combined with a near-positive dependency graph upper bound, this yields $\Pr(\wedge_i \overline{A_i}) = (1+o(1))e^{-\mu}$, recovering classical asymptotics and giving a new result: the number of graphs with degree sequence $d_1,\ldots,d_n$ and girth $\geq g$ is $\frac{(N-1)!!}{\prod_i d_i!} (1+o(1)) \exp\left(-\sum_{i=1}^{g-1} \frac{1}{2i}(\bar{D}/\bar{d})^i\right)$ where $D_j = d_j(d_j-1)$, under mild conditions on the degree sequence.

## Method
Lopsided LLL with negative dependency graphs in the uniform-random-matching space — events are "all perfect-matching extensions of partial matching $M$"; edges link partial matchings whose union is no longer a matching. Proves via induction on $N$ (Lemma 4: $\Pr(\wedge A_M^N) \leq \Pr(\wedge A_M^{N+2})$) that this is genuinely a negative dependency graph. Pairs the LLL lower bound with a new $\epsilon$-near-positive dependency graph upper bound (Theorem 2) so that lower and upper bounds asymptotically coincide; uses the LambertW-based function $y(\gamma)$ to track higher-order error terms.

## Result
- Theorem 1: $\Pr(\wedge_i \overline{A_i}) \geq \exp(-\sum_i \Pr(A_i) y(\epsilon) - \sum_i \Pr^2(A_i) y^2(\epsilon))$ given $\sum_{j \sim i} \Pr(A_j) + 2\Pr^2(A_j) < \epsilon < 1/4$.
- Theorem 2: $\Pr(\wedge_i \overline{A_i}) \leq \prod_i (1 - (1-\epsilon)\Pr(A_i))$ for $\epsilon$-near-positive dependency graphs.
- Theorems 7–10: enumeration of $d$-regular graphs / bipartite graphs / general degree sequence graphs with girth $\geq g$, agreeing with McKay–Wormald-type formulas under $g^6(d-1)^{2g-3} = o(n)$.
- Theorem 11: under (63), almost all graphs with given degree sequence and girth $\geq g$ have chromatic number $> k$ whenever $k^2 < (1-\epsilon)^2 \log(2\bar{d})$, sharpening Erdős's 1959 high-girth-high-chromatic existence result to a universal statement.

## Why it matters here
General background for probabilistic extremal arguments: LLL with non-trivial negative dependency in matching spaces is a tool for proving existence of structured configurations (e.g., packings, designs, codes) where natural bad events overlap in conflict-graph patterns; the random-matching framework could inform discrete-geometry / extremal-graph problems where solutions are realized as matchings under constraints. No direct arena tie to a specific problem in the current wiki.

## Open questions / connections
- Higher-order Poisson terms: can the framework be extended to $\Pr(X=k)$ for fixed $k$, not just $k=0$?
- Why is there no "second-term correction" to $-\mu$ in the exponent? The paper notes $e^{-\mu}$ sits between LLL lower and upper bounds, blocking the kind of refinement seen in (39)/(42).
- Extension to negative dependency graphs in matching spaces of arbitrary graphs (paper's construction fails beyond $K_N$ / $K_{N,N'}$ — counterexample on $C_6$).
- Connection to Janson inequality and Brun's sieve as alternative tools for the Poisson paradigm.
- Statistical-physics-based LLL improvements (Bissacot–Fernández, Scott–Sokal) not exploited.

## Key terms
Lovász Local Lemma, lopsided LLL, negative dependency graph, near-positive dependency graph, random perfect matchings, configuration model, asymptotic enumeration, Latin rectangles, regular graph enumeration, girth, chromatic number, Poisson paradigm, Erdős probabilistic method, McKay-Wormald, LambertW
