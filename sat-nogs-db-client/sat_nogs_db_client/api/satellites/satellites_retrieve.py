from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.satellite import Satellite
from ...models.satellites_retrieve_format import SatellitesRetrieveFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    satellite_identifier_sat_id: str,
    *,
    format_: Union[Unset, SatellitesRetrieveFormat] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_format_: Union[Unset, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/satellites/{satellite_identifier_sat_id}/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Satellite]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Satellite.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Satellite]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    satellite_identifier_sat_id: str,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, SatellitesRetrieveFormat] = UNSET,
) -> Response[Satellite]:
    """Retrieve details on a single satellite in SatNOGS DB

    Args:
        satellite_identifier_sat_id (str):
        format_ (Union[Unset, SatellitesRetrieveFormat]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Satellite]
    """

    kwargs = _get_kwargs(
        satellite_identifier_sat_id=satellite_identifier_sat_id,
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    satellite_identifier_sat_id: str,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, SatellitesRetrieveFormat] = UNSET,
) -> Optional[Satellite]:
    """Retrieve details on a single satellite in SatNOGS DB

    Args:
        satellite_identifier_sat_id (str):
        format_ (Union[Unset, SatellitesRetrieveFormat]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Satellite
    """

    return sync_detailed(
        satellite_identifier_sat_id=satellite_identifier_sat_id,
        client=client,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    satellite_identifier_sat_id: str,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, SatellitesRetrieveFormat] = UNSET,
) -> Response[Satellite]:
    """Retrieve details on a single satellite in SatNOGS DB

    Args:
        satellite_identifier_sat_id (str):
        format_ (Union[Unset, SatellitesRetrieveFormat]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Satellite]
    """

    kwargs = _get_kwargs(
        satellite_identifier_sat_id=satellite_identifier_sat_id,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    satellite_identifier_sat_id: str,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, SatellitesRetrieveFormat] = UNSET,
) -> Optional[Satellite]:
    """Retrieve details on a single satellite in SatNOGS DB

    Args:
        satellite_identifier_sat_id (str):
        format_ (Union[Unset, SatellitesRetrieveFormat]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Satellite
    """

    return (
        await asyncio_detailed(
            satellite_identifier_sat_id=satellite_identifier_sat_id,
            client=client,
            format_=format_,
        )
    ).parsed
