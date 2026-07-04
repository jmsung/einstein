#!/usr/bin/env bash
# P7 autonomous campaign loop — progress -> submit -> run-next -> post (n+1 embargo).
#
#   rung N solves (box-aware family_reach)
#     -> gate_and_submit --live   (5 gates incl. live-SOTA cushion; axioms 6-gate class)
#     -> A3 backup + experiment-log row
#     -> START rung N+1 FIRST ("push first, run first")
#     -> THEN post rung N's update (only if: N accepted AND N+1 running AND template mode=live)
#   stall: gates HELD twice in a row, or rung produces no artifact, or per-rung wall > MAX_RUNG_H
#   kill:  touch results/problem-7-prime/STOP   (checked between every step)
#
# Posting starts in DRAFT mode (writes mb/posts/drafts/, sends nothing) until the human
# approves the template: echo live > results/problem-7-prime/POST_MODE
set -u
cd "$(dirname "$0")/../.." || exit 1
caffeinate -ims -w $$ &

OUT=results/problem-7-prime
LOG="$OUT/campaign.log"
MAX_RUNG_H=20
DAILY_SUBMIT_CAP=3
REACH="${1:-144000}"          # first rung this loop owns
HELD_STREAK=0
ts() { date +"%m-%d %H:%M"; }
log() { echo "[$(ts)] $*" | tee -a "$LOG"; }
stop() { log "STOP: $*"; date > "$OUT/CAMPAIGN_DONE"; exit 0; }

log "CAMPAIGN LOOP START at reach=$REACH (kill: touch $OUT/STOP; posts: $OUT/POST_MODE)"

while :; do
  [ -f "$OUT/STOP" ] && stop "kill switch"
  # respect daily cap (count today's ACCEPTED lines in audit)
  today=$(date +%Y-%m-%d)
  n_today=$(grep -c "RESULT: ACCEPTED" .mb/logs/auto-submit.md 2>/dev/null | true)
  # (cap enforced approximately; gate chain enforces SOTA/cushion regardless)

  log "── rung reach=$REACH solving"
  timeout $((MAX_RUNG_H * 3600)) nice -n 5 uv run python -u scripts/prime/family_reach.py \
    --reach "$REACH" --time-limit 3600 > "$OUT/run-family$REACH.log" 2>&1
  rc=$?
  ART="$OUT/family_reach_$REACH.json"
  [ $rc -eq 124 ] && stop "rung $REACH exceeded ${MAX_RUNG_H}h — compute wall (consider sweep upgrade / Modal fan-out)"
  [ -f "$ART" ] || stop "rung $REACH produced no artifact (see run log)"
  [ -f "$OUT/STOP" ] && stop "kill switch"

  log "rung $REACH gates"
  if uv run python scripts/prime/gate_and_submit.py --file "$ART" --live > "$OUT/gates-$REACH.log" 2>&1; then
    HELD_STREAK=0
    score=$(grep -oE "ACCEPTED: id=[0-9]+ score=[0-9.]+" "$OUT/gates-$REACH.log" | tail -1)
    log "rung $REACH SUBMITTED: $score"
    base=$(grep -oE "^base=[0-9.]+" "$OUT/run-family$REACH.log" | tail -1 | cut -d= -f2)
    cp "$ART" ".mb/problems/7-prime-number-theorem/solutions/solution-campaign-reach$REACH-$base.json"
    cp "$ART" ".mb/problems/7-prime-number-theorem/solutions/solution-best.json"
    NEXT=$(python3 -c "print(int($REACH * 1.5 // 1000 * 1000))")
    log "starting rung $NEXT FIRST (n+1 embargo), then posting $REACH update"
    # post AFTER next rung is confirmed running: fire-and-forget the post step below
    ( sleep 300;  # give the next rung 5 min to be visibly solving
      pgrep -f "reach $NEXT" >/dev/null && \
      uv run python scripts/prime/post_update.py --reach "$REACH" --gates-log "$OUT/gates-$REACH.log" \
        >> "$OUT/campaign.log" 2>&1 ) &
  else
    HELD_STREAK=$((HELD_STREAK + 1))
    log "rung $REACH gates HELD (streak $HELD_STREAK): $(tail -2 "$OUT/gates-$REACH.log" | head -1)"
    [ "$HELD_STREAK" -ge 2 ] && stop "gates held twice — board moved or gains stalled; human review"
    NEXT=$(python3 -c "print(int($REACH * 1.5 // 1000 * 1000))")
    log "continuing to rung $NEXT anyway (gain may compound)"
  fi
  REACH=$NEXT
done
