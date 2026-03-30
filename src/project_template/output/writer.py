from __future__ import annotations

def build_output(signal, features, score, label):
    return {
        "n_samples": len(signal),
        "features": features,
        "score": score,
        "label": label,
    }
