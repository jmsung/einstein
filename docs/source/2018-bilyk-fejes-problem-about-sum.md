---
type: source
kind: paper
title: On the Fejes Tóth problem about the sum of angles between lines
authors: D. Bilyk, Ryan W. Matzke
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1801.07837
source_local: ../raw/2018-bilyk-fejes-problem-about-sum.pdf
topic: general-knowledge
cites:
---

# On the Fejes Tóth problem about the sum of angles between lines

**Authors:** D. Bilyk, Ryan W. Matzke  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1801.07837

## One-line
Proves new upper bounds for the sum of pairwise acute angles between $N$ unit vectors on $S^d$ (Fejes Tóth's 1959 conjecture) and gives three alternative proofs of the settled $d=1$ case.

## Key claim
For all $d \geq 2$, the energy $I(\mu) = \int\int \arccos|x\cdot y|\, d\mu(x)d\mu(y) \leq \tfrac{\pi}{2} - \tfrac{69}{50(d+1)}$; on $S^2$ this gives $\leq 1.1108$, improving the prior bound $\tfrac{3\pi}{8} \approx 1.178$ from Fodor–Vígh–Zarnócz. Conjectured optimum is $\tfrac{\pi}{2}\cdot\tfrac{d}{d+1}$, achieved by the orthonormal-basis measure $\nu_{\text{ONB}} = \tfrac{1}{d+1}\sum \delta_{e_i}$.

## Method
Upper-bound the potential $F(t)=\arccos|t|$ by a quadratic $\tfrac{\pi}{2}-bt^2$ (valid for $b\leq 50/69$) and apply the **frame potential** lower bound $I_{t^2}(\mu) \geq \tfrac{1}{d+1}$ (Benedetto–Fickus, with Cauchy–Schwarz on the second-moment matrix). For $d=1$: three independent proofs via (i) Chebyshev expansion showing $F$ is negative-definite, (ii) Fourier cosine series with a lemma identifying $\sigma_N$-maximizers from sign patterns of $\hat G(n)$, (iii) a new **Stolarsky-type principle** equating $L^2$ discrepancy w.r.t. antipodal quadrants $Q(x)=\{y:|x\cdot y|>\tfrac{\sqrt 2}{2}\}$ to $\tfrac{1}{4}-\tfrac{1}{\pi}I(\mu)$.

## Result
$I(\mu) \leq \tfrac{\pi}{2}-\tfrac{69}{50(d+1)}$ for all $d\geq 2$; conjecture proved for $d=1$ with $I(\mu)\leq \tfrac{\pi}{4}$ via three routes. **Dimension-reduction lemma**: if $\mu=\alpha\bar\nu+\beta\bar\lambda$ on orthogonal subspheres, $I_F(\mu)=\alpha^2 I_F(\nu)+\beta^2 I_F(\lambda)+2\alpha\beta F(0)$, yielding $M_{d-1}\leq \pi - \pi^2/(4M_d)$ and showing validity in dim $d$ implies validity in all lower dimensions.

## Why it matters here
Direct background for **autocorrelation/angle-sum extremal problems** and any arena problem where the maximizer is conjectured to be an orthonormal basis (not the uniform measure $\sigma$); introduces the "weak repulsion at orthogonality" regime which is distinct from classical Riesz-energy uniformization. The frame-potential + quadratic-dominator trick is a reusable technique template: dominate a non-tractable potential by $a-bt^2$ then invoke $I_{t^2}\geq 1/(d+1)$.

## Open questions / connections
- The quadratic-dominator method has "very little room for improvement" — proving the full conjecture in $d\geq 2$ requires fundamentally different ideas (no Chebyshev/Fourier/Stolarsky analogue carries over because $\arccos|t|$ is not negative-definite on $S^d$, $d\geq 2$).
- Dimension reduction means proving the conjecture for infinitely many $d$ suffices for all $d\geq 2$ — opens an asymptotic/large-$d$ attack route.
- Connection to **$p$-frame potential** $F(t)=|t|^p$ (Ehler–Okoudjou) and one-bit sensing tessellations (Bilyk–Lacey, $F(t)=(\arcsin t)^2$).

## Key terms
Fejes Tóth conjecture, frame potential, tight frame, Benedetto–Fickus, $p$-frame potential, orthonormal basis measure, Stolarsky invariance principle, $L^2$ spherical cap discrepancy, Chebyshev expansion, negative-definite potential, antipodal quadrants, dimension reduction, sphere energy optimization, $\arccos|x\cdot y|$ potential
