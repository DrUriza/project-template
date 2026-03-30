from __future__ import annotations

def decide(score: float) -> str:
    return "active_pattern" if score >= 0.2 else "quiet_pattern"
