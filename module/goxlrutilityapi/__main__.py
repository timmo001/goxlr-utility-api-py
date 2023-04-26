"""GoXLR Utility API: Main"""
from __future__ import annotations

import asyncio

import typer

from ._version import __version__
from .websocket_client import WebsocketClient

app = typer.Typer()

websocket_client = WebsocketClient()


@app.command(name="get_status", short_help="Get Status of GoXLR")
def get_status() -> None:
    """Get Status of GoXLR"""
    asyncio.run(websocket_client.connect())
    response = asyncio.run(websocket_client.get_status())
    typer.secho(response.json(), fg=typer.colors.GREEN)


@app.command(name="version", short_help="Module Version")
def version() -> None:
    """Module Version"""
    typer.secho(__version__.public(), fg=typer.colors.CYAN)


if __name__ == "__main__":
    app()
