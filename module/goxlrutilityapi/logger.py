"""GoXLR Utility API: Logger"""
import logging

from .const import DATE_FORMAT, FORMAT


def setup_logger(
    log_level: str = "INFO",
) -> logging.Logger:
    """Set up logging"""

    logging.basicConfig(
        datefmt=DATE_FORMAT,
        format=FORMAT,
        level=log_level,
    )

    logger = logging.getLogger("")
    logger.setLevel(log_level)

    return logger
