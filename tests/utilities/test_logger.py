"""Test logger."""

import logging
from pathlib import Path
from typing import Any
from unittest.mock import MagicMock

from utilities.log.logger import log_full_width, print_header, setup_logging

log = logging.getLogger("pyskel")


def test_logger_file(tmp_path: Path):
    """Test logging to log file.

    Args:
        tmp_path (Path): Temporary path from pytest.
    """
    config = MagicMock()
    config.general_config.log_file = "test.log"
    config.general_config.log_to_console = False
    config.general_config.output_directory = tmp_path

    setup_logging(config)
    log.info("This is a test log message.")

    log_file = tmp_path / "test.log"
    assert log_file.exists()

    with open(log_file, "r") as f:
        log_content = f.read()
        assert "This is a test log message." in log_content


def test_logger_console(tmp_path: Path, caplog: Any):
    """Test logging to console.

    Args:
        tmp_path (Path): Temporary path from pytest.
        caplog (Any): Log capture from terminal output.
    """
    config = MagicMock()
    config.general_config.log_file = None
    config.general_config.log_to_console = True
    config.general_config.output_directory = tmp_path

    setup_logging(config)

    log.propagate = True

    with caplog.at_level(logging.DEBUG, logger="pyskel"):
        log.info("This is a test log message.")

    assert "This is a test log message." in caplog.text


def test_logger_print_header(tmp_path: Path):
    """Test logging header print.

    Args:
        tmp_path (Path): Temporary path from pytest.
    """
    config = MagicMock()
    config.general_config.log_file = "test.log"
    config.general_config.log_to_console = False
    config.general_config.output_directory = tmp_path

    setup_logging(config)
    print_header()
    log.info("This is a test log message.")

    log_file = tmp_path / "test.log"
    assert log_file.exists()

    with open(log_file, "r") as f:
        log_content = f.read()
        assert (
            "____        _____ __        __" in log_content
        )  # exemplary line in log
        assert "General Python Skeleton" in log_content


def test_logger_log_full_width(tmp_path: Path):
    """Test logging full width log.

    Args:
        tmp_path (Path): Temporary path from pytest.
    """
    config = MagicMock()
    config.general_config.log_file = "test.log"
    config.general_config.log_to_console = False
    config.general_config.output_directory = tmp_path

    setup_logging(config)
    log_full_width("THIS IS A TEST")
    log_full_width()

    log_file = tmp_path / "test.log"
    assert log_file.exists()

    with open(log_file, "r") as f:
        log_content = f.read()
        assert (
            "====================== THIS IS A TEST ======================"
            in log_content
        )
        assert (
            "============================================================"
            in log_content
        )
