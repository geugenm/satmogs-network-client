# More info here - https://docs.satnogs.org/projects/satnogs-network/en/stable/api.html
import pathlib
import urllib.request
from datetime import datetime
from pprint import pprint
from urllib.parse import urlparse, parse_qs, ParseResult

from api.client import AuthenticatedClient
from api.client.api.observations import observations_list
from api.client.models import paginated_observation_list
from satnogs_network_downloader.dump_hex_to_csv import parse_to_csv


def extract_cursor(full_url: str) -> str:
    parsed_url = urlparse(full_url)

    query_params = parse_qs(parsed_url.query)

    cursor = query_params.get('cursor', [''])[0]

    return cursor


def main():
    client = AuthenticatedClient(base_url="https://network.satnogs.org",
                                 token="")

    with client as client:
        observation: paginated_observation_list = observations_list.sync(client=client, satellite_norad_cat_id=44420,
                                                                         start=datetime(2020, 1, 1),
                                                                         end=datetime(2020, 3, 1))
        for result in observation.results:
            if result.demoddata:
                for data in result.demoddata:
                    url: ParseResult = urlparse(data.payload_demod)
                    filename = pathlib.Path(url.path).name
                    file_path = pathlib.Path.cwd() / "cache"

                    urllib.request.urlretrieve(data.payload_demod, file_path / filename)

                    parse_to_csv(file_name=filename, full_path=file_path)
                pprint(result.demoddata)

if __name__ == "__main__":
    main()