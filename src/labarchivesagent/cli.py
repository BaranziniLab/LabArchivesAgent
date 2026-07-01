"""Command-line entry point for LabArchivesAgent."""

import logging
import os

from labarchivesagent.server import main as server_main

logger = logging.getLogger("LabArchivesAgent")


def main() -> None:
    log_level = os.getenv("LABARCHIVES_LOG_LEVEL", "INFO")
    logging.basicConfig(level=getattr(logging, log_level.upper(), logging.INFO))
    logger.info("Starting LabArchivesAgent")
    server_main(log_level=log_level)


if __name__ == "__main__":
    main()
