#!/usr/bin/env bash
# calibrate.sh — recalibrate this machine for the compute router.
#
# Detects the device (sysctl-derived key like apple-the workstation-high-memory),
# runs scripts/local_benchmark.py, diffs key metrics against the prior
# calibration for this device if one exists, then prints sample router
# invocations the user can sanity-check.
#
# When to re-run:
#   - Every 2-4 weeks (drift from macOS / Xcode / torch / numpy updates)
#   - After any major macOS upgrade
#   - When moving to a new Mac (writes a fresh per-device calibration)
#   - Any time the router seems to recommend "modal" for a workload that
#     felt fine on this machine, or vice versa
#
# The calibration lands at docs/agent/calibrations/<device-key>.json and
# is per-device — no other Mac's calibration is touched.

set -euo pipefail

cd "$(dirname "$0")/../.."   # repo root

KEY=$(uv run python scripts/compute_router.py --show-device | awk -F: '/^device-key:/{print $2}' | tr -d ' ')
CAL_DIR="docs/agent/calibrations"
NEW_CAL="$CAL_DIR/$KEY.json"
PRIOR_BACKUP="$(mktemp -t calibrate-prior-XXXXX.json)"

echo "device: $KEY"

if [[ -f "$NEW_CAL" ]]; then
  echo "prior calibration found: $NEW_CAL"
  cp "$NEW_CAL" "$PRIOR_BACKUP"
  HAS_PRIOR=1
else
  echo "no prior calibration for this device — first run"
  HAS_PRIOR=0
fi

echo
echo "==> running scripts/local_benchmark.py"
echo
uv run python scripts/local_benchmark.py
echo

if [[ "$HAS_PRIOR" -eq 1 ]]; then
  echo "==> drift vs prior calibration"
  uv run python - "$PRIOR_BACKUP" "$NEW_CAL" <<'PY'
import json, sys, pathlib

prior = json.loads(pathlib.Path(sys.argv[1]).read_text())
new = json.loads(pathlib.Path(sys.argv[2]).read_text())

METRICS = [
    ("cpu_single_core.matmul_2048_seconds", "CPU single 2048^3 (s)"),
    ("cpu_multi_core.matmul_4096_seconds", "CPU multi 4096^3 (s)"),
    ("cpu_mp_scaling.mp_speedup", "MP speedup (Nx)"),
    ("mps.matmul_4096_f32_seconds", "MPS f32 4096^3 (s)"),
    ("mpmath.dps50_1k_iters_seconds", "mpmath dps50 1k iters (s)"),
]

def get(d, path):
    cur = d
    for k in path.split("."):
        if not isinstance(cur, dict):
            return None
        cur = cur.get(k)
    return cur

def fmt_drift(old, new):
    if old is None or new is None or old == 0:
        return "?"
    pct = (new - old) / old * 100
    arrow = "↑" if pct > 0 else "↓" if pct < 0 else "="
    return f"{arrow}{abs(pct):.1f}%"

print(f"  prior date: {prior.get('timestamp', '?')}")
print(f"  new date:   {new.get('timestamp', '?')}")
print()
print(f"  {'metric':40} {'prior':>12} {'new':>12}  drift")
print(f"  {'-'*40} {'-'*12} {'-'*12}  {'-'*8}")
for path, label in METRICS:
    pv = get(prior, path)
    nv = get(new, path)
    pv_str = f"{pv:.4f}" if isinstance(pv, (int, float)) else str(pv)
    nv_str = f"{nv:.4f}" if isinstance(nv, (int, float)) else str(nv)
    print(f"  {label:40} {pv_str:>12} {nv_str:>12}  {fmt_drift(pv, nv)}")

# RAM headroom diff
prior_ram = prior.get("ram", {})
new_ram = new.get("ram", {})
diff_keys = sorted(set(prior_ram) | set(new_ram))
print()
print(f"  RAM headroom:")
for k in diff_keys:
    pv = prior_ram.get(k, "—")
    nv = new_ram.get(k, "—")
    flag = "" if pv == nv else "  (changed)"
    print(f"    {k:6} prior={pv:8} new={nv:8}{flag}")
PY
  rm -f "$PRIOR_BACKUP"
  echo
fi

echo "==> sample router queries you can run to sanity-check"
echo
cat <<'SAMPLES'
  # Sequential / mpmath polish — should always be local-cpu
  uv run python scripts/compute_router.py --workload mpmath --precision mpmath --hours 4 --ram 8

  # Float32 batched basin-hopping — should be local-mps if MPS available
  uv run python scripts/compute_router.py --workload basin-hop-pop --precision f32 --hours 4 --ram 8

  # Sustained float64 parallel tempering — should be modal
  uv run python scripts/compute_router.py --workload parallel-tempering --precision f64 --hours 6 --ram 16

  # Large LP that fits locally
  uv run python scripts/compute_router.py --workload lp-large --precision f64 --hours 4 --ram 64

  # Same LP but RAM-bound past local — should be modal
  uv run python scripts/compute_router.py --workload lp-large --precision f64 --hours 4 --ram 110

SAMPLES

echo "✓ calibration done. Committed under: $NEW_CAL"
