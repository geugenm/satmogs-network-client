from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import File

T = TypeVar("T", bound="OpticalObservationCreateRequest")


@_attrs_define
class OpticalObservationCreateRequest:
    """Serializer for creating an Optical Observation

    Attributes:
        data (File):
        diagnostic_plot (File):
    """

    data: File
    diagnostic_plot: File
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = self.data.to_tuple()

        diagnostic_plot = self.diagnostic_plot.to_tuple()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "diagnostic_plot": diagnostic_plot,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        data = self.data.to_tuple()

        diagnostic_plot = self.diagnostic_plot.to_tuple()

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "data": data,
                "diagnostic_plot": diagnostic_plot,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        data = File(payload=BytesIO(d.pop("data")))

        diagnostic_plot = File(payload=BytesIO(d.pop("diagnostic_plot")))

        optical_observation_create_request = cls(
            data=data,
            diagnostic_plot=diagnostic_plot,
        )

        optical_observation_create_request.additional_properties = d
        return optical_observation_create_request

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
