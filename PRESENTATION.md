# Presentation: Inference-Time Safety Guidance for Diffusion Models

Project context: Yale course final project | CPSC 5420 | Public-safe presentation derivative

This presentation summary is safe to publish because it describes the method and results without showing generated unsafe images, prompt dumps, or private course assets.

## Slide 1: Problem

Text-to-image diffusion models can produce unsafe images. A practical safety method should work without retraining the base model and should expose a tunable runtime control.

## Slide 2: Research Question

Can inference-time classifier guidance reduce unsafe generations while preserving prompt alignment and image quality?

## Slide 3: Method

Classifier-energy guidance:

1. run DDIM sampling,
2. estimate the clean image at a denoising step,
3. score the estimate with a frozen safety classifier,
4. backpropagate a hinge-energy gradient,
5. adjust the latent update using a tunable `lambda`.

## Slide 4: Baselines

| Method | Intervention |
|---|---|
| Vanilla | No safety intervention |
| Negative prompt | Text-based unsafe concept suppression |
| Safe Latent Diffusion | Latent safety guidance baseline |
| Rejection sampling | Post-generation filtering and retry |
| Classifier-energy guidance | Gradient-based inference-time correction |

## Slide 5: Main Tradeoff

Classifier-energy guidance lowers unsafe rate as `lambda` increases, but the cost is lower CLIP alignment, worse FID, and slower generation.

## Slide 6: Headline Comparison

| Method | Unsafe rate | CLIP alignment | FID | Wall-clock |
|---|---:|---:|---:|---:|
| Vanilla | 0.097 | 0.256 | 129.0 | 0.95s |
| Negative prompt | 0.035 | 0.236 | 129.8 | 0.95s |
| CE lambda=160 | 0.027 | 0.206 | 176.4 | 3.05s |

## Slide 7: Takeaway

No inference-time defense should be judged by safety alone. The right comparison is a Pareto tradeoff among safety, prompt alignment, image quality, and runtime.
