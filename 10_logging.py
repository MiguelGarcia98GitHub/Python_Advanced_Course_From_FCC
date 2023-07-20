# Logging: Capture stack traces and similar stuff
import logging

# By default, only levels of messages with level warning or above are printed
# But this configuration (and other things such as the output format) can be changed by changing it at the beginning, right after importing the module
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
)

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

# Create a customised logger (usually on a separate module to be imported somewhere else)
logger = logging.getLogger(
    "helper"
)  # this will create a logger with the name we provide, can also use __name__ to get the name of the file in most cases, could be for example "helper.py"
logger.info("hello from 10_logging.py")

# Lock handlers are objects responsible for dispatching the appropiate lock messages
logger = logging.getLogger("logging")
stream_h = logging.StreamHandler()
file_h = logging.FileHandler("file.log")

# level and the format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = "%(name)s - %(levelname)s - %(message)s"
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning("this is a warning")
logger.error("this is an error")

# There are also logger configurations for file config and dict config, but those are not so commonly used
