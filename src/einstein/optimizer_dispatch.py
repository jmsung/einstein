"""optimizer_dispatch.py — invoke per-problem optimizers from autonomous_loop.

Bridges the autonomous_loop orchestrator (which picks a strategy) to the
heterogeneous per-problem optimizer scripts (each with its own CLI). The
contract is uniform on the dispatch side:

    dispatch(problem_id, strategy=None) -> DispatchResult

The contract on the optimizer side is the *manifest* — a YAML entry per
problem listing the available optimizer scripts, their CLI args, expected
result file, and the parser to use. Adding a new problem = adding one
manifest entry + ensuring the script writes a result file the parser can
read. No central refactor required.

Parsers (named in manifest):

  json_score_payload  — result_file is JSON with {"score": float, "payload": ...}.
                        Most general. Recommended for new wirings.

Manifest schema (`src/einstein/optimizer_manifest.yaml`):

    14:
      slug: circle-packing-square
      default: slsqp_polish       # optional — used when strategy=None
      optimizers:
        slsqp_polish:
          script: scripts/circle_packing_square/slsqp_polish.py
          cli_args: []
          timeout_seconds: 300
          result_file: results/circle_packing_square/slsqp_polish_result.json
          result_parser: json_score_payload

`dispatch()` is the only public entry. Everything else is implementation
detail (subprocess invocation, result parsing, error handling).
"""

from __future__ import annotations

import json
import logging
import subprocess
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore[import-not-found]
except ImportError:  # pragma: no cover — pyyaml is a project dep
    yaml = None  # type: ignore[assignment]

log = logging.getLogger("optimizer_dispatch")

_REPO = Path(__file__).resolve().parents[2]
DEFAULT_MANIFEST_PATH = _REPO / "src" / "einstein" / "optimizer_manifest.yaml"
DEFAULT_TIMEOUT_SECONDS = 1800
STDOUT_TAIL_BYTES = 2048


@dataclass
class DispatchResult:
    """Outcome of one dispatch call. Score+payload populated only on ok=True."""

    ok: bool
    problem_id: int
    optimizer: str | None = None
    score: float | None = None
    payload: dict | None = None
    runtime_seconds: float = 0.0
    exit_code: int | None = None
    stdout_tail: str = ""
    stderr_tail: str = ""
    error: str | None = None
    extra: dict = field(default_factory=dict)


def load_manifest(path: Path | None = None) -> dict:
    """Return the manifest dict, or {} if file missing / yaml unavailable."""
    p = path if path is not None else DEFAULT_MANIFEST_PATH
    if not p.is_file() or yaml is None:
        return {}
    try:
        data = yaml.safe_load(p.read_text()) or {}
    except yaml.YAMLError as e:
        log.error("manifest yaml parse failed: %s", e)
        return {}
    # Top-level keys are problem_ids (ints in yaml are fine)
    return {int(k): v for k, v in data.items()}


def _resolve_optimizer(problem_entry: dict, strategy: str | None) -> tuple[str, dict] | None:
    """Pick the optimizer block for `strategy`, or fall back to `default`.

    Returns (optimizer_name, optimizer_block) or None if no match.
    """
    opts = problem_entry.get("optimizers") or {}
    if not opts:
        return None
    if strategy and strategy in opts:
        return strategy, opts[strategy]
    default = problem_entry.get("default")
    if default and default in opts:
        return default, opts[default]
    # Fall back to first listed
    first = next(iter(opts))
    return first, opts[first]


def _parse_result(result_file: Path, parser: str) -> tuple[float | None, dict | None, str | None]:
    """Returns (score, payload, error). On error, score+payload are None."""
    if not result_file.is_file():
        return None, None, f"result_file missing: {result_file}"
    if parser != "json_score_payload":
        return None, None, f"unknown result_parser: {parser}"
    try:
        data = json.loads(result_file.read_text())
    except (OSError, json.JSONDecodeError) as e:
        return None, None, f"result_file parse failed: {e}"
    if not isinstance(data, dict) or "score" not in data:
        return None, None, "result_file missing required 'score' field"
    try:
        score = float(data["score"])
    except (TypeError, ValueError):
        return None, None, f"result_file 'score' not numeric: {data['score']!r}"
    payload = data.get("payload")
    if payload is not None and not isinstance(payload, dict):
        return None, None, "result_file 'payload' must be dict or absent"
    return score, payload, None


def _tail(text: str, max_bytes: int = STDOUT_TAIL_BYTES) -> str:
    if len(text) <= max_bytes:
        return text
    return "…" + text[-(max_bytes - 1) :]


def dispatch(
    problem_id: int,
    strategy: str | None = None,
    *,
    manifest_path: Path | None = None,
    timeout_override: int | None = None,
    dry_run: bool = False,
    cwd: Path | None = None,
    subprocess_runner: Any = None,
) -> DispatchResult:
    """Look up `problem_id` (+ optional `strategy`) in the manifest, invoke the
    optimizer subprocess, parse its result file, return DispatchResult.

    `dry_run=True` returns a DispatchResult with ok=False, error="dry-run",
    and the optimizer field populated so callers can log the resolved entry
    without executing it.

    `subprocess_runner` is a test seam — defaults to `subprocess.run`.
    """
    manifest = load_manifest(manifest_path)
    entry = manifest.get(problem_id)
    if not entry:
        return DispatchResult(
            ok=False,
            problem_id=problem_id,
            error=f"no manifest entry for problem_id={problem_id}",
        )

    picked = _resolve_optimizer(entry, strategy)
    if picked is None:
        return DispatchResult(
            ok=False,
            problem_id=problem_id,
            error=f"no optimizer defined for problem_id={problem_id} (strategy={strategy})",
        )
    optimizer_name, opt = picked

    if dry_run:
        return DispatchResult(
            ok=False,
            problem_id=problem_id,
            optimizer=optimizer_name,
            error="dry-run",
        )

    script = (cwd or _REPO) / opt["script"]
    if not script.is_file():
        return DispatchResult(
            ok=False,
            problem_id=problem_id,
            optimizer=optimizer_name,
            error=f"script missing: {script}",
        )

    cli_args = list(opt.get("cli_args") or [])
    timeout = (
        timeout_override
        if timeout_override is not None
        else int(opt.get("timeout_seconds", DEFAULT_TIMEOUT_SECONDS))
    )
    cmd = ["uv", "run", "python", str(script), *cli_args]
    runner = subprocess_runner if subprocess_runner is not None else subprocess.run

    log.info("dispatch P%d → %s (timeout=%ds)", problem_id, optimizer_name, timeout)
    t0 = time.time()
    try:
        proc = runner(
            cmd,
            cwd=str(cwd or _REPO),
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return DispatchResult(
            ok=False,
            problem_id=problem_id,
            optimizer=optimizer_name,
            runtime_seconds=time.time() - t0,
            error=f"timeout after {timeout}s",
        )
    except (OSError, subprocess.SubprocessError) as e:
        return DispatchResult(
            ok=False,
            problem_id=problem_id,
            optimizer=optimizer_name,
            runtime_seconds=time.time() - t0,
            error=f"subprocess failed: {e}",
        )

    runtime = time.time() - t0
    stdout_tail = _tail(proc.stdout or "")
    stderr_tail = _tail(proc.stderr or "")

    if proc.returncode != 0:
        return DispatchResult(
            ok=False,
            problem_id=problem_id,
            optimizer=optimizer_name,
            runtime_seconds=runtime,
            exit_code=proc.returncode,
            stdout_tail=stdout_tail,
            stderr_tail=stderr_tail,
            error=f"optimizer exited with code {proc.returncode}",
        )

    result_file = (cwd or _REPO) / opt["result_file"]
    score, payload, parse_err = _parse_result(
        result_file, opt.get("result_parser", "json_score_payload")
    )
    if parse_err is not None:
        return DispatchResult(
            ok=False,
            problem_id=problem_id,
            optimizer=optimizer_name,
            runtime_seconds=runtime,
            exit_code=0,
            stdout_tail=stdout_tail,
            stderr_tail=stderr_tail,
            error=parse_err,
        )

    return DispatchResult(
        ok=True,
        problem_id=problem_id,
        optimizer=optimizer_name,
        score=score,
        payload=payload,
        runtime_seconds=runtime,
        exit_code=0,
        stdout_tail=stdout_tail,
        stderr_tail=stderr_tail,
    )


def _result_to_dict(r: DispatchResult, *, include_payload: bool) -> dict:
    """Serialize a DispatchResult to a JSON-friendly dict for CLI output.

    The payload (e.g. a 30k-element solution vector) is omitted by default —
    it bloats cycle logs and the score is the only field the autonomous loop
    needs. Pass --payload to include it.
    """
    d = {
        "ok": r.ok,
        "problem_id": r.problem_id,
        "optimizer": r.optimizer,
        "score": r.score,
        "runtime_seconds": round(r.runtime_seconds, 3),
        "exit_code": r.exit_code,
        "error": r.error,
    }
    if include_payload:
        d["payload"] = r.payload
    return d


def main(argv: list[str] | None = None) -> int:
    """CLI entrypoint — the sanctioned autonomous-loop dispatch command.

        uv run python -m einstein.optimizer_dispatch --problem-id 14 --strategy slsqp_polish

    Runs `dispatch(problem_id, strategy)`, prints the DispatchResult as JSON to
    stdout, and returns exit code 0 on success / 1 on dispatch failure. This is
    what makes the manifest reachable from the autonomous toolset — without it,
    the documented command was a silent no-op (see
    docs/wiki/findings/dead-end-p14-dispatch-cli-noop.md).
    """
    import argparse

    parser = argparse.ArgumentParser(
        prog="python -m einstein.optimizer_dispatch",
        description=main.__doc__.strip().split("\n", 1)[0],
    )
    parser.add_argument("--problem-id", type=int, required=True, help="Arena problem id.")
    parser.add_argument(
        "--strategy",
        type=str,
        default=None,
        help="Optimizer name from the manifest. Omit to use the problem's default.",
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        default=None,
        help=f"Manifest path (default: {DEFAULT_MANIFEST_PATH}).",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=None,
        help="Override the manifest timeout_seconds for this run.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Resolve the manifest entry and print it without executing.",
    )
    parser.add_argument(
        "--payload",
        action="store_true",
        help="Include the full solution payload in the JSON output (verbose).",
    )
    args = parser.parse_args(argv)

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    result = dispatch(
        args.problem_id,
        strategy=args.strategy,
        manifest_path=args.manifest,
        timeout_override=args.timeout,
        dry_run=args.dry_run,
    )
    print(json.dumps(_result_to_dict(result, include_payload=args.payload), indent=2))
    # dry-run is an informational success even though ok=False.
    if result.ok or (args.dry_run and result.error == "dry-run"):
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
