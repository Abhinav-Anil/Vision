"""Helper runner to start demos from the repository root.

Usage: python run_demo.py --script illusion
Valid scripts: illusion, vision_bounding, vision_video
"""

import argparse
import importlib.util
from pathlib import Path


def import_and_run(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if hasattr(mod, "main"):
        mod.main()
    else:
        print(f"{path.name} has no main() to run.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--script",
        choices=["illusion", "vision_bounding", "vision_video"],
        required=True,
    )
    args = parser.parse_args()

    base = Path(__file__).resolve().parent
    mapping = {
        "illusion": base / "illusion.py",
        "vision_bounding": base / "vision_bounding.py",
        "vision_video": base / "vision_video.py",
    }
    import_and_run(mapping[args.script])


if __name__ == "__main__":
    main()
