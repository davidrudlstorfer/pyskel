"""Test run procedure."""

from unittest.mock import MagicMock, patch

from munch import munchify

from pyskel.core.run import run_pyskel


def test_run_pyskel():
    """Test run procedure of PySkel."""
    # Mock config
    mock_config = munchify({"key": "value"})
    # mock runner
    mock_run_manager = MagicMock()
    with patch("pyskel.core.run.RunManager", return_value=mock_run_manager):
        # Mock exemplary_function
        mock_exemplary_function = MagicMock(return_value="Exemplary output")
        with patch(
            "pyskel.core.run.exemplary_function", mock_exemplary_function
        ):
            # Call run_pyskel with mock configuration
            run_pyskel(mock_config)

    # Check if functions are called
    mock_run_manager.init_run.assert_called_once()
    mock_exemplary_function.assert_called_once()
    mock_run_manager.finish_run.assert_called_once()
