#!/usr/bin/env bash
# Detached unattended continuation: wait for the running 96k probe, then ladder on.
# Survives session/network loss (nohup). Auto-submits when ONLINE; DRAFTS posts only
# (never sends). Self-halts at compute wall (MAX_RUNG_H) or 2 gate-HELDs. Kill: touch
# results/problem-7-prime/STOP.
cd /Users/jmsung/projects/einstein/cb-feat-p7-nextension-reclaim-v2
echo "[offline-ladder] waiting for 96k probe to finish $(date)"
while pgrep -f "family_reach.py --reach 96000" >/dev/null; do sleep 60; done
echo "[offline-ladder] 96k done; continuing ladder from 144k $(date)"
exec bash scripts/prime/campaign_loop.sh 144000
