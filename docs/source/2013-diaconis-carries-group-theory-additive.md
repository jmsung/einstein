---
type: source
kind: paper
title: Carries, group theory, and additive combinatorics
authors: Persi Diaconis, Xuancheng Shao, Kannan Soundararajan
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1309.0434v1
source_local: ../raw/2013-diaconis-carries-group-theory-additive.pdf
topic: general-knowledge
cites: 
---

# Carries, group theory, and additive combinatorics

**Authors:** Persi Diaconis, Xuancheng Shao, Kannan Soundararajan  ·  **Year:** 2013  ·  **Source:** http://arxiv.org/abs/1309.0434v1

## One-line
Frames the "carries" of base-$b$ addition as cocycles in group extensions and proves that if coset representatives have few carries, the extension must split — using approximate-homomorphism machinery from additive combinatorics.

## Key claim
For a finite-index normal subgroup $H \trianglelefteq G$ with coset representatives $X$, if $C(X) = |\{x,y \in X : xy \in X\}| / |X|^2 > 7/9$, then there exists a subgroup $K \leq G$ with $HK = G$ and $H \cap K = \{1\}$ (i.e., the extension splits as a semidirect product). The constant $7/9$ is sharp, attained by $3\mathbb{Z} \subset \mathbb{Z}$ with balanced representatives.

## Method
The proof reinterprets the coset-representative map $f: G/H \to G$ as an $\varepsilon$-approximate homomorphism with $\varepsilon = C(X)$, then invokes the Ben-Or–Coppersmith–Luby–Rubinfeld structure theorem: any $\varepsilon$-approximate homomorphism with $\varepsilon > 7/9$ agrees with a genuine homomorphism on a set of density $\geq 1 - \tau(\varepsilon)$, where $\tau(\varepsilon) = (3 - \sqrt{24\varepsilon - 15})/12$. Auxiliary results use Pollard's theorem (a Cauchy–Davenport generalization), Freiman's $3k-3$ theorem, Freiman isomorphism / rectification, and a Fournier-style argument on $\mathrm{Sym}_{1-\varepsilon}(A)$ sets.

## Result
- Optimal carry-count for $b\mathbb{Z} \subset \mathbb{Z}$: balanced digits $\{0, \pm 1, \ldots, \pm(b-1)/2\}$ achieve exactly $\lfloor b^2/4 \rfloor$ carries, the minimum; $C(\mathbb{Z}, b\mathbb{Z}) = 1 - \lfloor b^2/4 \rfloor / b^2 = 3/4 + o(1)$.
- For $p(\mathbb{Z}/p^2\mathbb{Z}) \subset \mathbb{Z}/p^2\mathbb{Z}$ with $p$ odd prime: at most $(3p^2+1)/4$ additive triples (via Pollard); balanced reps are again optimal.
- A weaker result (Fournier-style): if $C(A) \geq 1 - \delta$ with $\delta \leq 1/60$, then $A$ is close to a subgroup $K$ with $|K| \leq 10|A|/9$ and $|A \cap K| \geq (1-5\delta)|A|$.
- Characterization: if the carry matrix of $A \subset \mathbb{Z}/p^2\mathbb{Z}$ has only two distinct entries, $A$ is (up to dilation/translation) the standard digits $\{0,1,\ldots,p-1\}$.

## Why it matters here
General background; no direct arena tie. The paper is a clean gateway into **additive combinatorics machinery** (Cauchy–Davenport, Pollard, Freiman $3k-3$, Freiman isomorphism / rectification, Plünnecke-style sumset bounds, approximate-homomorphism theorems) which underpins extremal combinatorics work on Sidon-like sets, sumset/difference-set problems, and additive energy — tools potentially relevant to autocorrelation-inequality and discrete-combinatorics problems on the arena.

## Open questions / connections
- Two-dimensional carries: conjectured $C(\mathbb{Z}^2, b\mathbb{Z} \times b\mathbb{Z}) = (3/4 + o(1))^2 = 9/16 + o(1)$ via product of balanced reps; Shao [32] proves only $\leq 1 - 3\sqrt{3}/(4\pi) \approx 0.59$.
- Extend the two-carry-types characterization (Theorem 6.1) beyond cyclic prime-power groups.
- Behavior of $\varepsilon$-approximate homomorphisms for small $\varepsilon$ is governed by the **Polynomial Freiman–Ruzsa (PFR) conjecture** in finite-field settings — a major open problem in additive combinatorics.
- Sharpness of constants in the Fournier-style $\delta \leq 1/60$ bound.

## Key terms
carries, cocycle, group extension, semidirect product, coset representatives, approximate homomorphism, Cauchy-Davenport theorem, Pollard theorem, Freiman 3k-3 theorem, Freiman isomorphism, rectification, additive energy, sumset, PFR conjecture, Ben-Or-Coppersmith-Luby-Rubinfeld, Diaconis, Soundararajan, Green, Ruzsa, Lev
