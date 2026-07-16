"""
Logging configuration.

Provides a single logger instance for the entire application.
"""

from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler

from rag.config import Config

_LOGGER_INITIALIZED = False


def setup_logging() -> None:
    """
    Configure application logging.

    This function is idempotent and safe to call multiple times.
    """

    global _LOGGER_INITIALIZED

    if _LOGGER_INITIALIZED:
        return

    Config.LOG_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    formatter = logging.Formatter(
        fmt=(
            "%(asctime)s | "
            "%(levelname)-8s | "
            "%(name)s | "
            "%(message)s"
        ),
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    root_logger = logging.getLogger()

    root_logger.setLevel(
        getattr(
            logging,
            Config.LOG_LEVEL.upper(),
        )
    )

    # ----------------------------------------------------------
    # Console
    # ----------------------------------------------------------

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(
        formatter
    )

    # ----------------------------------------------------------
    # File
    # ----------------------------------------------------------

    file_handler = RotatingFileHandler(
        filename=Config.LOG_FILE,
        maxBytes=5 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8",
    )

    file_handler.setFormatter(
        formatter
    )

    # Prevent duplicate handlers
    if not root_logger.handlers:
        root_logger.addHandler(
            console_handler
        )
        root_logger.addHandler(
            file_handler
        )

    # Silence noisy libraries
    logging.getLogger(
        "httpx"
    ).setLevel(logging.WARNING)

    logging.getLogger(
        "openai"
    ).setLevel(logging.WARNING)

    logging.getLogger(
        "chromadb"
    ).setLevel(logging.WARNING)

    logging.getLogger(
        "bs4"
    ).setLevel(logging.WARNING)

    _LOGGER_INITIALIZED = True


def get_logger(
    name: str,
) -> logging.Logger:
    """
    Return a configured logger.
    """

    setup_logging()

    return logging.getLogger(name)
