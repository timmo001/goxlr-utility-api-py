"""GoXLR Utility API: Request Model."""
from dataclasses import dataclass, field
from typing import Any


@dataclass
class Request:
    """Request Model."""

    id: int | None = None
    data: str | dict[str, Any] = field(default_factory=dict)
