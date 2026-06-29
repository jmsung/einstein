# Heilbronn ablation — cold vs warm KB

- Status: **FINAL**
- Model: claude-haiku-4-5 · seeds 1,2,3 · timeout 600s · max-lesson-chars 4000
- Metric: `gap%` = fraction of the gap to the reference optimum closed (higher is better)

| problem | cold gap% | warm gap% | Δ (warm−cold) | seeds (c/w) |
|---|---|---|---|---|
| heil-n11 | 61.1% | 66.5% ✅ | +5.4 | 18/18 |
| heil-n12 | 54.2% | 56.3% ✅ | +2.2 | 18/18 |
| heil-n13 | 45.4% | 54.4% ✅ | +9.1 | 18/18 |
| heil-n14 | 38.6% | 43.7% ✅ | +5.1 | 18/18 |
| heil-n15 | 38.4% | 35.9% | -2.5 | 18/18 |
| heil-n16 | 29.3% | 27.7% | -1.6 | 18/18 |
| **MEAN** | **44.5%** | **47.4%** | **+2.9** | 108/108 |

## Takeaways
- Mean gap closed: **warm 47.4% vs cold 44.5%** (+2.9 pts) — warm ahead.
- Warm wins **4/6** problems head-to-head.
- Warm KB accumulating: lessons_read ranged 0→5 per solve (cold always 0).
