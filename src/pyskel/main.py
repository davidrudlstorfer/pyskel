"""Main routine of PySkel."""

import argparse
import os
import sys

import yaml
from munch import munchify

from pyskel.core.run import run_pyskel


def run_example() -> None:
    """Run PySkel with example config file."""

    sys.argv.extend(["--config_file_path", "src/pyskel/configs/config_example.yaml"])

    main()


def main() -> None:
    """Call PySkel runner with config.

    Raises:
        RuntimeError: If provided config is not a valid file.
    """
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument(
        "--config_file_path",
        "-cfp",
        help="Path to config file.",
        type=str,
        required=True,
    )
    args = parser.parse_args()

    if not os.path.isfile(args.config_file_path):
        raise RuntimeError("Config file not found! PySkel can not be executed!")

    # load config and convert to simple namespace for easier access
    with open(args.config_file_path, "r") as file:
        config = munchify(yaml.safe_load(file))

    # execute pyskel
    run_pyskel(config)


if __name__ == "__main__":  # pragma: no cover
    main()
    exit(0)
