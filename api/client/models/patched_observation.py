import datetime
import json
from typing import TYPE_CHECKING, Any, Dict, List, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.transmitter_type_enum import TransmitterTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.demod_data import DemodData


T = TypeVar("T", bound="PatchedObservation")


@_attrs_define
class PatchedObservation:
    """SatNOGS Network Observation API Serializer

    Attributes:
        id (Union[Unset, int]):
        start (Union[Unset, datetime.datetime]):
        end (Union[Unset, datetime.datetime]):
        ground_station (Union[None, Unset, int]):
        transmitter (Union[Unset, str]):
        norad_cat_id (Union[Unset, str]):
        payload (Union[Unset, str]):
        waterfall (Union[Unset, str]):
        demoddata (Union[Unset, List['DemodData']]):
        station_name (Union[Unset, str]):
        station_lat (Union[Unset, str]):
        station_lng (Union[Unset, str]):
        station_alt (Union[Unset, str]):
        vetted_status (Union[Unset, str]):
        vetted_user (Union[Unset, str]):
        vetted_datetime (Union[Unset, str]):
        archived (Union[Unset, bool]):
        archive_url (Union[None, Unset, str]):
        client_version (Union[Unset, str]):
        client_metadata (Union[Unset, str]):
        status (Union[Unset, str]):
        waterfall_status (Union[Unset, str]):
        waterfall_status_user (Union[None, Unset, int]):
        waterfall_status_datetime (Union[None, Unset, datetime.datetime]):
        rise_azimuth (Union[None, Unset, float]):
        set_azimuth (Union[None, Unset, float]):
        max_altitude (Union[None, Unset, float]):
        transmitter_uuid (Union[Unset, str]):
        transmitter_description (Union[Unset, str]):
        transmitter_type (Union[Unset, TransmitterTypeEnum]):
        transmitter_uplink_low (Union[None, Unset, int]):
        transmitter_uplink_high (Union[None, Unset, int]):
        transmitter_uplink_drift (Union[None, Unset, int]):
        transmitter_downlink_low (Union[None, Unset, int]):
        transmitter_downlink_high (Union[None, Unset, int]):
        transmitter_downlink_drift (Union[None, Unset, int]):
        transmitter_mode (Union[None, Unset, str]):
        transmitter_invert (Union[Unset, bool]):
        transmitter_baud (Union[None, Unset, float]):
        transmitter_updated (Union[Unset, str]):
        transmitter_status (Union[Unset, str]):
        tle0 (Union[Unset, str]):
        tle1 (Union[Unset, str]):
        tle2 (Union[Unset, str]):
        center_frequency (Union[Unset, str]):
        observer (Union[Unset, str]):
        observation_frequency (Union[Unset, str]):
        transmitter_unconfirmed (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    start: Union[Unset, datetime.datetime] = UNSET
    end: Union[Unset, datetime.datetime] = UNSET
    ground_station: Union[None, Unset, int] = UNSET
    transmitter: Union[Unset, str] = UNSET
    norad_cat_id: Union[Unset, str] = UNSET
    payload: Union[Unset, str] = UNSET
    waterfall: Union[Unset, str] = UNSET
    demoddata: Union[Unset, List["DemodData"]] = UNSET
    station_name: Union[Unset, str] = UNSET
    station_lat: Union[Unset, str] = UNSET
    station_lng: Union[Unset, str] = UNSET
    station_alt: Union[Unset, str] = UNSET
    vetted_status: Union[Unset, str] = UNSET
    vetted_user: Union[Unset, str] = UNSET
    vetted_datetime: Union[Unset, str] = UNSET
    archived: Union[Unset, bool] = UNSET
    archive_url: Union[None, Unset, str] = UNSET
    client_version: Union[Unset, str] = UNSET
    client_metadata: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    waterfall_status: Union[Unset, str] = UNSET
    waterfall_status_user: Union[None, Unset, int] = UNSET
    waterfall_status_datetime: Union[None, Unset, datetime.datetime] = UNSET
    rise_azimuth: Union[None, Unset, float] = UNSET
    set_azimuth: Union[None, Unset, float] = UNSET
    max_altitude: Union[None, Unset, float] = UNSET
    transmitter_uuid: Union[Unset, str] = UNSET
    transmitter_description: Union[Unset, str] = UNSET
    transmitter_type: Union[Unset, TransmitterTypeEnum] = UNSET
    transmitter_uplink_low: Union[None, Unset, int] = UNSET
    transmitter_uplink_high: Union[None, Unset, int] = UNSET
    transmitter_uplink_drift: Union[None, Unset, int] = UNSET
    transmitter_downlink_low: Union[None, Unset, int] = UNSET
    transmitter_downlink_high: Union[None, Unset, int] = UNSET
    transmitter_downlink_drift: Union[None, Unset, int] = UNSET
    transmitter_mode: Union[None, Unset, str] = UNSET
    transmitter_invert: Union[Unset, bool] = UNSET
    transmitter_baud: Union[None, Unset, float] = UNSET
    transmitter_updated: Union[Unset, str] = UNSET
    transmitter_status: Union[Unset, str] = UNSET
    tle0: Union[Unset, str] = UNSET
    tle1: Union[Unset, str] = UNSET
    tle2: Union[Unset, str] = UNSET
    center_frequency: Union[Unset, str] = UNSET
    observer: Union[Unset, str] = UNSET
    observation_frequency: Union[Unset, str] = UNSET
    transmitter_unconfirmed: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        start: Union[Unset, str] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        end: Union[Unset, str] = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat()

        ground_station: Union[None, Unset, int]
        if isinstance(self.ground_station, Unset):
            ground_station = UNSET
        else:
            ground_station = self.ground_station

        transmitter = self.transmitter

        norad_cat_id = self.norad_cat_id

        payload = self.payload

        waterfall = self.waterfall

        demoddata: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.demoddata, Unset):
            demoddata = []
            for demoddata_item_data in self.demoddata:
                demoddata_item = demoddata_item_data.to_dict()
                demoddata.append(demoddata_item)

        station_name = self.station_name

        station_lat = self.station_lat

        station_lng = self.station_lng

        station_alt = self.station_alt

        vetted_status = self.vetted_status

        vetted_user = self.vetted_user

        vetted_datetime = self.vetted_datetime

        archived = self.archived

        archive_url: Union[None, Unset, str]
        if isinstance(self.archive_url, Unset):
            archive_url = UNSET
        else:
            archive_url = self.archive_url

        client_version = self.client_version

        client_metadata = self.client_metadata

        status = self.status

        waterfall_status = self.waterfall_status

        waterfall_status_user: Union[None, Unset, int]
        if isinstance(self.waterfall_status_user, Unset):
            waterfall_status_user = UNSET
        else:
            waterfall_status_user = self.waterfall_status_user

        waterfall_status_datetime: Union[None, Unset, str]
        if isinstance(self.waterfall_status_datetime, Unset):
            waterfall_status_datetime = UNSET
        elif isinstance(self.waterfall_status_datetime, datetime.datetime):
            waterfall_status_datetime = self.waterfall_status_datetime.isoformat()
        else:
            waterfall_status_datetime = self.waterfall_status_datetime

        rise_azimuth: Union[None, Unset, float]
        if isinstance(self.rise_azimuth, Unset):
            rise_azimuth = UNSET
        else:
            rise_azimuth = self.rise_azimuth

        set_azimuth: Union[None, Unset, float]
        if isinstance(self.set_azimuth, Unset):
            set_azimuth = UNSET
        else:
            set_azimuth = self.set_azimuth

        max_altitude: Union[None, Unset, float]
        if isinstance(self.max_altitude, Unset):
            max_altitude = UNSET
        else:
            max_altitude = self.max_altitude

        transmitter_uuid = self.transmitter_uuid

        transmitter_description = self.transmitter_description

        transmitter_type: Union[Unset, str] = UNSET
        if not isinstance(self.transmitter_type, Unset):
            transmitter_type = self.transmitter_type.value

        transmitter_uplink_low: Union[None, Unset, int]
        if isinstance(self.transmitter_uplink_low, Unset):
            transmitter_uplink_low = UNSET
        else:
            transmitter_uplink_low = self.transmitter_uplink_low

        transmitter_uplink_high: Union[None, Unset, int]
        if isinstance(self.transmitter_uplink_high, Unset):
            transmitter_uplink_high = UNSET
        else:
            transmitter_uplink_high = self.transmitter_uplink_high

        transmitter_uplink_drift: Union[None, Unset, int]
        if isinstance(self.transmitter_uplink_drift, Unset):
            transmitter_uplink_drift = UNSET
        else:
            transmitter_uplink_drift = self.transmitter_uplink_drift

        transmitter_downlink_low: Union[None, Unset, int]
        if isinstance(self.transmitter_downlink_low, Unset):
            transmitter_downlink_low = UNSET
        else:
            transmitter_downlink_low = self.transmitter_downlink_low

        transmitter_downlink_high: Union[None, Unset, int]
        if isinstance(self.transmitter_downlink_high, Unset):
            transmitter_downlink_high = UNSET
        else:
            transmitter_downlink_high = self.transmitter_downlink_high

        transmitter_downlink_drift: Union[None, Unset, int]
        if isinstance(self.transmitter_downlink_drift, Unset):
            transmitter_downlink_drift = UNSET
        else:
            transmitter_downlink_drift = self.transmitter_downlink_drift

        transmitter_mode: Union[None, Unset, str]
        if isinstance(self.transmitter_mode, Unset):
            transmitter_mode = UNSET
        else:
            transmitter_mode = self.transmitter_mode

        transmitter_invert = self.transmitter_invert

        transmitter_baud: Union[None, Unset, float]
        if isinstance(self.transmitter_baud, Unset):
            transmitter_baud = UNSET
        else:
            transmitter_baud = self.transmitter_baud

        transmitter_updated = self.transmitter_updated

        transmitter_status = self.transmitter_status

        tle0 = self.tle0

        tle1 = self.tle1

        tle2 = self.tle2

        center_frequency = self.center_frequency

        observer = self.observer

        observation_frequency = self.observation_frequency

        transmitter_unconfirmed = self.transmitter_unconfirmed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if ground_station is not UNSET:
            field_dict["ground_station"] = ground_station
        if transmitter is not UNSET:
            field_dict["transmitter"] = transmitter
        if norad_cat_id is not UNSET:
            field_dict["norad_cat_id"] = norad_cat_id
        if payload is not UNSET:
            field_dict["payload"] = payload
        if waterfall is not UNSET:
            field_dict["waterfall"] = waterfall
        if demoddata is not UNSET:
            field_dict["demoddata"] = demoddata
        if station_name is not UNSET:
            field_dict["station_name"] = station_name
        if station_lat is not UNSET:
            field_dict["station_lat"] = station_lat
        if station_lng is not UNSET:
            field_dict["station_lng"] = station_lng
        if station_alt is not UNSET:
            field_dict["station_alt"] = station_alt
        if vetted_status is not UNSET:
            field_dict["vetted_status"] = vetted_status
        if vetted_user is not UNSET:
            field_dict["vetted_user"] = vetted_user
        if vetted_datetime is not UNSET:
            field_dict["vetted_datetime"] = vetted_datetime
        if archived is not UNSET:
            field_dict["archived"] = archived
        if archive_url is not UNSET:
            field_dict["archive_url"] = archive_url
        if client_version is not UNSET:
            field_dict["client_version"] = client_version
        if client_metadata is not UNSET:
            field_dict["client_metadata"] = client_metadata
        if status is not UNSET:
            field_dict["status"] = status
        if waterfall_status is not UNSET:
            field_dict["waterfall_status"] = waterfall_status
        if waterfall_status_user is not UNSET:
            field_dict["waterfall_status_user"] = waterfall_status_user
        if waterfall_status_datetime is not UNSET:
            field_dict["waterfall_status_datetime"] = waterfall_status_datetime
        if rise_azimuth is not UNSET:
            field_dict["rise_azimuth"] = rise_azimuth
        if set_azimuth is not UNSET:
            field_dict["set_azimuth"] = set_azimuth
        if max_altitude is not UNSET:
            field_dict["max_altitude"] = max_altitude
        if transmitter_uuid is not UNSET:
            field_dict["transmitter_uuid"] = transmitter_uuid
        if transmitter_description is not UNSET:
            field_dict["transmitter_description"] = transmitter_description
        if transmitter_type is not UNSET:
            field_dict["transmitter_type"] = transmitter_type
        if transmitter_uplink_low is not UNSET:
            field_dict["transmitter_uplink_low"] = transmitter_uplink_low
        if transmitter_uplink_high is not UNSET:
            field_dict["transmitter_uplink_high"] = transmitter_uplink_high
        if transmitter_uplink_drift is not UNSET:
            field_dict["transmitter_uplink_drift"] = transmitter_uplink_drift
        if transmitter_downlink_low is not UNSET:
            field_dict["transmitter_downlink_low"] = transmitter_downlink_low
        if transmitter_downlink_high is not UNSET:
            field_dict["transmitter_downlink_high"] = transmitter_downlink_high
        if transmitter_downlink_drift is not UNSET:
            field_dict["transmitter_downlink_drift"] = transmitter_downlink_drift
        if transmitter_mode is not UNSET:
            field_dict["transmitter_mode"] = transmitter_mode
        if transmitter_invert is not UNSET:
            field_dict["transmitter_invert"] = transmitter_invert
        if transmitter_baud is not UNSET:
            field_dict["transmitter_baud"] = transmitter_baud
        if transmitter_updated is not UNSET:
            field_dict["transmitter_updated"] = transmitter_updated
        if transmitter_status is not UNSET:
            field_dict["transmitter_status"] = transmitter_status
        if tle0 is not UNSET:
            field_dict["tle0"] = tle0
        if tle1 is not UNSET:
            field_dict["tle1"] = tle1
        if tle2 is not UNSET:
            field_dict["tle2"] = tle2
        if center_frequency is not UNSET:
            field_dict["center_frequency"] = center_frequency
        if observer is not UNSET:
            field_dict["observer"] = observer
        if observation_frequency is not UNSET:
            field_dict["observation_frequency"] = observation_frequency
        if transmitter_unconfirmed is not UNSET:
            field_dict["transmitter_unconfirmed"] = transmitter_unconfirmed

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")

        start: Union[Unset, bytes] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat().encode()

        end: Union[Unset, bytes] = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat().encode()

        ground_station: Union[Tuple[None, bytes, str], Unset]

        if isinstance(self.ground_station, Unset):
            ground_station = UNSET
        elif isinstance(self.ground_station, int):
            ground_station = (None, str(self.ground_station).encode(), "text/plain")
        else:
            ground_station = (None, str(self.ground_station).encode(), "text/plain")

        transmitter = (
            self.transmitter
            if isinstance(self.transmitter, Unset)
            else (None, str(self.transmitter).encode(), "text/plain")
        )

        norad_cat_id = (
            self.norad_cat_id
            if isinstance(self.norad_cat_id, Unset)
            else (None, str(self.norad_cat_id).encode(), "text/plain")
        )

        payload = self.payload if isinstance(self.payload, Unset) else (None, str(self.payload).encode(), "text/plain")

        waterfall = (
            self.waterfall if isinstance(self.waterfall, Unset) else (None, str(self.waterfall).encode(), "text/plain")
        )

        demoddata: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.demoddata, Unset):
            _temp_demoddata = []
            for demoddata_item_data in self.demoddata:
                demoddata_item = demoddata_item_data.to_dict()
                _temp_demoddata.append(demoddata_item)
            demoddata = (None, json.dumps(_temp_demoddata).encode(), "application/json")

        station_name = (
            self.station_name
            if isinstance(self.station_name, Unset)
            else (None, str(self.station_name).encode(), "text/plain")
        )

        station_lat = (
            self.station_lat
            if isinstance(self.station_lat, Unset)
            else (None, str(self.station_lat).encode(), "text/plain")
        )

        station_lng = (
            self.station_lng
            if isinstance(self.station_lng, Unset)
            else (None, str(self.station_lng).encode(), "text/plain")
        )

        station_alt = (
            self.station_alt
            if isinstance(self.station_alt, Unset)
            else (None, str(self.station_alt).encode(), "text/plain")
        )

        vetted_status = (
            self.vetted_status
            if isinstance(self.vetted_status, Unset)
            else (None, str(self.vetted_status).encode(), "text/plain")
        )

        vetted_user = (
            self.vetted_user
            if isinstance(self.vetted_user, Unset)
            else (None, str(self.vetted_user).encode(), "text/plain")
        )

        vetted_datetime = (
            self.vetted_datetime
            if isinstance(self.vetted_datetime, Unset)
            else (None, str(self.vetted_datetime).encode(), "text/plain")
        )

        archived = (
            self.archived if isinstance(self.archived, Unset) else (None, str(self.archived).encode(), "text/plain")
        )

        archive_url: Union[Tuple[None, bytes, str], Unset]

        if isinstance(self.archive_url, Unset):
            archive_url = UNSET
        elif isinstance(self.archive_url, str):
            archive_url = (None, str(self.archive_url).encode(), "text/plain")
        else:
            archive_url = (None, str(self.archive_url).encode(), "text/plain")

        client_version = (
            self.client_version
            if isinstance(self.client_version, Unset)
            else (None, str(self.client_version).encode(), "text/plain")
        )

        client_metadata = (
            self.client_metadata
            if isinstance(self.client_metadata, Unset)
            else (None, str(self.client_metadata).encode(), "text/plain")
        )

        status = self.status if isinstance(self.status, Unset) else (None, str(self.status).encode(), "text/plain")

        waterfall_status = (
            self.waterfall_status
            if isinstance(self.waterfall_status, Unset)
            else (None, str(self.waterfall_status).encode(), "text/plain")
        )

        waterfall_status_user: Union[Tuple[None, bytes, str], Unset]

        if isinstance(self.waterfall_status_user, Unset):
            waterfall_status_user = UNSET
        elif isinstance(self.waterfall_status_user, int):
            waterfall_status_user = (None, str(self.waterfall_status_user).encode(), "text/plain")
        else:
            waterfall_status_user = (None, str(self.waterfall_status_user).encode(), "text/plain")

        waterfall_status_datetime: Union[Tuple[None, bytes, str], Unset]

        if isinstance(self.waterfall_status_datetime, Unset):
            waterfall_status_datetime = UNSET
        elif isinstance(self.waterfall_status_datetime, datetime.datetime):
            waterfall_status_datetime = self.waterfall_status_datetime.isoformat().encode()
        else:
            waterfall_status_datetime = (None, str(self.waterfall_status_datetime).encode(), "text/plain")

        rise_azimuth: Union[Tuple[None, bytes, str], Unset]

        if isinstance(self.rise_azimuth, Unset):
            rise_azimuth = UNSET
        elif isinstance(self.rise_azimuth, float):
            rise_azimuth = (None, str(self.rise_azimuth).encode(), "text/plain")
        else:
            rise_azimuth = (None, str(self.rise_azimuth).encode(), "text/plain")

        set_azimuth: Union[Tuple[None, bytes, str], Unset]

        if isinstance(self.set_azimuth, Unset):
            set_azimuth = UNSET
        elif isinstance(self.set_azimuth, float):
            set_azimuth = (None, str(self.set_azimuth).encode(), "text/plain")
        else:
            set_azimuth = (None, str(self.set_azimuth).encode(), "text/plain")

        max_altitude: Union[Tuple[None, bytes, str], Unset]

        if isinstance(self.max_altitude, Unset):
            max_altitude = UNSET
        elif isinstance(self.max_altitude, float):
            max_altitude = (None, str(self.max_altitude).encode(), "text/plain")
        else:
            max_altitude = (None, str(self.max_altitude).encode(), "text/plain")

        transmitter_uuid = (
            self.transmitter_uuid
            if isinstance(self.transmitter_uuid, Unset)
            else (None, str(self.transmitter_uuid).encode(), "text/plain")
        )

        transmitter_description = (
            self.transmitter_description
            if isinstance(self.transmitter_description, Unset)
            else (None, str(self.transmitter_description).encode(), "text/plain")
        )

        transmitter_type: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.transmitter_type, Unset):
            transmitter_type = (None, str(self.transmitter_type.value).encode(), "text/plain")

        transmitter_uplink_low: Union[Tuple[None, bytes, str], Unset]

        if isinstance(self.transmitter_uplink_low, Unset):
            transmitter_uplink_low = UNSET
        elif isinstance(self.transmitter_uplink_low, int):
            transmitter_uplink_low = (None, str(self.transmitter_uplink_low).encode(), "text/plain")
        else:
            transmitter_uplink_low = (None, str(self.transmitter_uplink_low).encode(), "text/plain")

        transmitter_uplink_high: Union[Tuple[None, bytes, str], Unset]

        if isinstance(self.transmitter_uplink_high, Unset):
            transmitter_uplink_high = UNSET
        elif isinstance(self.transmitter_uplink_high, int):
            transmitter_uplink_high = (None, str(self.transmitter_uplink_high).encode(), "text/plain")
        else:
            transmitter_uplink_high = (None, str(self.transmitter_uplink_high).encode(), "text/plain")

        transmitter_uplink_drift: Union[Tuple[None, bytes, str], Unset]

        if isinstance(self.transmitter_uplink_drift, Unset):
            transmitter_uplink_drift = UNSET
        elif isinstance(self.transmitter_uplink_drift, int):
            transmitter_uplink_drift = (None, str(self.transmitter_uplink_drift).encode(), "text/plain")
        else:
            transmitter_uplink_drift = (None, str(self.transmitter_uplink_drift).encode(), "text/plain")

        transmitter_downlink_low: Union[Tuple[None, bytes, str], Unset]

        if isinstance(self.transmitter_downlink_low, Unset):
            transmitter_downlink_low = UNSET
        elif isinstance(self.transmitter_downlink_low, int):
            transmitter_downlink_low = (None, str(self.transmitter_downlink_low).encode(), "text/plain")
        else:
            transmitter_downlink_low = (None, str(self.transmitter_downlink_low).encode(), "text/plain")

        transmitter_downlink_high: Union[Tuple[None, bytes, str], Unset]

        if isinstance(self.transmitter_downlink_high, Unset):
            transmitter_downlink_high = UNSET
        elif isinstance(self.transmitter_downlink_high, int):
            transmitter_downlink_high = (None, str(self.transmitter_downlink_high).encode(), "text/plain")
        else:
            transmitter_downlink_high = (None, str(self.transmitter_downlink_high).encode(), "text/plain")

        transmitter_downlink_drift: Union[Tuple[None, bytes, str], Unset]

        if isinstance(self.transmitter_downlink_drift, Unset):
            transmitter_downlink_drift = UNSET
        elif isinstance(self.transmitter_downlink_drift, int):
            transmitter_downlink_drift = (None, str(self.transmitter_downlink_drift).encode(), "text/plain")
        else:
            transmitter_downlink_drift = (None, str(self.transmitter_downlink_drift).encode(), "text/plain")

        transmitter_mode: Union[Tuple[None, bytes, str], Unset]

        if isinstance(self.transmitter_mode, Unset):
            transmitter_mode = UNSET
        elif isinstance(self.transmitter_mode, str):
            transmitter_mode = (None, str(self.transmitter_mode).encode(), "text/plain")
        else:
            transmitter_mode = (None, str(self.transmitter_mode).encode(), "text/plain")

        transmitter_invert = (
            self.transmitter_invert
            if isinstance(self.transmitter_invert, Unset)
            else (None, str(self.transmitter_invert).encode(), "text/plain")
        )

        transmitter_baud: Union[Tuple[None, bytes, str], Unset]

        if isinstance(self.transmitter_baud, Unset):
            transmitter_baud = UNSET
        elif isinstance(self.transmitter_baud, float):
            transmitter_baud = (None, str(self.transmitter_baud).encode(), "text/plain")
        else:
            transmitter_baud = (None, str(self.transmitter_baud).encode(), "text/plain")

        transmitter_updated = (
            self.transmitter_updated
            if isinstance(self.transmitter_updated, Unset)
            else (None, str(self.transmitter_updated).encode(), "text/plain")
        )

        transmitter_status = (
            self.transmitter_status
            if isinstance(self.transmitter_status, Unset)
            else (None, str(self.transmitter_status).encode(), "text/plain")
        )

        tle0 = self.tle0 if isinstance(self.tle0, Unset) else (None, str(self.tle0).encode(), "text/plain")

        tle1 = self.tle1 if isinstance(self.tle1, Unset) else (None, str(self.tle1).encode(), "text/plain")

        tle2 = self.tle2 if isinstance(self.tle2, Unset) else (None, str(self.tle2).encode(), "text/plain")

        center_frequency = (
            self.center_frequency
            if isinstance(self.center_frequency, Unset)
            else (None, str(self.center_frequency).encode(), "text/plain")
        )

        observer = (
            self.observer if isinstance(self.observer, Unset) else (None, str(self.observer).encode(), "text/plain")
        )

        observation_frequency = (
            self.observation_frequency
            if isinstance(self.observation_frequency, Unset)
            else (None, str(self.observation_frequency).encode(), "text/plain")
        )

        transmitter_unconfirmed = (
            self.transmitter_unconfirmed
            if isinstance(self.transmitter_unconfirmed, Unset)
            else (None, str(self.transmitter_unconfirmed).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if ground_station is not UNSET:
            field_dict["ground_station"] = ground_station
        if transmitter is not UNSET:
            field_dict["transmitter"] = transmitter
        if norad_cat_id is not UNSET:
            field_dict["norad_cat_id"] = norad_cat_id
        if payload is not UNSET:
            field_dict["payload"] = payload
        if waterfall is not UNSET:
            field_dict["waterfall"] = waterfall
        if demoddata is not UNSET:
            field_dict["demoddata"] = demoddata
        if station_name is not UNSET:
            field_dict["station_name"] = station_name
        if station_lat is not UNSET:
            field_dict["station_lat"] = station_lat
        if station_lng is not UNSET:
            field_dict["station_lng"] = station_lng
        if station_alt is not UNSET:
            field_dict["station_alt"] = station_alt
        if vetted_status is not UNSET:
            field_dict["vetted_status"] = vetted_status
        if vetted_user is not UNSET:
            field_dict["vetted_user"] = vetted_user
        if vetted_datetime is not UNSET:
            field_dict["vetted_datetime"] = vetted_datetime
        if archived is not UNSET:
            field_dict["archived"] = archived
        if archive_url is not UNSET:
            field_dict["archive_url"] = archive_url
        if client_version is not UNSET:
            field_dict["client_version"] = client_version
        if client_metadata is not UNSET:
            field_dict["client_metadata"] = client_metadata
        if status is not UNSET:
            field_dict["status"] = status
        if waterfall_status is not UNSET:
            field_dict["waterfall_status"] = waterfall_status
        if waterfall_status_user is not UNSET:
            field_dict["waterfall_status_user"] = waterfall_status_user
        if waterfall_status_datetime is not UNSET:
            field_dict["waterfall_status_datetime"] = waterfall_status_datetime
        if rise_azimuth is not UNSET:
            field_dict["rise_azimuth"] = rise_azimuth
        if set_azimuth is not UNSET:
            field_dict["set_azimuth"] = set_azimuth
        if max_altitude is not UNSET:
            field_dict["max_altitude"] = max_altitude
        if transmitter_uuid is not UNSET:
            field_dict["transmitter_uuid"] = transmitter_uuid
        if transmitter_description is not UNSET:
            field_dict["transmitter_description"] = transmitter_description
        if transmitter_type is not UNSET:
            field_dict["transmitter_type"] = transmitter_type
        if transmitter_uplink_low is not UNSET:
            field_dict["transmitter_uplink_low"] = transmitter_uplink_low
        if transmitter_uplink_high is not UNSET:
            field_dict["transmitter_uplink_high"] = transmitter_uplink_high
        if transmitter_uplink_drift is not UNSET:
            field_dict["transmitter_uplink_drift"] = transmitter_uplink_drift
        if transmitter_downlink_low is not UNSET:
            field_dict["transmitter_downlink_low"] = transmitter_downlink_low
        if transmitter_downlink_high is not UNSET:
            field_dict["transmitter_downlink_high"] = transmitter_downlink_high
        if transmitter_downlink_drift is not UNSET:
            field_dict["transmitter_downlink_drift"] = transmitter_downlink_drift
        if transmitter_mode is not UNSET:
            field_dict["transmitter_mode"] = transmitter_mode
        if transmitter_invert is not UNSET:
            field_dict["transmitter_invert"] = transmitter_invert
        if transmitter_baud is not UNSET:
            field_dict["transmitter_baud"] = transmitter_baud
        if transmitter_updated is not UNSET:
            field_dict["transmitter_updated"] = transmitter_updated
        if transmitter_status is not UNSET:
            field_dict["transmitter_status"] = transmitter_status
        if tle0 is not UNSET:
            field_dict["tle0"] = tle0
        if tle1 is not UNSET:
            field_dict["tle1"] = tle1
        if tle2 is not UNSET:
            field_dict["tle2"] = tle2
        if center_frequency is not UNSET:
            field_dict["center_frequency"] = center_frequency
        if observer is not UNSET:
            field_dict["observer"] = observer
        if observation_frequency is not UNSET:
            field_dict["observation_frequency"] = observation_frequency
        if transmitter_unconfirmed is not UNSET:
            field_dict["transmitter_unconfirmed"] = transmitter_unconfirmed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.demod_data import DemodData

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _start = d.pop("start", UNSET)
        start: Union[Unset, datetime.datetime]
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = isoparse(_start)

        _end = d.pop("end", UNSET)
        end: Union[Unset, datetime.datetime]
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = isoparse(_end)

        def _parse_ground_station(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        ground_station = _parse_ground_station(d.pop("ground_station", UNSET))

        transmitter = d.pop("transmitter", UNSET)

        norad_cat_id = d.pop("norad_cat_id", UNSET)

        payload = d.pop("payload", UNSET)

        waterfall = d.pop("waterfall", UNSET)

        demoddata = []
        _demoddata = d.pop("demoddata", UNSET)
        for demoddata_item_data in _demoddata or []:
            demoddata_item = DemodData.from_dict(demoddata_item_data)

            demoddata.append(demoddata_item)

        station_name = d.pop("station_name", UNSET)

        station_lat = d.pop("station_lat", UNSET)

        station_lng = d.pop("station_lng", UNSET)

        station_alt = d.pop("station_alt", UNSET)

        vetted_status = d.pop("vetted_status", UNSET)

        vetted_user = d.pop("vetted_user", UNSET)

        vetted_datetime = d.pop("vetted_datetime", UNSET)

        archived = d.pop("archived", UNSET)

        def _parse_archive_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        archive_url = _parse_archive_url(d.pop("archive_url", UNSET))

        client_version = d.pop("client_version", UNSET)

        client_metadata = d.pop("client_metadata", UNSET)

        status = d.pop("status", UNSET)

        waterfall_status = d.pop("waterfall_status", UNSET)

        def _parse_waterfall_status_user(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        waterfall_status_user = _parse_waterfall_status_user(d.pop("waterfall_status_user", UNSET))

        def _parse_waterfall_status_datetime(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                waterfall_status_datetime_type_0 = isoparse(data)

                return waterfall_status_datetime_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        waterfall_status_datetime = _parse_waterfall_status_datetime(d.pop("waterfall_status_datetime", UNSET))

        def _parse_rise_azimuth(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        rise_azimuth = _parse_rise_azimuth(d.pop("rise_azimuth", UNSET))

        def _parse_set_azimuth(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        set_azimuth = _parse_set_azimuth(d.pop("set_azimuth", UNSET))

        def _parse_max_altitude(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        max_altitude = _parse_max_altitude(d.pop("max_altitude", UNSET))

        transmitter_uuid = d.pop("transmitter_uuid", UNSET)

        transmitter_description = d.pop("transmitter_description", UNSET)

        _transmitter_type = d.pop("transmitter_type", UNSET)
        transmitter_type: Union[Unset, TransmitterTypeEnum]
        if isinstance(_transmitter_type, Unset):
            transmitter_type = UNSET
        else:
            transmitter_type = TransmitterTypeEnum(_transmitter_type)

        def _parse_transmitter_uplink_low(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        transmitter_uplink_low = _parse_transmitter_uplink_low(d.pop("transmitter_uplink_low", UNSET))

        def _parse_transmitter_uplink_high(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        transmitter_uplink_high = _parse_transmitter_uplink_high(d.pop("transmitter_uplink_high", UNSET))

        def _parse_transmitter_uplink_drift(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        transmitter_uplink_drift = _parse_transmitter_uplink_drift(d.pop("transmitter_uplink_drift", UNSET))

        def _parse_transmitter_downlink_low(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        transmitter_downlink_low = _parse_transmitter_downlink_low(d.pop("transmitter_downlink_low", UNSET))

        def _parse_transmitter_downlink_high(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        transmitter_downlink_high = _parse_transmitter_downlink_high(d.pop("transmitter_downlink_high", UNSET))

        def _parse_transmitter_downlink_drift(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        transmitter_downlink_drift = _parse_transmitter_downlink_drift(d.pop("transmitter_downlink_drift", UNSET))

        def _parse_transmitter_mode(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        transmitter_mode = _parse_transmitter_mode(d.pop("transmitter_mode", UNSET))

        transmitter_invert = d.pop("transmitter_invert", UNSET)

        def _parse_transmitter_baud(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        transmitter_baud = _parse_transmitter_baud(d.pop("transmitter_baud", UNSET))

        transmitter_updated = d.pop("transmitter_updated", UNSET)

        transmitter_status = d.pop("transmitter_status", UNSET)

        tle0 = d.pop("tle0", UNSET)

        tle1 = d.pop("tle1", UNSET)

        tle2 = d.pop("tle2", UNSET)

        center_frequency = d.pop("center_frequency", UNSET)

        observer = d.pop("observer", UNSET)

        observation_frequency = d.pop("observation_frequency", UNSET)

        transmitter_unconfirmed = d.pop("transmitter_unconfirmed", UNSET)

        patched_observation = cls(
            id=id,
            start=start,
            end=end,
            ground_station=ground_station,
            transmitter=transmitter,
            norad_cat_id=norad_cat_id,
            payload=payload,
            waterfall=waterfall,
            demoddata=demoddata,
            station_name=station_name,
            station_lat=station_lat,
            station_lng=station_lng,
            station_alt=station_alt,
            vetted_status=vetted_status,
            vetted_user=vetted_user,
            vetted_datetime=vetted_datetime,
            archived=archived,
            archive_url=archive_url,
            client_version=client_version,
            client_metadata=client_metadata,
            status=status,
            waterfall_status=waterfall_status,
            waterfall_status_user=waterfall_status_user,
            waterfall_status_datetime=waterfall_status_datetime,
            rise_azimuth=rise_azimuth,
            set_azimuth=set_azimuth,
            max_altitude=max_altitude,
            transmitter_uuid=transmitter_uuid,
            transmitter_description=transmitter_description,
            transmitter_type=transmitter_type,
            transmitter_uplink_low=transmitter_uplink_low,
            transmitter_uplink_high=transmitter_uplink_high,
            transmitter_uplink_drift=transmitter_uplink_drift,
            transmitter_downlink_low=transmitter_downlink_low,
            transmitter_downlink_high=transmitter_downlink_high,
            transmitter_downlink_drift=transmitter_downlink_drift,
            transmitter_mode=transmitter_mode,
            transmitter_invert=transmitter_invert,
            transmitter_baud=transmitter_baud,
            transmitter_updated=transmitter_updated,
            transmitter_status=transmitter_status,
            tle0=tle0,
            tle1=tle1,
            tle2=tle2,
            center_frequency=center_frequency,
            observer=observer,
            observation_frequency=observation_frequency,
            transmitter_unconfirmed=transmitter_unconfirmed,
        )

        patched_observation.additional_properties = d
        return patched_observation

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
