import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.optical_identification import OpticalIdentification
    from ..models.optical_observation_data import OpticalObservationData


T = TypeVar("T", bound="OpticalObservation")


@_attrs_define
class OpticalObservation:
    """Serializer for Optical Observation

    Attributes:
        id (int):
        start (datetime.datetime):
        station_id (int):
        diagnostic_plot_url (str):
        identifications (List['OpticalIdentification']):
        uploader (Union[None, int]):
        data (OpticalObservationData):
    """

    id: int
    start: datetime.datetime
    station_id: int
    diagnostic_plot_url: str
    identifications: List["OpticalIdentification"]
    uploader: Union[None, int]
    data: "OpticalObservationData"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        start = self.start.isoformat()

        station_id = self.station_id

        diagnostic_plot_url = self.diagnostic_plot_url

        identifications = []
        for identifications_item_data in self.identifications:
            identifications_item = identifications_item_data.to_dict()
            identifications.append(identifications_item)

        uploader: Union[None, int]
        uploader = self.uploader

        data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "start": start,
                "station_id": station_id,
                "diagnostic_plot_url": diagnostic_plot_url,
                "identifications": identifications,
                "uploader": uploader,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.optical_identification import OpticalIdentification
        from ..models.optical_observation_data import OpticalObservationData

        d = src_dict.copy()
        id = d.pop("id")

        start = isoparse(d.pop("start"))

        station_id = d.pop("station_id")

        diagnostic_plot_url = d.pop("diagnostic_plot_url")

        identifications = []
        _identifications = d.pop("identifications")
        for identifications_item_data in _identifications:
            identifications_item = OpticalIdentification.from_dict(identifications_item_data)

            identifications.append(identifications_item)

        def _parse_uploader(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        uploader = _parse_uploader(d.pop("uploader"))

        data = OpticalObservationData.from_dict(d.pop("data"))

        optical_observation = cls(
            id=id,
            start=start,
            station_id=station_id,
            diagnostic_plot_url=diagnostic_plot_url,
            identifications=identifications,
            uploader=uploader,
            data=data,
        )

        optical_observation.additional_properties = d
        return optical_observation

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
