---
type: source
kind: paper
title: "Global Lyapunov functions: a long-standing open problem in mathematics, with symbolic transformers"
authors: Alberto Alfarano, Franccois Charton, Amaury Hayat
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2410.08304
source_local: ../raw/2024-alfarano-global-lyapunov-functions-long-standing.pdf
topic: general-knowledge
cites:
---

# Global Lyapunov functions: a long-standing open problem in mathematics, with symbolic transformers

**Authors:** Alberto Alfarano, Franccois Charton, Amaury Hayat  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2410.08304

## One-line
Sequence-to-sequence transformers trained on synthetic data discover global Lyapunov functions for dynamical systems, beating SOS solvers and finding new Lyapunov functions for polynomial and non-polynomial systems where no algorithm was previously known.

## Key claim
Backward-trained transformers (with a tiny 300-example forward "enrichment") reach 84–99% on held-out tests and 73–84% out-of-distribution; on random polynomial systems they find global Lyapunov functions for **10.1%** of cases vs **2.1%** for SOSTOOLS, and on non-polynomial systems (no prior algorithm) they discover Lyapunov functions for **12.7%** of cases.

## Method
**Backward data generation**: sample a random positive definite $V$ (with $V(0)=0$, $V\to\infty$), then construct $f$ as $f = -h_i^2(x)(\nabla V)_i + \sum g_i(x) e_i(x)$ where $e_i \perp \nabla V$, guaranteeing $\nabla V \cdot f \le 0$. The $e_i$ are chosen with a skew-symmetric trick ($e_i^{\tau_1(i)} = A_{\tau_2(i)}$, $e_i^{\tau_2(i)} = -A_{\tau_1(i)}$) to avoid leaking $\|\nabla V\|$ into $f$. Sympy simplification at the end obscures the generative shortcut. A small "forward mixture" of SOSTOOLS-solved systems is added (0.03% of training) to lift OOD accuracy. Verification uses both SOS (SumOfSquares/CVXOPT) and SMT (dReal interval analysis).

## Result
- In-domain: BPoly 100%, BNonPoly 87%, FBarr 98%, FLyap 88% (beam=50).
- OOD: BNonPoly→FLyap 75%; mixing 300 FBarr examples into BPoly raises FBarr accuracy 35→89% and FLyap 73→83%.
- Discovers $V(x) = \ln(1+5x_0^2) + x_1^2$ for Ahmadi et al.'s system (known to have no polynomial Lyapunov function), and non-diagonal/high-degree polynomial Lyapunov functions where findlyap times out at 4h. Beats Fossil 2, ANLC v2, LyzNet baselines (these find only local/semi-global Lyapunov functions via NN+SMT).

## Why it matters here
General background for the agent — not a direct arena problem solver, but a concrete demonstration of **backward generation** (sample solution → construct problem) as a transformer-training pattern that achieves OOD generalization with a tiny forward mixture. Could inform agent strategy for problems where a *verifier* is cheap but a *solver* is unknown (autocorrelation extremals, Sidon constructions, parameterized inequality discovery). The orthogonal-decomposition trick ($f = $ collinear + orthogonal to $\nabla V$) is a transferable design idea for generative dataset construction.

## Open questions / connections
- Does backward generation + tiny forward mixture extend to optimization problems on Einstein Arena where verifiers are cheap (SOS, LP duality checks)?
- The "multigen" finding — 5 systems per $V$ helps, 100 hurts — suggests a structural insight about transformer learning of "hidden invariants" worth probing for other invariant-discovery problems.
- Forward models trained on small SOS-solver datasets fail OOD (10–15%) — confirms a known failure mode of pure forward generation on hard math.
- Extends Lample & Charton (2019) symbolic-math transformer line; complements Romera-Paredes et al. (FunSearch), Wagner (RL for graph constructions) as a third pattern: backward-generated supervised training.

## Key terms
Lyapunov function, global asymptotic stability, sum-of-squares (SOS), SOSTOOLS, semidefinite programming, dynamical systems, backward generation, sequence-to-sequence transformer, symbolic regression, SMT solver, dReal, barrier function, LaSalle invariance principle, Ahmadi-Krstic-Parrilo, synthetic training data
