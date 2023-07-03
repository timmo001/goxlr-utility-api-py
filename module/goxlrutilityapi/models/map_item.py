"""GoXLR Utility API: Map Model"""
from __future__ import annotations

from typing import Optional

from pydantic import Field

from . import DefaultBaseModel


class MapItem(DefaultBaseModel):
    """MapItem Model"""

    key: str
    name: str
    icon: str
