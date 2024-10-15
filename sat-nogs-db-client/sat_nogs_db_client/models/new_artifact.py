from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewArtifact")


@_attrs_define
class NewArtifact:
    """SatNOGS Network New Artifact API Serializer

    Attributes:
        artifact_file (Union[None, Unset, str]):
    """

    artifact_file: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        artifact_file: Union[None, Unset, str]
        if isinstance(self.artifact_file, Unset):
            artifact_file = UNSET
        else:
            artifact_file = self.artifact_file

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if artifact_file is not UNSET:
            field_dict["artifact_file"] = artifact_file

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_artifact_file(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        artifact_file = _parse_artifact_file(d.pop("artifact_file", UNSET))

        new_artifact = cls(
            artifact_file=artifact_file,
        )

        new_artifact.additional_properties = d
        return new_artifact

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
