"""GoXLR Utility API: Request Model"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Optional, Union

from . import DefaultBaseModel


@dataclass
class Request(DefaultBaseModel):
    """Request Model"""

    id: Optional[int] = None
    data: Union[str, Dict[str, Any]] = field(metadata={"description": "Data"})
