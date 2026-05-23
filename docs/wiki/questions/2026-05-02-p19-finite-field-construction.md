---
type: question
author: agent
drafted: 2026-05-02
status: open
asked_by: ramanujan
related_problems: [P19]
related_concepts: [kronecker-decomposition.md, sidon-sets.md, modular-forms-magic-function.md]
---

# Could a finite-field / character-sum construction generate a P19 ratio below 2.639027?

## Question

P19 SOTA solutions all reduce to `B = A ⊕ 8011·R` with `R` a 4-mark Sidon ruler — a *combinatorial* construction. Number-theoretic constructions (Singer difference sets, Bose–Chowla, Paley) often generate Sidon-like sets with denser difference coverage than combinatorial search finds. Is there an algebraic generator that beats the 7-tie?

## Why it matters

Hidden algebraic structure (modular forms / Ramanujan graphs / character sums) has repeatedly been the source of breakthroughs in packing-adjacent problems (E8 magic function, Leech lattice, Cohn–Li d=17–21 kissing). If P19 has such structure, a generator would be a structural improvement that random search cannot find.

## What's the right algebraic object?

- **Singer difference sets**: `B = {0, 1, q+1, ..., q^h-1}` with parameters `(q^(h+1)-1)/(q-1), q^h, q^(h-1)`. The Singer parameters give Sidon sets but with specific size constraints — does any Singer set fit the P19 size+span constraints with better ratio?
- **Bose–Chowla construction**: `B_q = {x : x^q ≡ x mod p}` for prime p, q a primitive root.
- **Paley-type**: `B = {squares mod p}` for prime p ≡ 3 mod 4.
- **Ramanujan graphs / LPS**: spectral expanders with extremal Sidon properties.

## Hypotheses

- **H1**: The 7-way tie at 2.639027 corresponds exactly to a Bose–Chowla parameter — and improvement would require a different prime/q choice.
- **H2**: The combinatorial 4-mark ruler `{0,1,4,6}` IS the algebraic ruler in disguise (e.g., quadratic residues mod some small prime).
- **H3**: No known algebraic family fits P19's exact size/span; any improvement requires a new construction.

## Next step

1. Tabulate all known Sidon-set algebraic constructions with parameters near P19's size constraint.
2. Compute their ratios; compare to 2.639027.
3. If any beats: implement, verify, propose submission.
4. If none: H3 holds; archive as a finding ("known algebraic Sidon families do not generate P19 improvements").

## References

- `wiki/concepts/sidon-sets.md`
- `wiki/concepts/modular-forms-magic-function.md`
- `wiki/personas/ramanujan.md`
- `wiki/personas/gauss.md`
- `source/2010-vinuesa-sidon-thesis.md`
- `source/2022-ganzhinov-symmetric-lines.md` (Lubotzky-Phillips-Sarnak Ramanujan graphs)

## Suggested sources

*Auto-suggested by `docs/tools/gap_search.py` — arxiv query: `(all:"kronecker decomposition" OR all:"sidon sets" OR all:"finite-field character-sum construction generate a ratio") AND (cat:math.NT OR cat:math.CO OR cat:math.OC OR cat:math.MG OR cat:math.PR OR cat:math.CA OR cat:math.NA)`*

Review and `/wiki-ingest <arxiv-url>` any that look relevant. If none fit, close the question with `status: superseded` and a one-line explanation.

### 1. Sidon sets in algebraic geometry (2023)
**Authors:** Arthur Forey, Javier Fresán, Emmanuel Kowalski
**URL:** http://arxiv.org/abs/2301.12878v3
**Abstract:** We report new examples of Sidon sets in abelian groups arising from generalized jacobians of curves, and discuss some of their properties with respect to size and structure.

### 2. On large Sidon sets (2024)
**Authors:** Ingo Czerwinski, Alexander Pott
**URL:** http://arxiv.org/abs/2411.12911v3
**Abstract:** A Sidon set $M$ is a subset of $\mathbb{F}_2^t$ such that the sum of four distinct elements of $M$ is never 0. The goal is to find Sidon sets of large size. In this note we show that the graphs of almost perfect nonlinear (APN) functions with high linearity can be used to constru...

### 3. Constructions of Generalized Sidon Sets (2004)
**Authors:** Greg Martin, Kevin O'Bryant
**URL:** http://arxiv.org/abs/math/0408081v2
**Abstract:** We give explicit constructions of sets S with the property that for each integer k, there are at most g solutions to k=s_1+s_2, s_i\in S; such sets are called Sidon sets if g=2 and generalized Sidon sets if g\ge 3. We extend to generalized Sidon sets the Sidon-set constructions o...

