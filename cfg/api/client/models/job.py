import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Job")


@_attrs_define
class Job:
    """SatNOGS Network Job API Serializer

    Attributes:
        id (int):
        start (datetime.datetime):
        end (datetime.datetime):
        tle0 (str):
        tle1 (str):
        tle2 (str):
        frequency (str):
        mode (str):
        transmitter (str):
        baud (str):
        ground_station (Union[None, Unset, int]):
    """

    id: int
    start: datetime.datetime
    end: datetime.datetime
    tle0: str
    tle1: str
    tle2: str
    frequency: str
    mode: str
    transmitter: str
    baud: str
    ground_station: Union[None, Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        start = self.start.isoformat()

        end = self.end.isoformat()

        tle0 = self.tle0

        tle1 = self.tle1

        tle2 = self.tle2

        frequency = self.frequency

        mode = self.mode

        transmitter = self.transmitter

        baud = self.baud

        ground_station: Union[None, Unset, int]
        if isinstance(self.ground_station, Unset):
            ground_station = UNSET
        else:
            ground_station = self.ground_station

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "start": start,
                "end": end,
                "tle0": tle0,
                "tle1": tle1,
                "tle2": tle2,
                "frequency": frequency,
                "mode": mode,
                "transmitter": transmitter,
                "baud": baud,
            }
        )
        if ground_station is not UNSET:
            field_dict["ground_station"] = ground_station

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        start = isoparse(d.pop("start"))

        end = isoparse(d.pop("end"))

        tle0 = d.pop("tle0")

        tle1 = d.pop("tle1")

        tle2 = d.pop("tle2")

        frequency = d.pop("frequency")

        mode = d.pop("mode")

        transmitter = d.pop("transmitter")

        baud = d.pop("baud")

        def _parse_ground_station(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        ground_station = _parse_ground_station(d.pop("ground_station", UNSET))

        job = cls(
            id=id,
            start=start,
            end=end,
            tle0=tle0,
            tle1=tle1,
            tle2=tle2,
            frequency=frequency,
            mode=mode,
            transmitter=transmitter,
            baud=baud,
            ground_station=ground_station,
        )

        job.additional_properties = d
        return job

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
