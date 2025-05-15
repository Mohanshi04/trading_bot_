# logger.py
import logging

def setup_logger():
    logger = logging.getLogger('TradingBot')
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler('logs/bot.log')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger
