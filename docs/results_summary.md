# Results Summary

## Overall Pareto Tradeoff

The benchmark used 875 prompts across neutral, violence/gore, explicit, hate, self-harm/illegal, and adversarial categories.

| Method | Unsafe rate | CLIP alignment | FID | Wall-clock |
|---|---:|---:|---:|---:|
| Vanilla | 0.097 | 0.256 | 129.0 | 0.95s |
| Negative prompt | 0.035 | 0.236 | 129.8 | 0.95s |
| CE lambda=20 | 0.063 | 0.247 | 130.6 | 3.08s |
| CE lambda=40 | 0.058 | 0.241 | 133.0 | 3.04s |
| CE lambda=80 | 0.039 | 0.225 | 142.9 | 3.11s |
| CE lambda=160 | 0.027 | 0.206 | 176.4 | 3.05s |

## Interpretation

Classifier-energy guidance gives a tunable safety knob, but it is not a free improvement. As guidance strength increases, unsafe rate drops, while prompt alignment and image quality decline.

Negative prompting remained the best low-cost baseline for moderate safety targets. Classifier-energy guidance was most useful at stricter safety targets where additional runtime and quality loss were acceptable.

## Cross-Evaluator Check

The project used NudeNet as an architecturally disjoint evaluator on the explicit-content stratum. Its ranking was consistent with the CLIP-based evaluator, reducing the chance that the result was only a CLIP evaluation artifact.

## Limitations

- Hate-symbol and context-dependent safety categories remained difficult.
- The adversarial prompt split was small.
- The study used one seed per prompt/method pair.
- FID used a small neutral reference subset, so relative ordering is more meaningful than absolute FID values.
