import logging
from datetime import datetime

from sat_nogs_db_client import AuthenticatedClient

client = AuthenticatedClient(base_url="https://db.satnogs.org", token="")

from sat_nogs_db_client.models import telemetry_list_format
from sat_nogs_db_client.api.telemetry import telemetry_list

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

with client as client:
    my_data: telemetry_list_format = telemetry_list.sync(client=client, is_decoded=True, satellite="44420", start=datetime(2020, 1, 1), end=datetime(2020, 1, 3))

    print(my_data)