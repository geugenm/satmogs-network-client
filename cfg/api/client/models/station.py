import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Station")


@_attrs_define
class Station:
    """SatNOGS Network Station API Serializer

    Attributes:
        id (int):
        name (str):
        altitude (int):
        min_horizon (str):
        antenna (str):
        created (datetime.datetime):
        status (str):
        observations (str):
        lat (Union[None, Unset, float]): eg. 38.01697
        lng (Union[None, Unset, float]): eg. 23.7314
        qthlocator (Union[Unset, str]):
        last_seen (Union[None, Unset, datetime.datetime]):
        description (Union[Unset, str]): Max 500 characters
        client_version (Union[Unset, str]):
        target_utilization (Union[None, Unset, int]): Target utilization factor for your station
    """

    id: int
    name: str
    altitude: int
    min_horizon: str
    antenna: str
    created: datetime.datetime
    status: str
    observations: str
    lat: Union[None, Unset, float] = UNSET
    lng: Union[None, Unset, float] = UNSET
    qthlocator: Union[Unset, str] = UNSET
    last_seen: Union[None, Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    client_version: Union[Unset, str] = UNSET
    target_utilization: Union[None, Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        altitude = self.altitude

        min_horizon = self.min_horizon

        antenna = self.antenna

        created = self.created.isoformat()

        status = self.status

        observations = self.observations

        lat: Union[None, Unset, float]
        if isinstance(self.lat, Unset):
            lat = UNSET
        else:
            lat = self.lat

        lng: Union[None, Unset, float]
        if isinstance(self.lng, Unset):
            lng = UNSET
        else:
            lng = self.lng

        qthlocator = self.qthlocator

        last_seen: Union[None, Unset, str]
        if isinstance(self.last_seen, Unset):
            last_seen = UNSET
        elif isinstance(self.last_seen, datetime.datetime):
            last_seen = self.last_seen.isoformat()
        else:
            last_seen = self.last_seen

        description = self.description

        client_version = self.client_version

        target_utilization: Union[None, Unset, int]
        if isinstance(self.target_utilization, Unset):
            target_utilization = UNSET
        else:
            target_utilization = self.target_utilization

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "altitude": altitude,
                "min_horizon": min_horizon,
                "antenna": antenna,
                "created": created,
                "status": status,
                "observations": observations,
            }
        )
        if lat is not UNSET:
            field_dict["lat"] = lat
        if lng is not UNSET:
            field_dict["lng"] = lng
        if qthlocator is not UNSET:
            field_dict["qthlocator"] = qthlocator
        if last_seen is not UNSET:
            field_dict["last_seen"] = last_seen
        if description is not UNSET:
            field_dict["description"] = description
        if client_version is not UNSET:
            field_dict["client_version"] = client_version
        if target_utilization is not UNSET:
            field_dict["target_utilization"] = target_utilization

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        altitude = d.pop("altitude")

        min_horizon = d.pop("min_horizon")

        antenna = d.pop("antenna")

        created = isoparse(d.pop("created"))

        status = d.pop("status")

        observations = d.pop("observations")

        def _parse_lat(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        lat = _parse_lat(d.pop("lat", UNSET))

        def _parse_lng(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        lng = _parse_lng(d.pop("lng", UNSET))

        qthlocator = d.pop("qthlocator", UNSET)

        def _parse_last_seen(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_seen_type_0 = isoparse(data)

                return last_seen_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_seen = _parse_last_seen(d.pop("last_seen", UNSET))

        description = d.pop("description", UNSET)

        client_version = d.pop("client_version", UNSET)

        def _parse_target_utilization(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        target_utilization = _parse_target_utilization(d.pop("target_utilization", UNSET))

        station = cls(
            id=id,
            name=name,
            altitude=altitude,
            min_horizon=min_horizon,
            antenna=antenna,
            created=created,
            status=status,
            observations=observations,
            lat=lat,
            lng=lng,
            qthlocator=qthlocator,
            last_seen=last_seen,
            description=description,
            client_version=client_version,
            target_utilization=target_utilization,
        )

        station.additional_properties = d
        return station

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
