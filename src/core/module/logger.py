import logging
from pathlib import Path
from datetime import datetime
import os

DEFAULT_LOG_FORMAT = "%(asctime)s : %(levelname)s : %(process)d --- [%(name)s] : %(message)s"
DEFAULT_LOG_LEVEL = logging.DEBUG

BASE_PATH = Path(os.getcwd())
LOG_FOLDER_PATH: Path = BASE_PATH / "src" / "data" / "logs"
# LOG_NAME_FORMAT = LOG_FOLDER_PATH / f"{name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
LOG_PATH = LOG_FOLDER_PATH / "app.log"

class AppLogger:
    def __init__(self, name, log_to_console=False, log_to_file=True, level=DEFAULT_LOG_LEVEL, format=DEFAULT_LOG_FORMAT):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.log_to_console = log_to_console
        self.log_to_file = log_to_file
        self.format = format

        # Formatter
        formatter = logging.Formatter(format)

        # File Handler
        if log_to_file:
            LOG_FOLDER_PATH.mkdir(parents=True, exist_ok=True)  # Create logs directory if it doesn't exist
            file_handler = logging.FileHandler(LOG_PATH)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

        # Console Handler
        if log_to_console:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

    def __getattr__(self, attr):
        return getattr(self.logger, attr)

    def getLogger(self) -> logging.Logger:
        return self.logger