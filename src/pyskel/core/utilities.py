"""Utilities for PySkel main routine."""

import logging
import time

from utilities.log.logger import log_full_width, print_header, setup_logging

log = logging.getLogger("pyskel")


class RunManager:
    """Helper functions to manage a PySkel run."""

    def __init__(self, config):

        self.start_time = time.time()
        self.config = config

    def init_run(self):
        """Set up PySkel run including logger."""
        setup_logging(self.config)
        print_header()
        log_full_width("RUN STARTED")

    def finish_run(self):
        """Finish run and close all loggers (Important if module is used within
        other modules including a Python Logger!)"""

        log_full_width()
        log.info(f"Run took {time.time() - self.start_time} s.")
        log_full_width("RUN FINISHED")

        # close logger handlers (file)
        handlers = log.handlers[:]
        for handler in handlers:
            log.removeHandler(handler)
            handler.close()
