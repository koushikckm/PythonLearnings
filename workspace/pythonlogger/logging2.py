import logging

logging.basicConfig(filename="logging2.log", filemode="w", level=logging.INFO)
log = logging.getLogger("ex")

try:
    raise RuntimeError
except Exception:
    log.exception("Error!")