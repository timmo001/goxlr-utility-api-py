"""GoXLR Utility API: Request Model"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional

from . import DefaultBaseModel


@dataclass
class Request(DefaultBaseModel):
    """Request Model"""

    id: str
    method: str
    params: Dict[str, Any]
    jsonrpc: str = "2.0"
    metadata: Optional[Dict[str, Any]] = None
