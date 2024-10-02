# More info here - https://docs.satnogs.org/projects/satnogs-network/en/stable/api.html
import pathlib
from datetime import datetime
from os import PathLike

from api.client import AuthenticatedClient

client = AuthenticatedClient(base_url="https://network.satnogs.org", token="")

from api.client.models import paginated_observation_list
from api.client.api.observations import observations_list

from pprint import pprint
import urllib.request

from urllib.parse import urlparse, parse_qs, ParseResult


def parse_to_csv(file_name: str, full_path: pathlib.Path | PathLike):
    csv_file: pathlib.Path = full_path / f"{file_name}.csv"

    # extract timestamp from binary frame file name
    # the filename consists of three parts:
    # data_843421_2019-07-20T13-21-51
    # 1. prefix "data"
    # 2. observation id
    # 3. timestamp of the recorded frame in UTC
    # after the split the array index [2] contains the timestamp
    dobj: datetime = datetime.strptime(file_name.split('_')[2], '%Y-%m-%dT%H-%M-%S')
    obs_time: str = dobj.strftime('%Y-%m-%d %H:%M:%S')

    with open(full_path / file_name, 'rb') as f:
        hexdump = f.read().hex().upper()
    with open(csv_file, 'w') as f:
        f.write(obs_time + '|' + hexdump + '\n')

def extract_cursor(full_url: str) -> str:
    parsed_url = urlparse(full_url)

    query_params = parse_qs(parsed_url.query)

    cursor = query_params.get('cursor', [''])[0]

    return cursor


with client as client:
    observation: paginated_observation_list = observations_list.sync(client=client, satellite_norad_cat_id=44420,
                                                      start=datetime(2020, 1, 1), end=datetime(2020, 3, 1))
    for result in observation.results:
        if result.demoddata:
            for data in result.demoddata:
                url: ParseResult = urlparse(data.payload_demod)
                filename = pathlib.Path(url.path).name
                file_path = pathlib.Path.cwd() / "cache"

                urllib.request.urlretrieve(data.payload_demod, file_path / filename)

                parse_to_csv(file_name=filename, full_path=file_path)
            pprint(result.demoddata)

    observation1: paginated_observation_list = observations_list.sync(client=client, cursor=extract_cursor(observation.next_))
