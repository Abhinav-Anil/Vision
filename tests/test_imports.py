import ast
from pathlib import Path


def test_modules_define_main():
    base = Path(__file__).resolve().parent.parent
    files = ["illusion.py", "vision_bounding.py", "vision_video.py"]
    for f in files:
        source = (base / f).read_text(encoding="utf8")
        tree = ast.parse(source)
        found = any(
            isinstance(node, ast.FunctionDef) and node.name == "main"
            for node in tree.body
        )
        assert found, f"{f} must define a top-level main() function"
