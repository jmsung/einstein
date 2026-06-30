#!/usr/bin/env bash
# Overnight Tier-1+2 ablation closure — runs the three directional experiments
# SERIALLY (single Claude credential; concurrent runs contend for the rate limit).
#
#   1. #1 council confirmatory   (haiku, heil-n13/n14 x S4, equal solve-budget)
#   2. #8 prompt-tone (system)   (haiku, heil-n13/n14 x S4, neutral vs encouraging)
#   3. v3 near-transfer          (sonnet, Heilbronn->equal_circles 28/34 x S4, true refs)
#
# Each step: unbuffered (`python -u`), own results dir + log, continue-on-failure
# (one failure must not block the others), timestamped. Council + tone are RESUMABLE
# (records.jsonl). A final sentinel `results/overnight-closure/DONE` marks completion.
#
# $ cost ~ $0 (Claude-Code login billing); the real cost is wall-clock (~8-10 h).
set -u

cd "$(dirname "$0")/.." || exit 1
OUT=results/overnight-closure
mkdir -p "$OUT"
MASTER="$OUT/master.log"

ts() { date +"%Y-%m-%d %H:%M:%S"; }
log() { echo "[$(ts)] $*" | tee -a "$MASTER"; }

run_step() {
  local name="$1"; shift
  log "===== START $name ====="
  log "cmd: $*"
  local t0; t0=$(date +%s)
  "$@" >"$OUT/$name.log" 2>&1
  local rc=$?
  local t1; t1=$(date +%s)
  log "===== END $name (exit $rc, $(( (t1 - t0) / 60 )) min) ====="
  return $rc
}

log "OVERNIGHT CLOSURE START (serial, single credential)"

run_step council \
  uv run python -u scripts/run_council_confirmatory.py \
    --problem-ids heil-n13,heil-n14 --seeds 1,2,3,4 --model haiku \
    --solve-timeout 600 --results-dir results/council-confirmatory \
  || log "council step FAILED (continuing)"

run_step tone \
  uv run python -u scripts/run_tone_ablation.py \
    --problem-ids heil-n13,heil-n14 --seeds 1,2,3,4 --model haiku \
    --solve-timeout 600 --results-dir results/tone \
  || log "tone step FAILED (continuing)"

run_step near \
  uv run python -u scripts/run_transfer_ablation.py \
    --config config/ablation_transfer_near.yaml \
    --family-a heilbronn_triangle --family-b equal_circles_in_unit_square \
    --model sonnet --seeds 1,2,3,4 --timeout 600 \
    --results-dir results/transfer-near \
  || log "near step FAILED (continuing)"

log "OVERNIGHT CLOSURE COMPLETE"
date +"%Y-%m-%d %H:%M:%S" > "$OUT/DONE"
