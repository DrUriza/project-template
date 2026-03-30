from __future__ import annotations

def score_features(features: dict) -> float:
    return float(features.get("fft_peak", 0.0) + 0.1 * features.get("mean_abs_delta", 0.0))
