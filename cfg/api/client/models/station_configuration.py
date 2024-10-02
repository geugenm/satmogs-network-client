from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.station_configuration_configuration import StationConfigurationConfiguration


T = TypeVar("T", bound="StationConfiguration")


@_attrs_define
class StationConfiguration:
    """SatNOGS Network Station Configuration API Serializer

    Attributes:
        configuration (Union[Unset, StationConfigurationConfiguration]):
    """

    configuration: Union[Unset, "StationConfigurationConfiguration"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        configuration: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if configuration is not UNSET:
            field_dict["configuration"] = configuration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.station_configuration_configuration import StationConfigurationConfiguration

        d = src_dict.copy()
        _configuration = d.pop("configuration", UNSET)
        configuration: Union[Unset, StationConfigurationConfiguration]
        if isinstance(_configuration, Unset):
            configuration = UNSET
        else:
            configuration = StationConfigurationConfiguration.from_dict(_configuration)

        station_configuration = cls(
            configuration=configuration,
        )

        station_configuration.additional_properties = d
        return station_configuration

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
