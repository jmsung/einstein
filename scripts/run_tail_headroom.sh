#!/usr/bin/env bash
# §6.5 follow-up batch — the two experiments the paper's "what would settle it" promises.
# Serial (single credential), RESUMABLE (both write records.jsonl incrementally + skip done),
# disconnect-safe (fair-attempt guard drops offline/rate-limit cells for retry), and kept
# AWAKE for the whole run via caffeinate so sleep can't pause it.
#
#   1. Test 1 — memory TAIL (haiku, Heilbronn n13/n14/n15 x S20, cold vs warm):
#      does memory fatten the UPPER tail (p90/max/near-solve) even if the mean is flat?
#      ~120 cells @ 400s  -> up to ~13h (less in practice; many Haiku cells finish early).
#   2. Test 3 — HEADROOM transfer (sonnet, Heilbronn->equal_circles 60/80 x S4, true optima):
#      at harder n a capable model no longer solves cold, so warm-cold transfer is measurable.
#      KB_A build + 16 cells @ 600s -> ~4-6h.
#
# Total ~17-18h if run continuously; either step resumes if interrupted (re-run this script).
# $ cost ~ $0 (Claude-Code login); the real cost is wall-clock. Do NOT run while using Claude
# Code interactively in another window (same credential contends).
set -u
cd "$(dirname "$0")/.." || exit 1

# Keep the machine awake for the lifetime of THIS script (PID $$); caffeinate exits when we do.
caffeinate -ims -w $$ &

OUT=results/tail-headroom
mkdir -p "$OUT"
MASTER="$OUT/master.log"
ts() { date +"%Y-%m-%d %H:%M:%S"; }
log() { echo "[$(ts)] $*" | tee -a "$MASTER"; }

run_step() {
  local name="$1"; shift
  log "===== START $name ====="; log "cmd: $*"
  local t0; t0=$(date +%s)
  "$@" >"$OUT/$name.log" 2>&1
  local rc=$?
  log "===== END $name (exit $rc, $(( ($(date +%s) - t0) / 60 )) min) ====="
  return $rc
}

log "TAIL+HEADROOM BATCH START (caffeinated, serial, single credential)"

run_step memory-tail \
  uv run python -u scripts/run_memory_tail.py \
    --problem-ids heil-n13,heil-n14,heil-n15 --seeds "$(seq -s, 1 20)" \
    --model haiku --solve-timeout 400 --results-dir results/memory-tail \
  || log "memory-tail step FAILED (continuing)"

run_step headroom-transfer \
  uv run python -u scripts/run_transfer_ablation.py \
    --config config/ablation_transfer_xhard.yaml \
    --family-a heilbronn_triangle --family-b equal_circles_in_unit_square \
    --model sonnet --seeds 1,2,3,4 --timeout 600 \
    --results-dir results/transfer-xhard \
  || log "headroom-transfer step FAILED (continuing)"

log "TAIL+HEADROOM BATCH COMPLETE"
date +"%Y-%m-%d %H:%M:%S" > "$OUT/DONE"
