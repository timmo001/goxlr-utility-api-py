"""GoXLR Utility API: Response Model"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Generic, Optional, TypeVar

from . import DefaultBaseModel

T = TypeVar("T")


@dataclass
class Response(DefaultBaseModel, Generic[T]):
    """Response Model"""

    id: str
    result: Any
    jsonrpc: str = "2.0"
    error: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None
