---
type: source
kind: paper
title: Fourier Interpolation and Time-Frequency Localization
authors: A. Kulikov
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2005.12836
source_local: ../raw/2020-kulikov-fourier-interpolation-time-frequency-localizati.pdf
topic: general-knowledge
cites:
---

# Fourier Interpolation and Time-Frequency Localization

**Authors:** A. Kulikov  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2005.12836

## One-line
Proves that any Fourier interpolation formula must use at least $4R_1R_2 - C\log^{2+\varepsilon}(4R_1R_2)$ sample points in $[-R_1,R_1] \cup [-R_2,R_2]$ (function + Fourier-transform values), matching Slepian's $4WT$ Theorem.

## Key claim
For any interpolation formula $f(x) = \sum_{\lambda\in\Lambda} f^{(r(\lambda))}(\lambda) a_\lambda(x) + \sum_{\mu\in M} \hat f^{(k(\mu))}(\mu) b_\mu(x)$ valid on $C_c^\infty$, under mild polynomial-growth conditions on $b_\mu$ and $n_M$, the counting functions satisfy $n_\Lambda(R_1) + n_M(R_2) \geq 4R_1R_2 - C\log^{2+\varepsilon}(4R_1R_2)$. For even/odd restrictions, replace $4R_1R_2$ by $2R_1R_2$.

## Method
Constructs a smooth bump $f = \sum a_{j,k} \Phi_{j,k}(2R_2 x)$ from Israel's local cosine basis (Coifman–Meyer Whitney decomposition with sharp Fourier concentration $|\mathcal{F}\Phi_{j,k}(\xi)| \lesssim e^{-a_\eta(\delta_j|\xi-\xi_{j,k}|)^{1-\eta}}$). A Landau–Kolmogorov inequality lifts the decay bound to all derivatives. Linear algebra picks coefficients vanishing on the assumed nodes; if $|\Lambda \cap [-R_1,R_1]| + |M \cap [-R_2,R_2]|$ were too small, the resulting nonzero $f$ would contradict the interpolation formula via the tail decay of $\mathcal{F}\Phi_{j,k}$.

## Result
The lower bound $n_\Lambda(R_1) + n_M(R_2) \geq 4R_1R_2 - C\log^{2+\varepsilon}(4R_1R_2)$ is tight up to the log term: it matches the Radchenko–Viazovska formula (nodes $\pm\sqrt n$ giving $1 + 2[R^2]$) and the Bondarenko–Radchenko–Seip zeta-zero formula. As a corollary, $N(T) \geq \tfrac{T}{2\pi}\log\tfrac{T}{2\pi e} - C\log^{2+\varepsilon}(T)$ for Riemann zeta zeros, matching Riemann–von Mangoldt up to the log power.

## Why it matters here
General background for sphere-packing / autocorrelation problems where Cohn–Elkies / Viazovska-style interpolation formulas underpin LP duality bounds — confirms node-density is essentially forced by $4WT$ uncertainty, so any agent attempting to construct shorter magic-function interpolation must respect this floor. No direct arena tie, but informs the bandlimited-function and uncertainty-principle wiki entries.

## Open questions / connections
- Generalization to radial interpolation formulas in dimensions $\geq 5$ (Cohn–Kumar–Miller–Radchenko–Viazovska $E_8$/Leech, Stoller all-dim) — author flags as forthcoming.
- Whether the $\log^{2+\varepsilon}$ error term can be sharpened to $\log$ or removed.
- Local $4WT$ for arbitrary interval pairs $I,J$ not centered at origin (sketched in remarks).
- Extending to convolutions with non-$\delta$ distributions (e.g. Gaussians) — gives alternative proof that Ascensi–Lyubarskii–Seip uniqueness sets admit no interpolation formula.

## Key terms
Fourier interpolation, Slepian 4WT theorem, time-frequency localization, prolate spheroidal wave functions, Radchenko-Viazovska, Cohn-Elkies, magic function, local cosine basis, Coifman-Meyer, Whitney decomposition, Landau-Kolmogorov inequality, Beurling-Malliavin, Bondarenko-Radchenko-Seip, Riemann zeta zeros, sphere packing, uncertainty principle, sampling density, frame theory
