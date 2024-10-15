from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Artifact")


@_attrs_define
class Artifact:
    """SatNOGS DB Artifacts API Serializer

    Attributes:
        id (int):
        network_obs_id (Union[None, Unset, int]):
        artifact_file (Union[None, Unset, str]):
    """

    id: int
    network_obs_id: Union[None, Unset, int] = UNSET
    artifact_file: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        network_obs_id: Union[None, Unset, int]
        if isinstance(self.network_obs_id, Unset):
            network_obs_id = UNSET
        else:
            network_obs_id = self.network_obs_id

        artifact_file: Union[None, Unset, str]
        if isinstance(self.artifact_file, Unset):
            artifact_file = UNSET
        else:
            artifact_file = self.artifact_file

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if network_obs_id is not UNSET:
            field_dict["network_obs_id"] = network_obs_id
        if artifact_file is not UNSET:
            field_dict["artifact_file"] = artifact_file

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        def _parse_network_obs_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        network_obs_id = _parse_network_obs_id(d.pop("network_obs_id", UNSET))

        def _parse_artifact_file(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        artifact_file = _parse_artifact_file(d.pop("artifact_file", UNSET))

        artifact = cls(
            id=id,
            network_obs_id=network_obs_id,
            artifact_file=artifact_file,
        )

        artifact.additional_properties = d
        return artifact

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
