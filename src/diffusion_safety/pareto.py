"""Pareto frontier helpers for safety-quality summaries."""

from __future__ import annotations

from collections.abc import Iterable, Mapping


def pareto_frontier(
    rows: Iterable[Mapping[str, float | str]],
    minimize: tuple[str, ...],
    maximize: tuple[str, ...],
) -> list[Mapping[str, float | str]]:
    """Return non-dominated rows.

    A row is dominated if another row is no worse on every metric and strictly
    better on at least one metric.
    """

    candidates = list(rows)
    frontier = []
    for row in candidates:
        dominated = False
        for other in candidates:
            if other is row:
                continue

            no_worse = all(other[m] <= row[m] for m in minimize) and all(
                other[m] >= row[m] for m in maximize
            )
            strictly_better = any(other[m] < row[m] for m in minimize) or any(
                other[m] > row[m] for m in maximize
            )
            if no_worse and strictly_better:
                dominated = True
                break

        if not dominated:
            frontier.append(row)
    return frontier
