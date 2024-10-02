import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewObservation")


@_attrs_define
class NewObservation:
    """SatNOGS Network New Observation API Serializer

    Attributes:
        start (datetime.datetime):
        end (datetime.datetime):
        ground_station (int):
        transmitter_uuid (str):
        center_frequency (Union[Unset, int]):
    """

    start: datetime.datetime
    end: datetime.datetime
    ground_station: int
    transmitter_uuid: str
    center_frequency: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start = self.start.isoformat()

        end = self.end.isoformat()

        ground_station = self.ground_station

        transmitter_uuid = self.transmitter_uuid

        center_frequency = self.center_frequency

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start": start,
                "end": end,
                "ground_station": ground_station,
                "transmitter_uuid": transmitter_uuid,
            }
        )
        if center_frequency is not UNSET:
            field_dict["center_frequency"] = center_frequency

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        start = self.start.isoformat().encode()

        end = self.end.isoformat().encode()

        ground_station = (None, str(self.ground_station).encode(), "text/plain")

        transmitter_uuid = (None, str(self.transmitter_uuid).encode(), "text/plain")

        center_frequency = (
            self.center_frequency
            if isinstance(self.center_frequency, Unset)
            else (None, str(self.center_frequency).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "start": start,
                "end": end,
                "ground_station": ground_station,
                "transmitter_uuid": transmitter_uuid,
            }
        )
        if center_frequency is not UNSET:
            field_dict["center_frequency"] = center_frequency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start = isoparse(d.pop("start"))

        end = isoparse(d.pop("end"))

        ground_station = d.pop("ground_station")

        transmitter_uuid = d.pop("transmitter_uuid")

        center_frequency = d.pop("center_frequency", UNSET)

        new_observation = cls(
            start=start,
            end=end,
            ground_station=ground_station,
            transmitter_uuid=transmitter_uuid,
            center_frequency=center_frequency,
        )

        new_observation.additional_properties = d
        return new_observation

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
