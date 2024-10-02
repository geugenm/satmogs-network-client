import configparser
import pathlib
import urllib.request
from datetime import datetime
from http.client import HTTPMessage
from urllib.parse import urlparse, parse_qs, ParseResult

from api.client import AuthenticatedClient
from api.client.api.observations import observations_list
from api.client.models import paginated_observation_list, Observation
from satnogs_network_client.dump_hex_to_csv import parse_to_csv


def extract_cursor(full_url: str) -> str:
    parsed_url = urlparse(full_url)
    query_params = parse_qs(parsed_url.query)
    cursor = query_params.get('cursor', [''])[0]
    return cursor


def download(observations: list[Observation], cache_dir: pathlib.Path) -> None:
    for result in observations:
        if result.demoddata:
            for data in result.demoddata:
                url: ParseResult = urlparse(data.payload_demod)
                filename = pathlib.Path(url.path).name

                retrieve_result: tuple[str, HTTPMessage] = urllib.request.urlretrieve(data.payload_demod,
                                                                                      cache_dir / filename)

                print(f"Downloaded {retrieve_result[0]}")

                parse_to_csv(file_name=filename, full_path=cache_dir)


def main() -> None:
    config = configparser.ConfigParser()
    config.read('config.ini')

    base_url = config['API']['base_url']
    token = config['API']['token']
    satellite_norad_cat_id = config.getint('API', 'satellite_norad_cat_id')
    start_date = datetime.strptime(config['API']['start_date'], '%Y-%m-%d')
    end_date = datetime.strptime(config['API']['end_date'], '%Y-%m-%d')
    cache_dir = pathlib.Path(config['Paths']['cache_dir'])

    cache_dir.mkdir(exist_ok=True)

    client = AuthenticatedClient(base_url=base_url, token=token)

    with client as client:
        observations: paginated_observation_list = observations_list.sync(
            client=client,
            satellite_norad_cat_id=satellite_norad_cat_id,
            start=start_date,
            end=end_date
        )

        while observations.next_:
            print(f"Scanning next cursor: {observations.next_}...")

            observations = observations_list.sync(
                client=client, cursor=extract_cursor(observations.next_),
            )

            download(observations=observations.results, cache_dir=cache_dir)


if __name__ == "__main__":
    main()
