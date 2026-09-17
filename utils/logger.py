import logging
from pathlib import Path


# Project root folder
PROJECT_ROOT = Path(__file__).parent.parent

# Folder where logs will be stored
LOG_DIR = PROJECT_ROOT / "reports"

# Create reports folder if it doesn't exist
LOG_DIR.mkdir(exist_ok=True)

# Log file
LOG_FILE = LOG_DIR / "automation.log"


def get_logger(name):

    logger = logging.getLogger(name)

    # Prevent adding the same handler multiple times
    if not logger.handlers:

        logger.setLevel(logging.INFO)

        # Write logs to automation.log
        file_handler = logging.FileHandler(
            LOG_FILE,
            mode="a"
        )

        # Format of each log message
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger