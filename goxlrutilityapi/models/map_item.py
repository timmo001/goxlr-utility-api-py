"""GoXLR Utility API: Map Model."""
from dataclasses import dataclass


@dataclass
class MapItem:
    """MapItem Model."""

    key: str
    name: str
    icon: str
