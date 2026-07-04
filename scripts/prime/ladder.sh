#!/usr/bin/env bash
# P7 N-extension ladder — climb maxkey rungs toward the compute limit.
# Each rung: colgen (box-aware) from the previous rung's base, price sf<=N, select
# <=1999 keys, solve, save colgen_base_<N>.json to seed the next rung.
# Stop when a rung's base gain < GAIN_FLOOR (cardinality cap binding / law flattening).
# Empirical law: gap(base) ~ 0.036/ln(maxkey) — predicted rungs: 48k 0.99662,
# 64k 0.99675, 96k 0.99687, 128k 0.99694.
set -u
cd "$(dirname "$0")/../.." || exit 1
caffeinate -ims -w $$ &

RUNGS=(48000 64000 96000 128000 192000 256000 384000 512000 768000 1000000)
GAIN_FLOOR=0.000002        # 2e-6: below this a rung is not worth the next doubling
SEED_FILE="$1"             # starting base pf (unscaled), e.g. rescale-safe base or 32k winner
TIME_LIMIT="${2:-3600}"
OUT=results/problem-7-prime
LOG="$OUT/ladder.log"
ts() { date +"%H:%M:%S"; }
echo "[$(ts)] LADDER START seed=$SEED_FILE" | tee -a "$LOG"

prev_base=$(uv run python -c "
import json,sys; sys.path.insert(0,'src')
from einstein.prime.evaluator import compute_score_only
pf={int(k):float(v) for k,v in json.load(open('$SEED_FILE'))['partial_function'].items() if int(k)>=2}
print(f'{compute_score_only(pf):.10f}')")
echo "[$(ts)] seed base=$prev_base" | tee -a "$LOG"

seed="$SEED_FILE"
for N in "${RUNGS[@]}"; do
  echo "[$(ts)] ── rung N=$N (seed base=$prev_base)" | tee -a "$LOG"
  uv run python -u scripts/prime/colgen_reclaim.py \
    --seed-file "$seed" --extend-n "$N" --add-per-round 80 --rounds 3 \
    --time-limit "$TIME_LIMIT" --out-tag "$N" --rescale-safe \
    > "$OUT/rung-$N.log" 2>&1
  base_file="$OUT/colgen_base_$N.json"
  if [ ! -f "$base_file" ]; then
    echo "[$(ts)] rung $N produced no base file — STOP (see rung-$N.log)" | tee -a "$LOG"
    break
  fi
  new_base=$(uv run python -c "
import json,sys; sys.path.insert(0,'src')
from einstein.prime.evaluator import compute_score_only
pf={int(k):float(v) for k,v in json.load(open('$base_file'))['partial_function'].items() if int(k)>=2}
print(f'{compute_score_only(pf):.10f}')")
  gain=$(python3 -c "print(f'{$new_base - $prev_base:.2e}')")
  echo "[$(ts)] rung $N: base=$new_base gain=$gain" | tee -a "$LOG"
  improved=$(python3 -c "print(1 if $new_base - $prev_base >= $GAIN_FLOOR else 0)")
  if [ "$improved" = "0" ]; then
    echo "[$(ts)] gain below floor ($GAIN_FLOOR) — LADDER STALLED at N=$N" | tee -a "$LOG"
    break
  fi
  seed="$base_file"
  prev_base="$new_base"
done
echo "[$(ts)] LADDER DONE best_base=$prev_base seed=$seed" | tee -a "$LOG"
date > "$OUT/LADDER_DONE"
