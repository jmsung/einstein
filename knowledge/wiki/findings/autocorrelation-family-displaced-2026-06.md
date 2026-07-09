---
type: finding
author: agent
drafted: 2026-06-03
question_origin: leaderboard-audit
status: answered
related_concepts: [autocorrelation-inequality, parameterization-selection, equioscillation, cross-resolution-basin-transfer]
related_problems: [2, 3, 4]
cites: [../problems/2-first-autocorrelation.md, ../problems/3-autocorrelation.md, ../problems/4-third-autocorrelation.md, ../problems/_inventory.md]
---

# Autocorrelation family (P2, P3, P4) displaced from rank #1 — 2026-06-03 snapshot

## Question

Are P2, P3, P4 still "conquered, rank #1" as the inventory (`_inventory.md`, 2026-05-02) claims?

## Answer

**No.** Live leaderboard check (2026-06-03 22:12 UTC, via `scripts/check_submission.py --problem N --once`) shows JSAgent displaced on all three. Our scores have not moved since the inventory snapshot; the field passed us.

| Problem | Direction | JSAgent | Arena #1 | Gap (to beat) | Δ from prior tie-break |
|---|---|---|---|---|---|
| **P2** First Autocorr | min ↓ | **#3** @ 1.5028610916 (also #5 @ 1.5028616284) | OrganonAgent 1.5028609074 (CHRONOS #2 @ 1.5028609074) | **−1.84e-7** | our prior Δ-from-tie was 1.23e-6 → new SOTA improvement (1.8e-7) is ~7× tighter than our previous escape |
| **P3** Second Autocorr | max ↑ | **#3** @ 0.9622135 (tied with alpha_omega) | ClaudeExplorer 0.9626433 (CHRONOS #2 @ 0.9626410) | **+4.30e-4** | our prior Δ-from-tie was 1.5e-4 → SOTA jumped ~3× our last improvement; likely new basin, not polish |
| **P4** Third Autocorr | min ↓ | **#2** @ 1.4525212 (tied with alpha_omega) | OrganonAgent 1.4523043 | **−2.17e-4** | our prior Δ-from-tie was 1.52e-3 → SOTA found a ~7× smaller minimum |

Notable: **OrganonAgent** holds P2 + P4 (the family-twins, both `min(max·)/∫²`); **ClaudeExplorer** holds P3 (the `max(‖²/(‖·‖∞)` variant). Two different agents on twin problems with different optimization direction — suggests two distinct techniques, not one generalist who solved the family.

## Why this matters

1. **The wiki's "Tier S — conquered" claim was correct *at the time of inventory* but is stale by ~1 month.** Without a live leaderboard refresh in cycle-discipline, the wiki tier system rewards historical wins rather than current standing.
2. **These are now Phase 6 (`headroom-target-set`) candidates with real gaps**, not "conquered" S-tier. Specifically: P3 (+4.30e-4) and P4 (−2.17e-4) gaps are *substantially* larger than our prior tie-breaking improvements, which hints the leaders found structurally different solutions, not just polish. P2's gap (1.84e-7) is just above the strict-improve threshold (1e-7) — that one is a polish target.
3. **Our prior wisdom hooks are not refuted.** The wiki claims:
   - P2: peak-locking via exp(v); v² parameterization escapes.
   - P3: cross-resolution downsampling creates distinct basins.
   - P4: larger-n escape breaks piecewise-constant equioscillation traps.
   These remain reusable *frameworks*. What's new is that OrganonAgent + ClaudeExplorer have *also* found their own way past the previous tie-breaks, possibly via the same families of moves or possibly via something we haven't tried.

## What might still work

- **P2 (tight gap, 1.84e-7):** within mpmath-ULP-polish-style range *if* the polish has any degree of freedom past our current parameterization. Worth re-running the v² parameterization with higher β-cascade ceilings and/or larger-n (we last solved at 90k; try 200k+).
- **P3 (large gap, +4.30e-4):** likely needs a new basin, not polish. Re-attempt cross-resolution transplant with substantially higher source resolution (we used 1.6M → 100k; try 4M → 100k or a different downsampling kernel). Also: ClaudeExplorer's 0.9626433 sits ~5e-7 above CHRONOS's 0.9626410 — likely a *different* basin from CHRONOS, suggesting at least 2 distinct rank-1-territory basins exist; we may be in basin #3 or lower.
- **P4 (large gap, −2.17e-4):** mirror of P3's diagnosis. OrganonAgent's gain over our previous tie-break is 7× our last improvement, suggesting different basin or a parameterization we haven't tried. The same `min(max·)/∫²` structure as P2 + same agent as P2 → OrganonAgent likely has one technique that touches both.

## What this rules out

- **"Equioscillation escape via larger-n is the final word"** — no. Both OrganonAgent (P2, P4) and ClaudeExplorer (P3) have moved past our larger-n + parameterization-change basin without the wiki having a model of how. The technique is *necessary but not sufficient* on these problems.
- **The "conquered" tier in `_inventory.md`** — re-running the leaderboard check is now mandatory before trusting any "conquered" claim. Status drifts.

## Cycle-discipline implication

Add a leaderboard-refresh step to `/where` or to inventory regeneration: any problem with `status: conquered` or `status: rank-1-tied` should be re-verified against the live leaderboard before being treated as "no work needed." A stale conquered claim is worse than no claim — it actively suppresses work that would otherwise happen.

See also: [Phase 6 — headroom-target-set](../../../../mb/progress.md), [_active_queue.md](../problems/_active_queue.md), [agent-stance](../../../.claude/rules/agent-stance.md) (honest about lack of information → leaderboard is the ground truth, not the inventory).
