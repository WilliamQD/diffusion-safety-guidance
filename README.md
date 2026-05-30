# Inference-Time Safety Guidance for Diffusion Models

Curated portfolio version of a collaborative Yale deep learning final project on safety-quality tradeoffs in text-to-image diffusion sampling.

![Diffusion](https://img.shields.io/badge/Diffusion-safety_eval-blue)
![Pareto](https://img.shields.io/badge/Pareto-tradeoff_analysis-purple)
![PyTorch](https://img.shields.io/badge/PyTorch-research_stack-orange)
![Public safe](https://img.shields.io/badge/Public--safe-no_image_outputs-green)

Project context: Yale course final project | CPSC 5420 | Curated public showcase

This repository is a display-first summary of the project. It does not duplicate unsafe image galleries, large generation outputs, raw prompt dumps, model weights, or private course artifacts. The full collaborative implementation is linked below.

**Read the deliverables:** [Report](REPORT.md) | [Presentation](PRESENTATION.md)

## At a Glance

<table>
  <tr>
    <td><strong>Research question</strong><br>Can inference-time guidance reduce unsafe generations without retraining?</td>
    <td><strong>Evaluation lens</strong><br>Safety is measured as a tradeoff against CLIP alignment, FID, and runtime.</td>
    <td><strong>Public boundary</strong><br>No generated image galleries, prompt dumps, model weights, or unsafe examples.</td>
  </tr>
</table>

## Overview

The project studied whether inference-time classifier guidance can reduce unsafe generations from Stable Diffusion without retraining the model. The method evaluates a frozen safety classifier on the Tweedie estimate of the predicted clean image at each denoising step, then applies a classifier-energy gradient to steer the latent update.

The key design goal was not to claim a free safety improvement. We evaluated safety as a Pareto tradeoff against prompt alignment, FID, and runtime.

## Full Collaborative Implementation

Full group repository:

https://github.com/Severus-Yang0/Inference-time-safety-guidance-for-diffusion-models-submission

This portfolio repo focuses on William Zhang's public-facing contribution and a concise, safe-to-share summary of the method/results.

## My Contribution

This was a collaborative course project with Boyu Yang, Luojia Xia, William Zhang, and Vincent Lin.

My contribution focused on:

- leading the empirical results write-up and analysis,
- writing the conclusion, limitations, and future-work sections,
- polishing the final report,
- contributing to presentation slides,
- participating in the recorded presentation.

## Technical Approach

The experiment compared five method families under a shared DDIM sampling setup:

- vanilla sampling,
- negative prompting,
- Safe Latent Diffusion,
- rejection sampling,
- classifier-energy guidance at multiple `lambda` values.

Classifier-energy guidance used a continuous strength knob. At stronger values, it pushed the unsafe rate lower, but at the cost of prompt alignment, FID, and runtime.

## Headline Results

Overall benchmark: 875 prompts across six hazard categories.

| Method | Unsafe rate | CLIP alignment | FID | Wall-clock |
|---|---:|---:|---:|---:|
| Vanilla | 0.097 | 0.256 | 129.0 | 0.95s |
| Negative prompt | 0.035 | 0.236 | 129.8 | 0.95s |
| CE lambda=80 | 0.039 | 0.225 | 142.9 | 3.11s |
| CE lambda=160 | 0.027 | 0.206 | 176.4 | 3.05s |

The main result: classifier-energy guidance reached the strictest safety point, while negative prompting remained the strongest low-cost baseline at moderate safety levels.

On the explicit-content stratum, an architecturally disjoint NudeNet evaluator agreed with the CLIP-based ranking. CE lambda=160 had the lowest strict-explicit unsafe rate in that check.

## Public Code Included Here

This repo includes small, safe utility code for the adaptive guidance schedule and Pareto table handling:

```text
REPORT.md
PRESENTATION.md
src/diffusion_safety/
  schedule.py       # adaptive guidance strength function
  pareto.py         # identify non-dominated safety-quality points
tests/
  test_diffusion_safety.py
docs/
  method_summary.md
  results_summary.md
  privacy.md
  contribution_note.md
```

It intentionally does not include image generations, prompt CSVs, or model outputs.

## Run the Public Checks

```bash
python -m unittest discover -s tests
```

## Skills Demonstrated

- Deep learning research communication
- Diffusion-model safety evaluation
- Pareto tradeoff analysis
- Cross-evaluator validation
- Limitations-aware technical writing
- Collaborative report polish and empirical result synthesis
