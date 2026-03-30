from __future__ import annotations

def basic_normalize(signal):
    if not signal:
        raise ValueError("signal cannot be empty")
    m = max(abs(x) for x in signal) or 1.0
    return [x / m for x in signal]
