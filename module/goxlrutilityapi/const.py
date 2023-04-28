"""GoXLR Utility API: Constants"""

from typing import Any, Final, Type

from .models import DefaultBaseModel
from .models.patch import Patch
from .models.request import Request
from .models.response import Response
from .models.status import Status

# General
DEFAULT_HOST: Final[str] = "localhost"
DEFAULT_PORT: Final[int] = 14564

# API
KEY_DATA: Final[str] = "data"
KEY_ID: Final[str] = "id"
KEY_TYPE: Final[str] = "type"
REQUEST_TYPE_GET_STATUS: Final[str] = "GetStatus"
RESPONSE_TYPE_PATCH: Final[str] = "Patch"
RESPONSE_TYPE_STATUS: Final[str] = "Status"

# Models
MODEL_PATCH: Type[Patch] = Patch
MODEL_REQUEST: Type[Request] = Request
MODEL_RESPONSE: Type[Response[Any]] = Response
MODEL_STATUS: Type[Status] = Status

MODEL_MAP: Final[dict[str, Type[DefaultBaseModel]]] = {
    RESPONSE_TYPE_PATCH: MODEL_PATCH,
    RESPONSE_TYPE_STATUS: MODEL_STATUS,
}
