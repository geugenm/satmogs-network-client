# More info here - https://docs.satnogs.org/projects/satnogs-network/en/stable/api.html
from datetime import datetime

from api.client import AuthenticatedClient

client = AuthenticatedClient(base_url="https://network.satnogs.org", token="")

from api.client.models import paginated_observation_list
from api.client.api.observations import observations_list

from pprint import pprint
from urllib.parse import urlparse, parse_qs

def extract_cursor(url: str) -> str:
    parsed_url = urlparse(url)

    query_params = parse_qs(parsed_url.query)

    cursor = query_params.get('cursor', [''])[0]

    return cursor

with client as client:
    observation: paginated_observation_list = observations_list.sync(client=client, satellite_norad_cat_id=44420,
                                                      start=datetime(2020, 1, 1), end=datetime(2020, 3, 1))
    pprint(observation)

    observation1: paginated_observation_list = observations_list.sync(client=client, cursor=extract_cursor(observation.next_))
    pprint(observation1)
