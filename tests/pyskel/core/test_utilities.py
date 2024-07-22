"""Test utilities."""

import os
import time
from pathlib import Path
from unittest.mock import MagicMock, patch

import yaml
from munch import munchify
from pyskel.core.utilities import RunManager


def test_run_manager_init_run() -> None:
    """Test run manager init_run function."""

    mock_config = MagicMock()

    with (
        patch("pyskel.core.utilities.setup_logging") as mock_setup_logging,
        patch("pyskel.core.utilities.print_header") as mock_print_header,
        patch("pyskel.core.utilities.log_full_width") as mock_log_full_width,
        patch(
            "pyskel.core.utilities.RunManager.write_config"
        ) as mock_write_config,
    ):
        run_manager = RunManager(mock_config)

        run_manager.init_run()

        mock_setup_logging.assert_called_once_with(
            mock_config.general.log_to_console,
            mock_config.general.log_file,
            mock_config.general.output_directory,
            mock_config.general.sim_name,
            "pyskel",
        )
        mock_print_header.assert_called_once()
        mock_log_full_width.assert_called_once_with("RUN STARTED")
        mock_write_config.assert_called_once()


def test_write_config(tmp_path: Path) -> None:
    """Test write_config function.

    Args:
        tmp_path (Path): Temporary from pytest.
    """

    mock_config = munchify(
        {
            "general": {
                "output_directory": f"{tmp_path}",
                "sim_name": "sim_name",
            }
        }
    )

    run_manager = RunManager(mock_config)

    run_manager.write_config()

    with open(os.path.join(tmp_path, "sim_name", "config.yaml"), "r") as file:
        assert file.read() == yaml.dump(mock_config.toDict())

    # check invalid input parameter combination
    mock_config = munchify(
        {
            "general": {
                "output_directory": None,
                "sim_name": None,
            }
        }
    )
    run_manager = RunManager(mock_config)

    try:
        run_manager.write_config()
    except ValueError as error:
        assert str(error) == (
            "Output directory and sim name must be provided for output!"
        )


def test_run_manager_finish_run() -> None:
    """Test run manager finish_run function."""

    mock_config = MagicMock()

    with (
        patch("pyskel.core.utilities.log_full_width") as mock_log_full_width,
        patch("pyskel.core.utilities.log") as mock_log,
    ):

        run_manager = RunManager(mock_config)

        run_manager.finish_run(start_time=time.time())

        mock_log_full_width.assert_called_with("RUN FINISHED")
        mock_log.info.assert_called_once()
