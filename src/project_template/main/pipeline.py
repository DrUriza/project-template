from __future__ import annotations

from project_template.input.loader import load_demo_signal
from project_template.processing.etl import basic_normalize
from project_template.features.extractors import extract_features
from project_template.models.scorer import score_features
from project_template.decision.rules import decide
from project_template.output.writer import build_output


def run_pipeline():
    signal = load_demo_signal()
    signal = basic_normalize(signal)
    features = extract_features(signal)
    score = score_features(features)
    label = decide(score)
    return build_output(signal, features, score, label)


if __name__ == "__main__":
    print(run_pipeline())