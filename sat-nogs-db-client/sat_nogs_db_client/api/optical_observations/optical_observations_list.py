import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.optical_observation import OpticalObservation
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    after: Union[Unset, datetime.datetime] = UNSET,
    before: Union[Unset, datetime.datetime] = UNSET,
    last_n: Union[Unset, float] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_after: Union[Unset, str] = UNSET
    if not isinstance(after, Unset):
        json_after = after.isoformat()
    params["after"] = json_after

    json_before: Union[Unset, str] = UNSET
    if not isinstance(before, Unset):
        json_before = before.isoformat()
    params["before"] = json_before

    params["last_n"] = last_n

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/optical-observations/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["OpticalObservation"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = OpticalObservation.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["OpticalObservation"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    after: Union[Unset, datetime.datetime] = UNSET,
    before: Union[Unset, datetime.datetime] = UNSET,
    last_n: Union[Unset, float] = UNSET,
) -> Response[List["OpticalObservation"]]:
    """View for Optical Identifications

    Args:
        after (Union[Unset, datetime.datetime]):
        before (Union[Unset, datetime.datetime]):
        last_n (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['OpticalObservation']]
    """

    kwargs = _get_kwargs(
        after=after,
        before=before,
        last_n=last_n,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    after: Union[Unset, datetime.datetime] = UNSET,
    before: Union[Unset, datetime.datetime] = UNSET,
    last_n: Union[Unset, float] = UNSET,
) -> Optional[List["OpticalObservation"]]:
    """View for Optical Identifications

    Args:
        after (Union[Unset, datetime.datetime]):
        before (Union[Unset, datetime.datetime]):
        last_n (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['OpticalObservation']
    """

    return sync_detailed(
        client=client,
        after=after,
        before=before,
        last_n=last_n,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    after: Union[Unset, datetime.datetime] = UNSET,
    before: Union[Unset, datetime.datetime] = UNSET,
    last_n: Union[Unset, float] = UNSET,
) -> Response[List["OpticalObservation"]]:
    """View for Optical Identifications

    Args:
        after (Union[Unset, datetime.datetime]):
        before (Union[Unset, datetime.datetime]):
        last_n (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['OpticalObservation']]
    """

    kwargs = _get_kwargs(
        after=after,
        before=before,
        last_n=last_n,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    after: Union[Unset, datetime.datetime] = UNSET,
    before: Union[Unset, datetime.datetime] = UNSET,
    last_n: Union[Unset, float] = UNSET,
) -> Optional[List["OpticalObservation"]]:
    """View for Optical Identifications

    Args:
        after (Union[Unset, datetime.datetime]):
        before (Union[Unset, datetime.datetime]):
        last_n (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['OpticalObservation']
    """

    return (
        await asyncio_detailed(
            client=client,
            after=after,
            before=before,
            last_n=last_n,
        )
    ).parsed
