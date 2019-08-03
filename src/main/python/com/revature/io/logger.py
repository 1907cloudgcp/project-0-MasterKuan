import logging

def simple_logger():
    logger = logging.getLogger("server_log")

    #default level is WARNING

    logging.basicConfig(level=logging.ERROR, filename="../error/servererrors.log")

    logger.debug("Use it for tracing")
    logger.info("Use it for informational messages")
    logger.warning("Use it for operations that may raise error")
    logger.error("Use it to notify a rasied error")
    logger.critical("Use it to notify of a critical issue (system error)")

