"""GoXLR Utility API: Helper"""
from __future__ import annotations

from typing import Optional

from .models.status import Mixer, Status


async def get_mixer_from_status(status: Status) -> Optional[Mixer]:
    """Get first mixer from status"""
    return next(iter(status.mixers.values()), None)
