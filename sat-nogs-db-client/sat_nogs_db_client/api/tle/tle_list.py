from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.latest_tle_set import LatestTleSet
from ...models.tle_list_format import TleListFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    format_: Union[Unset, TleListFormat] = UNSET,
    norad_cat_id: Union[Unset, int] = UNSET,
    sat_id: Union[Unset, str] = UNSET,
    tle_source: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_format_: Union[Unset, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params["norad_cat_id"] = norad_cat_id

    params["sat_id"] = sat_id

    params["tle_source"] = tle_source

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/tle/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["LatestTleSet"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = LatestTleSet.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["LatestTleSet"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, TleListFormat] = UNSET,
    norad_cat_id: Union[Unset, int] = UNSET,
    sat_id: Union[Unset, str] = UNSET,
    tle_source: Union[Unset, str] = UNSET,
) -> Response[List["LatestTleSet"]]:
    """Read-only view into the most recent two-line elements (TLE) in the SatNOGS DB
    database

    Args:
        format_ (Union[Unset, TleListFormat]):
        norad_cat_id (Union[Unset, int]):
        sat_id (Union[Unset, str]):
        tle_source (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['LatestTleSet']]
    """

    kwargs = _get_kwargs(
        format_=format_,
        norad_cat_id=norad_cat_id,
        sat_id=sat_id,
        tle_source=tle_source,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, TleListFormat] = UNSET,
    norad_cat_id: Union[Unset, int] = UNSET,
    sat_id: Union[Unset, str] = UNSET,
    tle_source: Union[Unset, str] = UNSET,
) -> Optional[List["LatestTleSet"]]:
    """Read-only view into the most recent two-line elements (TLE) in the SatNOGS DB
    database

    Args:
        format_ (Union[Unset, TleListFormat]):
        norad_cat_id (Union[Unset, int]):
        sat_id (Union[Unset, str]):
        tle_source (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['LatestTleSet']
    """

    return sync_detailed(
        client=client,
        format_=format_,
        norad_cat_id=norad_cat_id,
        sat_id=sat_id,
        tle_source=tle_source,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, TleListFormat] = UNSET,
    norad_cat_id: Union[Unset, int] = UNSET,
    sat_id: Union[Unset, str] = UNSET,
    tle_source: Union[Unset, str] = UNSET,
) -> Response[List["LatestTleSet"]]:
    """Read-only view into the most recent two-line elements (TLE) in the SatNOGS DB
    database

    Args:
        format_ (Union[Unset, TleListFormat]):
        norad_cat_id (Union[Unset, int]):
        sat_id (Union[Unset, str]):
        tle_source (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['LatestTleSet']]
    """

    kwargs = _get_kwargs(
        format_=format_,
        norad_cat_id=norad_cat_id,
        sat_id=sat_id,
        tle_source=tle_source,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, TleListFormat] = UNSET,
    norad_cat_id: Union[Unset, int] = UNSET,
    sat_id: Union[Unset, str] = UNSET,
    tle_source: Union[Unset, str] = UNSET,
) -> Optional[List["LatestTleSet"]]:
    """Read-only view into the most recent two-line elements (TLE) in the SatNOGS DB
    database

    Args:
        format_ (Union[Unset, TleListFormat]):
        norad_cat_id (Union[Unset, int]):
        sat_id (Union[Unset, str]):
        tle_source (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['LatestTleSet']
    """

    return (
        await asyncio_detailed(
            client=client,
            format_=format_,
            norad_cat_id=norad_cat_id,
            sat_id=sat_id,
            tle_source=tle_source,
        )
    ).parsed
