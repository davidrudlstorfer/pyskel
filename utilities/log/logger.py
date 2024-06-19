"""Logging module for PySkel."""

import logging
import os
from typing import Any, Optional

import pyfiglet

log = logging.getLogger("pyskel")

TERMINAL_WIDTH = 60


def setup_logging(config: Any) -> None:
    """Setup logging files and handlers.

    Args:
        config (object): Munch type object containing all configs for current
        run. Config options can be called via attribute-style access.
    """
    # setup format for logging to file
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)-8s %(message)s",
        datefmt="%d-%m %H:%M:%S",
    )

    if config.general_config.log_file is not None:
        logging_file_path = os.path.join(
            config.general_config.output_directory,
            config.general_config.log_file,
        )
        file_handler = logging.FileHandler(logging_file_path, mode="w")
        file_handler.setFormatter(formatter)
        log.propagate = False
        log.addHandler(file_handler)
        log.setLevel(logging.DEBUG)

    if config.general_config.log_to_console:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        log.addHandler(stream_handler)
        log.setLevel(logging.DEBUG)


def print_header() -> None:
    """Print header for PySkel."""
    print_centered_multiline_block(
        pyfiglet.figlet_format("PySkel", font="slant"), TERMINAL_WIDTH
    )
    print_centered_multiline_block("General Python Skeleton", TERMINAL_WIDTH)


def print_centered_multiline_block(string: str, output_width: int) -> None:
    """Print a multiline text as a block in the center. This is a new test to
    test the docstring formatter.

    Args:
        string (str): String to be printed
        output_width (int): Terminal output width
    """
    lines = string.split("\n")
    max_line_width = max(len(line) for line in lines)
    if max_line_width % 2:
        output_width += 1
    for line in lines:
        log.info(line.ljust(max_line_width).center(output_width))


def log_full_width(text: Optional[str] = None) -> None:
    """Log full width text/headline.

    Args:
        text (Optional[str], optional): Text to be logged. Defaults to None and
        only prints new section.
    """
    if text is None:
        out_str = "=" * TERMINAL_WIDTH
    else:
        text_width = len(text)
        fill_width = int((TERMINAL_WIDTH - text_width) / 2) - 1
        out_str = "=" * fill_width + " " + text + " " + "=" * fill_width

    log.info("")
    log.info(out_str)
    log.info("")
