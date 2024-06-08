"""GoXLR Utility API: Response Model."""
from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class Response(Generic[T]):
    """Response Model."""

    id: int | None = None
    type: str | None = None
    data: T | None = None
