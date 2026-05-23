---
type: source
kind: paper
title: Periodic words, common subsequences and frogs
authors: B. Bukh, Christopher Cox
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1912.03510
source_local: ../raw/2019-bukh-periodic-words-common-subsequences.pdf
topic: general-knowledge
cites:
---

# Periodic words, common subsequences and frogs

**Authors:** B. Bukh, Christopher Cox  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1912.03510

## One-line
Sharp asymptotics for the expected longest common subsequence (LCS) between a random word $R \sim \Sigma^n$ and a periodic word $W^{(\rho n)}$, derived via a novel interacting particle system ("frog dynamics") that is a labeled variant of PushTASEP.

## Key claim
$\mathbb{E}\,\mathrm{LCS}(R, W^{(\rho n)}) = \gamma_W n - \tau_W \sqrt{n} + O(1)$, where $\gamma_W(\rho)$ is a piecewise-linear, concave function of $\rho$, $\tau_W \neq 0$ only at slope-change points, and both constants are finitely computable from $W$ — in sharp contrast to the classical Chvátal–Sankoff constant $\gamma$, which is not known to be computable.

## Method
Encode $\mathrm{LCS}(R, W^{(x)})$ as a "$k$-height" function whose $k$ ledges induce a bijection ("frog arrangement") on a cycle of $k$ lily pads. Appending a symbol to $R$ corresponds to one step of the frog Markov chain (agitated frogs hop to the next pad not occupied by a nastier agitated frog). Average frog speeds $s_m$ from the chain's stationary distribution give $\gamma_W = \rho - \frac{1}{k}\sum_{s_m \le \rho}(\rho - s_m)$; Gaussian fluctuation analysis yields $\tau_W$ and a CLT (or a max-of-two-Gaussians limit when $\tau_W = 0$).

## Result
For irreducible $W \in \Sigma^k$: unique stationary distribution exists, $\gamma_W$ has the explicit speed-sum formula above, $\mathrm{LCS}(R, W^{(\rho n)})$ is asymptotically normal with linear variance except at slope-change $\rho$ (where it converges to $\min$ of two Gaussians). For the special case $W = 12\cdots k$ (all distinct letters): $s_m = (k+1)/[(k+2-m)(k+1-m)]$, and the stationary distribution has a closed form counting Dyck-path-like arrangements of $\pm 1$'s. New $O(n^{3/2})$ probabilistic algorithm for LCS of two random words yields refined Chvátal–Sankoff estimate $\gamma \approx 0.8122$ (binary alphabet) and the conjecture $\mathbb{E}\,\mathrm{LCS}(R,R') = \gamma n - \Theta(n^{1/3})$.

## Why it matters here
General background; no direct arena tie. The frog-dynamics / PushTASEP connection and the periodic-word LCS framework are not used by any of the 23 Einstein Arena problems (sphere packing, kissing, autocorrelation, etc.). Faint relevance: the $O(n^{1/3})$ subleading-correction conjecture and the "minimum of two Gaussians" limit are examples of the kind of refined finite-size scaling analysis that might inform future variance/fluctuation findings if combinatorial-string problems ever enter the arena.

## Open questions / connections
- Rate of convergence and variance of the standard Chvátal–Sankoff LCS — is $\mathrm{Var}\,\mathrm{LCS}(R,R') = \Theta(n)$? (still open; Conjecture 38 implies yes.)
- Asymptotic behavior of $c_k = \max_W \lim_n \frac{1}{n}\mathbb{E}\,\mathrm{LCS}(R, W)$ vs Chvátal–Sankoff $\gamma_k \sim 2/\sqrt{k}$; authors conjecture $c_k \sim 2/\sqrt{k}$ as well, with $c_2 \ge 0.8211$.
- High-level explanation for the Dyck-path coupling and time-reversal property (Claim 36) — possible link to Angel's multi-species TASEP coupling and Ferrari–Martin queuing interpretation.

## Key terms
longest common subsequence, LCS, Chvátal–Sankoff constant, periodic word, frog dynamics, PushTASEP, interacting particle system, stationary distribution, Dyck paths, Markov chain CLT, multi-species TASEP, $k$-height
