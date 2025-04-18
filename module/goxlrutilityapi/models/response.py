"""GoXLR Utility API: Response Model"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Generic, Optional, TypeVar

from . import DefaultBaseModel

T = TypeVar("T")


@dataclass
class Response(DefaultBaseModel, Generic[T]):
    """Response Model"""

    id: Optional[int] = field(default=None, metadata={"description": "Message ID"})
    type: Optional[str] = field(
        default=None, metadata={"description": "Type of Response"}
    )
    data: T = field(default=None, metadata={"description": "Data"})
