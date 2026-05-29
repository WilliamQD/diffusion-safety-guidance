# Method Summary

The project evaluated an inference-time safety intervention for text-to-image diffusion models.

## Classifier-Energy Guidance

At each denoising step, the sampler forms a Tweedie estimate of the clean image, decodes it, scores it with a frozen safety classifier, and backpropagates a hinge-energy gradient into the latent update.

The correction strength is controlled by a scalar `lambda`, making the method tunable at inference time.

## Adaptive Schedule

The adaptive schedule increases guidance when the predicted clean image violates the safety threshold and applies the correction only inside a selected timestep window.

This is useful because early denoising steps are noisy and late steps may leave too little room for meaningful correction.

## Baselines

The method was compared against:

- vanilla DDIM sampling,
- negative prompting,
- Safe Latent Diffusion,
- rejection sampling.

All methods were evaluated under a shared sampling loop to keep the comparison focused on the intervention rather than incidental implementation differences.
