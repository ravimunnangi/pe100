import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def log1():
    logger.info(f'Log from loging1.py')