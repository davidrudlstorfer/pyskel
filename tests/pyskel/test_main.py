"""Test main."""

from pathlib import Path
from unittest.mock import MagicMock, mock_open, patch

import pytest
import yaml
from munch import munchify
from pyskel.main import main


def test_main_config_file_exists(tmp_path: Path) -> None:
    """Test main when config exists.

    Args:
        tmp_path (Path): Temporary path from pytest.
    """

    mock_config_data = {"key": "value"}
    config_file_path = tmp_path / "test_config.yaml"
    with open(config_file_path, "w") as f:
        yaml.dump(mock_config_data, f)

    with patch(
        "argparse.ArgumentParser.parse_args",
        return_value=MagicMock(config_file_path=config_file_path),
    ):
        with patch(
            "builtins.open", mock_open(read_data=yaml.dump(mock_config_data))
        ):
            with patch("yaml.safe_load", return_value=mock_config_data):
                mock_run_pyskel = MagicMock()
                with patch("pyskel.main.run_pyskel", mock_run_pyskel):
                    # Run main function
                    main()

    captured_config = mock_run_pyskel.call_args[0][0]
    assert captured_config == munchify(mock_config_data)


def test_main_config_file_not_exists() -> None:
    """Test main when config does not exist."""

    with patch(
        "argparse.ArgumentParser.parse_args",
        return_value=MagicMock(config_file_path="nonexistent_config.yaml"),
    ):
        with pytest.raises(RuntimeError, match="Config file not found!"):
            main()
