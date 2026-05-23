---
type: source
kind: paper
title: An Algorithmic Proof of the Lovasz Local Lemma via Resampling Oracles
authors: Nicholas Harvey, Jan Vondrak
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1504.02044v3
source_local: ../raw/2015-harvey-algorithmic-proof-lovasz-local.pdf
ingested_for_concept: probabilistic-method.md
cites: 
---

# An Algorithmic Proof of the Lovasz Local Lemma via Resampling Oracles

**Authors:** Nicholas Harvey, Jan Vondrak  ·  **Year:** 2015  ·  **Source:** http://arxiv.org/abs/1504.02044v3

## One-line
Gives an efficient algorithmic proof of the Lovász Local Lemma in *general* probability spaces by replacing the Moser–Tardos variable-resampling step with an abstract "resampling oracle" $r_i: \Omega \to \Omega$ that removes conditioning on $E_i$ without creating non-neighbor events.

## Key claim
If events $E_1,\dots,E_n$ satisfy the (GLL) criterion $\Pr[E_i] \le x_i \prod_{j\in\Gamma(i)}(1-x_j)$ and resampling oracles exist, then `MaximalSetResample` finds a state in $\bigcap_i \overline{E_i}$ in expected $O\big(\sum_i \tfrac{x_i}{1-x_i} \cdot \sum_j \log\tfrac{1}{1-x_j}\big)$ oracle calls — at most quadratically worse than Moser–Tardos, but valid beyond the variable model. Resampling oracles provably exist iff a "lopsided association" condition (LopA) holds, which sits strictly between (Dep) and (Lop).

## Method
Abstracts the resampling primitive: any randomized $r_i$ satisfying (R1) $\omega \sim \mu|E_i \Rightarrow r_i(\omega) \sim \mu$ and (R2) $r_i$ cannot create non-neighbor events. The algorithm repeatedly builds a maximal independent set $J_t$ of currently-occurring events and resamples each. Analysis uses Shearer's independence polynomials $\tilde q_S$ via a stable-set-sequence / coupling argument; the cluster-expansion criterion (CLL) is shown to imply Shearer's region by a new elementary induction on $|S|$ using log-subadditivity $Y_{A\cup B} \le Y_A Y_B$ of the independent-set polynomial.

## Result
Three algorithmic theorems: (i) (GLL) ⇒ $O(\sum_i \tfrac{x_i}{1-x_i} \cdot \sum_j \log\tfrac{1}{1-x_j})$ resamplings; (ii) Shearer's criterion with $\epsilon$-slack ⇒ $O(\tfrac{n}{\epsilon}\log\tfrac{1}{\epsilon})$ resamplings; (iii) (CLL) with $\epsilon$-slack ⇒ $\tfrac{2}{\epsilon}(\sum_j \ln(1+y_j) + t)$ resamplings with probability $\ge 1-e^{-t}$. Efficient resampling oracles are constructed for variable model, random permutations (Fisher–Yates), perfect matchings in $K_{2n}$, and spanning trees in $K_n$, yielding new bounds on rainbow spanning trees, rainbow matchings, and packings of Latin transversals. Appendix A shows the Moser–Tardos witness tree lemma is *false* for general resampling oracles.

## Why it matters here
General background; no direct arena tie. Possibly informs combinatorial-existence reasoning for discrete problems (P12 graph extremal, Latin-transversal-flavored constructions, hypergraph matchings) where LLL gives non-constructive guarantees — but the Einstein Arena problems studied so far (sphere packing, autocorrelation, kissing) are continuous optimization, not LLL-style probabilistic existence.

## Open questions / connections
- Can the quadratic gap vs Moser–Tardos be closed without a witness-tree lemma (which Appendix A rules out in the general oracle framework)?
- Is there a restricted variant of resampling oracles in which the witness tree lemma *is* true, enabling derandomization and parallel LLL algorithms in non-product spaces?
- Extends Moser–Tardos [2009], Pegden [2014] (cluster expansion in variable model), Kolipaka–Szegedy [2011] (Shearer in variable model), Harris–Srinivasan [2014] (permutations) — unifies them under one abstraction.

## Key terms
Lovász Local Lemma, LLL, resampling oracle, Moser–Tardos, Shearer's criterion, cluster expansion, lopsidependency, lopsided association, independent-set polynomial, witness tree lemma, Latin transversal, rainbow matching, rainbow spanning tree, dependency graph
