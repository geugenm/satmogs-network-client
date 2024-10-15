from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.telemetry import Telemetry


T = TypeVar("T", bound="PaginatedTelemetryList")


@_attrs_define
class PaginatedTelemetryList:
    """
    Attributes:
        next_ (Union[None, Unset, str]):  Example: http://api.example.org/accounts/?cursor=cD00ODY%3D".
        previous (Union[None, Unset, str]):  Example: http://api.example.org/accounts/?cursor=cj0xJnA9NDg3.
        results (Union[Unset, List['Telemetry']]):
    """

    next_: Union[None, Unset, str] = UNSET
    previous: Union[None, Unset, str] = UNSET
    results: Union[Unset, List["Telemetry"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        next_: Union[None, Unset, str]
        if isinstance(self.next_, Unset):
            next_ = UNSET
        else:
            next_ = self.next_

        previous: Union[None, Unset, str]
        if isinstance(self.previous, Unset):
            previous = UNSET
        else:
            previous = self.previous

        results: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if next_ is not UNSET:
            field_dict["next"] = next_
        if previous is not UNSET:
            field_dict["previous"] = previous
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.telemetry import Telemetry

        d = src_dict.copy()

        def _parse_next_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        next_ = _parse_next_(d.pop("next", UNSET))

        def _parse_previous(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        previous = _parse_previous(d.pop("previous", UNSET))

        results = []
        _results = d.pop("results", UNSET)
        for results_item_data in _results or []:
            results_item = Telemetry.from_dict(results_item_data)

            results.append(results_item)

        paginated_telemetry_list = cls(
            next_=next_,
            previous=previous,
            results=results,
        )

        paginated_telemetry_list.additional_properties = d
        return paginated_telemetry_list

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
