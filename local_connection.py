"""Minimal local repository connection using SQLite."""

from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Iterable


def connect_local_repository(db_path: str = "data/local_repository.db") -> sqlite3.Connection:
    """Create/connect to a local SQLite repository database."""
    path = Path(db_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path)
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS repository_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
        """
    )
    connection.commit()
    return connection


def add_repository_item(connection: sqlite3.Connection, name: str) -> None:
    """Add a single item to the local repository table."""
    connection.execute("INSERT OR IGNORE INTO repository_items(name) VALUES (?)", (name,))
    connection.commit()


def list_repository_items(connection: sqlite3.Connection) -> Iterable[str]:
    """Read all items currently stored in the local repository table."""
    rows = connection.execute("SELECT name FROM repository_items ORDER BY id").fetchall()
    return [row[0] for row in rows]

