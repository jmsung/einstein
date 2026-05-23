---
type: source
kind: paper
title: Spectra of eigenstates in fermionic tensor quantum mechanics
authors: I. Klebanov, A. Milekhin, F. Popov, G. Tarnopolsky
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1802.10263
source_local: ../raw/2018-klebanov-spectra-eigenstates-fermionic-tensor.pdf
topic: general-knowledge
cites:
---

# Spectra of eigenstates in fermionic tensor quantum mechanics

**Authors:** I. Klebanov, A. Milekhin, F. Popov, G. Tarnopolsky  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1802.10263

## One-line
Analyzes the Hilbert-space spectrum of the $O(N_1)\times O(N_2)\times O(N_3)$ Majorana tensor quantum mechanics with tetrahedral Hamiltonian $H \sim g\,\psi^{abc}\psi^{ab'c'}\psi^{a'bc'}\psi^{a'b'c}$, deriving energy bounds, singlet counts, and exact spectra in matrix-model limits.

## Key claim
(i) Number of $SO(N)^3$ singlets jumps from 2 ($N=2$) → 36 ($N=4$) → 595{,}354{,}780 ($N=6$), nonzero only when all $N_i$ even, and asymptotically $\sim \exp(N^3 \log 2 / 2 - 3 N^2 \log N / 2)$. (ii) Energies scale at most as $N^3$ in the melonic large-$N$ limit ($J = gN^{3/2}$ fixed); non-singlet/singlet gap is $O(J/N)$. (iii) For $N_3 = 2$ the model reduces to an exactly solvable $O(N_1)\times O(N_2)\times U(1)$ complex matrix model with closed-form Hamiltonian $H = -\tfrac{g}{2}\big[\tfrac{2}{N_1}(4C_2^{SU(N_1)} - C_2^{SO(N_1)} + C_2^{SO(N_2)} + Q^2) - \tfrac{1}{4}N_1 N_2 (N_1+N_2)\big]$ with integer spectrum in units of $g/4$.

## Method
Combines (a) Casimir-operator algebra: writes $H$ as a linear combination of quadratic Casimirs of nested symmetry subgroups, then uses positivity $C_2 \geq 0$ to bound energies; (b) Cauchy–Schwarz on density matrices $\rho_R$ projected onto irreps to derive refined bounds $|E_R| \leq \tfrac{g}{16} N_1 N_2 N_3 \big(N_1 N_2 N_3 + \sum N_i^2 - 4 - \tfrac{8}{N_1 N_2 N_3} \sum (N_i+2) C_i^R\big)^{1/2}$; (c) character-integral / Schur-polynomial decomposition of $SU(N_1 N_2)$ representations into $SO(N_1) \times SO(N_2)$ irreps for the matrix model; (d) conformal-propagator estimate of overlap angle $\cos\theta \approx 0.66$ to extract ground state energy $E_0 \approx -0.041 J N^3$.

## Result
Singlet-state count via integral formula; explicit energy bound $|E| \leq \tfrac{g}{16} N^3 (N+2)\sqrt{N-1}$ for $O(N)^3$ singlets; saturation of bound $|E| \leq \tfrac{g}{8}N_1 N_2 (N_1+N_2)$ for $N_3=2$ ground state (rectangular $N_1/2 \times N_2$ Young diagram for $SU(N_1)$); 't Hooft-limit ground state $E_0 = -\tfrac{\lambda}{4}N^2$ with $O(\lambda)$ gaps; full singlet partition upper bound $P(N^2/8) \sim \exp(\pi N/\sqrt{3})$ for $O(N)^2 \times O(2)$.

## Why it matters here
General background; no direct arena tie. This is high-energy-physics tensor quantum mechanics (SYK/holography motivation), not in any of the 23 arena problem categories. The Casimir-bound technique and Cauchy–Schwarz-on-density-matrix argument are methodologically interesting but the discrete-symmetry / Lie-algebraic framing doesn't transfer to continuous optimization on $\mathbb{R}^n$.

## Open questions / connections
- Whether the $\exp(-cN^3)$ conjectured singlet-sector gap can be proven (paper only argues plausibility from density of states fitting into $O(N^3)$ window).
- Extension of the exactly-solvable matrix-model technique to $N_3 \geq 3$ — paper handles $N_3=1,2$ only; $N_3=3$ already breaks the Casimir-only structure.
- Relation to Gurau–Witten model ($O(N)^6$) singlet spectrum [Krishnan–Kumar 2018, ref 46].
- Whether anomalies fully explain the $N_i$-odd absence of singlets, or whether a stronger group-theoretic obstruction exists (sec 5.2).

## Key terms
Majorana tensor quantum mechanics, SYK model, melonic large-N limit, tetrahedral Hamiltonian, quadratic Casimir bounds, $O(N)^3$ symmetry, singlet counting, Schwinger–Dyson equations, conformal propagator, 't Hooft limit, Schur polynomials, Young diagram Casimirs, Klebanov, Witten, Gurau
