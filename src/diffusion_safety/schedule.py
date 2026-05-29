"""Adaptive guidance schedule used in the project write-up."""

from __future__ import annotations

import math


def adaptive_lambda(
    base_lambda: float,
    max_unsafe_score: float,
    threshold: float,
    timestep: int,
    active_window: tuple[int, int] = (15, 40),
    beta: float = 20.0,
) -> float:
    """Compute an adaptive classifier-energy guidance strength.

    Guidance is active only inside ``active_window`` and increases smoothly as
    the unsafe score exceeds the evaluation threshold.
    """

    start, end = active_window
    if timestep < start or timestep > end:
        return 0.0

    margin = max_unsafe_score - threshold
    sigmoid = 1.0 / (1.0 + math.exp(-beta * margin))
    return base_lambda * sigmoid
