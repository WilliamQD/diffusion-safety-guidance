# Report: Inference-Time Safety Guidance for Diffusion Models

Project context: Yale course final project | CPSC 5420 | Public-safe report derivative

This report summarizes the collaborative final project in a public-safe format. It omits generated image galleries, raw prompt dumps, model weights, private course artifacts, and unsafe examples.

## Abstract

Text-to-image diffusion models can generate unsafe imagery even from prompts that appear benign. Retraining a model for every safety policy is expensive and inflexible, so this project studied an inference-time alternative: apply classifier-energy guidance during denoising by scoring the Tweedie estimate of the clean image and backpropagating a safety gradient into the latent update.

The method exposes a tunable safety knob. Increasing the guidance strength lowers unsafe rate, but it also reduces prompt alignment, worsens FID, and increases runtime. The main conclusion is that safety interventions should be reported as tradeoffs, not as isolated improvements.

## Method

The project used a shared DDIM sampling loop across baselines. Classifier-energy guidance formed a predicted clean image estimate at denoising steps, decoded it through the VAE, scored it with a frozen safety classifier, and applied a hinge-energy gradient to steer the latent update away from unsafe concepts.

The correction strength was controlled by a scalar `lambda`, with an adaptive schedule that increases guidance when the predicted clean image violates the safety threshold and applies guidance in a mid-to-late timestep window.

## Baselines

The evaluation compared:

- vanilla sampling,
- negative prompting,
- Safe Latent Diffusion,
- rejection sampling,
- classifier-energy guidance at multiple `lambda` values.

## Benchmark

The benchmark used 875 prompts across neutral, violence/gore, explicit, hate, self-harm/illegal, and adversarial categories. Metrics included unsafe rate, CLIP prompt alignment, FID, and wall-clock runtime.

## Results

| Method | Unsafe rate | CLIP alignment | FID | Wall-clock |
|---|---:|---:|---:|---:|
| Vanilla | 0.097 | 0.256 | 129.0 | 0.95s |
| Negative prompt | 0.035 | 0.236 | 129.8 | 0.95s |
| CE lambda=80 | 0.039 | 0.225 | 142.9 | 3.11s |
| CE lambda=160 | 0.027 | 0.206 | 176.4 | 3.05s |

Classifier-energy guidance reached the strictest safety point in the reported comparison. Negative prompting remained the strongest low-cost baseline for moderate safety targets.

## Cross-Evaluator Check

For explicit-content prompts, an architecturally disjoint NudeNet evaluator agreed with the CLIP-based ranking. This reduced the chance that the result was only an artifact of using CLIP for both guidance and evaluation.

## Limitations

- The safety-quality tradeoff is real; stricter guidance reduces unsafe rate but hurts quality and alignment.
- Hate-symbol and context-dependent safety categories remained difficult.
- The adversarial prompt split was small.
- FID used a small neutral reference subset, so relative ordering is more reliable than absolute values.
- The study used one seed per prompt/method pair.

## Contribution

This was a collaborative project by Boyu Yang, Luojia Xia, William Zhang, and Vincent Lin. William Zhang focused on empirical results analysis, limitations/future-work writing, report polish, slide contribution, and recorded presentation participation.

The full collaborative implementation is linked from the repository README.
