---
type: finding
author: agent
drafted: 2026-05-25
question_origin: js/feat/research-synthesis G1
status: answered
related_problems: []
related_concepts: []
related_findings:
  - research-synthesis-design
cites:
  - ../../tools/refresh_qmd.sh
---

# Fix: qmd Metal-init warning + Darwin SIGABRT on `qmd query` — adopt CPU mode

## TL;DR

The Goal-1 premise as written in the branch file ("embed all 1450 chunks; Metal
compile failure") was based on the visible stderr warning, not on what the
system actually did. **Embedding was always working** — node-llama-cpp's Metal
init prints `ggml_metal_library_init_from_source: error compiling source` and
then continues anyway. The real bug is downstream: on macOS 26.4 + Apple
clang 21 + node-llama-cpp 3.18.1, `qmd query` (the reranking path) exits with
`Abort trap: 6` (SIGABRT) reliably. **Chosen mitigation: set
`QMD_FORCE_CPU=1` for repo qmd usage**; clean exits, ~16s for a full hybrid
query+rerank on the 1727-doc wiki corpus, no functional loss. The pre-existing
4436 Metal-computed vectors were re-embedded under CPU to align fingerprints
(per `qmd doctor`).

## Diagnosis receipts

Reproduction:

```text
$ qmd --version                                       # 2.1.0 (Apr 29)
$ qmd embed --max-batch-mb 50
[node-llama-cpp] ggml_metal_library_init_from_source: error compiling source
✓ All content hashes already have embeddings.          # ← system functional
$ qmd vsearch "magic function modular form bound" -c einstein-wiki-source -n 3
Score: 53% / 50% / 48%                                 # ← vec retrieval real
```

Hybrid pipeline (lex + vec + hyde + rerank) end-to-end:

```text
$ qmd query "literature-driven planning" -c einstein-wiki -n 3 --verbose
Embedding 4 queries... (256ms)
Reranking 22 chunks... (2.9s)
Score: 88% (basin-rigidity.md) ...                     # ← reranking works
```

Toolchain state at diagnosis:

| Component | Version |
|---|---|
| macOS | 26.4.1 / build 25E253 |
| Apple clang | 21.0.0 (clang-2100.0.123.102) |
| Xcode tools | `/Library/Developer/CommandLineTools` |
| `qmd` (installed → updated) | 2.1.0 → **2.5.2** |
| `node-llama-cpp` (bundled) | 3.18.1 (latest on npm) |
| GPU | a local workstation, VRAM 107.5 GB |

`qmd doctor` device probe confirms Metal IS detected (`✓ device probe: GPU
metal (macOS Metal backend); offloading enabled; devices: a local workstation`) — the
stderr warning is from a *probe step* that the runtime then succeeds in
overriding. But the actual `qmd query` execution hits the documented Darwin
Metal finalizer abort (`Abort trap: 6`, exit code 134) on every run:

```text
$ for i in 1 2 3; do qmd query "magic function" -c einstein-wiki-source -n 2 >/dev/null 2>&1; echo "run $i: exit=$?"; done
/bin/bash: line 23: 64527 Abort trap: 6  qmd query ...
run 1: exit=134
run 2: exit=134
run 3: exit=134
```

CPU mode (the chosen fix):

```text
$ for i in 1 2 3; do QMD_FORCE_CPU=1 qmd query "magic function" -c einstein-wiki-source -n 2 >/dev/null 2>&1; echo "run $i: exit=$?"; done
run 1: exit=0
run 2: exit=0
run 3: exit=0
```

The qmd 2.5.0 CHANGELOG explicitly added `QMD_FORCE_CPU=1` / `--no-gpu`,
`qmd doctor`, and a fix to "use a safe immediate-exit path on Darwin to avoid
ggml Metal finalizer aborts" specifically for `qmd query --json`. The regular
`qmd query` path on this stack still aborts; CPU bypass is the durable
workaround until either node-llama-cpp or qmd patches the non-JSON Darwin
exit path.

## Chosen fix

1. **Update `qmd` 2.1.0 → 2.5.2** (`npm install -g @tobilu/qmd@2.5.2`).
   Brings `qmd doctor`, `QMD_FORCE_CPU=1`, and the scoped `--force` knob.
2. **Set `QMD_FORCE_CPU=1`** in [`../../tools/refresh_qmd.sh`](../../tools/refresh_qmd.sh).
   That covers the cycle-end refresh path. Interactive `qmd query` /
   `qmd vsearch` invocations also need the env var — prefix it manually, or
   export it in your shell rc:

   ```bash
   export QMD_FORCE_CPU=1                              # ~/.zshrc, ~/.bashrc
   ```

3. **Force-rebuild vectors under CPU** to align fingerprints (Metal and CPU
   produce vectors that differ at distance ≈ 0.000238 due to float
   precision — functionally fine, but `qmd doctor` flags the mismatch):

   ```bash
   QMD_FORCE_CPU=1 qmd embed --force -c einstein-wiki         # ~1m41s
   QMD_FORCE_CPU=1 qmd embed --force -c einstein-wiki-source  # ~8m est.
   ```

## What this rules out as the root cause

- **Not** missing vectors (4436 already present pre-fix).
- **Not** Metal entirely absent (probe detects a local workstation GPU successfully).
- **Not** node-llama-cpp version mismatch (already at latest 3.18.1).
- **Not** Xcode toolchain missing (`xcode-select -p` returns valid path).
- **Not** an embed bug (`qmd embed` completes successfully even with the
  warning).

## What might still work (deferred)

- A node-llama-cpp release that compiles Metal shader sources against
  macOS 26 / clang 21. Upstream effort; out of scope for this repo.
- `QMD_LLAMA_GPU=metal` explicit override (added in qmd 2.5.0) might
  produce different abort behavior; untested.
- Building node-llama-cpp from source against current Xcode SDK with
  patched Metal shaders. High effort, low return — CPU is fast enough.

## Implications for the branch

Goal 1 as originally framed ("G2 falls back to keyword-only and the synthesis
step is half-blind without this fix") was inaccurate — hybrid retrieval was
working all along. G2 (pre-cycle synthesis) can proceed normally with hybrid
lex+vec+rerank queries; CPU latency (≤20s per full query) is acceptable for
a once-per-cycle step.

The cycle-discipline.md rule continues to apply unchanged: cycle-start `qmd
query` is mandatory; cycle-end `refresh_qmd.sh` is mandatory. The change here
is that the refresh script silently uses CPU mode, and the cycle-start query
needs `QMD_FORCE_CPU=1` in the agent's shell environment to avoid SIGABRT.

## Regression detection

If `qmd query` exits 134 (`Abort trap: 6`) in the future, the env var is
missing from the calling context. If `qmd doctor` warns about
fingerprint mismatch, vectors were computed with one backend and queries with
another — re-run `qmd embed --force` with the same `QMD_FORCE_CPU` setting as
the query path.

See also: [`research-synthesis-design`](research-synthesis-design.md) (the
G0 finding — G1's premise inversion sharpens its "synthesis step substrate"
claim).
