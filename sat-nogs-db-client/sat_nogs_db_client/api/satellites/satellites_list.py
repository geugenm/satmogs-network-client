from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.satellite import Satellite
from ...models.satellites_list_format import SatellitesListFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    format_: Union[Unset, SatellitesListFormat] = UNSET,
    in_orbit: Union[Unset, bool] = UNSET,
    norad_cat_id: Union[Unset, str] = UNSET,
    sat_id: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_format_: Union[Unset, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params["in_orbit"] = in_orbit

    params["norad_cat_id"] = norad_cat_id

    params["sat_id"] = sat_id

    params["status"] = status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/satellites/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["Satellite"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Satellite.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["Satellite"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, SatellitesListFormat] = UNSET,
    in_orbit: Union[Unset, bool] = UNSET,
    norad_cat_id: Union[Unset, str] = UNSET,
    sat_id: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
) -> Response[List["Satellite"]]:
    """Retrieve a full or filtered list of satellites in SatNOGS DB

    Args:
        format_ (Union[Unset, SatellitesListFormat]):
        in_orbit (Union[Unset, bool]):
        norad_cat_id (Union[Unset, str]):
        sat_id (Union[Unset, str]):
        status (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['Satellite']]
    """

    kwargs = _get_kwargs(
        format_=format_,
        in_orbit=in_orbit,
        norad_cat_id=norad_cat_id,
        sat_id=sat_id,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, SatellitesListFormat] = UNSET,
    in_orbit: Union[Unset, bool] = UNSET,
    norad_cat_id: Union[Unset, str] = UNSET,
    sat_id: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
) -> Optional[List["Satellite"]]:
    """Retrieve a full or filtered list of satellites in SatNOGS DB

    Args:
        format_ (Union[Unset, SatellitesListFormat]):
        in_orbit (Union[Unset, bool]):
        norad_cat_id (Union[Unset, str]):
        sat_id (Union[Unset, str]):
        status (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['Satellite']
    """

    return sync_detailed(
        client=client,
        format_=format_,
        in_orbit=in_orbit,
        norad_cat_id=norad_cat_id,
        sat_id=sat_id,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, SatellitesListFormat] = UNSET,
    in_orbit: Union[Unset, bool] = UNSET,
    norad_cat_id: Union[Unset, str] = UNSET,
    sat_id: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
) -> Response[List["Satellite"]]:
    """Retrieve a full or filtered list of satellites in SatNOGS DB

    Args:
        format_ (Union[Unset, SatellitesListFormat]):
        in_orbit (Union[Unset, bool]):
        norad_cat_id (Union[Unset, str]):
        sat_id (Union[Unset, str]):
        status (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['Satellite']]
    """

    kwargs = _get_kwargs(
        format_=format_,
        in_orbit=in_orbit,
        norad_cat_id=norad_cat_id,
        sat_id=sat_id,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, SatellitesListFormat] = UNSET,
    in_orbit: Union[Unset, bool] = UNSET,
    norad_cat_id: Union[Unset, str] = UNSET,
    sat_id: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
) -> Optional[List["Satellite"]]:
    """Retrieve a full or filtered list of satellites in SatNOGS DB

    Args:
        format_ (Union[Unset, SatellitesListFormat]):
        in_orbit (Union[Unset, bool]):
        norad_cat_id (Union[Unset, str]):
        sat_id (Union[Unset, str]):
        status (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['Satellite']
    """

    return (
        await asyncio_detailed(
            client=client,
            format_=format_,
            in_orbit=in_orbit,
            norad_cat_id=norad_cat_id,
            sat_id=sat_id,
            status=status,
        )
    ).parsed
