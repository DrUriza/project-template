from __future__ import annotations

import numpy as np

from signal_freq_analysis.fourier.fft_tools import compute_fft_magnitude

def extract_features(signal):
    signal = np.asarray(signal, dtype=float)

    freqs, mags = compute_fft_magnitude(signal, sample_rate_hz=1.0)

    fft_peak = float(freqs[np.argmax(mags)]) if len(freqs) > 0 else 0.0

    features = {
        "length": int(len(signal)),
        "fft_peak": fft_peak,
        "mean_abs_delta": float(np.mean(np.abs(np.diff(signal)))) if len(signal) > 1 else 0.0,
        "std_signal": float(np.std(signal)) if len(signal) > 0 else 0.0,
        "energy": float(np.sum(signal ** 2)),
    }

    return features