import logging

from glouton.shared import config

if config is not None:
    _config = config.read()
    if _config is not None:
        logging.basicConfig(filename=_config['LOGFILE'],
                            format='%(asctime)s %(levelname)s:%(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p',
                            level=logging.DEBUG)
