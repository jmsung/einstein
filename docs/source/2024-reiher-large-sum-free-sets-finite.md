---
type: source
kind: paper
title: Large sum-free sets in finite vector spaces I
authors: Christian Reiher, S. Zotova
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2408.11232
source_local: ../raw/2024-reiher-large-sum-free-sets-finite.pdf
topic: general-knowledge
cites:
---

# Large sum-free sets in finite vector spaces I

**Authors:** Christian Reiher, S. Zotova  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2408.11232

## One-line
Determines the second-largest possible size of a sum-free subset of $\mathbb{F}_p^n$ for primes $p \geq 11$ with $p \equiv 2 \pmod 3$, and classifies the extremal configurations.

## Key claim
For $p = 6m-1 \geq 11$ prime and $n \geq 1$: if $A \subseteq \mathbb{F}_p^n$ is sum-free and not contained in the "cuboid" extremal set $[\tfrac{p+1}{3}, \tfrac{2p-1}{3}] \times \mathbb{F}_p^{n-1}$, then $|A| \leq \tfrac{p-2}{3} p^{n-1}$. The bound is tight, achieved by an explicit family of "structured" sets (Definition 1.3) built from a small set $P \subseteq \mathbb{F}_p^{n-1}$ with $0 \notin P+P$.

## Method
Additive-combinatorial structure theory plus Fourier analysis on $\mathbb{F}_p^n$. Core tools: Cauchy–Davenport, Vosper's critical-pair theorem, and Kneser's theorem (used via Lemma 2.5/2.6 to constrain coset structure when $|A|+|B|+|C|$ is large). A non-trivial character with low $\mathrm{Re}\,\widehat{A}(\gamma)$ (Lemma 5.1) forces the slice profile $k \mapsto |A_k|$ to be near-constant; case analysis on $p=11$ vs $p\geq 17$ closes the argument, with the $p=11$ case requiring a delicate cosine-weighted inequality on Fourier coefficients.

## Result
$\mathrm{sf}_1(\mathbb{F}_p^n) = \tfrac{p-2}{3} p^{n-1}$ for all primes $p \geq 11$ with $p \equiv 2 \pmod 3$ and $n \geq 1$. The extremal class $\widetilde{\mathrm{SF}}_1(\mathbb{F}_p^n)$ is exactly the collection of structured sets — products $B \times \mathbb{F}_p^{n-\ell}$ where $B$ is "very structured" on $\mathbb{F}_p^\ell$. Improves Versteegen's prior upper bound $< (\tfrac{p}{3} - \tfrac{1}{6} + \tfrac{1}{p})p^{n-1}$ to the sharp constant and adds the matching classification.

## Why it matters here
General background; no direct arena tie. The paper sits in extremal additive combinatorics over $\mathbb{F}_p^n$ — the same arena as cap-set / sum-free / Sidon-type problems that appear in Einstein problems related to combinatorial extremal questions. The Kneser-theorem / Cauchy–Davenport / Vosper toolkit and the Fourier-on-$\mathbb{F}_p^n$ technique (Parseval + character minimum) are reusable for any extremal problem in finite vector spaces.

## Open questions / connections
- Determining $\mathrm{sf}_2(\mathbb{F}_5^n)$ — flagged as the next natural open problem (the $p=5$ case has unusually rigid extremal sets).
- Extending the $\mathrm{sf}_k$ hierarchy (Definition 1.2) to all finite abelian groups — analogous to Polcyn–Ruciński's higher Turán numbers for hypergraph matchings.
- Companion paper (Part II, Reiher–Zotova, unpublished) handles related cases; Lev's periodicity conjecture for $p=3$ recently proved by Reiher.

## Key terms
sum-free set, finite vector space, $\mathbb{F}_p^n$, Cauchy–Davenport theorem, Vosper theorem, Kneser theorem, symmetry group, additive combinatorics, Fourier analysis on finite groups, Pontryagin dual, Parseval identity, extremal combinatorics, Green–Ruzsa, structured set, cuboid extremal configuration
