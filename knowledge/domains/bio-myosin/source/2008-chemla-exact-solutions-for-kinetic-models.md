<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: bio-myosin
domains: [bio-myosin, sci-physics]
title: Exact Solutions for Kinetic Models of Macromolecular Dynamics
authors: [Yann R. Chemla, Jeffrey R. Moffitt, Carlos Bustamante]
year: 2008
doi: 10.1021/jp076153r
source_url: https://doi.org/10.1021/jp076153r
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Exact Solutions for Kinetic Models of Macromolecular Dynamics

## TL;DR
A general matrix formalism, working in Fourier–Laplace space, that yields exact closed-form analytical solutions for the mean velocity, diffusion constant/randomness parameter, branching probabilities, and dwell-time distributions of arbitrarily complex molecular-motor kinetic cycles — including branched and reversible cycles that previous methods could not handle.

## Key findings
- **Core object.** The motor is modeled as a continuous-time random walk on a discrete, periodic 1-D lattice. The master equation is transformed to Fourier–Laplace space (eq 4) and solved for the position probability density `P̃(q,s) = C(q,s)/|R(q,s)|` (eq 9), where `|R(q,s)|` is the characteristic polynomial of the rate matrix `M(q)`.
- **Velocity and diffusion need only the polynomial's low-order coefficients.** `V = −i γ̇(0)/β(0)` (eq 11) and `D` (eq 12) depend only on the three lowest-order coefficients (α, β, γ) of `|R(q,s)|` — **no full eigenvalue solution required**. These reproduce Koza's and Derrida's earlier results (eqs 14–15) for an arbitrary n-state reversible linear cycle.
- **Randomness parameter** `r = 2D/Vd` (eq 13) is given a Michaelis–Menten-like form (eq 34): `r = 1 − 2(q_cat²/k_cat²)·[T](Q_M+[T])/(K_M+[T])²`, defining two new macroscopic constants **q_cat** (effective rate, tied to the number of rate-limiting catalytic transitions) and **Q_M**. At saturating substrate `r → 1 − 2k_cat²/q_cat² ≤ 1`; `r₀ = 1` at low [T] (binding rate-limiting). `r` gives a *lower bound* on the number of rate-limiting transitions.
- **Dwell-time distributions for branched/correlated steppers.** For an irreversible stepping cycle there is a single distribution, `ψ̃(s) = γ₊/|R⁻(s)|` (eqs 18–19). For motors taking multiple step types, the paper introduces a **dwell-time-distribution matrix** ψ̃(s) with conditional elements ψ̃_ij (step before × step after) and the general relation `P̃(q,s) = p₀ᵀ(I − ψ̃(s)G(q))⁻¹ Ψ̃(s)` (eq 22). This distinguishes **correlated** stepping (statistics depend on preceding *and* succeeding step) from **uncorrelated** stepping (eq 23).
- **Worked example (3 models, simulated ATP-dependent motor data, ~10⁶ steps).** Model 1 (linear E→T→D cycle) and Model 3 (same cycle with reversible stepping) yield *identical* V and r despite very different stepping behavior — demonstrating that V and r alone cannot resolve the cycle. Model 2 (parallel forward/backward branches, uncorrelated) is ruled out because measured `p₋₋ = 0` while `p₋` is finite, violating `p±± = p±p±`. Only the **dwell-time distributions** discriminate: ψ₊₊(t), ψ₊₋(t), ψ₋₊(t) fit to 3, 2, and 1 exponentials respectively (Fig 3d–f), proving exactly **3 kinetic states** and locating the irreversible and stepping transitions.
- The number of exponentials summing to a dwell-time histogram equals the exact number of kinetic states — the maximal kinetic information extractable.

## Methods (brief)
Analytical derivation built on Koza's and Derrida's master-equation formalism, extended to Fourier–Laplace space with matrix algebra (amenable to computer-algebra implementation). Validated against Monte Carlo simulations of 3- and 4-state cycles (Figs 2–3). Appendices give full recursion relations for the characteristic-polynomial coefficients and the moment connections.

## Limitations
Assumes exponentially distributed state lifetimes (Markovian); arbitrary waiting-time distributions are out of scope. Off-diagonal dwell-time distributions cannot generally be extracted for m > 2 step types. Resolving closely spaced exponentials requires large step counts (~10⁶ here), and transitions faster than measurement resolution are invisible — inherent limits of any fluctuation measurement.

## Citations of interest
- Koza, *J. Phys. A* 1999 / *Physica A* 2000 (refs 33–34) — the master-equation matrix method this work extends.
- Derrida, *J. Stat. Phys.* 1983 (ref 32) — velocity/diffusion for 1-D periodic hopping.
- Schnitzer & Block, *CSH Symp. Quant. Biol.* 1995 (ref 15) — randomness parameter as a lower bound on rate-limiting steps.
- Shaevitz, Block & Schnitzer, *Biophys. J.* 2005 (ref 36) — recursive dwell-time-distribution method (single-distribution limitation this paper overcomes).
- Tsygankov, Lindén & Fisher, *Phys. Rev. E* 2007 (ref 39) — conditional dwell times and back-stepping (consistent branching-probability results).
- Rief, Rock, Mehta, Mooseker, Cheney & Spudich, *PNAS* 2000 (ref 20) — myosin-V stepping kinetics / processivity model.
