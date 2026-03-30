# project_template

Base project template for robotics, automation, trading, sensor, or micro-doppler systems.

## Architecture
- `input`: acquisition and loading
- `processing`: ETL and normalization
- `math`: local pure math functions
- `features`: feature extraction
- `models`: scoring or inference
- `decision`: final rule / classification
- `output`: serialization or actuator command formatting
- `hmi`: visualization layer when needed

## Demo
```bash
python scripts/run_demo.py
```
