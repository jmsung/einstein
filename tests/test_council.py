"""Tests for the mathematician council dispatch scaffolding.

The council package is a thin runtime that parses persona definitions
from a private config file into ``Persona`` objects, then dispatches a
core + specialist subset for a given problem category. All persona
content lives outside the public package; this module is scaffolding
only.
"""

from __future__ import annotations

import textwrap
from pathlib import Path

import pytest

from einstein.council import Persona, dispatch, load_personas
from einstein.council.personas import COUNCIL_PATH


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def fake_council_md(tmp_path: Path) -> Path:
    """Minimal council markdown matching the canonical config structure."""
    content = textwrap.dedent(
        """\
        # Mathematician Council

        Some preamble text that should be ignored.

        ## Core Council (always runs)

        ### 1. Gauss — Number theory, algebraic constructions

        - **Real expertise**: CRT, character sums
        - **Prompt seed**: "Approach as algebraic construction."
        - **Literature focus**: Ireland-Rosen, Iwaniec-Kowalski
        - **Example insight**: P7 LP over squarefree integers.

        ### 2. Riemann — Complex analysis, spectral theory

        - **Real expertise**: zeta function, equilibrium measure
        - **Prompt seed**: "Think spectrally."
        - **Literature focus**: Saff-Totik, Trefethen ATAP
        - **Example insight**: Chebyshev equioscillation.

        ---

        ## Specialist Bench (conditional triggers)

        ### Viazovska — Sphere packing optimality proofs

        - **Real expertise**: E8, Leech magic functions
        - **Trigger rule**: `problem.category in {"sphere_packing", "kissing_number"}`
        - **Prompt seed**: "Viazovska-style optimality proof?"
        - **Literature focus**: Viazovska 2016
        - **Example insight**: P6 LP gap.

        ### Turán — Graph theory, Turán density

        - **Real expertise**: Turán theorem, extremal graph theory
        - **Trigger rule**: `problem.category == "graph_theory"`
        - **Prompt seed**: "Turán-type bound?"
        - **Literature focus**: Bollobás extremal graph theory
        - **Example insight**: P13 extremal graphon.
        """
    )
    path = tmp_path / "mathematician-council.md"
    path.write_text(content)
    return path


# ---------------------------------------------------------------------------
# Persona dataclass
# ---------------------------------------------------------------------------


class TestPersona:
    def test_persona_fields(self):
        p = Persona(
            name="Gauss",
            perspective="Number theory",
            tier="core",
            expertise="CRT",
            prompt_seed="Algebraic construction.",
            literature="Ireland-Rosen",
            example_insight="P7 LP",
            trigger_categories=frozenset(),
        )
        assert p.name == "Gauss"
        assert p.tier == "core"
        assert p.trigger_categories == frozenset()

    def test_persona_is_frozen(self):
        p = Persona(
            name="Gauss",
            perspective="Number theory",
            tier="core",
            expertise="",
            prompt_seed="",
            literature="",
            example_insight="",
            trigger_categories=frozenset(),
        )
        with pytest.raises((AttributeError, Exception)):
            p.name = "Other"  # type: ignore[misc]


# ---------------------------------------------------------------------------
# load_personas — markdown parsing
# ---------------------------------------------------------------------------


class TestLoadPersonas:
    def test_parses_core_and_bench(self, fake_council_md: Path):
        personas = load_personas(fake_council_md)
        names = [p.name for p in personas]
        assert names == ["Gauss", "Riemann", "Viazovska", "Turán"]

    def test_core_tier_assigned(self, fake_council_md: Path):
        personas = load_personas(fake_council_md)
        by_name = {p.name: p for p in personas}
        assert by_name["Gauss"].tier == "core"
        assert by_name["Riemann"].tier == "core"
        assert by_name["Viazovska"].tier == "bench"
        assert by_name["Turán"].tier == "bench"

    def test_perspective_extracted(self, fake_council_md: Path):
        personas = load_personas(fake_council_md)
        by_name = {p.name: p for p in personas}
        assert "Number theory" in by_name["Gauss"].perspective
        assert "Complex analysis" in by_name["Riemann"].perspective

    def test_fields_extracted(self, fake_council_md: Path):
        personas = load_personas(fake_council_md)
        gauss = next(p for p in personas if p.name == "Gauss")
        assert "CRT" in gauss.expertise
        assert "algebraic construction" in gauss.prompt_seed.lower()
        assert "Ireland-Rosen" in gauss.literature
        assert "P7" in gauss.example_insight

    def test_trigger_categories_parsed(self, fake_council_md: Path):
        personas = load_personas(fake_council_md)
        by_name = {p.name: p for p in personas}
        assert by_name["Viazovska"].trigger_categories == frozenset(
            {"sphere_packing", "kissing_number"}
        )
        assert by_name["Turán"].trigger_categories == frozenset({"graph_theory"})

    def test_core_personas_have_no_triggers(self, fake_council_md: Path):
        personas = load_personas(fake_council_md)
        for p in personas:
            if p.tier == "core":
                assert p.trigger_categories == frozenset()

    def test_missing_file_returns_empty(self, tmp_path: Path):
        personas = load_personas(tmp_path / "does_not_exist.md")
        assert personas == []

    def test_default_path_resolves_when_config_present(self):
        # When the private config is available, default load should
        # return the canonical 10 core + 3 bench personas.
        if not COUNCIL_PATH or not COUNCIL_PATH.exists():
            pytest.skip("Council config not available in this environment")
        personas = load_personas()
        core = [p for p in personas if p.tier == "core"]
        bench = [p for p in personas if p.tier == "bench"]
        assert len(core) == 10
        assert len(bench) >= 3


# ---------------------------------------------------------------------------
# dispatch
# ---------------------------------------------------------------------------


class TestDispatch:
    def test_dispatch_returns_all_core(self, fake_council_md: Path):
        result = dispatch("kissing_number", path=fake_council_md)
        names = [p.name for p in result]
        assert "Gauss" in names
        assert "Riemann" in names

    def test_dispatch_triggers_matching_specialist(self, fake_council_md: Path):
        result = dispatch("kissing_number", path=fake_council_md)
        names = [p.name for p in result]
        assert "Viazovska" in names
        assert "Turán" not in names

    def test_dispatch_no_specialist_for_unrelated_category(
        self, fake_council_md: Path
    ):
        result = dispatch("autocorrelation", path=fake_council_md)
        names = [p.name for p in result]
        assert "Viazovska" not in names
        assert "Turán" not in names
        # Core still present
        assert "Gauss" in names

    def test_dispatch_triggers_graph_theory_specialist(self, fake_council_md: Path):
        result = dispatch("graph_theory", path=fake_council_md)
        names = [p.name for p in result]
        assert "Turán" in names
        assert "Viazovska" not in names

    def test_dispatch_missing_file_returns_empty(self, tmp_path: Path):
        result = dispatch("kissing_number", path=tmp_path / "missing.md")
        assert result == []

    def test_dispatch_order_core_before_bench(self, fake_council_md: Path):
        result = dispatch("kissing_number", path=fake_council_md)
        tiers = [p.tier for p in result]
        # All core entries must precede all bench entries
        first_bench = next((i for i, t in enumerate(tiers) if t == "bench"), len(tiers))
        assert all(t == "core" for t in tiers[:first_bench])
