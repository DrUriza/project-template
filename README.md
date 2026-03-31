# project_template

Base project template for robotics, automation, trading, sensor, or micro-doppler systems.

## Architecture

- `input`: acquisition and loading
- `processing`: ETL, cleaning, normalization, fusion
- `math`: local project math that is not part of the shared library
- `features`: feature extraction
- `models`: scoring, ML, inference
- `decision`: business rules or control logic
- `output`: serialization, reports, signals
- `hmi`: visualization or user interface
- `main`: pipeline orchestration

## Repository structure

```text
project-template/
├── src/project_template/
│   ├── main/
│   ├── input/
│   ├── processing/
│   ├── math/
│   ├── features/
│   ├── models/
│   ├── decision/
│   ├── output/
│   └── hmi/
├── tests/
├── scripts/
├── pyproject.toml
└── README.md