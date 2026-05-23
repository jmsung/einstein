---
type: source
kind: paper
title: Polygonal Complexes and Graphs for Crystallographic Groups
authors: D. Pellicer, E. Schulte
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1310.4905
source_local: ../raw/2013-pellicer-polygonal-complexes-graphs-crystallographic.pdf
topic: general-knowledge
cites:
---

# Polygonal Complexes and Graphs for Crystallographic Groups

**Authors:** D. Pellicer, E. Schulte  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1310.4905

## One-line
Survey of the classification program for highly symmetric discrete polyhedral structures (regular polygonal complexes, chiral polyhedra, two-orbit polyhedra) in Euclidean 3-space $E^3$.

## Key claim
The classification is complete in three regimes: (i) exactly 48 regular polyhedra in $E^3$ (18 finite + 30 apeirohedra); (ii) exactly 25 regular polygonal complexes that are not polyhedra (4 non-simply-flag-transitive + 21 simply-flag-transitive), enumerated by mirror vector; (iii) chiral polyhedra fall into 6 infinite 2-parameter families of apeirohedra (3 finite-faced, 3 helix-faced); (iv) finite regular polyhedra of index 2 comprise 22 infinite families (2 vertex-orbits) + 10 individual polyhedra (1 vertex-orbit).

## Method
Group-theoretic classification via Wythoff's construction: a regular complex is reconstructed from the special group $G^* = G/T(G)$ (a finite subgroup of $O(3)$) plus distinguished generating involutions $R_0, R_1, R_2$ satisfying Coxeter-type relations $R_i^2 = (R_0R_1)^p = (R_1R_2)^q = (R_0R_2)^2 = I$. Bieberbach's theorem reduces the crystallographic-group analysis to the finite quotient. Cases are indexed by the **mirror vector** $(\dim R_0, \dim R_1, \dim R_2)$ and by translation lattices ($\mathbb{Z}^3$, fcc, bcc, $\Lambda_{(a,a,0)}$, etc.). Chiral polyhedra use rotational generators $S_1, S_2$ with $S_1^p = S_2^q = (S_1S_2)^2 = I$.

## Result
- 48 regular polyhedra in $E^3$: 9 Platonic + Kepler-Poinsot, 9 Petrie-duals, 6 planar apeirohedra, 12 blended apeirohedra, 12 pure apeirohedra.
- 25 non-polyhedral regular polygonal complexes (Theorems 2-3): 4 arising as 2-skeleta of regular 4-apeirotopes (paired via Petrie-duality), and 21 simply flag-transitive complexes catalogued in Table 2 by mirror vectors $(1,2), (1,1), (0,1), (0,2), (2,1), (2,2)$ with edge multiplicities $r \in \{3,4,6,8\}$.
- 6 chiral apeirohedron families: $P(a,b)$ of type $\{6,6\}$, $Q(c,d)$ of type $\{4,6\}$, $Q(c,d)^*$ of type $\{6,4\}$ (finite-faced, skew); $P_1, P_2, P_3$ helix-faced. Helix-faced chiral polyhedra are combinatorially regular; finite-faced ones are combinatorially chiral. Special groups confined to $[3,3]^+$, $[3,4]$, $[3,4]^+$.
- Special groups never contain rotations of period $\neq 2,3,4,6$, and period 6 only in $E^2$.

## Why it matters here
General background; no direct arena tie. Could inform discrete-geometry problems requiring crystallographic-symmetry constructions (e.g., periodic point/edge configurations on lattices $\mathbb{Z}^3$, fcc, bcc); the mirror-vector / Wythoff-construction framework is a candidate template for generating symmetric initial configurations in packing or kissing-number searches.

## Open questions / connections
- Full enumeration of all 2-orbit polyhedra in $E^3$ across the seven classes $2^I$, $I \subsetneq \{0,1,2\}$ — currently only chiral ($I = \emptyset$) and index-2 regular are done.
- Enumeration of edge-transitive polyhedra in $E^3$ — open.
- Extension to finite 2-orbit or edge-transitive **polygonal complexes** (not polyhedra) — even existence is open.
- Realization theory for non-regular polytopes / complexes in arbitrary dimension (cf. McMullen's forthcoming *Geometric Regular Polytopes*).

## Key terms
regular polyhedra, polygonal complexes, chiral polyhedra, two-orbit polyhedra, crystallographic groups, Wythoff construction, Petrie duality, Grünbaum-Dress polyhedra, apeirohedra, mirror vector, Schläfli symbol, special group, Bieberbach theorem, Coxeter, McMullen, Schulte, Pellicer, Petrie-Coxeter, helical polygon, skew polygon, face-centered cubic lattice, body-centered cubic lattice, regular maps, index-2 polyhedra
