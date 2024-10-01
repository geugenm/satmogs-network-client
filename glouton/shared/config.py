import json
import logging
import pathlib
from typing import Dict, Any


def read():
    default_config: Dict[str, Any] = {
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

    config_path: pathlib.Path = pathlib.Path(__file__).parent / "glouton" / "config.json"
    logging.info(f"Searching for config file: {config_path}")

    try:
        with open(config_path, 'r', encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"Error reading config: {e}, using embedded default: {default_config}")
        logging.warning("API requiring operations will be unavailable.")
        return default_config
