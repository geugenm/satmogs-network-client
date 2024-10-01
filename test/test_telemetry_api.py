from datetime import datetime

import pytest

from glouton.domain.parameters.programCmd import ProgramCmd
from glouton.services.telemetry import TelemetryService


@pytest.fixture
def glouton_conf() -> ProgramCmd:
    return ProgramCmd(
        norad_id="44420",
        ground_station_id=None,
        start_date=datetime(2020, 1, 1),
        end_date=datetime(2022, 3, 25),
        observation_status=None,
        working_dir="test_dir",
        waterfalls=False,
        demoddata=True,
        demoddata_modules=["CSV"],
        waterfall_modules=None,
        user=None,
        transmitter_uuid=None,
        transmitter_mode=None,
        transmitter_type=None,
        frame_modules=None,
        observer=None,
        app_source=None,
        transmitter=None,
        archives=None,
        archive_modules=None,
        archive_end_modules=None,
        demoddata_end_modules=None,
        frame_end_modules=None,
        waterfall_end_modules=None,
    )


@pytest.mark.parametrize(
    "norad_id, start_date, end_date",
    [
        ("44420", "2020-01-01T00:00:00", "2020-01-01T00:00:00"),
    ],
)
def test_observations_service_extract(
        glouton_conf: ProgramCmd, norad_id: str, start_date: str, end_date: str
) -> None:
    glouton_conf.norad_id = norad_id
    glouton_conf.start_date = datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%S")
    glouton_conf.end_date = datetime.strptime(end_date, "%Y-%m-%dT%H:%M:%S")

    telemetry_service: TelemetryService = TelemetryService(glouton_conf)
    telemetry_service.extract()
