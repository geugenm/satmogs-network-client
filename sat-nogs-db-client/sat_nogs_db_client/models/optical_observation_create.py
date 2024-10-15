from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OpticalObservationCreate")


@_attrs_define
class OpticalObservationCreate:
    """Serializer for creating an Optical Observation

    Attributes:
        data (str):
        diagnostic_plot (str):
    """

    data: str
    diagnostic_plot: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = self.data

        diagnostic_plot = self.diagnostic_plot

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        data = d.pop("data")

        diagnostic_plot = d.pop("diagnostic_plot")

        optical_observation_create = cls(
            data=data,
            diagnostic_plot=diagnostic_plot,
        )

        optical_observation_create.additional_properties = d
        return optical_observation_create

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
