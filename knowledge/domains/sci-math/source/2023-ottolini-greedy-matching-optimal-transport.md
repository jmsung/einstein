---
type: source
kind: paper
title: Greedy Matching in Optimal Transport with concave cost
authors: Andrea Ottolini, Stefan Steinerberger
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2307.03140v2
source_local: ../raw/2023-ottolini-greedy-matching-optimal-transport.pdf
topic: general-knowledge
cites: 
---

# Greedy Matching in Optimal Transport with concave cost

**Authors:** Andrea Ottolini, Stefan Steinerberger  ·  **Year:** 2023  ·  **Source:** http://arxiv.org/abs/2307.03140v2

## One-line
Proves that a naive nearest-pair greedy algorithm achieves near-optimal cost for optimal transport with concave cost $c(x,y)=d(x,y)^p$ when $0<p<1/2$, in any metric space.

## Key claim
For any two $n$-point sets $X,Y$ in a metric space and $0<p<1$, greedy matching satisfies $\mathrm{Greedy}_p(X,Y) \leq c_p \cdot W_1(X,Y)^p \cdot n^{1-p}$ for $0<p<1/2$ (with $\sqrt{n}\log n$ at $p=1/2$ and $n^p$ for $1/2<p<1$), with constant $c_p \sim 1+2p$ as $p\to 0^+$. The $n^{1-p}$ rate is order-optimal for $p<1/2$.

## Method
The proof combines two ingredients applied inductively over greedy stages: (i) an averaging/pigeonhole bound $c_k \leq W_1(X_k,Y_k)/(n-k+1)$ since the minimum is below the mean of the optimal matching distances, and (ii) a triangle-inequality "swap" argument showing $W_1(X_{k+1},Y_{k+1}) \leq W_1(X_k,Y_k)(1 + 1/(n-k+1))$. Iterating gives $W_1(X_k,Y_k) \leq (n+1)/(n-k+2) \cdot W_1(X,Y)$, and summing $\sum k^{-2p}$ yields the three-regime bound; a referee-suggested metric-power trick ($d^\alpha$ is still a metric) sharpens the random-iid corollary.

## Result
For iid uniform points on $[0,1]^d$ and $0<p<1/2$: $\mathbb{E}\,\mathrm{Greedy}_p \lesssim n^{1-p}$ when $d=1, p<1/4$; $n^{1-p/2}$ when $d=1, 1/4 \leq p < 1/2$ or $d=2$; $n^{1-p/d}$ when $d\geq 3$. Also gives a lower bound $\beta_p(d) \geq \omega_d^{-p/d} \Gamma(1+p/d)$ on the Barthe–Bordenave limit constant, implying $\beta_1(p)=1+O(p)$ as $p\to 0^+$. Proposition 3: as the cost becomes $(\log d)^{2k+1}$ for large $k$, greedy becomes exactly optimal due to scale-separation.

## Why it matters here
General background; no direct arena tie. Closest connections are methodological: the swap-then-triangle-inequality argument is a clean "local-greedy controlled by global-optimum" template that could inspire bounds for combinatorial problems where greedy heuristics are compared to OPT, and the scale-separation argument (Proposition 3) is a reusable trick for problems where cost functions decouple across length scales.

## Open questions / connections
- Identify the phase-transition value $p^* \in (0,1)$ where Dyck matching overtakes greedy matching as the better approximation for iid points on $[0,1]$.
- Prove $\mathbb{E}\,\mathrm{Greedy}_p \leq c_p n^{1-p}$ for $d=1$ and all $p<1/2$ (currently only $p<1/4$); the local-blind nature of greedy makes Caracciolo–D'Achille–Erba–Sportiello–style global techniques inapplicable.
- Extends Gangbo–McCann's qualitative concave-OT picture and complements Dyck matching (Caracciolo et al.) and Goldman–Trevisan limit constants.

## Key terms
optimal transport, concave cost, greedy matching, Wasserstein distance, $W_1$, Dyck matching, McCann non-crossing, Gangbo-McCann, Barthe-Bordenave, Caracciolo, Bobkov-Ledoux, Ajtai-Komlos-Tusnady, Euclidean random assignment, Birkhoff-von Neumann
