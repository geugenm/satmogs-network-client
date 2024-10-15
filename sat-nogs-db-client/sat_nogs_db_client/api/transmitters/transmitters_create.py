from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.transmitter import Transmitter
from ...models.transmitter_request import TransmitterRequest
from ...models.transmitters_create_format import TransmittersCreateFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: TransmitterRequest,
    format_: Union[Unset, TransmittersCreateFormat] = UNSET,
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
        "url": "/api/transmitters/",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/ld+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Transmitter]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = Transmitter.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Transmitter]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: TransmitterRequest,
    format_: Union[Unset, TransmittersCreateFormat] = UNSET,
) -> Response[Transmitter]:
    """Creates a transmitter suggestion.

    Args:
        format_ (Union[Unset, TransmittersCreateFormat]):
        body (TransmitterRequest): SatNOGS DB Transmitter API Serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Transmitter]
    """

    kwargs = _get_kwargs(
        body=body,
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: TransmitterRequest,
    format_: Union[Unset, TransmittersCreateFormat] = UNSET,
) -> Optional[Transmitter]:
    """Creates a transmitter suggestion.

    Args:
        format_ (Union[Unset, TransmittersCreateFormat]):
        body (TransmitterRequest): SatNOGS DB Transmitter API Serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Transmitter
    """

    return sync_detailed(
        client=client,
        body=body,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: TransmitterRequest,
    format_: Union[Unset, TransmittersCreateFormat] = UNSET,
) -> Response[Transmitter]:
    """Creates a transmitter suggestion.

    Args:
        format_ (Union[Unset, TransmittersCreateFormat]):
        body (TransmitterRequest): SatNOGS DB Transmitter API Serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Transmitter]
    """

    kwargs = _get_kwargs(
        body=body,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: TransmitterRequest,
    format_: Union[Unset, TransmittersCreateFormat] = UNSET,
) -> Optional[Transmitter]:
    """Creates a transmitter suggestion.

    Args:
        format_ (Union[Unset, TransmittersCreateFormat]):
        body (TransmitterRequest): SatNOGS DB Transmitter API Serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Transmitter
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            format_=format_,
        )
    ).parsed
