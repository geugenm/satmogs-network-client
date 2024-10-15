import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.iaru_coordination_enum import IaruCoordinationEnum
from ..models.service_enum import ServiceEnum
from ..models.status_enum import StatusEnum
from ..models.type_enum import TypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transmitter_request_itu_notification import TransmitterRequestItuNotification


T = TypeVar("T", bound="TransmitterRequest")


@_attrs_define
class TransmitterRequest:
    """SatNOGS DB Transmitter API Serializer

    Attributes:
        description (str): Short description for this entry, like: UHF 9k6 AFSK Telemetry
        updated (datetime.datetime):
        type (Union[Unset, TypeEnum]):
        uplink_low (Union[None, Unset, int]): Frequency (in Hz) for the uplink, or bottom of the uplink range for a
            transponder
        uplink_high (Union[None, Unset, int]): Frequency (in Hz) for the top of the uplink range for a transponder
        uplink_drift (Union[None, Unset, int]): Receiver drift from the published uplink frequency, stored in parts
            per billion (PPB)
        downlink_low (Union[None, Unset, int]): Frequency (in Hz) for the downlink, or bottom of the downlink range
            for a transponder
        downlink_high (Union[None, Unset, int]): Frequency (in Hz) for the top of the downlink range for a transponder
        downlink_drift (Union[None, Unset, int]): Transmitter drift from the published downlink frequency, stored in
            parts per billion (PPB)
        invert (Union[Unset, bool]): True if this is an inverted transponder
        baud (Union[None, Unset, float]): The number of modulated symbols that the transmitter sends every second
        status (Union[Unset, StatusEnum]):
        citation (Union[Unset, str]): A reference (preferrably URL) for this entry or edit
        service (Union[Unset, ServiceEnum]):
        iaru_coordination (Union[Unset, IaruCoordinationEnum]):
        iaru_coordination_url (Union[Unset, str]): URL for more details on this frequency coordination
        itu_notification (Union[Unset, TransmitterRequestItuNotification]):
    """

    description: str
    updated: datetime.datetime
    type: Union[Unset, TypeEnum] = UNSET
    uplink_low: Union[None, Unset, int] = UNSET
    uplink_high: Union[None, Unset, int] = UNSET
    uplink_drift: Union[None, Unset, int] = UNSET
    downlink_low: Union[None, Unset, int] = UNSET
    downlink_high: Union[None, Unset, int] = UNSET
    downlink_drift: Union[None, Unset, int] = UNSET
    invert: Union[Unset, bool] = UNSET
    baud: Union[None, Unset, float] = UNSET
    status: Union[Unset, StatusEnum] = UNSET
    citation: Union[Unset, str] = UNSET
    service: Union[Unset, ServiceEnum] = UNSET
    iaru_coordination: Union[Unset, IaruCoordinationEnum] = UNSET
    iaru_coordination_url: Union[Unset, str] = UNSET
    itu_notification: Union[Unset, "TransmitterRequestItuNotification"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        updated = self.updated.isoformat()

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        uplink_low: Union[None, Unset, int]
        if isinstance(self.uplink_low, Unset):
            uplink_low = UNSET
        else:
            uplink_low = self.uplink_low

        uplink_high: Union[None, Unset, int]
        if isinstance(self.uplink_high, Unset):
            uplink_high = UNSET
        else:
            uplink_high = self.uplink_high

        uplink_drift: Union[None, Unset, int]
        if isinstance(self.uplink_drift, Unset):
            uplink_drift = UNSET
        else:
            uplink_drift = self.uplink_drift

        downlink_low: Union[None, Unset, int]
        if isinstance(self.downlink_low, Unset):
            downlink_low = UNSET
        else:
            downlink_low = self.downlink_low

        downlink_high: Union[None, Unset, int]
        if isinstance(self.downlink_high, Unset):
            downlink_high = UNSET
        else:
            downlink_high = self.downlink_high

        downlink_drift: Union[None, Unset, int]
        if isinstance(self.downlink_drift, Unset):
            downlink_drift = UNSET
        else:
            downlink_drift = self.downlink_drift

        invert = self.invert

        baud: Union[None, Unset, float]
        if isinstance(self.baud, Unset):
            baud = UNSET
        else:
            baud = self.baud

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        citation = self.citation

        service: Union[Unset, str] = UNSET
        if not isinstance(self.service, Unset):
            service = self.service.value

        iaru_coordination: Union[Unset, str] = UNSET
        if not isinstance(self.iaru_coordination, Unset):
            iaru_coordination = self.iaru_coordination.value

        iaru_coordination_url = self.iaru_coordination_url

        itu_notification: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.itu_notification, Unset):
            itu_notification = self.itu_notification.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "updated": updated,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type
        if uplink_low is not UNSET:
            field_dict["uplink_low"] = uplink_low
        if uplink_high is not UNSET:
            field_dict["uplink_high"] = uplink_high
        if uplink_drift is not UNSET:
            field_dict["uplink_drift"] = uplink_drift
        if downlink_low is not UNSET:
            field_dict["downlink_low"] = downlink_low
        if downlink_high is not UNSET:
            field_dict["downlink_high"] = downlink_high
        if downlink_drift is not UNSET:
            field_dict["downlink_drift"] = downlink_drift
        if invert is not UNSET:
            field_dict["invert"] = invert
        if baud is not UNSET:
            field_dict["baud"] = baud
        if status is not UNSET:
            field_dict["status"] = status
        if citation is not UNSET:
            field_dict["citation"] = citation
        if service is not UNSET:
            field_dict["service"] = service
        if iaru_coordination is not UNSET:
            field_dict["iaru_coordination"] = iaru_coordination
        if iaru_coordination_url is not UNSET:
            field_dict["iaru_coordination_url"] = iaru_coordination_url
        if itu_notification is not UNSET:
            field_dict["itu_notification"] = itu_notification

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.transmitter_request_itu_notification import TransmitterRequestItuNotification

        d = src_dict.copy()
        description = d.pop("description")

        updated = isoparse(d.pop("updated"))

        _type = d.pop("type", UNSET)
        type: Union[Unset, TypeEnum]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = TypeEnum(_type)

        def _parse_uplink_low(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        uplink_low = _parse_uplink_low(d.pop("uplink_low", UNSET))

        def _parse_uplink_high(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        uplink_high = _parse_uplink_high(d.pop("uplink_high", UNSET))

        def _parse_uplink_drift(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        uplink_drift = _parse_uplink_drift(d.pop("uplink_drift", UNSET))

        def _parse_downlink_low(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        downlink_low = _parse_downlink_low(d.pop("downlink_low", UNSET))

        def _parse_downlink_high(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        downlink_high = _parse_downlink_high(d.pop("downlink_high", UNSET))

        def _parse_downlink_drift(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        downlink_drift = _parse_downlink_drift(d.pop("downlink_drift", UNSET))

        invert = d.pop("invert", UNSET)

        def _parse_baud(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        baud = _parse_baud(d.pop("baud", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, StatusEnum]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = StatusEnum(_status)

        citation = d.pop("citation", UNSET)

        _service = d.pop("service", UNSET)
        service: Union[Unset, ServiceEnum]
        if isinstance(_service, Unset):
            service = UNSET
        else:
            service = ServiceEnum(_service)

        _iaru_coordination = d.pop("iaru_coordination", UNSET)
        iaru_coordination: Union[Unset, IaruCoordinationEnum]
        if isinstance(_iaru_coordination, Unset):
            iaru_coordination = UNSET
        else:
            iaru_coordination = IaruCoordinationEnum(_iaru_coordination)

        iaru_coordination_url = d.pop("iaru_coordination_url", UNSET)

        _itu_notification = d.pop("itu_notification", UNSET)
        itu_notification: Union[Unset, TransmitterRequestItuNotification]
        if isinstance(_itu_notification, Unset):
            itu_notification = UNSET
        else:
            itu_notification = TransmitterRequestItuNotification.from_dict(_itu_notification)

        transmitter_request = cls(
            description=description,
            updated=updated,
            type=type,
            uplink_low=uplink_low,
            uplink_high=uplink_high,
            uplink_drift=uplink_drift,
            downlink_low=downlink_low,
            downlink_high=downlink_high,
            downlink_drift=downlink_drift,
            invert=invert,
            baud=baud,
            status=status,
            citation=citation,
            service=service,
            iaru_coordination=iaru_coordination,
            iaru_coordination_url=iaru_coordination_url,
            itu_notification=itu_notification,
        )

        transmitter_request.additional_properties = d
        return transmitter_request

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
