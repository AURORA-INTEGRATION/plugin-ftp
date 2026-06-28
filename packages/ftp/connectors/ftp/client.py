"""Shared FTP/FTPS client for the `ftp` connector.

Each call opens a short-lived connection (FTP control sockets don't pool well).
Operation scripts (upload/download/listFiles/delete) import these helpers.
"""
from __future__ import annotations

import ftplib
from typing import Any


def _connect(config: dict[str, Any]) -> ftplib.FTP:
    host = config.get("host")
    if not host:
        raise ValueError("ftp connector: `host` is required")
    raw_port = config.get("port")
    try:
        port = int(raw_port) if raw_port not in (None, "") else 21
    except (TypeError, ValueError):
        port = 21

    ftp: ftplib.FTP = ftplib.FTP_TLS() if config.get("secure") else ftplib.FTP()
    ftp.connect(host, port, timeout=30)
    user = config.get("username")
    if user:
        ftp.login(user, config.get("password") or "")
    else:
        ftp.login()
    if isinstance(ftp, ftplib.FTP_TLS):
        ftp.prot_p()  # encrypt the data channel
    ftp.set_pasv(bool(config.get("passive", True)))
    return ftp


def test_connection(config: dict[str, Any]) -> dict[str, Any]:
    ftp = _connect(config)
    try:
        ftp.voidcmd("NOOP")
        return {"ok": True}
    finally:
        _quit(ftp)


def upload(config: dict[str, Any], local_path: str, remote_path: str) -> dict[str, Any]:
    ftp = _connect(config)
    try:
        with open(local_path, "rb") as fh:
            ftp.storbinary(f"STOR {remote_path}", fh)
        return {"success": True, "remote_path": remote_path}
    finally:
        _quit(ftp)


def download(config: dict[str, Any], remote_path: str, local_path: str) -> dict[str, Any]:
    ftp = _connect(config)
    try:
        with open(local_path, "wb") as fh:
            ftp.retrbinary(f"RETR {remote_path}", fh.write)
        return {"success": True, "local_path": local_path}
    finally:
        _quit(ftp)


def list_files(config: dict[str, Any], remote_path: str = "") -> dict[str, Any]:
    ftp = _connect(config)
    try:
        names = ftp.nlst(remote_path) if remote_path else ftp.nlst()
        return {"files": names, "count": len(names)}
    finally:
        _quit(ftp)


def delete(config: dict[str, Any], remote_path: str, ignore_missing: bool = False) -> dict[str, Any]:
    ftp = _connect(config)
    try:
        try:
            ftp.delete(remote_path)
        except ftplib.error_perm:
            if ignore_missing:
                return {"success": True, "remote_path": remote_path, "existed": False}
            raise
        return {"success": True, "remote_path": remote_path, "existed": True}
    finally:
        _quit(ftp)


def _quit(ftp: ftplib.FTP) -> None:
    try:
        ftp.quit()
    except Exception:
        try:
            ftp.close()
        except Exception:
            pass
