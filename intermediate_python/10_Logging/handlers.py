import logging

logger = logging.getLogger(__name__)
# Create logging handlers
file_handler = logging.FileHandler("file.log")
stream_handler = logging.StreamHandler()

# Set the format and log levels for the handlers
file_handler.level = logging.WARNING
stream_handler.level = logging.ERROR
FORMATER = logging.Formatter("%(asctime)s %(name)-5s %(levelname)-5s %(message)s")
file_handler.setFormatter(FORMATER)
stream_handler.setFormatter(FORMATER)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


logger.debug("This is a debug message")
logger.info("This is a log infor message")
logger.warning("This is a warning log message")
logger.error("This is an error log message")
logger.critical("This is a critical log message")
