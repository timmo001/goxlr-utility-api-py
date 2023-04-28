"""GoXLR Utility API: Constants"""

from .models.patch import Patch
from .models.request import Request
from .models.response import Response
from .models.status import Status

# Logging
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
FORMAT = "%(asctime)s %(levelname)s (%(threadName)s) [%(name)s] %(message)s"

# API
KEY_DATA = "data"
KEY_ID = "id"
KEY_TYPE = "type"
REQUEST_TYPE_GET_STATUS = "GetStatus"
RESPONSE_TYPE_PATCH = "Patch"
RESPONSE_TYPE_STATUS = "Status"

# Models
MODEL_PATCH = Patch
MODEL_REQUEST = Request
MODEL_RESPONSE = Response
MODEL_STATUS = Status

MODEL_MAP = {
    RESPONSE_TYPE_PATCH: MODEL_PATCH,
    RESPONSE_TYPE_STATUS: MODEL_STATUS,
}
