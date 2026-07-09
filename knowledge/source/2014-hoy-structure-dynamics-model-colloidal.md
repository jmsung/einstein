---
type: source
kind: paper
title: Structure and dynamics of model colloidal clusters with short-range attractions.
authors: R. Hoy
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1407.3889
source_local: ../raw/2014-hoy-structure-dynamics-model-colloidal.pdf
topic: general-knowledge
cites:
---

# Structure and dynamics of model colloidal clusters with short-range attractions.

**Authors:** R. Hoy  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1407.3889

## One-line
Exact enumeration of mechanically stable sticky-hard-sphere packings up to $N=13$ combined with MD simulations of short-range Morse clusters, characterizing equilibrium and quench-rate-dependent structure plus relaxation dynamics.

## Key claim
For $N=13$, only $\sim 1\%$ of isostatic ($N_c = 3N-6 = 33$) mechanically stable packings have Barlow (close-packed) order; the remaining $\sim 99\%$ are "off-pathway" nuclei with stacking faults or fivefold-symmetric defects, and this off-pathway fraction grows rapidly with $N$. Total macrostate counts: $M(13,33) = 95799$, $M(13,34) = 1318$, $M(13,35) = 96$, $M(13,36) = 8$ (the eight degenerate ground states).

## Method
Exact enumeration of nonisomorphic adjacency matrices using NAUTY (extending Arkus–Manoharan–Brenner and Hoy–Harwayne-Gidansky procedures) to find all mechanically stable sticky-hard-sphere packings for $N \le 13$ at each contact number $N_c$. Macrostates are classified by structural motif (Barlow / stack-fault / fivefold). Molecular dynamics with a modified Morse potential ($\alpha D = 150$, cutoff $r_c/D = 31/30$) seeded from "ideally prepared ensembles" weighted by permutational entropies $\omega_k$, with thermal quenches at three rates and a Langevin thermostat.

## Result
Enumerated $M(N,N_c)$ and counts of Barlow / stack-fault / fivefold macrostates for $N \le 13$, $0 \le H = N_c - N_{\rm ISO} \le 3$. The eight $N=13$ ground states ($N_c = 36$) include one FCC and one HCP core-shell cluster plus six irregular Barlow/stack-faulted structures. Slow quenches ($|\dot T| = 10^{-5}/\tau$) over-populate FCC/HCP states (deeper, narrower wells); fast quenches favor higher-vibrational-entropy disordered states. Equilibrium relaxation $f_{\rm mad}(t)$ becomes strongly non-exponential at low $T$, reflecting glassy dynamics and macrostate-dependent escape rates (states with three-bonded "loose" atoms rearrange fastest).

## Why it matters here
General background; no direct arena tie. Most relevant as an enumeration-of-discrete-geometry reference: counts of mechanically stable sphere-contact graphs at small $N$, and the structural-motif classification (Barlow / stack-fault / fivefold) that distinguishes on- vs off-pathway nuclei — adjacent to sphere-packing and discrete-geometry problems but at finite cluster sizes rather than asymptotic packing density.

## Open questions / connections
- Extends Arkus–Manoharan–Brenner (2009, 2011) and Hoy–Harwayne-Gidansky–O'Hern (2012) enumerations from $N \le 11$ to $N = 13$; cross-validates with Holmes-Cerfon (2014, arXiv:1407.3285).
- Glassy non-exponential relaxation at low $T$ in $N=13$ Morse clusters — deferred to follow-up work; relation to bulk dynamical arrest in sticky-sphere systems.
- Noro–Frenkel mapping ($B_2^*$, $\sigma_{\rm eff}$) to translate results across pair potentials; ranges of $N$, $c_p$, $B_2^*$ for comparison with experiments left open.
- Energy barriers between off-pathway and Barlow nuclei — quantified elsewhere (Holmes-Cerfon–Gortler–Brenner 2013) but not here.

## Key terms
sticky hard spheres, Morse potential, mechanically stable packings, isostatic, hyperstatic, Barlow packings, stacking faults, fivefold symmetry, exact enumeration, adjacency matrix, NAUTY, ground-state clusters, permutational entropy, Noro-Frenkel, colloidal clusters, glassy dynamics, Manoharan, Holmes-Cerfon, Arkus-Brenner
