# Ablation raw data — Cold-vs-Warm knowledge-compounding (claim #4)

Raw per-cell results behind the compounding ablation verdict, preserved for reproducibility
and the JSAgent paper (the live `results/` dirs are gitignored). Numbers + analysis live in
[`../results-compounding-evidence.md`](../results-compounding-evidence.md); pre-reg in
[`../2026-06-26-heilbronn-haiku-compounding-preregistration.md`](../2026-06-26-heilbronn-haiku-compounding-preregistration.md).

## Files

| File | What |
|---|---|
| `heilbronn-clean-runs.jsonl` | **FINAL** — S=18, 216 cells, **per-cell isolated cwds** (contamination-free). The headline data. |
| `heilbronn-clean-telemetry.jsonl` | per-cell cost/error/wall for the clean run (efficiency DV: timeout rate, wall-clock). |
| `heilbronn-clean-SUMMARY.md` | per-problem cold/warm gap% table for the clean run. |
| `heilbronn-contaminated-runs.jsonl` | Stage C, S=18 — **SUPERSEDED** (confounded by a cross-cell filesystem channel before the cwd-isolation fix). Kept for the clean-vs-contaminated comparison. |
| `heilbronn-contaminated-SUMMARY.md` | per-problem table for the contaminated run. |

## Verdict (clean, contamination-free)

- **Capability (H1): NOT supported** — mean Δ(warm−cold) gap_closed = **+3.6 pts**, 95% CI **[−0.7, +7.9]** (warm wins 5/6).
- **Compounding (H2): null** — within-problem Δ-vs-banked slope ≈ 0.
- **Efficiency (D): SUPPORTED** — cold times out **26%** vs warm **9%** (~3×); mean wall 344s vs 255s.
- Clean ≈ contaminated (+3.6 vs +2.9) → the filesystem channel was **not** masking a Warm advantage; the null is real. Headline: *memory buys efficiency, not capability.*

## `runs.jsonl` schema (one JSON object per cell)

`problem_id, arm (cold|warm), seed, sequence_index, score_coldinit, score_final, score_optimum_ref,`
`gap_closed, cycles, wall_clock_s, trajectory, lessons_written, lessons_read, dead_ends_avoided,`
`kb_state_hash_before, kb_state_hash_after` (+ `replicates, gap_closed_std, gap_closed_reps` when k-replicate is used).

## Provenance

Produced by `scripts/run_ablation.py` (model `claude-haiku-4-5`, timeout 600s, max-lesson-chars 4000,
seeds 0–17). Re-analyze: `scripts/analyze_ablation.py <runs.jsonl>`. Transcripts (large, per-cell agent
stdout) were not archived here — they live in the gitignored run dir.
