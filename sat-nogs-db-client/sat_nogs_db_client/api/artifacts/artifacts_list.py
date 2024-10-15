from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_artifact_list import PaginatedArtifactList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    network_obs_id: Union[Unset, int] = UNSET,
    observation_ids: Union[Unset, List[int]] = UNSET,
    page: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["network_obs_id"] = network_obs_id

    json_observation_ids: Union[Unset, List[int]] = UNSET
    if not isinstance(observation_ids, Unset):
        json_observation_ids = observation_ids

    params["observation_ids"] = json_observation_ids

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/artifacts/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedArtifactList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedArtifactList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedArtifactList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    network_obs_id: Union[Unset, int] = UNSET,
    observation_ids: Union[Unset, List[int]] = UNSET,
    page: Union[Unset, int] = UNSET,
) -> Response[PaginatedArtifactList]:
    """Artifacts are file-formatted objects collected from a satellite observation.

    Args:
        network_obs_id (Union[Unset, int]):
        observation_ids (Union[Unset, List[int]]):
        page (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedArtifactList]
    """

    kwargs = _get_kwargs(
        network_obs_id=network_obs_id,
        observation_ids=observation_ids,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    network_obs_id: Union[Unset, int] = UNSET,
    observation_ids: Union[Unset, List[int]] = UNSET,
    page: Union[Unset, int] = UNSET,
) -> Optional[PaginatedArtifactList]:
    """Artifacts are file-formatted objects collected from a satellite observation.

    Args:
        network_obs_id (Union[Unset, int]):
        observation_ids (Union[Unset, List[int]]):
        page (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedArtifactList
    """

    return sync_detailed(
        client=client,
        network_obs_id=network_obs_id,
        observation_ids=observation_ids,
        page=page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    network_obs_id: Union[Unset, int] = UNSET,
    observation_ids: Union[Unset, List[int]] = UNSET,
    page: Union[Unset, int] = UNSET,
) -> Response[PaginatedArtifactList]:
    """Artifacts are file-formatted objects collected from a satellite observation.

    Args:
        network_obs_id (Union[Unset, int]):
        observation_ids (Union[Unset, List[int]]):
        page (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedArtifactList]
    """

    kwargs = _get_kwargs(
        network_obs_id=network_obs_id,
        observation_ids=observation_ids,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    network_obs_id: Union[Unset, int] = UNSET,
    observation_ids: Union[Unset, List[int]] = UNSET,
    page: Union[Unset, int] = UNSET,
) -> Optional[PaginatedArtifactList]:
    """Artifacts are file-formatted objects collected from a satellite observation.

    Args:
        network_obs_id (Union[Unset, int]):
        observation_ids (Union[Unset, List[int]]):
        page (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedArtifactList
    """

    return (
        await asyncio_detailed(
            client=client,
            network_obs_id=network_obs_id,
            observation_ids=observation_ids,
            page=page,
        )
    ).parsed
