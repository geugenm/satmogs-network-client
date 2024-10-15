import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.transmitter_type_enum import TransmitterTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.demod_data import DemodData


T = TypeVar("T", bound="Observation")


@_attrs_define
class Observation:
    """SatNOGS Network Observation API Serializer

    Attributes:
        id (int):
        start (datetime.datetime):
        end (datetime.datetime):
        ground_station (Union[None, int]):
        transmitter (str):
        norad_cat_id (str):
        payload (str):
        waterfall (str):
        station_name (str):
        station_lat (str):
        station_lng (str):
        station_alt (str):
        vetted_status (str):
        vetted_user (str):
        vetted_datetime (str):
        archived (bool):
        archive_url (Union[None, str]):
        status (str):
        waterfall_status (str):
        waterfall_status_user (Union[None, int]):
        waterfall_status_datetime (Union[None, datetime.datetime]):
        rise_azimuth (Union[None, float]):
        set_azimuth (Union[None, float]):
        max_altitude (Union[None, float]):
        transmitter_uuid (str):
        transmitter_description (str):
        transmitter_type (TransmitterTypeEnum):
        transmitter_uplink_low (Union[None, int]):
        transmitter_uplink_high (Union[None, int]):
        transmitter_uplink_drift (Union[None, int]):
        transmitter_downlink_low (Union[None, int]):
        transmitter_downlink_high (Union[None, int]):
        transmitter_downlink_drift (Union[None, int]):
        transmitter_mode (Union[None, str]):
        transmitter_invert (bool):
        transmitter_baud (Union[None, float]):
        transmitter_updated (str):
        transmitter_status (str):
        tle0 (str):
        tle1 (str):
        tle2 (str):
        center_frequency (str):
        observer (str):
        observation_frequency (str):
        transmitter_unconfirmed (str):
        demoddata (Union[Unset, List['DemodData']]):
        client_version (Union[Unset, str]):
        client_metadata (Union[Unset, str]):
    """

    id: int
    start: datetime.datetime
    end: datetime.datetime
    ground_station: Union[None, int]
    transmitter: str
    norad_cat_id: str
    payload: str
    waterfall: str
    station_name: str
    station_lat: str
    station_lng: str
    station_alt: str
    vetted_status: str
    vetted_user: str
    vetted_datetime: str
    archived: bool
    archive_url: Union[None, str]
    status: str
    waterfall_status: str
    waterfall_status_user: Union[None, int]
    waterfall_status_datetime: Union[None, datetime.datetime]
    rise_azimuth: Union[None, float]
    set_azimuth: Union[None, float]
    max_altitude: Union[None, float]
    transmitter_uuid: str
    transmitter_description: str
    transmitter_type: TransmitterTypeEnum
    transmitter_uplink_low: Union[None, int]
    transmitter_uplink_high: Union[None, int]
    transmitter_uplink_drift: Union[None, int]
    transmitter_downlink_low: Union[None, int]
    transmitter_downlink_high: Union[None, int]
    transmitter_downlink_drift: Union[None, int]
    transmitter_mode: Union[None, str]
    transmitter_invert: bool
    transmitter_baud: Union[None, float]
    transmitter_updated: str
    transmitter_status: str
    tle0: str
    tle1: str
    tle2: str
    center_frequency: str
    observer: str
    observation_frequency: str
    transmitter_unconfirmed: str
    demoddata: Union[Unset, List["DemodData"]] = UNSET
    client_version: Union[Unset, str] = UNSET
    client_metadata: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        start = self.start.isoformat()

        end = self.end.isoformat()

        ground_station: Union[None, int]
        ground_station = self.ground_station

        transmitter = self.transmitter

        norad_cat_id = self.norad_cat_id

        payload = self.payload

        waterfall = self.waterfall

        station_name = self.station_name

        station_lat = self.station_lat

        station_lng = self.station_lng

        station_alt = self.station_alt

        vetted_status = self.vetted_status

        vetted_user = self.vetted_user

        vetted_datetime = self.vetted_datetime

        archived = self.archived

        archive_url: Union[None, str]
        archive_url = self.archive_url

        status = self.status

        waterfall_status = self.waterfall_status

        waterfall_status_user: Union[None, int]
        waterfall_status_user = self.waterfall_status_user

        waterfall_status_datetime: Union[None, str]
        if isinstance(self.waterfall_status_datetime, datetime.datetime):
            waterfall_status_datetime = self.waterfall_status_datetime.isoformat()
        else:
            waterfall_status_datetime = self.waterfall_status_datetime

        rise_azimuth: Union[None, float]
        rise_azimuth = self.rise_azimuth

        set_azimuth: Union[None, float]
        set_azimuth = self.set_azimuth

        max_altitude: Union[None, float]
        max_altitude = self.max_altitude

        transmitter_uuid = self.transmitter_uuid

        transmitter_description = self.transmitter_description

        transmitter_type = self.transmitter_type.value

        transmitter_uplink_low: Union[None, int]
        transmitter_uplink_low = self.transmitter_uplink_low

        transmitter_uplink_high: Union[None, int]
        transmitter_uplink_high = self.transmitter_uplink_high

        transmitter_uplink_drift: Union[None, int]
        transmitter_uplink_drift = self.transmitter_uplink_drift

        transmitter_downlink_low: Union[None, int]
        transmitter_downlink_low = self.transmitter_downlink_low

        transmitter_downlink_high: Union[None, int]
        transmitter_downlink_high = self.transmitter_downlink_high

        transmitter_downlink_drift: Union[None, int]
        transmitter_downlink_drift = self.transmitter_downlink_drift

        transmitter_mode: Union[None, str]
        transmitter_mode = self.transmitter_mode

        transmitter_invert = self.transmitter_invert

        transmitter_baud: Union[None, float]
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

        demoddata: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.demoddata, Unset):
            demoddata = []
            for demoddata_item_data in self.demoddata:
                demoddata_item = demoddata_item_data.to_dict()
                demoddata.append(demoddata_item)

        client_version = self.client_version

        client_metadata = self.client_metadata

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "start": start,
                "end": end,
                "ground_station": ground_station,
                "transmitter": transmitter,
                "norad_cat_id": norad_cat_id,
                "payload": payload,
                "waterfall": waterfall,
                "station_name": station_name,
                "station_lat": station_lat,
                "station_lng": station_lng,
                "station_alt": station_alt,
                "vetted_status": vetted_status,
                "vetted_user": vetted_user,
                "vetted_datetime": vetted_datetime,
                "archived": archived,
                "archive_url": archive_url,
                "status": status,
                "waterfall_status": waterfall_status,
                "waterfall_status_user": waterfall_status_user,
                "waterfall_status_datetime": waterfall_status_datetime,
                "rise_azimuth": rise_azimuth,
                "set_azimuth": set_azimuth,
                "max_altitude": max_altitude,
                "transmitter_uuid": transmitter_uuid,
                "transmitter_description": transmitter_description,
                "transmitter_type": transmitter_type,
                "transmitter_uplink_low": transmitter_uplink_low,
                "transmitter_uplink_high": transmitter_uplink_high,
                "transmitter_uplink_drift": transmitter_uplink_drift,
                "transmitter_downlink_low": transmitter_downlink_low,
                "transmitter_downlink_high": transmitter_downlink_high,
                "transmitter_downlink_drift": transmitter_downlink_drift,
                "transmitter_mode": transmitter_mode,
                "transmitter_invert": transmitter_invert,
                "transmitter_baud": transmitter_baud,
                "transmitter_updated": transmitter_updated,
                "transmitter_status": transmitter_status,
                "tle0": tle0,
                "tle1": tle1,
                "tle2": tle2,
                "center_frequency": center_frequency,
                "observer": observer,
                "observation_frequency": observation_frequency,
                "transmitter_unconfirmed": transmitter_unconfirmed,
            }
        )
        if demoddata is not UNSET:
            field_dict["demoddata"] = demoddata
        if client_version is not UNSET:
            field_dict["client_version"] = client_version
        if client_metadata is not UNSET:
            field_dict["client_metadata"] = client_metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.demod_data import DemodData

        d = src_dict.copy()
        id = d.pop("id")

        start = isoparse(d.pop("start"))

        end = isoparse(d.pop("end"))

        def _parse_ground_station(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        ground_station = _parse_ground_station(d.pop("ground_station"))

        transmitter = d.pop("transmitter")

        norad_cat_id = d.pop("norad_cat_id")

        payload = d.pop("payload")

        waterfall = d.pop("waterfall")

        station_name = d.pop("station_name")

        station_lat = d.pop("station_lat")

        station_lng = d.pop("station_lng")

        station_alt = d.pop("station_alt")

        vetted_status = d.pop("vetted_status")

        vetted_user = d.pop("vetted_user")

        vetted_datetime = d.pop("vetted_datetime")

        archived = d.pop("archived")

        def _parse_archive_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        archive_url = _parse_archive_url(d.pop("archive_url"))

        status = d.pop("status")

        waterfall_status = d.pop("waterfall_status")

        def _parse_waterfall_status_user(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        waterfall_status_user = _parse_waterfall_status_user(d.pop("waterfall_status_user"))

        def _parse_waterfall_status_datetime(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                waterfall_status_datetime_type_0 = isoparse(data)

                return waterfall_status_datetime_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        waterfall_status_datetime = _parse_waterfall_status_datetime(d.pop("waterfall_status_datetime"))

        def _parse_rise_azimuth(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        rise_azimuth = _parse_rise_azimuth(d.pop("rise_azimuth"))

        def _parse_set_azimuth(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        set_azimuth = _parse_set_azimuth(d.pop("set_azimuth"))

        def _parse_max_altitude(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        max_altitude = _parse_max_altitude(d.pop("max_altitude"))

        transmitter_uuid = d.pop("transmitter_uuid")

        transmitter_description = d.pop("transmitter_description")

        transmitter_type = TransmitterTypeEnum(d.pop("transmitter_type"))

        def _parse_transmitter_uplink_low(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        transmitter_uplink_low = _parse_transmitter_uplink_low(d.pop("transmitter_uplink_low"))

        def _parse_transmitter_uplink_high(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        transmitter_uplink_high = _parse_transmitter_uplink_high(d.pop("transmitter_uplink_high"))

        def _parse_transmitter_uplink_drift(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        transmitter_uplink_drift = _parse_transmitter_uplink_drift(d.pop("transmitter_uplink_drift"))

        def _parse_transmitter_downlink_low(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        transmitter_downlink_low = _parse_transmitter_downlink_low(d.pop("transmitter_downlink_low"))

        def _parse_transmitter_downlink_high(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        transmitter_downlink_high = _parse_transmitter_downlink_high(d.pop("transmitter_downlink_high"))

        def _parse_transmitter_downlink_drift(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        transmitter_downlink_drift = _parse_transmitter_downlink_drift(d.pop("transmitter_downlink_drift"))

        def _parse_transmitter_mode(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        transmitter_mode = _parse_transmitter_mode(d.pop("transmitter_mode"))

        transmitter_invert = d.pop("transmitter_invert")

        def _parse_transmitter_baud(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        transmitter_baud = _parse_transmitter_baud(d.pop("transmitter_baud"))

        transmitter_updated = d.pop("transmitter_updated")

        transmitter_status = d.pop("transmitter_status")

        tle0 = d.pop("tle0")

        tle1 = d.pop("tle1")

        tle2 = d.pop("tle2")

        center_frequency = d.pop("center_frequency")

        observer = d.pop("observer")

        observation_frequency = d.pop("observation_frequency")

        transmitter_unconfirmed = d.pop("transmitter_unconfirmed")

        demoddata = []
        _demoddata = d.pop("demoddata", UNSET)
        for demoddata_item_data in _demoddata or []:
            demoddata_item = DemodData.from_dict(demoddata_item_data)

            demoddata.append(demoddata_item)

        client_version = d.pop("client_version", UNSET)

        client_metadata = d.pop("client_metadata", UNSET)

        observation = cls(
            id=id,
            start=start,
            end=end,
            ground_station=ground_station,
            transmitter=transmitter,
            norad_cat_id=norad_cat_id,
            payload=payload,
            waterfall=waterfall,
            station_name=station_name,
            station_lat=station_lat,
            station_lng=station_lng,
            station_alt=station_alt,
            vetted_status=vetted_status,
            vetted_user=vetted_user,
            vetted_datetime=vetted_datetime,
            archived=archived,
            archive_url=archive_url,
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
            demoddata=demoddata,
            client_version=client_version,
            client_metadata=client_metadata,
        )

        observation.additional_properties = d
        return observation

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
