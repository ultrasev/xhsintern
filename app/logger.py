from loguru import logger

logger.add("/tmp/xhsintern.log", rotation="100kb", retention="10 days")
