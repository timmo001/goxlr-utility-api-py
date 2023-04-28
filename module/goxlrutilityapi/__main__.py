"""GoXLR Utility API: Main"""
from __future__ import annotations

import asyncio
from threading import Thread

import typer

from ._version import __version__
from .logger import setup_logger
from .models.response import Response
from .websocket_client import WebsocketClient

app = typer.Typer()


class WebsocketThread(Thread):
    """Websocket Listener Thread"""

    def __init__(self) -> None:
        """Initialize Websocket Listener Thread"""
        super().__init__()
        self._loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self._loop)
        self.websocket_client = WebsocketClient()

    def start(self) -> None:
        """Connect and start listening for messages"""
        self._loop.run_until_complete(self.websocket_client.connect())
        self._loop.create_task(
            self.websocket_client.listen(),
            name="Websocket Listener",
        )

    def stop(self) -> None:
        """Stop listening for messages"""
        self._loop.stop()

    def get_status(self) -> Response:
        """Get Status of GoXLR"""
        return self._loop.run_until_complete(self.websocket_client.get_status())


def setup_websocket() -> WebsocketThread:
    """Listen for messages on another thread"""
    websocket_thread = WebsocketThread()
    websocket_thread.start()
    return websocket_thread


@app.command(name="get_status", short_help="Get Status of GoXLR")
def get_status(debug: bool = False) -> None:
    """Get Status of GoXLR"""
    if debug:
        setup_logger("DEBUG")
    websocket_thread = setup_websocket()
    response = websocket_thread.get_status()
    websocket_thread.stop()
    typer.secho(response.json(), fg=typer.colors.GREEN)


@app.command(name="version", short_help="Module Version")
def version() -> None:
    """Module Version"""
    typer.secho(__version__.public(), fg=typer.colors.CYAN)


if __name__ == "__main__":
    app()
