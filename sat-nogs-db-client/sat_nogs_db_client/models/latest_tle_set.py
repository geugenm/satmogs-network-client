import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="LatestTleSet")


@_attrs_define
class LatestTleSet:
    """SatNOGS DB LatestTleSet API Serializer

    Attributes:
        tle0 (str):
        tle1 (str):
        tle2 (str):
        tle_source (str):
        sat_id (str):
        norad_cat_id (int):
        updated (datetime.datetime):
    """

    tle0: str
    tle1: str
    tle2: str
    tle_source: str
    sat_id: str
    norad_cat_id: int
    updated: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tle0 = self.tle0

        tle1 = self.tle1

        tle2 = self.tle2

        tle_source = self.tle_source

        sat_id = self.sat_id

        norad_cat_id = self.norad_cat_id

        updated = self.updated.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tle0": tle0,
                "tle1": tle1,
                "tle2": tle2,
                "tle_source": tle_source,
                "sat_id": sat_id,
                "norad_cat_id": norad_cat_id,
                "updated": updated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tle0 = d.pop("tle0")

        tle1 = d.pop("tle1")

        tle2 = d.pop("tle2")

        tle_source = d.pop("tle_source")

        sat_id = d.pop("sat_id")

        norad_cat_id = d.pop("norad_cat_id")

        updated = isoparse(d.pop("updated"))

        latest_tle_set = cls(
            tle0=tle0,
            tle1=tle1,
            tle2=tle2,
            tle_source=tle_source,
            sat_id=sat_id,
            norad_cat_id=norad_cat_id,
            updated=updated,
        )

        latest_tle_set.additional_properties = d
        return latest_tle_set

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
