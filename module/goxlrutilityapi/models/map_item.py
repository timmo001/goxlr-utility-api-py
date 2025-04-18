"""GoXLR Utility API: Map Model"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional

from . import DefaultBaseModel


@dataclass
class MapItem(DefaultBaseModel):
    """GoXLR Utility API: Map Item Model"""
    name: str
    value: Any
    description: Optional[str] = None
    options: Optional[Dict[str, Any]] = None
