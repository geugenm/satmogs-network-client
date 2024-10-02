from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_station_list import PaginatedStationList
from ...models.stations_list_status import StationsListStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client_version: Union[Unset, str] = UNSET,
    id: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    status: Union[Unset, StationsListStatus] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["client_version"] = client_version

    params["id"] = id

    params["name"] = name

    params["page"] = page

    json_status: Union[Unset, int] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/stations/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedStationList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedStationList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedStationList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    client_version: Union[Unset, str] = UNSET,
    id: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    status: Union[Unset, StationsListStatus] = UNSET,
) -> Response[PaginatedStationList]:
    """SatNOGS Network Station API view class

    Args:
        client_version (Union[Unset, str]):
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        page (Union[Unset, int]):
        status (Union[Unset, StationsListStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedStationList]
    """

    kwargs = _get_kwargs(
        client_version=client_version,
        id=id,
        name=name,
        page=page,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    client_version: Union[Unset, str] = UNSET,
    id: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    status: Union[Unset, StationsListStatus] = UNSET,
) -> Optional[PaginatedStationList]:
    """SatNOGS Network Station API view class

    Args:
        client_version (Union[Unset, str]):
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        page (Union[Unset, int]):
        status (Union[Unset, StationsListStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedStationList
    """

    return sync_detailed(
        client=client,
        client_version=client_version,
        id=id,
        name=name,
        page=page,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    client_version: Union[Unset, str] = UNSET,
    id: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    status: Union[Unset, StationsListStatus] = UNSET,
) -> Response[PaginatedStationList]:
    """SatNOGS Network Station API view class

    Args:
        client_version (Union[Unset, str]):
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        page (Union[Unset, int]):
        status (Union[Unset, StationsListStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedStationList]
    """

    kwargs = _get_kwargs(
        client_version=client_version,
        id=id,
        name=name,
        page=page,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    client_version: Union[Unset, str] = UNSET,
    id: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    status: Union[Unset, StationsListStatus] = UNSET,
) -> Optional[PaginatedStationList]:
    """SatNOGS Network Station API view class

    Args:
        client_version (Union[Unset, str]):
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        page (Union[Unset, int]):
        status (Union[Unset, StationsListStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedStationList
    """

    return (
        await asyncio_detailed(
            client=client,
            client_version=client_version,
            id=id,
            name=name,
            page=page,
            status=status,
        )
    ).parsed
