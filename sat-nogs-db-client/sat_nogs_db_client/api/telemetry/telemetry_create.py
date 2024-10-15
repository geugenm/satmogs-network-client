from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.telemetry_create_format import TelemetryCreateFormat
from ...models.telemetry_request import TelemetryRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Union[
        TelemetryRequest,
        TelemetryRequest,
    ],
    format_: Union[Unset, TelemetryCreateFormat] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    json_format_: Union[Unset, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/telemetry/",
        "params": params,
    }

    if isinstance(body, TelemetryRequest):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, TelemetryRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.CREATED:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        TelemetryRequest,
        TelemetryRequest,
    ],
    format_: Union[Unset, TelemetryCreateFormat] = UNSET,
) -> Response[Any]:
    """Creates a frame of telemetry data from a satellite observation.

    Args:
        format_ (Union[Unset, TelemetryCreateFormat]):
        body (TelemetryRequest): SatNOGS DB Telemetry API Serializer
        body (TelemetryRequest): SatNOGS DB Telemetry API Serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        TelemetryRequest,
        TelemetryRequest,
    ],
    format_: Union[Unset, TelemetryCreateFormat] = UNSET,
) -> Response[Any]:
    """Creates a frame of telemetry data from a satellite observation.

    Args:
        format_ (Union[Unset, TelemetryCreateFormat]):
        body (TelemetryRequest): SatNOGS DB Telemetry API Serializer
        body (TelemetryRequest): SatNOGS DB Telemetry API Serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
