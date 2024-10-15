from pathlib import Path
from os import PathLike
from datetime import datetime

def parse_to_csv(file_name: str, full_path: Path | PathLike) -> None:
    csv_file: Path = full_path / f"{file_name}.csv"

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