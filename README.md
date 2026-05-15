# Vision

[![Lint](https://github.com/OWNER/REPO/actions/workflows/python-lint.yml/badge.svg)](https://github.com/OWNER/REPO/actions/workflows/python-lint.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A small collection of simple computer-vision demos demonstrating
motion detection, bounding boxes, and basic video processing using
OpenCV, Pandas, Bokeh and NumPy.

## Features

- Motion detection with bounding boxes (`vision_bounding.py`)
- Simple motion time-logging demo (`illusion.py`)
- Basic video capture/merge example (`vision_video.py`)

## Files

- `illusion.py` — motion detection and CSV logging of movement times
- `vision_bounding.py` — bounding-box visualization and basic Bokeh graph
- `vision_video.py` — simple video capture/merge example

## Requirements

Install runtime dependencies with:

```
pip install -r requirements.txt
```

These scripts expect a working webcam available at device index 0.

## Tests

Run the test suite with:

```
pip install -r requirements-dev.txt
pytest -q
```

## Publishing

A GitHub Actions workflow template is included at `.github/workflows/publish.yml` to publish a built wheel to PyPI when a tag `v*` is pushed. To enable publishing, set the `PYPI_API_TOKEN` secret in the repository settings.

Replace `OWNER/REPO` in the badge URLs above with your GitHub repository path to enable live status badges.

## Usage

Run any demo from the repository root. Example:

```
python illusion.py
python vision_bounding.py
python vision_video.py
```

Press `q` (or as noted in the script) to stop camera capture windows.

## Contributing

Contributions are welcome — see `CONTRIBUTING.md` for details.

## License

This project is licensed under the MIT License — see `LICENSE`.


