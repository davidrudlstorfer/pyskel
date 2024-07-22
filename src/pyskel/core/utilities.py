"""Utilities for PySkel main routine."""

import logging
import os
import time

import yaml
from pytoda.logger import log_full_width, print_header, setup_logging

log = logging.getLogger("pyskel")


class RunManager:
    """Helper functions to manage a PySkel run."""

    def __init__(self, config):

        self.config = config

    def init_run(self) -> None:
        """Set up PySkel run including logger."""

        setup_logging(
            self.config.general.log_to_console,
            self.config.general.log_file,
            self.config.general.output_directory,
            self.config.general.sim_name,
            "pyskel",
        )

        print_header(
            title="PySkel",
            description="General Python Skeleton",
        )

        log_full_width("RUN STARTED")

        self.write_config()

    def write_config(self) -> None:
        """Export and write current setup config to .yaml file for future
        reference."""

        log.info("Writing input config to file ...")
        log.info("")

        # create output folder structure
        if (
            self.config.general.output_directory is None
            or self.config.general.sim_name is None
        ):
            raise ValueError(
                "Output directory and sim name must be provided for output!"
            )
        os.makedirs(
            os.path.join(
                self.config.general.output_directory,
                self.config.general.sim_name,
            ),
            exist_ok=True,
        )

        with open(
            os.path.join(
                self.config.general.output_directory,
                self.config.general.sim_name,
                "config.yaml",
            ),
            "w",
        ) as file:
            yaml.dump(self.config.toDict(), file)

        log.info("     ... done.")
        log.info("")

    def finish_run(self, start_time: float) -> None:
        """Finish run and close all loggers (Important if module is used within
        other modules including a Python Logger!)"""

        log_full_width()
        log.info(f"Run took {time.time() - start_time} s.")
        log_full_width("RUN FINISHED")

        # close logger handlers (file)
        handlers = log.handlers[:]
        for handler in handlers:
            log.removeHandler(handler)
            handler.close()
