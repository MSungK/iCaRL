import logging
from os import makedirs

def setup_logger():
    makedirs('logs', exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s",
        handlers=[logging.StreamHandler(), logging.FileHandler('./logs/debug.log')])