import logging


def testfunction(var1,var2):
    logger = logging.getLogger("logger1.logger2.testfunction")
    logger.info("added %s and %s to get %s" % (var1, var2, var1+var2))
    return var1+var2