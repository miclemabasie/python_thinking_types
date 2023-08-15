import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.propagate = False
logger.info("This is a helper log info message")