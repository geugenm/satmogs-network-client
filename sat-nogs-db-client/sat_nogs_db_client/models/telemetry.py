from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.telemetry_associated_satellites import TelemetryAssociatedSatellites


T = TypeVar("T", bound="Telemetry")


@_attrs_define
class Telemetry:
    """SatNOGS DB Telemetry API Serializer

    Attributes:
        sat_id (str):
        norad_cat_id (int):
        transmitter (str):
        decoded (str):
        frame (str):
        associated_satellites (TelemetryAssociatedSatellites):
        version (Union[Unset, str]):
        observation_id (Union[None, Unset, int]):
        station_id (Union[None, Unset, int]):
    """

    sat_id: str
    norad_cat_id: int
    transmitter: str
    decoded: str
    frame: str
    associated_satellites: "TelemetryAssociatedSatellites"
    version: Union[Unset, str] = UNSET
    observation_id: Union[None, Unset, int] = UNSET
    station_id: Union[None, Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sat_id = self.sat_id

        norad_cat_id = self.norad_cat_id

        transmitter = self.transmitter

        decoded = self.decoded

        frame = self.frame

        associated_satellites = self.associated_satellites.to_dict()

        version = self.version

        observation_id: Union[None, Unset, int]
        if isinstance(self.observation_id, Unset):
            observation_id = UNSET
        else:
            observation_id = self.observation_id

        station_id: Union[None, Unset, int]
        if isinstance(self.station_id, Unset):
            station_id = UNSET
        else:
            station_id = self.station_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sat_id": sat_id,
                "norad_cat_id": norad_cat_id,
                "transmitter": transmitter,
                "decoded": decoded,
                "frame": frame,
                "associated_satellites": associated_satellites,
            }
        )
        if version is not UNSET:
            field_dict["version"] = version
        if observation_id is not UNSET:
            field_dict["observation_id"] = observation_id
        if station_id is not UNSET:
            field_dict["station_id"] = station_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.telemetry_associated_satellites import TelemetryAssociatedSatellites

        d = src_dict.copy()
        sat_id = d.pop("sat_id")

        norad_cat_id = d.pop("norad_cat_id")

        transmitter = d.pop("transmitter")

        decoded = d.pop("decoded")

        frame = d.pop("frame")

        associated_satellites = TelemetryAssociatedSatellites.from_dict(d.pop("associated_satellites"))

        version = d.pop("version", UNSET)

        def _parse_observation_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        observation_id = _parse_observation_id(d.pop("observation_id", UNSET))

        def _parse_station_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        station_id = _parse_station_id(d.pop("station_id", UNSET))

        telemetry = cls(
            sat_id=sat_id,
            norad_cat_id=norad_cat_id,
            transmitter=transmitter,
            decoded=decoded,
            frame=frame,
            associated_satellites=associated_satellites,
            version=version,
            observation_id=observation_id,
            station_id=station_id,
        )

        telemetry.additional_properties = d
        return telemetry

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
