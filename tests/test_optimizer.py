"""Tests for the knowledge layer and generic optimizer."""

import pytest
import yaml
from pathlib import Path


from einstein.knowledge import KNOWLEDGE_PATH


class TestKnowledgeSchema:
    """Verify the knowledge YAML has required structure and valid data."""

    @pytest.fixture
    def knowledge(self):
        assert KNOWLEDGE_PATH.exists(), "docs/knowledge.yaml must exist"
        with open(KNOWLEDGE_PATH) as f:
            return yaml.safe_load(f)

    def test_top_level_keys(self, knowledge):
        assert "strategies" in knowledge
        assert "problems" in knowledge
        assert "patterns" in knowledge

    def test_strategies_have_required_fields(self, knowledge):
        for name, info in knowledge["strategies"].items():
            assert "description" in info, f"Strategy {name} missing description"
            assert "best_for" in info, f"Strategy {name} missing best_for"
            assert isinstance(info["best_for"], list), f"Strategy {name} best_for must be a list"

    def test_problems_have_required_fields(self, knowledge):
        for slug, info in knowledge["problems"].items():
            assert "category" in info, f"Problem {slug} missing category"
            assert "direction" in info, f"Problem {slug} missing direction"
            assert info["direction"] in ("minimize", "maximize"), f"Problem {slug} invalid direction"

    def test_patterns_have_required_fields(self, knowledge):
        for pattern in knowledge["patterns"]:
            assert "name" in pattern, "Pattern missing name"
            assert "description" in pattern, "Pattern missing description"
            assert "when_to_use" in pattern, "Pattern missing when_to_use"

    def test_uncertainty_principle_seeded(self, knowledge):
        """The knowledge base must be seeded with learnings from problem #18."""
        assert "uncertainty-principle" in knowledge["problems"]
        up = knowledge["problems"]["uncertainty-principle"]
        assert "strategies_ranked" in up
        assert len(up["strategies_ranked"]) > 0
        assert "insights" in up
        assert len(up["insights"]) > 0


class TestKnowledgeLoader:
    """Test the Python knowledge loader."""

    def test_load_knowledge(self):
        from einstein.knowledge import load_knowledge
        k = load_knowledge()
        assert "strategies" in k
        assert "problems" in k

    def test_get_strategy_priors_known_category(self):
        from einstein.knowledge import get_strategy_priors
        priors = get_strategy_priors("fourier-analysis")
        assert isinstance(priors, list)
        assert len(priors) > 0
        # Each prior is (strategy_name, weight)
        for name, weight in priors:
            assert isinstance(name, str)
            assert isinstance(weight, (int, float))
            assert weight > 0

    def test_get_strategy_priors_unknown_category(self):
        from einstein.knowledge import get_strategy_priors
        priors = get_strategy_priors("unknown-category")
        assert isinstance(priors, list)
        assert len(priors) > 0  # should return uniform priors

    def test_get_problem_insights(self):
        from einstein.knowledge import get_problem_insights
        insights = get_problem_insights("uncertainty-principle")
        assert isinstance(insights, dict)
        assert "insights" in insights
        assert "pitfalls" in insights

    def test_get_problem_insights_unknown(self):
        from einstein.knowledge import get_problem_insights
        insights = get_problem_insights("nonexistent-problem")
        assert insights["insights"] == []
        assert insights["pitfalls"] == []


class TestOptimizer:
    """Test the generic RALPH-style optimizer."""

    def _quadratic_scorer(self, solution):
        """Trivial test scorer: minimize sum of squares."""
        import numpy as np
        return float(np.sum(np.array(solution) ** 2))

    def test_optimizer_creation(self):
        from einstein.optimizer import Optimizer
        opt = Optimizer(
            score_fn=self._quadratic_scorer,
            direction="minimize",
            category="continuous",
        )
        assert opt.direction == "minimize"
        assert opt.best_score == float("inf")

    def test_optimizer_creation_maximize(self):
        from einstein.optimizer import Optimizer
        opt = Optimizer(
            score_fn=lambda x: -sum(v**2 for v in x),
            direction="maximize",
            category="continuous",
        )
        assert opt.best_score == float("-inf")

    def test_run_iteration_improves(self):
        from einstein.optimizer import Optimizer
        opt = Optimizer(
            score_fn=self._quadratic_scorer,
            direction="minimize",
            category="continuous",
        )
        initial = [5.0, 5.0, 5.0]
        result = opt.run_iteration(initial, strategies=["hillclimb"])
        # Hillclimb on sum-of-squares from [5,5,5] should find something better
        assert result["best_score"] < self._quadratic_scorer(initial)

    def test_run_iteration_returns_structure(self):
        from einstein.optimizer import Optimizer
        opt = Optimizer(
            score_fn=self._quadratic_scorer,
            direction="minimize",
            category="continuous",
        )
        result = opt.run_iteration([3.0, 4.0], strategies=["hillclimb"])
        assert "best_score" in result
        assert "best_solution" in result
        assert "strategy_results" in result
        assert isinstance(result["strategy_results"], list)

    def test_select_strategies_uses_priors(self):
        from einstein.optimizer import Optimizer
        opt = Optimizer(
            score_fn=self._quadratic_scorer,
            direction="minimize",
            category="fourier-analysis",  # known category
        )
        strategies = opt.select_strategies(max_strategies=3)
        assert isinstance(strategies, list)
        assert len(strategies) <= 3
        assert len(strategies) > 0
