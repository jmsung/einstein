---
type: source
kind: paper
title: Unified Functional Hashing in Automatic Machine Learning
authors: Ryan Gillard, S. Jonany, Yingjie Miao, M. Munn, Connal de Souza, Jonathan Dungay, Chen Liang, David R. So, Quoc V. Le, Esteban Real
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2302.05433
source_local: ../raw/2023-gillard-unified-functional-hashing-automatic.pdf
topic: general-knowledge
cites:
---

# Unified Functional Hashing in Automatic Machine Learning

**Authors:** Ryan Gillard, S. Jonany, Yingjie Miao, M. Munn, Connal de Souza, Jonathan Dungay, Chen Liang, David R. So, Quoc V. Le, Esteban Real  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2302.05433

## One-line
Speeds up evolutionary AutoML by hashing candidates on their input-output behavior so functionally-equivalent duplicates can be cached instead of re-evaluated.

## Key claim
A single representation-agnostic "unified functional hash" (UFH), computed from a tiny canonical input batch, detects functional equivalence across compute graphs, code, and lambdas; plugged into regularized evolution as a Functional Equivalence Cache (FEC), it yields 2x–10x search-time savings across MNAS, AutoML-Zero, AutoRL, and NAS-Bench-101 without degrading final quality, with cache hit fractions consistently above $0.5$.

## Method
Run the candidate's normal forward/backward pass on a fixed canonical mini-batch ($N_E \approx 10$ examples, $N_S \approx 3$ seeded reps), with all RNGs reset to a fixed seed; harvest floating-point "hashable outputs" (e.g. logits), truncate mantissas to $m_{\text{bits}}$, and mix sign/exponent/mantissa into one integer via a hash-mixing primitive. The hash keys three techniques: FEC (cache fitness by hash), FCM (re-mutate child until its hash differs from parent), and tabulist (deny re-entry of over-explored hashes). Variants discussed: forgetful FEC (drop key with probability $F=0.1$ on hit) and aggregating FEC (running mean over up to $M$ evals per hash to combat noise).

## Result
FEC improves outcomes across all four setups; FCM and tabulist are neutral-to-positive. Cache-hit fraction $>0.5$ everywhere (evolution proposes equivalent candidates very often). Collision study on NAS-Bench-101: $m_{\text{bits}}=1$ yields ~1291 models/hash, $m_{\text{bits}}=5$ yields ~3.9, $m_{\text{bits}}\geq 7$ yields ~1; quality only degrades at very coarse precision, and forgetful cache recovers most of the loss. Cost scaling: FEC beats baseline whenever $N_E N_S \ll h \cdot N_T$ (cache hit rate $h$, training steps $N_T$), which is generically true.

## Why it matters here
General background; no direct arena tie — the paper is about ML search infrastructure, not math optimization. The transferable idea for the autonomous loop: **functional fingerprinting via a few canonical inputs + RNG reset + mantissa truncation** could deduplicate "structurally different but functionally identical" optimizer configurations, mutated solution candidates, or wiki-generated code variants in the agent's self-improvement cycle.

## Open questions / connections
- Could a UFH-style fingerprint detect when basin-hopping / parallel-tempering restarts are actually exploring the same basin (functional duplicates of the same local optimum)?
- Forgetful and aggregating FEC variants are sketched but not fully characterized — when does noisy fitness ($\sigma$ vs gap to next basin) make FEA preferable to FEC?
- Relates to evolutionary search literature [36] (modified clearing / FCM), Glover's tabu search [17,18], and predictor-based NAS [44]; orthogonal to GNN predictors so combinable.
- Hash-collision rate vs $(m_{\text{bits}}, N_E, N_S)$ has only empirical guidance — no theoretical false-positive bound given.

## Key terms
unified functional hashing, UFH, functional equivalence cache, FEC, FCM, tabulist, regularized evolution, neural architecture search, AutoML-Zero, NAS-Bench-101, MNAS, AutoRL, hash collision, mantissa truncation, canonical inputs, evolutionary computation, deduplication, Real
