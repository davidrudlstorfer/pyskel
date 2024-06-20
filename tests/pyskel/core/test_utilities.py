"""Test utilities."""

from unittest.mock import MagicMock, patch

from pyskel.core.utilities import RunManager


def test_run_manager_init_run():
    """Test run manager init_run function."""
    # Mock config
    mock_config = MagicMock()

    # Mock setup_logging, log_full_width, and logging.getLogger
    with (
        patch("pyskel.core.utilities.setup_logging") as mock_setup_logging,
        patch("pyskel.core.utilities.log_full_width") as mock_log_full_width,
        patch("pyskel.core.utilities.print_header") as mock_print_header,
    ):
        # Create an instance of RunManager
        run_manager = RunManager(mock_config)

        # Call init_run method
        run_manager.init_run()

        # Assertions
        mock_setup_logging.assert_called_once_with(mock_config)
        mock_print_header.assert_called_once()
        mock_log_full_width.assert_called_once_with("RUN STARTED")


def test_run_manager_finish_run():
    """Test run manager finish_run function."""
    # Mock config
    mock_config = MagicMock()

    # Mock log_full_width, logging handlers, and logging.getLogger
    with (
        patch("pyskel.core.utilities.log_full_width") as mock_log_full_width,
        patch("pyskel.core.utilities.log") as mock_log,
    ):

        # Create an instance of RunManager
        run_manager = RunManager(mock_config)

        # Call finish_run method
        run_manager.finish_run()

        # Assertions
        mock_log_full_width.assert_called_with("RUN FINISHED")
        mock_log.info.assert_called_once()
