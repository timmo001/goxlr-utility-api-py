#!/usr/bin/env python3
"""Append a `.dev0` suffix to the package version in setup.py if not present."""

from __future__ import annotations

from pathlib import Path
import re


def main() -> None:
    """Append a `.dev0` suffix to the package version in setup.py if not present."""
    project_root = Path(__file__).resolve().parents[1]
    setup_path = project_root / "module" / "setup.py"
    contents = setup_path.read_text(encoding="utf-8")

    match = re.search(r'version="([^"]+)"', contents)
    if not match:
        raise SystemExit("version field not found in setup.py")

    version = match.group(1)
    if version.endswith(".dev0"):
        print("Already a dev version")
        return

    new_version = f"{version}.dev0"
    new_contents = contents.replace(
        f'version="{version}"', f'version="{new_version}"', 1
    )
    setup_path.write_text(new_contents, encoding="utf-8")
    print(f"Updated version to {new_version}")


if __name__ == "__main__":
    main()
