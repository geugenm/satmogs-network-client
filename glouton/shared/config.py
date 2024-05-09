import logging
import os
import sys
import json


def read():
    default_config = {
        "DEFAULT": {
            "NETWORK_API_URL": "https://network.satnogs.org/api/",
            "DB_API_URL": "https://db.satnogs.org/api/",
            "DB_API_KEY": "",
            "HTTPS_PROXY": "",
            "HTTP_PROXY": ""
        },
        "MODULES": {
            "FOR_EACH": {
                "ARCHIVE": [],
                "WATERFALL": [],
                "DEMODDATA": [],
                "FRAME": [],
                "FOR_ALL_OBSERVATION": []
            },
            "END": {
                "ARCHIVE": [],
                "WATERFALL": [],
                "DEMODDATA": [],
                "FRAME": [],
                "FOR_ALL_OBSERVATION": []
            }
        },
        "LOGFILE": "glouton.log"
    }

    config_path = os.path.join(os.path.dirname(sys.argv[0]), "glouton", "config.json")

    try:
        logging.info(f"Searching for config file: {config_path}")
        with open(config_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.info(f"config.json not found, using defaults: {default_config}")
        return default_config
    except Exception as e:
        logging.error(f"Error reading config: {e}, using default: {default_config}")
        return default_config
