---
type: source
kind: paper
title: Sharp endpoint extension inequalities for the moment curve on finite fields
authors: Chandan Biswas, Emanuel Carneiro, Taryn C. Flock, Diogo Oliveira e Silva, Betsy Stovall, James Tautges
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2508.08377v1
source_local: ../raw/2025-biswas-sharp-endpoint-extension-inequalities.pdf
topic: general-knowledge
cites: 
---

# Sharp endpoint extension inequalities for the moment curve on finite fields

**Authors:** Chandan Biswas, Emanuel Carneiro, Taryn C. Flock, Diogo Oliveira e Silva, Betsy Stovall, James Tautges  ·  **Year:** 2025  ·  **Source:** http://arxiv.org/abs/2508.08377v1

## One-line
First sharp endpoint $L^2 \to L^{2d}$ Fourier extension inequalities for the moment curve $\Gamma = \{(\xi,\xi^2,\dots,\xi^d) : \xi \in \mathbb{F}_q\}$ over finite fields, with optimal constant and constant-modulus maximizers identified in two complementary regimes.

## Key claim
Conjecture 1 — the sharp inequality $\|(f\sigma)^\vee\|_{L^{2d}} \le \big(q^{-d} \sum_{\ell \in P_d} \binom{d}{\ell}^2 \binom{q}{b(\ell)}\big)^{1/(2d)} \|f\|_{L^2}$ with maximizers exactly those $f$ with $|f|$ constant — is proven (Thm 2) for all dimensions $2 \le d \le 20$, and (Thm 3) for all $d$ provided $q \ge \tfrac{d(d-1)}{2\log 6} + \tfrac{2d-1}{3}$.

## Method
Five-step strategy bridging analysis, algebra, and combinatorics: (1) reformulate the extension inequality as counting solutions of the Newton power-sum system $\sum t_i^k = \zeta_k$, with multiplicities indexed by integer partitions $\ell \in P_d$; (2) rewrite as a weighted symmetric-sum inequality $\sum_\ell \omega_\ell \Sigma_\ell \ge 0$ and invoke **Muirhead's inequality** under the dominance order on partitions; (3) verify a fractional matching condition between $\mathcal{N} = \{\omega_\ell < 0\}$ and $\mathcal{P} = \{\omega_\ell \ge 0\}$ via **Strassen's theorem** on weighted bipartite graphs; (4) for low $d$, brute-force check the $2^{|\mathcal{N}|}$ subset conditions in SageMath; (5) for large $q$, asymptotic estimates force $|\mathcal{N}| \le 3$ with all partitions automatically comparable.

## Result
Optimal constant $C^{2d} = q^{-d} \sum_{\ell \in P_d} \binom{d}{\ell}^2 \binom{q}{b(\ell)}$ where $b(\ell)$ records multiplicities of part-values and $b_0(\ell) = |\{i : \ell_i=0\}| + (q-d)$. Maximizers: exactly $|f| \equiv$ const, equality forced by Muirhead's equality case applied to the partition $(d,0,\dots,0)$ which dominates all of $P_d$. The number of conditions to verify in the low-$q$ regime grows at least like $\exp(\pi\sqrt{2d/3}/(12(\log d)^2))$, explaining why $d=20$ is the current computational ceiling.

## Why it matters here
General background; no direct arena tie — the moment curve appears tangentially in discrete geometry (cyclic polytopes, no-three-in-line) and Vinogradov / decoupling theory, but this paper's contribution is a sharp-inequality technique. The **Muirhead + Strassen-style fractional-matching reduction** is potentially transferable: any sharp-inequality problem expressible as a weighted symmetric-sum inequality with comparable-partition structure could use the same pipeline, which may inform autocorrelation (P14, P17) or LP-bound problems where dominance-order reductions arise.

## Open questions / connections
- Extending Conjecture 1 to $d > 20$ — purely a compute scaling problem ($|P_d|$-subset enumeration).
- General polynomial maps $\Phi(t_1,\dots,t_d) = \gamma(t_1)+\dots+\gamma(t_d)$ where $\{t_i\}$ is *not* uniquely recoverable from $\zeta$ (e.g., $\gamma(\xi)=(\xi,\xi^3,\xi^5)$ admits $(1,t,-t)$ family) — method breaks down; tied to unresolved continuous dichotomy [Biswas-Stovall 2025, Thm 1.3].
- Connection to continuous moment-curve maximizers [Biswas-Stovall 2023]: existence known but functional form still elusive — finite-field constant-modulus answer suggests the continuous analogue might be gaussian/exponential, but no proof.

## Key terms
Fourier extension, moment curve, finite fields, sharp restriction theory, Muirhead's inequality, Strassen's theorem, fractional matching, dominance order, integer partitions, symmetric sums, Newton power sums, bipartite graph matching
