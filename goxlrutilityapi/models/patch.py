"""GoXLR Utility API: Patch Models."""
from dataclasses import dataclass
from typing import Any


@dataclass
class Patch:
    """Patch Model."""

    op: str
    path: str
    value: Any


@dataclass
class Data:
    """Data Model."""

    patch: list[Patch] = Field(..., alias="Patch")
