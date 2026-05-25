---
type: source
kind: paper
title: Building a Framework for Predictive Science
authors: M. McKerns, Leif Strand, Tim Sullivan, A. Fang, M. Aivazis
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1202.1056
source_local: ../raw/2012-mckerns-building-framework-predictive-science.pdf
topic: general-knowledge
cites:
---

# Building a Framework for Predictive Science

**Authors:** M. McKerns, Leif Strand, Tim Sullivan, A. Fang, M. Aivazis  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1202.1056

## One-line
Presents `mystic` (optimization) and `pathos` (heterogeneous compute) — Python frameworks for massively-parallel global optimization wrapped around an Optimal Uncertainty Quantification (OUQ) formulation that turns UQ into constrained global optimization over probability measures.

## Key claim
Rigorous UQ — including McDiarmid concentration-of-measure bounds and the more general OUQ extremal-probability problem — can be cast as a finite-dimensional global optimization once reduction theorems collapse the feasible measure set $\mathcal{A}$ to a subset $\mathcal{A}_\Delta$ of product measures, each marginal $\mu_i$ supported on at most $1+n_i+n$ points (Dirac convex combinations). For information consisting of subdiameters $\mathrm{osc}_i(G,E)\le D_i$ and $\mathbb{E}[G]\le 0$, $U(\mathcal{A}_{MD})\le \exp(-2a^2/\sum D_i^2)$ recovers McDiarmid as a corollary of the OUQ supremum.

## Method
Decomposes optimizers into solver / termination-condition / monitor / constraints / map components so any solver (Nelder–Mead, Powell, Differential Evolution) can be parallelized by injecting a `Map` (MPI, SSH, multiprocessing). Constraints are handled set-based ($\phi(x)=f(c(x))$) rather than penalty-based ($\phi=f+kp$), decoupling constraint-solving (itself an optimization, via a SymPy parser) from cost evaluation. Adds nested-solver patterns (`BuckshotSolver`, `LatticeSolver`) that launch $N$ local optimizers in parallel from scattered/lattice starts, and casts subdiameter $\mathrm{osc}_i(f,E)=\sup\{|f(y)-f(x)|: x_j=y_j, j\ne i\}$ and PoF $\mu[H\le 0]$ as cost metrics over `product_measure` objects.

## Result
A working software stack: `mystic` (solvers + constraints + measure toolkit), `pathos` (SSH/MPI/IPC launchers, `sshTunnel`, `dill` for session/object serialization, `pox` for filesystem, `pyina` for MPI map-reduce). Demonstrates set-based constraint decoupling on problems with $K\approx 200$ constraints, OUQ reductions for PoF bounds with mean-and-subdiameter information, and nested parallel optimizers for diameter and OUQ computations (carddealer/pool strategies, lattice/buckshot multistart).

## Why it matters here
General background; no direct arena tie — but informs the agent's **compute-router** and **multistart-as-parallel-global** patterns: nested `BuckshotSolver` / `LatticeSolver` parallel-multistart is essentially what this repo does for P11/P15/P16-style multistart polish, and the set-based constraint-decoupling pattern ($x=c(x)$ projection before unconstrained step) is directly applicable to highly-constrained packing problems where penalty methods struggle.

## Open questions / connections
- Can the OUQ measure-reduction (marginals as 2-Dirac convex combinations) be repurposed to bound arena verifier-vs-local-evaluator drift as an extremal-measure problem over input-perturbation distributions?
- The "launch $N$ optimizers in parallel + dynamic constraints to avoid revisiting the same minimum" future-work item is exactly the basin-avoidance pattern relevant to P11 (Hardin–Sloane multistart) and P1 (three-way local optima).
- Connects to concentration-of-measure literature [LED01, BBL04, MCD89] and to the OUQ reduction theorems in Owhadi–Scovel–Sullivan–McKerns–Ortiz (arXiv 1009.0679).

## Key terms
mystic, pathos, optimal uncertainty quantification, OUQ, McDiarmid inequality, concentration of measure, subdiameter, product measure, Dirac measure reduction, parallel global optimization, BuckshotSolver, LatticeSolver, Differential Evolution, set-based constraints, nested optimizer, multistart, probability of failure, Owhadi, Sullivan, McKerns
