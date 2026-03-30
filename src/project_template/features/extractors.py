from __future__ import annotations

from pathlib import Path
import sys

try:
    from signal_freq_analysis.fourier import compute_fft_magnitude
    from signal_freq_analysis.wavelet import moving_window_energy
    from signal_freq_analysis.tda import sliding_window_embedding
    from signal_freq_analysis.micro_doppler import compute_md_proxy_features
except ModuleNotFoundError:
    # fallback note for first-time users
    compute_fft_magnitude = None
    moving_window_energy = None
    sliding_window_embedding = None
    compute_md_proxy_features = None

def extract_features(signal):
    features = {"length": len(signal)}
    if compute_fft_magnitude:
        freqs, mag = compute_fft_magnitude(signal, sample_rate_hz=float(len(signal)))
        features["fft_peak"] = float(max(mag))
    else:
        features["fft_peak"] = 0.0

    if moving_window_energy:
        features["wavelet_energy_len"] = int(len(moving_window_energy(signal, window_size=min(4, len(signal)))))
    else:
        features["wavelet_energy_len"] = 0

    if sliding_window_embedding:
        features["tda_rows"] = int(sliding_window_embedding(signal, dimension=3, delay=1).shape[0])
    else:
        features["tda_rows"] = 0

    if compute_md_proxy_features:
        features.update(compute_md_proxy_features(signal))
    else:
        features["mean_abs_delta"] = 0.0
        features["std_signal"] = 0.0
        features["energy"] = 0.0
    return features
