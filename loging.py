import logging
from pathlib import Path
import loging1

logger = logging.getLogger(__name__)

logFilePath='/Users/ravimunnangi/Documents/python/pe100/log.txt'

print(type(logFilePath))
print(logFilePath)

logging.basicConfig(
    format=f'%(asctime)s ({Path(__file__).parent.name}) - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO,
    handlers=[ logging.FileHandler(logFilePath), logging.StreamHandler() ]
)

logger.info(f'Program execution started')
try:
    num = 1
    den = 0
    if den == 0:
        logging.critical(f'Division by zero')
    print(num/den)
except Exception as e:
    logging.exception(e)

loging1.log1()