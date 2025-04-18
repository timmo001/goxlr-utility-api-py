"""GoXLR Utility API: Patch Models"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, List

from . import DefaultBaseModel


@dataclass
class Patch(DefaultBaseModel):
    """Patch Model"""

    op: str
    path: str
    value: Any


@dataclass
class Data(DefaultBaseModel):
    """Data Model"""

    patch: List[Patch] = field(metadata={"alias": "Patch"})
