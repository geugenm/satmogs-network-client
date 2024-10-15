from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.transmitter import Transmitter
from ...models.transmitters_list_format import TransmittersListFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    alive: Union[Unset, bool] = UNSET,
    format_: Union[Unset, TransmittersListFormat] = UNSET,
    mode: Union[Unset, int] = UNSET,
    sat_id: Union[Unset, str] = UNSET,
    satellite_norad_cat_id: Union[Unset, str] = UNSET,
    service: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    type: Union[Unset, str] = UNSET,
    uplink_mode: Union[Unset, int] = UNSET,
    uuid: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["alive"] = alive

    json_format_: Union[Unset, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params["mode"] = mode

    params["sat_id"] = sat_id

    params["satellite__norad_cat_id"] = satellite_norad_cat_id

    params["service"] = service

    params["status"] = status

    params["type"] = type

    params["uplink_mode"] = uplink_mode

    params["uuid"] = uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/transmitters/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["Transmitter"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Transmitter.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["Transmitter"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    alive: Union[Unset, bool] = UNSET,
    format_: Union[Unset, TransmittersListFormat] = UNSET,
    mode: Union[Unset, int] = UNSET,
    sat_id: Union[Unset, str] = UNSET,
    satellite_norad_cat_id: Union[Unset, str] = UNSET,
    service: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    type: Union[Unset, str] = UNSET,
    uplink_mode: Union[Unset, int] = UNSET,
    uuid: Union[Unset, str] = UNSET,
) -> Response[List["Transmitter"]]:
    """View into the Transmitter entities in the SatNOGS DB database.
    Transmitters are inclusive of Transceivers and Transponders

    Args:
        alive (Union[Unset, bool]):
        format_ (Union[Unset, TransmittersListFormat]):
        mode (Union[Unset, int]):
        sat_id (Union[Unset, str]):
        satellite_norad_cat_id (Union[Unset, str]):
        service (Union[Unset, str]):
        status (Union[Unset, str]):
        type (Union[Unset, str]):
        uplink_mode (Union[Unset, int]):
        uuid (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['Transmitter']]
    """

    kwargs = _get_kwargs(
        alive=alive,
        format_=format_,
        mode=mode,
        sat_id=sat_id,
        satellite_norad_cat_id=satellite_norad_cat_id,
        service=service,
        status=status,
        type=type,
        uplink_mode=uplink_mode,
        uuid=uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    alive: Union[Unset, bool] = UNSET,
    format_: Union[Unset, TransmittersListFormat] = UNSET,
    mode: Union[Unset, int] = UNSET,
    sat_id: Union[Unset, str] = UNSET,
    satellite_norad_cat_id: Union[Unset, str] = UNSET,
    service: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    type: Union[Unset, str] = UNSET,
    uplink_mode: Union[Unset, int] = UNSET,
    uuid: Union[Unset, str] = UNSET,
) -> Optional[List["Transmitter"]]:
    """View into the Transmitter entities in the SatNOGS DB database.
    Transmitters are inclusive of Transceivers and Transponders

    Args:
        alive (Union[Unset, bool]):
        format_ (Union[Unset, TransmittersListFormat]):
        mode (Union[Unset, int]):
        sat_id (Union[Unset, str]):
        satellite_norad_cat_id (Union[Unset, str]):
        service (Union[Unset, str]):
        status (Union[Unset, str]):
        type (Union[Unset, str]):
        uplink_mode (Union[Unset, int]):
        uuid (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['Transmitter']
    """

    return sync_detailed(
        client=client,
        alive=alive,
        format_=format_,
        mode=mode,
        sat_id=sat_id,
        satellite_norad_cat_id=satellite_norad_cat_id,
        service=service,
        status=status,
        type=type,
        uplink_mode=uplink_mode,
        uuid=uuid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    alive: Union[Unset, bool] = UNSET,
    format_: Union[Unset, TransmittersListFormat] = UNSET,
    mode: Union[Unset, int] = UNSET,
    sat_id: Union[Unset, str] = UNSET,
    satellite_norad_cat_id: Union[Unset, str] = UNSET,
    service: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    type: Union[Unset, str] = UNSET,
    uplink_mode: Union[Unset, int] = UNSET,
    uuid: Union[Unset, str] = UNSET,
) -> Response[List["Transmitter"]]:
    """View into the Transmitter entities in the SatNOGS DB database.
    Transmitters are inclusive of Transceivers and Transponders

    Args:
        alive (Union[Unset, bool]):
        format_ (Union[Unset, TransmittersListFormat]):
        mode (Union[Unset, int]):
        sat_id (Union[Unset, str]):
        satellite_norad_cat_id (Union[Unset, str]):
        service (Union[Unset, str]):
        status (Union[Unset, str]):
        type (Union[Unset, str]):
        uplink_mode (Union[Unset, int]):
        uuid (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['Transmitter']]
    """

    kwargs = _get_kwargs(
        alive=alive,
        format_=format_,
        mode=mode,
        sat_id=sat_id,
        satellite_norad_cat_id=satellite_norad_cat_id,
        service=service,
        status=status,
        type=type,
        uplink_mode=uplink_mode,
        uuid=uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    alive: Union[Unset, bool] = UNSET,
    format_: Union[Unset, TransmittersListFormat] = UNSET,
    mode: Union[Unset, int] = UNSET,
    sat_id: Union[Unset, str] = UNSET,
    satellite_norad_cat_id: Union[Unset, str] = UNSET,
    service: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    type: Union[Unset, str] = UNSET,
    uplink_mode: Union[Unset, int] = UNSET,
    uuid: Union[Unset, str] = UNSET,
) -> Optional[List["Transmitter"]]:
    """View into the Transmitter entities in the SatNOGS DB database.
    Transmitters are inclusive of Transceivers and Transponders

    Args:
        alive (Union[Unset, bool]):
        format_ (Union[Unset, TransmittersListFormat]):
        mode (Union[Unset, int]):
        sat_id (Union[Unset, str]):
        satellite_norad_cat_id (Union[Unset, str]):
        service (Union[Unset, str]):
        status (Union[Unset, str]):
        type (Union[Unset, str]):
        uplink_mode (Union[Unset, int]):
        uuid (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['Transmitter']
    """

    return (
        await asyncio_detailed(
            client=client,
            alive=alive,
            format_=format_,
            mode=mode,
            sat_id=sat_id,
            satellite_norad_cat_id=satellite_norad_cat_id,
            service=service,
            status=status,
            type=type,
            uplink_mode=uplink_mode,
            uuid=uuid,
        )
    ).parsed
