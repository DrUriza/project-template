from __future__ import annotations

def mean(values):
    if not values:
        raise ValueError("values cannot be empty")
    return sum(values) / len(values)
