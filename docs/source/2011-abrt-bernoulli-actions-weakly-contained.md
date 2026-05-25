---
type: source
kind: paper
title: Bernoulli actions are weakly contained in any free action
authors: M. Abért, B. Weiss
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1103.1063
source_local: ../raw/2011-abrt-bernoulli-actions-weakly-contained.pdf
topic: general-knowledge
cites:
---

# Bernoulli actions are weakly contained in any free action

**Authors:** M. Abért, B. Weiss  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1103.1063

## One-line
For any countable group $\Gamma$, every free probability-measure-preserving action weakly contains all Bernoulli (i.i.d.) shift actions of $\Gamma$.

## Key claim
**Theorem 1:** If $\Gamma$ is countable infinite and $f$ is a free p.m.p. action of $\Gamma$, then $f$ weakly contains every Bernoulli action $\kappa^\Gamma$. Consequently all free factors of i.i.d. are weakly equivalent, and (Corollary 2) for finitely generated $\Gamma$ the cost is maximal on free factors of i.i.d., so all such free factors share the same cost.

## Method
Reduce to finite-alphabet Bernoulli $\kappa(p_1,\ldots,p_d)$ via Lemma 5 (matching cylinder-set frequencies). Use freeness (Lemma 6) to find scale $s>0$ such that $F$-neighborhoods of typical points are $s$-separated, then partition $X$ into pieces of diameter $<s$ and assign i.i.d. labels $U_j \sim \kappa$ per piece. A second-moment / Chebyshev argument shows $\mu(G_\alpha) \to \prod_{\gamma\in F} p_{\alpha(\gamma)}$ with high probability, giving the required random labeling.

## Result
Every free p.m.p. action weakly contains all Bernoulli shifts. For finitely generated $\Gamma$, $\mathrm{gcost}(f) \le \mathrm{gcost}(g)$ whenever $f$ weakly contains $g$ (Theorem 9), extending Kechris's monotonicity to groupoid cost. Theorem 3: an ergodic action $f$ is weakly equivalent to $f \times I$ iff $f$ is not strongly ergodic. Theorem 4 (relative Glasner–Weiss): if $f$ is strongly ergodic then $E(f,K) \subseteq E(\Gamma,K)$; otherwise $E(f,K)$ is convex. Recovers Rokhlin's lemma as a quick corollary.

## Why it matters here
General background; no direct arena tie. The constructions (random labelings with bounded-dependence + second-moment concentration on free orbits) are technically adjacent to probabilistic combinatorics methods used in extremal/Sidon-type problems, but the paper's results target ergodic theory and group-action cost rather than the arena's optimization problems.

## Open questions / connections
- Fixed Price problem: does every free action of a countable group have the same cost? This paper reduces it (for infinite $\Gamma$) to whether some Bernoulli action has cost 1.
- Extends Kechris's cost monotonicity (free actions) to groupoid cost for non-free actions.
- Connects to Glasner–Weiss [5], Connes–Weiss, Jones–Schmidt [6], Schmidt [9,10] on strong ergodicity and property (T).
- Behavior of factors of i.i.d. for groups with torsion (nontrivial factors need not be free).

## Key terms
weak containment, Bernoulli action, i.i.d. process, free action, p.m.p. action, cost, groupoid cost, factor of i.i.d., strong ergodicity, Rokhlin lemma, Glasner-Weiss theorem, property (T), Kechris, Gaboriau, second moment method
