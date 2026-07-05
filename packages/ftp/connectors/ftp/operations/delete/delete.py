"""FTP connector — Delete operation."""
from __future__ import annotations

from typing import NotRequired, TypedDict

from aurora_engine.connector_helper import get_connector_config
from aurora_engine.service_types import ServiceContext

from connectors.ftp.client import DeleteResult, delete


class DeleteInput(TypedDict):
    """Flow input of ``common.connectors.ftp.delete`` (see delete.yml)."""

    ftp_alias: str
    remote_path: str
    ignore_missing: NotRequired[bool]


def run(input: DeleteInput, context: ServiceContext) -> DeleteResult:
    config = get_connector_config("ftp", input["ftp_alias"])
    return delete(
        config,
        remote_path=input["remote_path"],
        ignore_missing=bool(input.get("ignore_missing")),
    )
