from io import BytesIO
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="NewArtifactRequest")


@_attrs_define
class NewArtifactRequest:
    """SatNOGS Network New Artifact API Serializer

    Attributes:
        artifact_file (Union[File, None, Unset]):
    """

    artifact_file: Union[File, None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        artifact_file: Union[FileJsonType, None, Unset]
        if isinstance(self.artifact_file, Unset):
            artifact_file = UNSET
        elif isinstance(self.artifact_file, File):
            artifact_file = self.artifact_file.to_tuple()

        else:
            artifact_file = self.artifact_file

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if artifact_file is not UNSET:
            field_dict["artifact_file"] = artifact_file

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        artifact_file: Union[Tuple[None, bytes, str], Unset]

        if isinstance(self.artifact_file, Unset):
            artifact_file = UNSET
        elif isinstance(self.artifact_file, File):
            artifact_file = self.artifact_file.to_tuple()
        else:
            artifact_file = (None, str(self.artifact_file).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if artifact_file is not UNSET:
            field_dict["artifact_file"] = artifact_file

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_artifact_file(data: object) -> Union[File, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                artifact_file_type_0 = File(payload=BytesIO(data))

                return artifact_file_type_0
            except:  # noqa: E722
                pass
            return cast(Union[File, None, Unset], data)

        artifact_file = _parse_artifact_file(d.pop("artifact_file", UNSET))

        new_artifact_request = cls(
            artifact_file=artifact_file,
        )

        new_artifact_request.additional_properties = d
        return new_artifact_request

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
