"""GoXLR Utility API: Patch Models"""
from __future__ import annotations

from pydantic import BaseModel, Field  # pylint: disable=no-name-in-module


class Patch(BaseModel):
    """Patch Model"""

    op: str
    path: str
    value: int


class Data(BaseModel):
    """Data Model"""

    patch: list[Patch] = Field(..., alias="Patch")
