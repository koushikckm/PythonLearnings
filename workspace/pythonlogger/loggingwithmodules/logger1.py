import logging
import logger2


# ----------------------------------------------------------------------
def main():
    """
    The main entry point of the application
    """
    logger = logging.getLogger("logger1")
    logger.setLevel(logging.INFO)

    # create the logging file handler
    fh = logging.FileHandler("commonlogfile.log")

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    # add handler to logger object
    logger.addHandler(fh)

    logger.info("Program started")
    result = logger2.testfunction(10, 15)
    logger.info("Done!")


if __name__ == "__main__":
    main()