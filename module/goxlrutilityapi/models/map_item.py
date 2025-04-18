"""GoXLR Utility API: Map Model"""
from __future__ import annotations

from dataclasses import dataclass

from . import DefaultBaseModel


@dataclass
class MapItem(DefaultBaseModel):
    """MapItem Model"""

    key: str
    name: str
    icon: str
