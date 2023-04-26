"""GoXLR Utility API: Patch Models"""
from __future__ import annotations

from pydantic import BaseModel, Field


class Patch(BaseModel):
    op: str
    path: str
    value: int


class Data(BaseModel):
    patch: list[Patch] = Field(..., alias="Patch")
