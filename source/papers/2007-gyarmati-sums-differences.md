---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: published_paper
source_url: https://projecteuclid.org/euclid.facm/1229618749
source_local: sources/2007-gyarmati-sums-differences.pdf
cites:
  - ../papers/2010-vinuesa-sidon-thesis.md
  - problem-19-difference-bases/literature.md
  - problem-19-difference-bases/strategy.md
---

[[../home]] | [[../index]]

# Gyarmati, Hennecart & Ruzsa — Sums and Differences of Finite Sets

**Authors:** Katalin Gyarmati, François Hennecart, Imre Z. Ruzsa
**Year:** 2007 (Functiones et Approximatio Commentarii Mathematici 37(1):175–186)

## Summary

Pure additive combinatorics. For finite subsets A, B of an abelian group with **|A + B| ≤ K|A|** (small-sumset condition), the paper derives sharp inequalities relating |A − B| to |A| and K, and bounds the ratio |X − B|/|X| as X varies over subsets of A. Headline result: there exists a subset X ⊆ A with |X − B| ≤ K^c |X| for an explicit constant c — a refinement of Plünnecke's inequality that gives different (often better) bounds when comparing sums vs. differences.

The methods are clean Plünnecke-graph arguments and combinatorial counting. The paper is the modern reference for "given small sumset, what does the difference set look like" — which is the structural question underlying every Sidon-set / B_h[g] / difference-basis problem.

## Key Techniques

- **Plünnecke graphs** — bipartite addition graphs where iteration gives the inequalities
- **Tensorization** — |hA − kA| bounds derived by lifting to product groups
- **Sharp constants** — many of the inequalities have explicit best-possible exponents
- **Subset selection** — the "X ⊆ A" formulation often gives stronger bounds than the full set

## Relevance to Einstein Arena

### Problem 19 — Difference Bases (frozen)

P19 is the discrete-ruler instantiation of the Sidon / restricted-difference problem. The Plünnecke-Ruzsa inequalities in this paper bound how large a difference set must be given the size of the sum set — the structural lower-bound side of the difference-basis problem. While the arena P19 evaluator works on integer rulers (not abstract abelian groups), the asymptotic ratio k²/L is governed by the same machinery.

### Cross-cutting — additive combinatorics
The Plünnecke-Ruzsa inequalities here are the standard tools used elsewhere in the wiki when bounding sumset growth. Useful background for any arena problem involving |A + A|, |A − A|, or B_h[g] sets.

## Limitations

- Pure structure theory — no explicit constructions of extremal sets
- Asymptotic only — gives existence of X ⊆ A but no constructive recipe
- Abelian-group setting; arena P19 works specifically on integer intervals
- 2007 — does not include later sharpenings by Schoen, Petridis, etc.

## See Also

- [[2010-vinuesa-sidon-thesis]] — uses Plünnecke-Ruzsa as Chapter 1 tool
- [[../problem-19-difference-bases/literature]]
- [[../problem-19-difference-bases/strategy]]
