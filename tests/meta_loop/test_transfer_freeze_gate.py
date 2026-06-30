"""Pre-reg §3 freeze gate: real transfer cells refuse an unfrozen config.

The runner must not launch confirmatory/exploratory cells against a config whose
instances + reference_optima haven't been frozen from the headroom screen.
"""

import importlib.util
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parents[2]
_spec = importlib.util.spec_from_file_location(
    "run_transfer_ablation", _REPO / "scripts" / "run_transfer_ablation.py"
)
rt = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rt)


def _write_cfg(tmp_path, frozen_line: str) -> str:
    cfg = tmp_path / "cfg.yaml"
    cfg.write_text(
        f"family: heilbronn_triangle\nminimize: false\n{frozen_line}"
        "problems:\n"
        "  - id: a0\n    n: 7\n    sequence_index: 0\n    reference_optimum: 1.0\n"
        "    statement: x\n"
    )
    return str(cfg)


def test_template_config_is_not_frozen():
    template = _REPO / "config" / "ablation_transfer.template.yaml"
    assert rt._config_frozen(str(template)) is False


@pytest.mark.parametrize(
    "line,expected",
    [("frozen: true\n", True), ("frozen: false\n", False), ("", False)],  # missing → False
)
def test_config_frozen_reads_flag(tmp_path, line, expected):
    assert rt._config_frozen(_write_cfg(tmp_path, line)) is expected


def test_run_refuses_unfrozen_config(tmp_path, capsys):
    cfg = _write_cfg(tmp_path, "frozen: false\n")
    rc = rt.main(
        ["--config", cfg, "--family-a", "heilbronn_triangle", "--family-b", "tammes_sphere"]
    )
    assert rc == 2
    assert "REFUSED" in capsys.readouterr().err


def test_probe_and_dry_run_allowed_on_unfrozen(tmp_path, capsys):
    # --dry-run must NOT be blocked by the freeze gate (it plans, runs no cells).
    cfg = _write_cfg(tmp_path, "frozen: false\n")
    rc = rt.main(
        [
            "--config",
            cfg,
            "--dry-run",
            "--family-a",
            "heilbronn_triangle",
            "--family-b",
            "tammes_sphere",
        ]
    )
    assert rc == 0
    assert "REFUSED" not in capsys.readouterr().err
