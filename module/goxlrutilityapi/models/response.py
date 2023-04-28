"""GoXLR Utility API: Response Model"""
from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, Field  # pylint: disable=no-name-in-module


class Response(BaseModel):
    """Response Model"""

    id: Optional[int] = Field(None, description="Message ID")
    data: Optional[Any] = Field(None, description="Data")
    type: Optional[str] = Field(None, description="Type of Response")
