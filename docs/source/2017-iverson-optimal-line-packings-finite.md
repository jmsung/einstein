---
type: source
kind: paper
title: OPTIMAL LINE PACKINGS FROM FINITE GROUP ACTIONS
authors: Joseph W. Iverson, J. Jasper, D. Mixon
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1709.03558
source_local: ../raw/2017-iverson-optimal-line-packings-finite.pdf
topic: general-knowledge
cites:
---

# OPTIMAL LINE PACKINGS FROM FINITE GROUP ACTIONS

**Authors:** Joseph W. Iverson, J. Jasper, D. Mixon  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1709.03558

## One-line
Unifies many disparate constructions of optimal line packings (equiangular tight frames, ETFs) by deriving them as projections in the adjacency algebras of Schurian association schemes arising from transitive finite group actions.

## Key claim
Every transitive action of a finite group $G$ on a set $X$ (with point stabilizer $H$) yields a Schurian scheme whose spherical-function projections $E_j = \frac{m_j}{|X|} \sum_i \omega_j(a_i) A_i$ are Gram matrices of homogeneous $(G,H)$-frames; for Gelfand pairs (multiplicity-free $(G,H)$) every projection in the adjacency algebra has this form, and many such projections are ETFs achieving the Welch bound $\mu \geq \sqrt{(n-d)/(d(n-1))}$. As a concrete payoff, $(H \rtimes \mathrm{Sp}(K), \mathrm{Sp}(K))$ is a Gelfand pair (Thm 5.3) and yields the first known infinite family of ETFs with Heisenberg symmetry: $\Phi_E$ of $|A|^2$ vectors in $\mathbb{C}^{|A|(|A|+1)/2}$ and Naimark complement $\Phi_O$ in $\mathbb{C}^{|A|(|A|-1)/2}$, for any finite abelian $A$ of odd order (Thm 6.4).

## Method
Identify the adjacency algebra $\mathcal{A}$ of a Schurian scheme with the commutant $C(\lambda)$ of the permutation representation, and with the bi-$H$-invariant convolution algebra $L^2(H\backslash G/H)$; use spherical functions $\omega_j$ from the character table to enumerate projections $E_j$. Read each projection as a Gram matrix → recover frame vectors up to unitary equivalence. For the Heisenberg construction: build the Schrödinger representation $\pi_\gamma$ of $H = K \times C_{\exp(A)}$, $K = A \times \hat{A}$, then take $\rho_\gamma(u,1) P_E$ and $\rho_\gamma(u,1) P_O$ where $P_E, P_O$ project onto even/odd functions in $L^2(A)$; show the resulting frame is equiangular and tight via Hilbert–Schmidt orthonormality of $\{|A|^{-1/2}\pi_\gamma(u,1)\}_{u \in K}$.

## Result
Inner products of the Heisenberg ETF: $\langle \rho_\gamma(u,1)P_E, \rho_\gamma(v,1)P_E \rangle = \tfrac{1}{2}\gamma([u,v]^{1/2})$ for $u \neq v$ (and $\tfrac{|A|+1}{2}$ on diagonal); dually $-\tfrac{1}{2}\gamma([u,v]^{1/2})$ for $\Phi_O$. The construction recovers known parameter pairs $(d,n) = (10,25), (15,25)$, and a GAP search over $|G| \leq 100{,}000$ degree $\leq 24$ shows the spherical-function + projective-reduction construction accounts for **all** known real/complex ETF sizes with $n \leq 30$ except 4×16, 12×16, 5×25, 20×25 (SIC-POVMs and Naimark complements, themselves Heisenberg-group projective reductions). Example 3.6 exhibits a real ETF of 28 vectors in $\mathbb{R}^7$ from $\mathrm{AGL}(\mathbb{F}_3^2)$ acting on lines in $\mathbb{F}_3^2$.

## Why it matters here
Provides a constructive group-theoretic recipe for ETFs / optimal projective packings — directly relevant to any Einstein Arena problem framed as line packing or Grassmannian optimization (Tammes-type problems, real/complex projective coherence minimization). Anchors what "highly symmetric optimal arrangement" actually means: the Gram matrix lives in a commutative ∗-subalgebra with few distinct entries, so the search reduces from continuous to discrete (enumerate subsets $D \subseteq \{0,\dots,r\}$). Complements existing wiki content on Cohn–Elkies / LP duality (continuous) and difference sets / harmonic frames (abelian special case).

## Open questions / connections
- Relationship between Heisenberg-symmetric ETFs constructed here and the conjectured Heisenberg-covariant SIC-POVMs of Zauner's conjecture — "we expect there to be some sort of relationship (as in [2])" but it is left open.
- Which other Gelfand pairs $(G,H)$ produce ETFs? The GAP enumeration is complete only up to $|G| \leq 100{,}000$, degree $\leq 24$, multiplicity 1 — larger searches may reveal new infinite families.
- Generalizes the abelian harmonic-frame / difference-set construction (Xia–Zhou–Giannakis 2005) and the central-group-frame / hyperdifference-set construction (Iverson–Jasper–Mixon 2016) into one Gelfand-pair framework — what is the right "hyperdifference set" analog for arbitrary Gelfand pairs?

## Key terms
equiangular tight frames, ETF, Welch bound, Schurian association schemes, Gelfand pairs, spherical functions, Heisenberg group, symplectic group, Schrödinger representation, line packing, projective reduction, harmonic frames, difference sets, SIC-POVM, Zauner conjecture, Naimark complement, group frames, adjacency algebra, coherence minimization
