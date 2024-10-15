from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TelemetryRequest")


@_attrs_define
class TelemetryRequest:
    """SatNOGS DB Telemetry API Serializer

    Attributes:
        version (Union[Unset, str]):
        observation_id (Union[None, Unset, int]):
        station_id (Union[None, Unset, int]):
    """

    version: Union[Unset, str] = UNSET
    observation_id: Union[None, Unset, int] = UNSET
    station_id: Union[None, Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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
        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if observation_id is not UNSET:
            field_dict["observation_id"] = observation_id
        if station_id is not UNSET:
            field_dict["station_id"] = station_id

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        version = self.version if isinstance(self.version, Unset) else (None, str(self.version).encode(), "text/plain")

        observation_id: Union[Tuple[None, bytes, str], Unset]

        if isinstance(self.observation_id, Unset):
            observation_id = UNSET
        elif isinstance(self.observation_id, int):
            observation_id = (None, str(self.observation_id).encode(), "text/plain")
        else:
            observation_id = (None, str(self.observation_id).encode(), "text/plain")

        station_id: Union[Tuple[None, bytes, str], Unset]

        if isinstance(self.station_id, Unset):
            station_id = UNSET
        elif isinstance(self.station_id, int):
            station_id = (None, str(self.station_id).encode(), "text/plain")
        else:
            station_id = (None, str(self.station_id).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if observation_id is not UNSET:
            field_dict["observation_id"] = observation_id
        if station_id is not UNSET:
            field_dict["station_id"] = station_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
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

        telemetry_request = cls(
            version=version,
            observation_id=observation_id,
            station_id=station_id,
        )

        telemetry_request.additional_properties = d
        return telemetry_request

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
