from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateObservation")


@_attrs_define
class UpdateObservation:
    """SatNOGS Network Observation API Serializer for uploading audio and waterfall.
    This is Serializer is used temporarily until waterfall_old and payload_old fields are removed.

        Attributes:
            id (int):
            payload (Union[Unset, str]):
            waterfall (Union[Unset, str]):
            client_metadata (Union[Unset, str]):
            client_version (Union[Unset, str]):
    """

    id: int
    payload: Union[Unset, str] = UNSET
    waterfall: Union[Unset, str] = UNSET
    client_metadata: Union[Unset, str] = UNSET
    client_version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        payload = self.payload

        waterfall = self.waterfall

        client_metadata = self.client_metadata

        client_version = self.client_version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if payload is not UNSET:
            field_dict["payload"] = payload
        if waterfall is not UNSET:
            field_dict["waterfall"] = waterfall
        if client_metadata is not UNSET:
            field_dict["client_metadata"] = client_metadata
        if client_version is not UNSET:
            field_dict["client_version"] = client_version

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = (None, str(self.id).encode(), "text/plain")

        payload = self.payload if isinstance(self.payload, Unset) else (None, str(self.payload).encode(), "text/plain")

        waterfall = (
            self.waterfall if isinstance(self.waterfall, Unset) else (None, str(self.waterfall).encode(), "text/plain")
        )

        client_metadata = (
            self.client_metadata
            if isinstance(self.client_metadata, Unset)
            else (None, str(self.client_metadata).encode(), "text/plain")
        )

        client_version = (
            self.client_version
            if isinstance(self.client_version, Unset)
            else (None, str(self.client_version).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "id": id,
            }
        )
        if payload is not UNSET:
            field_dict["payload"] = payload
        if waterfall is not UNSET:
            field_dict["waterfall"] = waterfall
        if client_metadata is not UNSET:
            field_dict["client_metadata"] = client_metadata
        if client_version is not UNSET:
            field_dict["client_version"] = client_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        payload = d.pop("payload", UNSET)

        waterfall = d.pop("waterfall", UNSET)

        client_metadata = d.pop("client_metadata", UNSET)

        client_version = d.pop("client_version", UNSET)

        update_observation = cls(
            id=id,
            payload=payload,
            waterfall=waterfall,
            client_metadata=client_metadata,
            client_version=client_version,
        )

        update_observation.additional_properties = d
        return update_observation

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
