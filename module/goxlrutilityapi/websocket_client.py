"""GoXLR Utility API: Websocket Client"""
from __future__ import annotations

import asyncio
import socket
from collections.abc import Awaitable, Callable
from typing import Any, Optional

import aiohttp

from .base import Base
from .const import KEY_DATA, KEY_ID, REQUEST_TYPE_GET_STATUS, RESPONSE_TYPE_STATUS
from .exceptions import (
    BadMessageException,
    ConnectionClosedException,
    ConnectionErrorException,
)
from .models.request import Request
from .models.response import Response


class WebsocketClient(Base):
    """Websocket Client"""

    def __init__(self) -> None:
        """Initialize Websocket Client"""
        super().__init__()
        self._current_id: int = 1
        self._responses: dict[int, tuple[asyncio.Future[Response], Optional[str]]] = {}
        self._session: Optional[aiohttp.ClientSession] = None
        self._websocket: Optional[aiohttp.ClientWebSocketResponse] = None

    @property
    def connected(self) -> bool:
        """Get connection state."""
        return self._websocket is not None and not self._websocket.closed

    async def disconnect(self) -> None:
        """Disconnect from server"""
        self._logger.info("Disconnecting from WebSocket")
        if self._websocket is not None:
            await self._websocket.close()

    async def connect(
        self,
        host: str = "localhost",
        port: int = 14564,
        session: Optional[aiohttp.ClientSession] = None,
    ) -> None:
        """Connect to server"""
        if session:
            self._session = session
        else:
            self._logger.info("Creating new aiohttp client session")
            self._session = aiohttp.ClientSession()
        url = f"ws://{host}:{port}/api/websocket"
        self._logger.info(
            "Connecting to WebSocket: %s (aiohttp: %s)",
            url,
            aiohttp.__version__,
        )
        try:
            self._websocket = await self._session.ws_connect(url=url, heartbeat=30)
        except (
            aiohttp.WSServerHandshakeError,
            aiohttp.ClientConnectionError,
            socket.gaierror,
        ) as error:
            self._logger.warning(
                "Failed to connect to WebSocket: %s - %s",
                error.__class__.__name__,
                error,
            )
            raise ConnectionErrorException from error
        self._logger.info("Connected to WebSocket")

    async def _send_message(
        self,
        request,
        wait_for_response: bool = True,
        response_type: Optional[str] = None,
    ) -> Response:
        """Send a message to the WebSocket"""
        if not self.connected or self._websocket is None:
            raise ConnectionClosedException("Connection is closed")

        self._current_id += 1
        request.id = self._current_id

        future: asyncio.Future[Response] = asyncio.get_running_loop().create_future()
        self._responses[request.id] = future, response_type
        await self._websocket.send_str(request.json())
        self._logger.debug("Sent message: %s", request.json())
        if wait_for_response:
            try:
                return await future
            finally:
                self._responses.pop(request.id)
        return Response(
            id=request.id,
            data=None,
        )

    async def get_status(self) -> Response:
        """Get status from GoXLR"""
        self._logger.info("Getting status from GoXLR")
        return await self._send_message(
            Request(data=REQUEST_TYPE_GET_STATUS),
            wait_for_response=True,
            response_type=RESPONSE_TYPE_STATUS,
        )

    async def listen(
        self,
        callback: Optional[Callable[[str, Any], Awaitable[None]]] = None,
    ) -> None:
        """Listen for messages and map to modules"""

        async def _callback_message(message: dict) -> None:
            """Message Callback"""
            self._logger.debug("New message: %s", message[KEY_ID])

            # Get first object in message
            message_type = message[KEY_DATA].popitem()[0]
            self._logger.info("Message type: %s", message_type)

            # if message.get(KEY_ID) is not None:
            #     response_tuple = self._responses.get(message[KEY_ID])
            #     if response_tuple is not None:
            #         future, response_type = response_tuple
            #         if (
            #             response_type is not None
            #             and response_type != message[EVENT_TYPE]
            #         ):
            #             self._logger.info(
            #                 "Response type '%s' does not match requested type '%s'.",
            #                 message[EVENT_TYPE],
            #                 response_type,
            #             )
            #         else:
            #             response = Response(**message)

            #             if (
            #                 response.type == TYPE_DATA_UPDATE
            #                 and response.module is not None
            #                 and message[EVENT_DATA] is not None
            #             ):
            #                 # Find model from module
            #                 model = MODEL_MAP.get(message[EVENT_MODULE])
            #                 if model is None:
            #                     self._logger.warning(
            #                         "Unknown model: %s", message[EVENT_MODULE]
            #                     )
            #                 else:
            #                     response.data = model(**message[EVENT_DATA])

            #             self._logger.info(
            #                 "Response: %s",
            #                 response.json(
            #                     include={
            #                         EVENT_ID,
            #                         EVENT_TYPE,
            #                         EVENT_SUBTYPE,
            #                         EVENT_MESSAGE,
            #                     },
            #                     exclude_unset=True,
            #                 ),
            #             )

            #             try:
            #                 future.set_result(response)
            #             except asyncio.InvalidStateError:
            #                 self._logger.debug(
            #                     "Future already set for response ID: %s",
            #                     message[EVENT_ID],
            #                 )

            # if message[EVENT_TYPE] == TYPE_ERROR:
            #     if message[EVENT_SUBTYPE] == SUBTYPE_LISTENER_ALREADY_REGISTERED:
            #         self._logger.debug(message)
            #     else:
            #         self._logger.warning("Error message: %s", message)
            # elif (
            #     message[EVENT_TYPE] == TYPE_DATA_UPDATE
            #     and message[EVENT_MODULE] is not None
            #     and message[EVENT_DATA] is not None
            # ):
            #     self._logger.debug(
            #         "New data for: %s\n%s", message[EVENT_MODULE], message[EVENT_DATA]
            #     )
            #     model = MODEL_MAP.get(message[EVENT_MODULE])
            #     if model is None:
            #         self._logger.warning("Unknown model: %s", message[EVENT_MODULE])
            #     else:
            #         if callback is not None:
            #             await callback(
            #                 message[EVENT_MODULE],
            #                 model(**message[EVENT_DATA]),
            #             )

        await self.listen_for_messages(callback=_callback_message)

    async def listen_for_messages(
        self,
        callback: Callable[[dict[Any, Any]], Awaitable[None]],
    ) -> None:
        """Listen for messages"""
        if not self.connected:
            raise ConnectionClosedException("Connection is closed")

        self._logger.info("Listen for messages")
        if self._websocket is not None:
            while not self._websocket.closed:
                message = await self.receive_message()
                if isinstance(message, dict):
                    await callback(message)

    async def receive_message(self) -> Optional[dict]:
        """Receive message"""
        if not self.connected or self._websocket is None:
            raise ConnectionClosedException("Connection is closed")

        try:
            message = await self._websocket.receive()
        except RuntimeError:
            return None

        if message.type == aiohttp.WSMsgType.ERROR:
            raise ConnectionErrorException(self._websocket.exception())

        if message.type in (
            aiohttp.WSMsgType.CLOSE,
            aiohttp.WSMsgType.CLOSED,
            aiohttp.WSMsgType.CLOSING,
        ):
            raise ConnectionClosedException("Connection closed to server")

        if message.type == aiohttp.WSMsgType.TEXT:
            message_json = message.json()

            return message_json

        raise BadMessageException(f"Unknown message type: {message.type}")
