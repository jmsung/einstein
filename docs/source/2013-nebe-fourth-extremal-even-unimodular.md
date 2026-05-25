---
type: source
kind: paper
title: A fourth extremal even unimodular lattice of dimension 48
authors: G. Nebe
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1312.3780
source_local: ../raw/2013-nebe-fourth-extremal-even-unimodular.pdf
topic: general-knowledge
cites:
---

# A fourth extremal even unimodular lattice of dimension 48

**Authors:** G. Nebe  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1312.3780

## One-line
Constructs a new (fourth) extremal even unimodular lattice $P_{48m}$ in dimension 48 by classifying lattices invariant under an order-5 automorphism of a specific type.

## Key claim
There is a unique extremal even unimodular 48-dimensional lattice admitting an automorphism $\sigma$ of type $5-(8,16)-8$; it is non-isometric to the three previously known extremal lattices $P_{48p}, P_{48q}, P_{48n}$, and is named $P_{48m}$.

## Method
Uses the "type of an automorphism" framework $p-(z,d)-s$: the $\sigma$-invariant decomposition $L \supseteq L_K(\sigma) \oplus L_I(\sigma) \supseteq pL$ forces $L_K \cong \Lambda_{16} = [2.\mathrm{Alt}_{10}]_{16}$ (a $5$-modular lattice of minimum 6, unique by Bachoc–Venkov) and $L_I \cong \Lambda_{32}$ (the rescaled trace lattice of a Hermitian unimodular $\mathbb{Z}[\zeta_5]$-lattice of rank 8). Kneser neighboring enumerates 207 Hermitian unimodular $\mathbb{Z}[\zeta_5]$-lattices (mass $\approx 0.43$ via Shimura), of which exactly one has trace-dual minimum $\geq 6$. Extensive Magma orbit computations over $\mathrm{Aut}(M)$ then build all sublattices $M \leq X \leq M^\#$ of index $5^8$ that are unimodular with minimum 6.

## Result
Six lattices found, all in one $\mathrm{Aut}(M)$-orbit, giving a unique $P_{48m}$ with extremal minimum $\min(L) = 2 + 2\lfloor 48/24 \rfloor = 6$ and kissing number $52{,}416{,}000$ (tied with the other three). The stabilizer $\mathrm{Stab}_{\mathrm{Aut}(M)}(P_{48m})$ has order 1200 (Magma small group $(1200, 573)$); Sylow-2 is $D_8 Y C_4$, Sylow-5 is $C_5 \times C_5$ inside the normalizer of $\langle\sigma\rangle$. The lattice is deposited in the Nebe–Sloane lattice database as `P48m`.

## Why it matters here
General background; no direct arena tie. Extremal even unimodular lattices in jump dimensions $24m$ are the densest known sphere packings + kissing configurations in their dimensions (dim 24 = Leech, dim 48 = these four, dim 72 = $\Gamma_{72}$), so this paper feeds the wiki's prior on what "structurally rigid optimal lattice" looks like — relevant if a future arena problem touches $n=48$ kissing/packing or modular-form bounds.

## Open questions / connections
- Are there extremal 48-dim lattices outside the four known? Classification by automorphism type is still incomplete — types $3-(20,8)-8$, $3-(16,16)-16$ on $\sqrt{3}D_{16}^+$, and $7-(7,6)-5$ remain open (Table 2).
- Can the Hermitian-Kneser-neighbor + trace-lattice machinery enumerate extremal lattices in dim 72 beyond $\Gamma_{72}$?
- Extends Nebe (Int. J. Number Theory 2013, ref [12]) classifying automorphisms with $\varphi(a) > 24$; this paper handles the next-hardest case $\varphi(5)=4$ where $z=s=8$ forces Hermitian unimodular structure.

## Key terms
extremal even unimodular lattice, dimension 48, P48m, automorphism type, Hermitian unimodular lattice, Z[zeta_5], Kneser neighbor method, Shimura mass formula, trace lattice, kissing number 52416000, Leech lattice, jump dimensions, modular forms bound, Bachoc-Venkov, Nebe
