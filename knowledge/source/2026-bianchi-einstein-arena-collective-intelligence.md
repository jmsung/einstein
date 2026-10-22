---
type: source
kind: paper
title: "Harnessing the Collective Intelligence of AI Agents in the Wild for New Discoveries"
authors: Federico Bianchi, Yongchan Kwon, Aneesh Pappu, James Zou
year: 2026
author: agent
drafted: 2026-06-22
ingested_at: 2026-06-22
ingested_by: agent
source_type: arxiv
source_url: https://arxiv.org/abs/2606.10402
source_local: ../raw/2026-bianchi-einstein-arena-collective-intelligence.pdf
source_hash: 3f4b1fbe9f45
topic: agentic-harness
note: "The paper describing EinsteinArena — the platform this repo's agent (JSAgent) competes on. JSAgent is cited [23] and credited in both flagship case studies."
---

# Harnessing the Collective Intelligence of AI Agents in the Wild for New Discoveries

**Bianchi, Kwon (Together AI), Pappu (Stanford), Zou (Together AI / Stanford). arXiv 2606.10402v1, May 2026 (posted 9 Jun 2026).**

> This is the paper that describes **EinsteinArena itself** — the platform this repository's agent
> targets. **JSAgent — this repo's agent — is reference [23]** and is credited by name in both
> case studies. The paper is therefore a primary external record of our own work, not just background.

## Thesis

Scientific discovery is collective: researchers share partial results, inspect failed attempts, and
build on each other over long horizons. Existing AI-discovery systems (AlphaEvolve, Virtual Lab,
TTT-Discover) run in **isolation** — a single orchestrated run produces a privately-evaluated
candidate. EinsteinArena instead makes the **platform** the shared, persistent state, so later agents
inherit promising directions instead of restarting from scratch. Claim: open, decentralized, in-the-wild
agent collaboration can produce new SOTA discoveries that no single isolated agent found.

## Headline results

- **12 new state-of-the-art results** on open math problems since launch (March 19 2026).
- Flagship: **kissing number in dimension 11 lower bound 593 → 604** (the record stood at 582 for ~42
  years; 582→592→593 then arena agents 594→604). One of the largest improvements since Best's 1980
  construction.

## Platform design (§2)

Three core components, all public ("transparency is the central design principle"):
1. **Curated open problems** each with a public **verifier** (executable Python; downloadable so local
   runs are semantically identical to server-side — agents iterate offline, submit only credible gains).
2. **Live leaderboard** — one best solution per agent per problem.
3. **Per-problem discussion board** — agents post findings, failed approaches, questions; Llama-Guard
   moderation. This board *stores the path to the frontier* (the leaderboard stores only the frontier).

Problem spec = NL description + `solutionSchema` (JSON) + `scoring` (min/max) + `verifier` (Python
`dict → float`). Verifiers manually audited and hardened against invalid submissions. High-precision
problems (kissing number) use `decimal.Decimal` at **30–80 significant digits** — the kissing verifier
was upgraded post-launch because double precision was insufficient.

- **Registration**: SHA256 proof-of-work (`SHA256(challenge + n)` with `k` leading zero bits) → Bearer
  token. Humans behind agents are not disclosed (encourages broad participation; ensures leaderboard
  reflects agent capability).
- **Evaluation**: isolated **E2B sandboxes**; results written back, leaderboard updated by acceptance rules.
- **Acceptance**: a submission joins the leaderboard only if it beats the agent's own best; to take the
  **top** spot it must beat the current best by a per-problem **minimum-improvement threshold δ** (chosen
  low enough to encourage iteration, high enough to reject float noise).
- `skill.md` (API/submission instructions) at `einsteinarena.com/skill.md`; platform + analysis code at
  `github.com/vinid/einstein-arena`. Problems curated from AlphaEvolve's repository.

## Table 1 — problems and scores (bold = arena SOTA)

| Problem | Scoring | Prior best (source) | EinsteinArena best |
|---|---|---|---|
| Kissing number (d=11) | max | 593 (AlphaEvolve) | **604** |
| Erdős minimum overlap | min | 0.380876 (TTT-Discover) | **0.380871** |
| 1st autocorrelation inequality | min | 1.5028629 (TTT-Discover) | **1.5028609** |
| 2nd autocorrelation inequality | max | 0.9610 (AlphaEvolve) | **0.9626** |
| 3rd autocorrelation inequality | min | 1.4556 (AlphaEvolve) | **1.4523** |
| Flat polynomials (degree 69) | min | 1.34093 | **1.28093** |
| Max/min distance ratio (n=16) | min | 12.889266 | **12.889230** |
| Prime number theorem | max | 0.92129 | **0.99490** |
| Circles packing in a square (n=26) | max | 2.635983085 | **2.635983095** |
| Circles in rectangle (n=21) | max | 2.365832133 | **2.365832385** |
| Tammes problem (n=50) | max | 0.5134719 | **0.5134721** |
| Edges vs. triangles | max | -0.71249 | **-0.71171** |
| Difference bases | min | 2.63902747 | — |
| Heilbronn for triangles (n=11) | max | 0.03652989 | — |
| Thomson problem (n=282) | min | 37147.29442 | — |

(All prior bests from AlphaEvolve except where noted; SimpleTES later beat Erdős with 0.380868 but only
after the arena had already reached 0.380871.)

## Case Study I — Kissing number K(11), 594 → 604 (§3)

Two stages: build a valid n=594 config (score = total overlap; 0 = valid), then extend n.

- **594 config**: strong initial construction by `alpha_omega_agents` [13]; `alpha_omega_agents` and
  **JSAgent [23]** iterated on it.
- **`KawaiiCorgi`'s linearized surrogate**: observed the leaderboard score was nonlinear; built a
  least-squares surrogate **Σ_{i<j}(cᵢᵀcⱼ − 2)²** and optimized with the **LSQR** algorithm seeded from
  the strong initial construction. Smooth quadratic objective → efficient optimization; loss dropped
  ~10⁻¹⁰ → 10⁻⁵⁰ (mean overlap ≪ 10⁻⁵⁰).
- **Integer-snapping**: after LSQR, most inner products xᵢᵀxⱼ were near simple integers (−2, 0, 1) but
  not exact → a final **integer-snapping** post-processing step made them exact, yielding a provably
  valid (verifier-certifiable) construction. Pattern: find a numerically near-valid config, then convert
  it to an exact discrete structure.
- **594 → 604**: surrogate + integer-snapping pushed n=600 "with relative ease." Analyzing all configs
  for 594 ≤ n ≤ 600 revealed a **shared 496-vector backbone** (highly structured) → exploring extensions
  in a larger algebraic space gave a new n=604 construction (details in the paper's Appendix B).
- **Discussion topic mix (Fig 4)**: structural/lattice decoding 34%, best-score announcements 26%,
  new-basin discovery 10%, generic brainstorming 8%, micro-perturbation refinement 7%, exact-certificate
  discussion 6%, summary/synthesis 5%, old-approach revisit 5%.
- **Solution lineage (Fig 5)**: CHRONOS early refinement → Gradient finds the 0.156-overlap basin (long
  plateau) → `alpha_omega_agents` jumps to a **new basin at 0.0119** (breaks the plateau, not polishes
  it) → CHRONOS/`alpha_omega_agents`/`KawaiiCorgi` preserve the 17,088-pair active-set topology and drive
  the residual to 0.

## Case Study II — 2nd autocorrelation inequality (§4)

Find optimal C in **‖f⋆f‖₂² ≤ C‖f⋆f‖₁‖f⋆f‖∞** over non-negative f (⋆ = autoconvolution); discretized to
step functions over `interval` bins. AlphaEvolve C ≥ 0.9610 → arena **0.9626**.

- **Key method: Dinkelbach optimization** — iteratively maximize ‖f⋆f‖₂² − λ‖f⋆f‖₁‖f⋆f‖∞, updating λ
  each step; multiple agents reported improvements (Fig 3b shows **JSAgent ↔ ClaudeExplorer** discussing
  exactly this). Plus simulated annealing.
- **Lineage (Fig 6)**: initial family = AlphaEvolve (0.961021) + TTT-Discover (0.959180) + Together-AI
  (0.961266) at 5×10⁴ intervals → Together-AI doubles to 10⁵ → OpusMathAgent / CHRONOS / ClaudeExplorer
  refine → **JSAgent achieves the strongest 10⁵-interval solution at 0.962214** → final breakthrough:
  ClaudeExplorer raises resolution to 4×10⁵ → **0.962643**.
- Lesson the paper draws: progress was **collective refinement** (agents identify a method's limits,
  adapt it, combine with complementary ideas), not a single breakthrough.

## Related work & discussion (§5–6)

- Differs from AlphaEvolve / TTT-Discover / Virtual Lab (single run, fixed pipeline, private eval) and
  from fixed-role multi-agent work (homogeneous teams, predefined interaction patterns, small N, single
  session). EinsteinArena: **heterogeneous agents on varied base models, emergent coordination,
  asynchronous over days, verifiable shared artifacts.** Closest: CORAL (shared memory, single run),
  AgentRxiv (shared preprint server), ClawdLab (collaboration beyond exact verifiers).
- **Verification is load-bearing and needs ongoing maintenance** — agents optimize aggressively against
  the scoring function, so verifiers must be public, reproducible, and hardened (kissing → 80-digit
  Decimal).
- **Open tensions**: a public leaderboard may bias agents toward short-horizon score-chasing over slow
  but promising directions; open discussion is useful only if traces are reusable (failed attempts
  without explanation are noise); **competition vs. collaboration** — the kissing result required agents
  to share information that helped competitors. Transfer to non-exact-verifier domains (formal proof,
  algorithm design, comp-bio) is untested.

## Why this matters to this repo

1. **External validation that JSAgent contributes** — credited in both flagship case studies (kissing
   594-iteration; 2nd-autocorr best 10⁵ at 0.962214). Our own P3 page already records the 0.962214
   cross-resolution result the paper attributes to JSAgent.
2. **Methods named in the paper that our wiki already holds**: Dinkelbach
   ([dinkelbach-fractional-programming](../wiki/techniques/dinkelbach-fractional-programming.md)),
   cross-resolution basin transfer ([cross-resolution-basin-transfer](../wiki/techniques/cross-resolution-basin-transfer.md)),
   parallel-tempering SA, micro-perturbation refinement.
3. **A method our wiki may NOT hold**: KawaiiCorgi's linearized surrogate Σ(cᵢᵀcⱼ−2)² + LSQR +
   **integer-snapping** for kissing — "find numerically near-valid, then snap to an exact discrete
   certificate."
4. **Discrepancy worth resolving**: our P6 page treats kissing-d11 as fixed n=594, score 0 = "terminal,
   unbeatable." The paper frames it as **maximize n**, with the record now **604**. Either the arena
   reformulated the problem or our page is stale. See the question filed alongside this ingest.
