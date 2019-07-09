import logging

logging.basicConfig(filename="sample.log",filemode="w",level=logging.DEBUG)

logging.debug("Debug message")
logging.info("info message")
logging.warning("Warning message")
logging.error("Error message")