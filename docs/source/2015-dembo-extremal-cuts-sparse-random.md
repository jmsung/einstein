---
type: source
kind: paper
title: Extremal Cuts of Sparse Random Graphs
authors: A. Dembo, Andrea Montanari, Subhabrata Sen
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1503.03923
source_local: ../raw/2015-dembo-extremal-cuts-sparse-random.pdf
topic: general-knowledge
cites:
---

# Extremal Cuts of Sparse Random Graphs

**Authors:** A. Dembo, Andrea Montanari, Subhabrata Sen  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1503.03923

## One-line
Sharp $\sqrt{\gamma}$-order asymptotics for Max-Cut, max-bisection, and min-bisection on sparse Erdős–Rényi and random $\gamma$-regular graphs, expressed via the Parisi ground-state energy $P_* \approx 0.7632$ of the Sherrington–Kirkpatrick spin glass.

## Key claim
For both $G(n,\lceil \gamma n\rceil)$ and $G_{\text{Reg}}(n,\gamma)$, w.h.p. as $n\to\infty$: $\text{MCUT}/n = \gamma/4 + P_*\sqrt{\gamma/4} + o_\gamma(\sqrt{\gamma})$, $\text{mcut}/n = \gamma/4 - P_*\sqrt{\gamma/4} + o_\gamma(\sqrt{\gamma})$, and $\text{MaxCut}/n$ matches MCUT to first order — confirming the physics conjecture that max-bisection and Max-Cut coincide up to $o(n)$.

## Method
Guerra–Toninelli interpolation from spin-glass theory: replace the sparse graph Hamiltonian $H_G(\sigma)=-\sum_{(i,j)\in E}\sigma_i\sigma_j$ by a complete graph with Gaussian weights $J_{ij}/\sqrt{n}$, showing the swap costs only $n\cdot o_\gamma(\sqrt{\gamma})$ in expectation by exploiting Poisson↔Gaussian moment matching. Then drop the zero-magnetization (balanced-partition) constraint at $o_\gamma(\sqrt{\gamma})$ cost, reducing to the SK ground state, which Talagrand's proof of the Parisi formula evaluates as $P_*$. Extension to regular graphs uses a delicate "embedding" of a slightly-sparser Erdős–Rényi graph into a $\gamma$-regular one via two-stage half-edge pairing + Azuma–Hoeffding.

## Result
$P_* = \inf_{x\in D_\beta} P_\beta[x]$ via the Parisi functional (PDE in (1.4)), with $P_* = 0.76321 \pm 0.00003$ (Crisanti–Rizzo) and Guerra's RS upper bound $P_* \le \sqrt{2/\pi} \approx 0.7979$. As application: the natural min-bisection test $T_{\text{cut}}$ for stochastic block model community detection succeeds when $(a-b)^2 \ge 8P_*^2(a+b)+o(a+b)$, suboptimal vs the Kesten–Stigum threshold $(a-b)^2 > 2(a+b)$ by a factor $4P_*^2 \approx 2.33$.

## Why it matters here
General background for extremal graph theory and spin-glass-style optimization landscapes; no direct Einstein Arena problem ties, but the $P_* = 0.7632$ constant and Parisi-formula framework are the canonical example of a non-trivial ground-state energy obtained via replica-symmetry-breaking — a stance worth knowing when an arena problem's landscape exhibits a hierarchy of metastable basins (parallel-tempering territory).

## Open questions / connections
- Exact value (not just leading $\sqrt{\gamma}$ coefficient) of the $o_\gamma(\sqrt{\gamma})$ correction terms — currently unresolved.
- Extends Guerra–Toninelli interpolation [GT02,GT04] and Franz–Leone diluted-spin bounds [FL03] from bounds to sharp asymptotics; whether the same Poisson↔Gaussian interpolation handles other diluted CSPs (random k-SAT, NAE-SAT, coloring) at this precision.
- Algorithmic gap: $T_{\text{cut}}$ is information-theoretic, not polynomial — closing the $4P_*^2$ factor with an efficient test remains open.

## Key terms
Parisi formula, Sherrington-Kirkpatrick model, spin glass ground state, Guerra-Toninelli interpolation, Max-Cut, min bisection, max bisection, Erdős-Rényi random graph, random regular graph, anti-ferromagnetic Ising, replica symmetry breaking, stochastic block model, Talagrand, $P_* \approx 0.7632$, diluted mean-field
