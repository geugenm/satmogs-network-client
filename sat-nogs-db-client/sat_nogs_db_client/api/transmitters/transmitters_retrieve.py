from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.transmitter import Transmitter
from ...models.transmitters_retrieve_format import TransmittersRetrieveFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: str,
    *,
    format_: Union[Unset, TransmittersRetrieveFormat] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_format_: Union[Unset, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/transmitters/{uuid}/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Transmitter]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Transmitter.from_dict(response.json())

        return response_200
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
    uuid: str,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, TransmittersRetrieveFormat] = UNSET,
) -> Response[Transmitter]:
    """View into the Transmitter entities in the SatNOGS DB database.
    Transmitters are inclusive of Transceivers and Transponders

    Args:
        uuid (str):
        format_ (Union[Unset, TransmittersRetrieveFormat]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Transmitter]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: str,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, TransmittersRetrieveFormat] = UNSET,
) -> Optional[Transmitter]:
    """View into the Transmitter entities in the SatNOGS DB database.
    Transmitters are inclusive of Transceivers and Transponders

    Args:
        uuid (str):
        format_ (Union[Unset, TransmittersRetrieveFormat]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Transmitter
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, TransmittersRetrieveFormat] = UNSET,
) -> Response[Transmitter]:
    """View into the Transmitter entities in the SatNOGS DB database.
    Transmitters are inclusive of Transceivers and Transponders

    Args:
        uuid (str):
        format_ (Union[Unset, TransmittersRetrieveFormat]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Transmitter]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: str,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, TransmittersRetrieveFormat] = UNSET,
) -> Optional[Transmitter]:
    """View into the Transmitter entities in the SatNOGS DB database.
    Transmitters are inclusive of Transceivers and Transponders

    Args:
        uuid (str):
        format_ (Union[Unset, TransmittersRetrieveFormat]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Transmitter
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            format_=format_,
        )
    ).parsed
