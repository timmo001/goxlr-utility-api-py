"""GoXLR Utility API: Main"""
from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Callable
from typing import Optional

import typer

from ._version import __version__
from .const import KEY_DATA, KEY_ID, KEY_TYPE
from .exceptions import (
    BadMessageException,
    ConnectionClosedException,
    ConnectionErrorException,
)
from .logger import setup_logger
from .models.patch import Patch
from .models.response import Response
from .models.status import Status
from .websocket_client import WebsocketClient

app = typer.Typer()

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
websocket_client = WebsocketClient()


def setup_websocket(
    callback: Optional[Callable[[Response[Patch]], Awaitable[None]]] = None
) -> bool:
    """Listen for messages on another thread"""
    try:
        loop.run_until_complete(websocket_client.connect())
        loop.create_task(
            websocket_client.listen(callback),
            name="Websocket Listener",
        )
    except (
        BadMessageException,
        ConnectionClosedException,
        ConnectionErrorException,
    ) as error:
        typer.secho(f"Error: {error}", fg=typer.colors.RED)
        loop.stop()
        return False
    return True


async def patch_callback(response: Response[Patch]) -> None:
    """Patch response callback function"""
    typer.secho(
        response.json(
            include={
                KEY_ID,
                KEY_TYPE,
                KEY_DATA,
            },
            exclude_unset=True,
        ),
        fg=typer.colors.GREEN,
    )


@app.command(name="get_status", short_help="Get Status of GoXLR")
def get_status(debug: bool = False) -> None:
    """Get Status of GoXLR"""
    if debug:
        setup_logger("DEBUG")
    if setup_websocket() is False:
        typer.secho("Failed to connect to GoXLR", fg=typer.colors.RED)
        return
    try:
        status: Status = loop.run_until_complete(websocket_client.get_status())
    except BadMessageException as error:
        typer.secho(
            f"Failed to get status from GoXLR: {error}",
            fg=typer.colors.RED,
        )
        return

    typer.secho(status.json(), fg=typer.colors.GREEN)


@app.command(
    name="listen_for_messages",
    short_help="Listen for patch messages from GoXLR",
)
def listen_for_messages(debug: bool = False) -> None:
    """Listen for patch messages from GoXLR"""
    if debug:
        setup_logger("DEBUG")
    setup_websocket(patch_callback)
    typer.secho("Listening for messages...", fg=typer.colors.GREEN)
    loop.run_forever()


@app.command(name="set_accent_color", short_help="Set Accent Color")
def set_accent_color(
    color: str = typer.Argument(..., help="Color Hex Value (RRGGBB)"),
    debug: bool = False,
) -> None:
    """Set Accent Color"""
    if debug:
        setup_logger("DEBUG")
    if setup_websocket() is False:
        typer.secho("Failed to connect to GoXLR", fg=typer.colors.RED)
        return
    try:
        loop.run_until_complete(websocket_client.get_status())
    except BadMessageException as error:
        typer.secho(
            f"Failed to get status from GoXLR: {error}",
            fg=typer.colors.RED,
        )
        return

    try:
        loop.run_until_complete(websocket_client.set_accent_color(color))
    except BadMessageException as error:
        typer.secho(
            f"Failed to set accent color: {error}",
            fg=typer.colors.RED,
        )
        return

    typer.secho(f"Accent color set to {color}", fg=typer.colors.GREEN)


@app.command(name="set_button_color", short_help="Set Button Color")
def set_button_color(
    button: str = typer.Argument(..., help="Button Name"),
    color_one: str = typer.Argument(..., help="Color 1 Hex Value (RRGGBB)"),
    color_two: str = typer.Argument(..., help="Color 2 Hex Value (RRGGBB)"),
    debug: bool = False,
) -> None:
    """Set Button Color"""
    if debug:
        setup_logger("DEBUG")
    if setup_websocket() is False:
        typer.secho("Failed to connect to GoXLR", fg=typer.colors.RED)
        return
    try:
        loop.run_until_complete(websocket_client.get_status())
    except BadMessageException as error:
        typer.secho(
            f"Failed to get status from GoXLR: {error}",
            fg=typer.colors.RED,
        )
        return

    try:
        loop.run_until_complete(
            websocket_client.set_button_color(
                button,
                color_one,
                color_two,
            )
        )
    except BadMessageException as error:
        typer.secho(
            f"Failed to set button color: {error}",
            fg=typer.colors.RED,
        )
        return

    typer.secho(
        f"{button} color set to {color_one} and {color_two}",
        fg=typer.colors.GREEN,
    )


@app.command(name="version", short_help="Module Version")
def version() -> None:
    """Module Version"""
    typer.secho(__version__.public(), fg=typer.colors.CYAN)


if __name__ == "__main__":
    app()
    loop.stop()
