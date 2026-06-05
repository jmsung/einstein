---
type: finding
author: agent
drafted: 2026-06-04
question_origin: problem-3
status: answered
answer_question: ../questions/2026-06-04-p3-arena-resolution-cap-2M.md
related_concepts: [autocorrelation-inequality, cross-resolution-basin-transfer, triple-verify]
related_problems: [3]
supersedes: dead-end-p3-resolution-inflation.md
cites:
  - ../questions/2026-06-04-p3-arena-resolution-cap-2M.md
  - src/einstein/triple_verify/resolution_guard.py
  - scripts/autocorrelation/recon_p3_sota.py
  - scripts/autocorrelation/resolution_scaling_p3.py
  - mb/problems/3-autocorrelation/solutions/sota_recon.json
---

# P3: the arena scores at the submitted resolution (up to 2,000,000) — resolution IS the lever

## The correction
The earlier finding `dead-end-p3-resolution-inflation.md` concluded that promoting
a high-resolution P3 solution is a dead end because "the arena downsamples to 100k."
**That inference was wrong.** The P3 problem page states the discretization length
is *"your choice, up to 2,000,000"*, and the live leaderboard proves the arena
scores at the submitted length:

| rank | agent | board score | n (submitted) | C2 recomputed @ n |
|---|---|---|---|---|
| #1 | ClaudeExplorer | 0.9626433188 | **400000** | 0.962643318763 |
| #2 | CHRONOS | 0.9626409542 | 400000 | 0.962640954225 |
| #3 | JSAgent (us) | 0.9622135366 | **100000** | 0.962213536592 |

The #1 array recomputes (via the exact `oaconvolve` verifier) to its board score
to ~1e-10. The arena did **not** downsample it to 100k. Our board score sat at
0.9622 only because **we submitted a 100k array** — never the high-res one. The
prior finding mistook "we submitted low-res" for "the arena downsamples."

## Evidence
- `recon_p3_sota.py`: downloads the live top-8, recomputes C2 at each array's own
  length. #1/#2 are n=400000; their recompute matches the board exactly.
- `resolution_scaling_p3.py` (exact `oaconvolve`): C2 climbs with **native**
  resolution across basins — 100k≈0.9620, 400k(leader)=0.96264, 1.6M(ours)=0.96272.
- Our 1.6M-native array scores **0.9627190**, triple-verified 3-way (fast /
  fftconvolve / mpmath dps=30) to a spread of ~6e-15. That already **beats arena
  #1 (0.9626433) by +7.57e-5.**

## The obstruction that remains (why this isn't a free win)
1. **PAYLOAD CAP ~4.5MB — the binding constraint.** Despite the page saying "up
   to 2,000,000", the arena POST is a Vercel function with a ~4.5MB body limit
   (`FUNCTION_PAYLOAD_TOO_LARGE`). Measured: 700k zeros (3.5MB) accepted, 1M zeros
   (5MB) → 413. Our 1.6M dense array is 36MB → **permanently unsubmittable**; even
   the zeros at n=1.6M alone exceed the cap. **This is why the leaders stopped at
   400k.** ClaudeExplorer fits 400k only by being **74% zeros** (sparse, 2.7MB).
   So the prior `dead-end-p3-resolution-inflation` had the right *conclusion* (the
   1.6M can't be submitted) for the *wrong reason* (payload cap, not downsampling).
2. **You cannot win by re/up-sampling.** Linear-interpolating the leader's 400k to
   2M *lowers* C2 (0.9623); Fourier-resample destroys it (0.83). Our 1.6M
   up-sampled to 2M collapses to 0.88; *down-sampled* to a submittable 400-700k it
   craters to 0.77-0.92. These optima are resolution-brittle — a higher-n record
   requires **native** optimization at the submittable n.
3. **The real frontier:** maximize C2 s.t. compact-JSON < 4.5MB. This rewards
   **sparse + high-n**: a sparse solution carries more points (more resolution →
   higher C2) under the byte budget. The leaders sit at 400k; sparsity allows
   ~550-700k submittable — the one unexploited lever. The board ranks by raw score
   (CHRONOS sits 2.4e-6 below #1, both listed), so any verified submittable C2 >
   0.9626433 takes #1. The arena `minImprovement`=1e-4 appears NOT to be a
   cross-agent acceptance gate (else CHRONOS couldn't sit 2.4e-6 from #1).

## What this rules in / out
- **RULES IN:** native optimization at the *submittable* resolution (n≈550-700k,
  sparse, under the 4.5MB cap) as the live record lever. The leaders stopped at
  400k; the sparsity-enabled headroom to ~700k is the one unexploited dimension.
- **RULES OUT:** (a) submitting the 1.6M solution — payload cap, permanently;
  (b) up/down-sampling an existing optimum to a submittable n — resolution-brittle;
  (c) the claim that high-res scores are "artifacts" — they are real at the
  submitted length, just unsubmittable above ~700k.
- **Honest EV:** this is a hard optimization, not a sure win. The leaders are
  strong at the 400k frontier; the bet is that native sparse ~700k buys enough
  resolution to clear 0.9626433. Outcome uncertain; campaign running
  (`scripts/autocorrelation/submittable_frontier.py`).

## Code corrected
- `resolution_guard.ARENA_RESOLUTION_CAP`: 100_000 → 2_000_000 (+ regression test).
- This finding supersedes the conclusion of `dead-end-p3-resolution-inflation.md`
  (which remains as the record of the mis-inference — its "what might still work"
  section pointed the wrong way).
