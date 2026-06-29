# Heilbronn ablation — cold vs warm KB

- Status: **FINAL**
- Model: claude-haiku-4-5 · seeds 1,2,3 · timeout 600s · max-lesson-chars 4000
- Metric: `gap%` = fraction of the gap to the reference optimum closed (higher is better)

| problem | cold gap% | warm gap% | Δ (warm−cold) | seeds (c/w) |
|---|---|---|---|---|
| heil-n11 | 66.4% | 68.7% ✅ | +2.3 | 18/18 |
| heil-n12 | 50.2% | 56.1% ✅ | +6.0 | 18/18 |
| heil-n13 | 45.9% | 50.3% ✅ | +4.4 | 18/18 |
| heil-n14 | 33.9% | 36.5% ✅ | +2.7 | 18/18 |
| heil-n15 | 38.2% | 34.7% | -3.5 | 18/18 |
| heil-n16 | 23.0% | 33.0% ✅ | +10.0 | 18/18 |
| **MEAN** | **42.9%** | **46.6%** | **+3.6** | 108/108 |

## Takeaways
- Mean gap closed: **warm 46.6% vs cold 42.9%** (+3.6 pts) — warm ahead.
- Warm wins **5/6** problems head-to-head.
- Warm KB accumulating: lessons_read ranged 0→5 per solve (cold always 0).
