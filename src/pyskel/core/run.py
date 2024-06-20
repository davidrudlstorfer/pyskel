"""Runner which executes the main routine of PySkel."""

import logging
from typing import Any

from pyskel.core.example import exemplary_function
from pyskel.core.utilities import RunManager

log = logging.getLogger("pyskel")


def run_pyskel(config: Any) -> None:
    """General run procedure of PySkel.

    Args:
        config (Any): Munch type object containing all configs for current
        run. Config options can be called via attribute-style access.
    """

    run_manager = RunManager(config)
    run_manager.init_run()

    # add overall execution here
    log.info("Output of exemplary program: " + str(exemplary_function(2, 4)))

    run_manager.finish_run()
