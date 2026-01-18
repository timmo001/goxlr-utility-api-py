#!/usr/bin/env python3
"""Increment development version in setup.py.

X.Y.Z.devN -> X.Y.Z.dev(N+1)
X.Y.Z -> X.Y.Z.dev1
"""

from __future__ import annotations

from pathlib import Path
import re


def main() -> None:
    """Increment development version in setup.py."""
    project_root = Path(__file__).resolve().parents[1]
    setup_path = project_root / "module" / "setup.py"
    contents = setup_path.read_text(encoding="utf-8")

    match = re.search(r'version="([^"]+)"', contents)
    if not match:
        raise SystemExit("version field not found in setup.py")

    version = match.group(1)
    dev_match = re.match(r"^(.+)\.dev(\d+)$", version)

    if dev_match:
        base, dev_num = dev_match.groups()
        new_version = f"{base}.dev{int(dev_num) + 1}"
    else:
        new_version = f"{version}.dev1"

    new_contents = contents.replace(
        f'version="{version}"', f'version="{new_version}"', 1
    )
    setup_path.write_text(new_contents, encoding="utf-8")
    print(f"Updated version to {new_version}")


if __name__ == "__main__":
    main()
