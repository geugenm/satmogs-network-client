from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.telemetry import Telemetry
from ...models.telemetry_retrieve_format import TelemetryRetrieveFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    format_: Union[Unset, TelemetryRetrieveFormat] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_format_: Union[Unset, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/telemetry/{id}/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Telemetry]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Telemetry.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Telemetry]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, TelemetryRetrieveFormat] = UNSET,
) -> Response[Telemetry]:
    """View into the Telemetry objects in the SatNOGS DB database. Currently,
    this table is inclusive of all data collected from satellite downlink
    observations

    Args:
        id (int):
        format_ (Union[Unset, TelemetryRetrieveFormat]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Telemetry]
    """

    kwargs = _get_kwargs(
        id=id,
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, TelemetryRetrieveFormat] = UNSET,
) -> Optional[Telemetry]:
    """View into the Telemetry objects in the SatNOGS DB database. Currently,
    this table is inclusive of all data collected from satellite downlink
    observations

    Args:
        id (int):
        format_ (Union[Unset, TelemetryRetrieveFormat]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Telemetry
    """

    return sync_detailed(
        id=id,
        client=client,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, TelemetryRetrieveFormat] = UNSET,
) -> Response[Telemetry]:
    """View into the Telemetry objects in the SatNOGS DB database. Currently,
    this table is inclusive of all data collected from satellite downlink
    observations

    Args:
        id (int):
        format_ (Union[Unset, TelemetryRetrieveFormat]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Telemetry]
    """

    kwargs = _get_kwargs(
        id=id,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, TelemetryRetrieveFormat] = UNSET,
) -> Optional[Telemetry]:
    """View into the Telemetry objects in the SatNOGS DB database. Currently,
    this table is inclusive of all data collected from satellite downlink
    observations

    Args:
        id (int):
        format_ (Union[Unset, TelemetryRetrieveFormat]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Telemetry
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            format_=format_,
        )
    ).parsed
