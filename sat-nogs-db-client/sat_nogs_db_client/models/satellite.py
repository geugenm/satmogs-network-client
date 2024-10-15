import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.satellite_associated_satellites import SatelliteAssociatedSatellites
    from ..models.satellite_telemetries import SatelliteTelemetries


T = TypeVar("T", bound="Satellite")


@_attrs_define
class Satellite:
    """SatNOGS DB Satellite API Serializer

    Attributes:
        sat_id (str):
        norad_cat_id (int):
        norad_follow_id (int):
        name (str):
        names (str):
        image (str):
        status (str):
        decayed (datetime.datetime):
        launched (datetime.datetime):
        deployed (datetime.datetime):
        website (str):
        operator (str):
        countries (str):
        telemetries (SatelliteTelemetries):
        updated (datetime.datetime):
        citation (str):
        is_frequency_violator (bool):
        associated_satellites (SatelliteAssociatedSatellites):
    """

    sat_id: str
    norad_cat_id: int
    norad_follow_id: int
    name: str
    names: str
    image: str
    status: str
    decayed: datetime.datetime
    launched: datetime.datetime
    deployed: datetime.datetime
    website: str
    operator: str
    countries: str
    telemetries: "SatelliteTelemetries"
    updated: datetime.datetime
    citation: str
    is_frequency_violator: bool
    associated_satellites: "SatelliteAssociatedSatellites"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sat_id = self.sat_id

        norad_cat_id = self.norad_cat_id

        norad_follow_id = self.norad_follow_id

        name = self.name

        names = self.names

        image = self.image

        status = self.status

        decayed = self.decayed.isoformat()

        launched = self.launched.isoformat()

        deployed = self.deployed.isoformat()

        website = self.website

        operator = self.operator

        countries = self.countries

        telemetries = self.telemetries.to_dict()

        updated = self.updated.isoformat()

        citation = self.citation

        is_frequency_violator = self.is_frequency_violator

        associated_satellites = self.associated_satellites.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sat_id": sat_id,
                "norad_cat_id": norad_cat_id,
                "norad_follow_id": norad_follow_id,
                "name": name,
                "names": names,
                "image": image,
                "status": status,
                "decayed": decayed,
                "launched": launched,
                "deployed": deployed,
                "website": website,
                "operator": operator,
                "countries": countries,
                "telemetries": telemetries,
                "updated": updated,
                "citation": citation,
                "is_frequency_violator": is_frequency_violator,
                "associated_satellites": associated_satellites,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.satellite_associated_satellites import SatelliteAssociatedSatellites
        from ..models.satellite_telemetries import SatelliteTelemetries

        d = src_dict.copy()
        sat_id = d.pop("sat_id")

        norad_cat_id = d.pop("norad_cat_id")

        norad_follow_id = d.pop("norad_follow_id")

        name = d.pop("name")

        names = d.pop("names")

        image = d.pop("image")

        status = d.pop("status")

        decayed = isoparse(d.pop("decayed"))

        launched = isoparse(d.pop("launched"))

        deployed = isoparse(d.pop("deployed"))

        website = d.pop("website")

        operator = d.pop("operator")

        countries = d.pop("countries")

        telemetries = SatelliteTelemetries.from_dict(d.pop("telemetries"))

        updated = isoparse(d.pop("updated"))

        citation = d.pop("citation")

        is_frequency_violator = d.pop("is_frequency_violator")

        associated_satellites = SatelliteAssociatedSatellites.from_dict(d.pop("associated_satellites"))

        satellite = cls(
            sat_id=sat_id,
            norad_cat_id=norad_cat_id,
            norad_follow_id=norad_follow_id,
            name=name,
            names=names,
            image=image,
            status=status,
            decayed=decayed,
            launched=launched,
            deployed=deployed,
            website=website,
            operator=operator,
            countries=countries,
            telemetries=telemetries,
            updated=updated,
            citation=citation,
            is_frequency_violator=is_frequency_violator,
            associated_satellites=associated_satellites,
        )

        satellite.additional_properties = d
        return satellite

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
