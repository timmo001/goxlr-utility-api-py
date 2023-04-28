from typing import Type, Union

from .models.patch import Patch
from .models.status import Status

ResponseTypes: Union[Type[Status], Type[Patch]]
