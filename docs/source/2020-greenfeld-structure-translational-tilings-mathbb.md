---
type: source
kind: paper
title: The structure of translational tilings in $\mathbb{Z}^d$
authors: Rachel Greenfeld, Terence Tao
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2010.03254v3
source_local: ../raw/2020-greenfeld-structure-translational-tilings-mathbb.pdf
topic: general-knowledge
cites: 
---

# The structure of translational tilings in $\mathbb{Z}^d$

**Authors:** Rachel Greenfeld, Terence Tao  ·  **Year:** 2020  ·  **Source:** http://arxiv.org/abs/2010.03254v3

## One-line
Proves that every level-one translational tiling of a periodic set in $\mathbb{Z}^2$ by a finite tile is weakly periodic, with a polynomial-in-diameter bound on the period, and exhibits a non-weakly-periodic level-4 counterexample.

## Key claim
For finite $F \subset \mathbb{Z}^2$ with $|F| > 1$ and any level-one tiling $A$ of an $\ell\mathbb{Z}^2$-periodic set $E$, there is a sublattice $\Lambda$ of index $\ll_{|F|} \ell\,\mathrm{diam}(F)^{2(|F|-1)^2}$ such that $A$ restricted to each coset of $\Lambda$ is $Lh_j$-periodic for one of $\le |F|-1$ incommensurable directions $h_j$; the planar periodic tiling conjecture holds with period $M \ll_{|F|} \ell\,\mathrm{diam}(F)^{O(|F|^4)}$, giving exponential-type decidability $\exp(O_{|F|}(\mathrm{diam}(F)^{O(|F|^4)}))$. A level-4 tiling by an 8-element tile is constructed that is not weakly periodic.

## Method
Physical-space "dilation lemma": if $1_F * 1_A = k$ then $1_{rF} * 1_A = k$ for all $r \equiv 1 \pmod q$ where $q$ is the lcm of small primes — proven via Fermat's little theorem and the Frobenius identity $(x+y)^p = x^p + y^p \pmod p$. Averaging over dilations yields a structure theorem $1_A = \tfrac{1}{\ell}1_F * 1_A - \sum_{f \in F\setminus\{0\}} \varphi_f$ with each $\varphi_f$ being $qf\mathbb{Z}$-periodic. In dimension 2, discrete differentiation reduces the $\varphi_f \bmod 1$ to polynomials, then Weyl equidistribution + an exponential-sum estimate (Stechkin) rules out the equidistributed case, leaving periodicity. A "slicing lemma" converts weakly periodic tilings to fully periodic ones with polynomial period blow-up.

## Result
Theorem 1.3(i): level-one tilings of periodic sets in $\mathbb{Z}^2$ are always weakly periodic (finite disjoint union of one-direction-periodic sets). Theorem 1.3(ii): an explicit 8-element tile $F = \{0,1\} \cdot (0,2) + \{0,1\} \cdot (1,0) + \{0,1\} \cdot (2,-2)$ admits a level-4 tiling $A$ built from $\chi(m_1,m_2) = (-1)^{\lfloor m_2/2 \rfloor + m_1}$ and $\{\alpha m_i\}$ (with $\alpha$ irrational) that is provably not weakly periodic. Corollary 3.5 gives a polynomial-in-diameter universal period for all 1-D tilings of a bounded tile.

## Why it matters here
General background; no direct arena tie. Closest relevance is to combinatorial / discrete-geometry problems involving lattice arrangements, packings, or periodic structure detection — the dilation lemma and "averaging over admissible dilations" trick is a transferable technique for problems where a structure is preserved under multiplicative symmetry. Adds machinery beyond what the wiki currently has on tiling / periodicity.

## Open questions / connections
- Does the periodic tiling conjecture hold in $\mathbb{Z}^d$ for $d > 2$ when $|F|$ is composite and not 4? (Open; only known for $|F|$ prime or $=4$.)
- Higher-level analogue of Conjecture 1.1 in $\mathbb{Z}^2$: does every level-$k$ tileable $F$ admit a periodic level-$k$ tiling? (Counterexample here is not weakly periodic but does admit a periodic level-4 tiling, so leaves this open.)
- Can the $\exp(\mathrm{diam}(F)^{O(|F|^4)})$ decidability bound be improved to polynomial without assuming $P = NP$? Bíró's $\exp(O_\varepsilon(\mathrm{diam}(F)^{1/3+\varepsilon}))$ in 1-D is the current best comparable benchmark.
- Connects to Granville–Rudnick on torsion points / Lang's conjecture (roots of unity in zero sets of finitely-supported $\mathbb{Z}$-valued functions lie on finitely many codimension-1 subgroups).

## Key terms
translational tiling, periodic tiling conjecture, weak periodicity, dilation lemma, Frobenius identity, level-$k$ tiling, structure theorem, $\mathbb{Z}^2$ lattice, Bhattacharya, Lagarias–Wang, Weyl equidistribution, decidability, Greenfeld, Tao
