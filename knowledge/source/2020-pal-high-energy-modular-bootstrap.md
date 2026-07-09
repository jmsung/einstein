---
type: source
kind: paper
title: High energy modular bootstrap, global symmetries and defects
authors: Sridip Pal, Zheng Sun
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2004.12557
source_local: ../raw/2020-pal-high-energy-modular-bootstrap.pdf
topic: general-knowledge
cites:
---

# High energy modular bootstrap, global symmetries and defects

**Authors:** Sridip Pal, Zheng Sun  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2004.12557

## One-line
Rigorous Cardy-like asymptotic formulas for the growth of operators in defect Hilbert spaces and symmetry-charged sectors of unitary 2D CFTs, using Tauberian techniques applied to torus partition functions with topological defect line (TDL) insertions.

## Key claim
For any unitary modular-invariant 2D CFT with faithful finite global symmetry $G$, every irrep $\alpha$ appears in the untwisted spectrum with growth $d_\alpha^2 |G|^{-1} \rho_0(\Delta)$ where $\rho_0(\Delta) = \tfrac{1}{4}(c/48\Delta^3)^{1/4} \exp(2\pi\sqrt{c\Delta/3})$; the same holds in any $g_0$-twisted sector when $G$ is non-anomalous, and analogous formulas hold for $U(1)$ and for non-invertible TDLs (with quantum-dimension prefactor $N_0$).

## Method
Tauberian formalism: bandlimited majorant/minorant functions $\phi_\pm$ (Beurling–Selberg style) sandwich the indicator of the dimension window $[\Delta-\delta,\Delta+\delta]$, then $S$-modular transformation maps the defect/symmetry-projected partition function to a dual channel dominated by the vacuum. Heavy-state contributions are bounded via HKS-type estimates with $\Lambda < 2\pi$ Fourier support; light contributions reproduce the Cardy kernel. Extension to vector-valued modular functions $Z(\beta) = F \cdot Z(4\pi^2/\beta)$ with $F^2 = I$ unifies all cases.

## Result
Theorems 1–4 give two-sided bounds $c_- N_0 \rho_0(\Delta) \le \tfrac{1}{2\delta}\int_{\Delta-\delta}^{\Delta+\delta} \rho_{\mathcal H_{\mathcal L}}(\Delta')\,d\Delta' \le c_+ N_0 \rho_0(\Delta)$ with $c_\pm = 1 \pm 1/(2\delta)$ and order-one error. For Virasoro primaries ($c>1$) and large $c$, $\Delta$ is replaced by $\Delta - c/12$ and $c$ by $c-1$. For $U(1)$ with Kac–Moody level $k$: charge-$Q$ growth $\sim \tfrac{1}{k}(c/48\Delta^2)^{1/2} \exp(2\pi\sqrt{c\Delta/3})$. Verified numerically against Ising (with $\mathbb Z_2$ and duality defect $\mathcal N$) and compact boson at $R=\tfrac{1}{2}$.

## Why it matters here
General background; no direct arena tie. The Tauberian bandlimited-majorant/minorant technique (Beurling–Selberg extremizers narrowing a dimension/frequency window) is structurally identical to LP-duality methods used in autocorrelation and sphere-packing problems, so the paper provides a worked example of Tauberian sandwich bounds on positive measures — potentially transferable framing for P5/P6/P11 (autocorrelation) and Cohn–Elkies-style problems.

## Open questions / connections
- Extension to LL H-squared and off-diagonal three-point coefficients where positivity holds in one channel only (mentioned as immediate application).
- Spin-sensitive refinement of these growth formulas following Pal–Sun 2019 (arXiv:1910.07727).
- Bounding the lowest nontrivial Virasoro primary dimension and constructing extremal functionals in the presence of TDLs.

## Key terms
Tauberian theorem, Cardy formula, modular bootstrap, Beurling–Selberg extremizer, bandlimited majorant, topological defect line, defect Hilbert space, vector-valued modular function, global symmetry irrep growth, S modular transformation, JT gravity Schwarzian limit, HKS bound
