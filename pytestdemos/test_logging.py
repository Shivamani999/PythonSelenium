import logging

def test_loggingdemo():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler("logfile.log")
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    logger.setLevel(logging.DEBUG)
    logger.debug("A Debug statement")
    logger.info("A Info logger")
    logger.warning("A warning logger")
    logger.error("A error logger")
    logger.critical("A critical error logger")
