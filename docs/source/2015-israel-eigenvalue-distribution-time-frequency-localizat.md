---
type: source
kind: paper
title: The Eigenvalue Distribution of Time-Frequency Localization Operators
authors: Arie Israel
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1502.04404
source_local: ../raw/2015-israel-eigenvalue-distribution-time-frequency-localizat.pdf
topic: general-knowledge
cites:
---

# The Eigenvalue Distribution of Time-Frequency Localization Operators

**Authors:** Arie Israel  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1502.04404

## One-line
Provides quantitative upper and lower bounds on how many eigenvalues of a time-frequency localization operator (TFLO) lie in the "plunge region" $(\epsilon, 1-\epsilon)$ via a wave-packet (local cosine) approximate diagonalization.

## Key claim
For $J=[-1/2,1/2]$, $I=[-D/2,D/2]$, $\Lambda = |I|\cdot|J| = D$, and each $\eta \in (0,1/2]$, the eigenvalues $\lambda_k$ of $T_{I,J} = R_I P_J R_I$ satisfy $\{k : \lambda_k \in (\epsilon, 1-\epsilon)\} \subset [D-K, D+K]$ where $K = A_\eta \cdot (\log\log D \cdot \epsilon^{-1})^{1+\eta} \cdot \log(D\epsilon^{-1})$. This improves the $D$-dependence over Osipov's $\log(D)^2 \log(1/\epsilon)$ bound but is sub-optimal in $\epsilon$ by a factor of $\log(1/\epsilon)$.

## Method
Build an orthonormal local-cosine (Coifman–Meyer) basis $\{\Phi_{(j,k)}\}$ over the Whitney decomposition of $I$, using a $C^\infty$ cutoff $\theta$ with near-exponential Fourier decay $|\hat\theta(\xi)| \lesssim \exp(-a|\xi|^{1-\eta})$. Partition basis indices into "low" (time-freq box inside $I\times J$, where $T\Phi \approx \Phi$), "high" (outside, where $T\Phi \approx 0$), and "medium" (boundary). A functional-analysis lemma then bounds $M_\epsilon \leq 2\cdot\#(\Gamma_{\text{med}})$, so counting boundary wave packets gives the eigenvalue count.

## Result
The "plunge region" of the TFLO spectrum has size $O((\log\log D \cdot \epsilon^{-1})^{1+\eta} \log(D\epsilon^{-1}))$, with the bulk $\approx D$ eigenvalues near 1 and the rest decaying. Theorem 1 (from Landau) anchors the median: $\lambda_{[D]-1} \leq 1/2 \leq \lambda_{[D]}$. The wave-packet construction is constructive and avoids the asymptotic-only machinery of Landau [3] and the complicated eigenvalue formulas of Osipov [7].

## Why it matters here
Connects to the uncertainty / functional-inequality cluster of Einstein Arena problems: PSWFs are the canonical extremals for time-frequency concentration, the same family that appears in Cohn–Elkies-style sphere packing magic functions and Beurling–Selberg extremal problems. The local-cosine / wave-packet technique gives a constructive tool for analyzing operators whose extremals are otherwise only accessible via numerical PDE solvers — potentially relevant for autocorrelation inequality problems.

## Open questions / connections
- Can the method close the $\log(1/\epsilon)$ gap to reach the conjectured optimum $K'' = C\log(D)\log(1/\epsilon)$?
- Extension to higher-dimensional TFLOs (domains in $\mathbb{R}^d \times \mathbb{R}^d$) — explicitly left as future work; relevant for $d$-dim sphere packing extremals.
- Relation to the Slepian–Pollak–Landau original asymptotics [3,5,6] and to Beurling–Selberg one-sided extremal problems.

## Key terms
prolate spheroidal wave functions, PSWF, time-frequency localization, plunge region, local cosine basis, Coifman-Meyer, Whitney decomposition, wave packets, bandlimited functions, eigenvalue distribution, Slepian, Landau-Pollak, uncertainty principle, Fourier concentration
