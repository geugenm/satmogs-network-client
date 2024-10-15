from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.new_artifact import NewArtifact
from ...models.new_artifact_request import NewArtifactRequest
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        NewArtifactRequest,
        NewArtifactRequest,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/artifacts/",
    }

    if isinstance(body, NewArtifactRequest):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, NewArtifactRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[NewArtifact]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = NewArtifact.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[NewArtifact]:
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
        NewArtifactRequest,
        NewArtifactRequest,
    ],
) -> Response[NewArtifact]:
    """Creates observation artifact from an [HDF5 formatted file][hdf5ref]
    * Requires session or key authentication to create an artifact

    [hdf5ref]: https://en.wikipedia.org/wiki/Hierarchical_Data_Format

    Args:
        body (NewArtifactRequest): SatNOGS Network New Artifact API Serializer
        body (NewArtifactRequest): SatNOGS Network New Artifact API Serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NewArtifact]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: Union[
        NewArtifactRequest,
        NewArtifactRequest,
    ],
) -> Optional[NewArtifact]:
    """Creates observation artifact from an [HDF5 formatted file][hdf5ref]
    * Requires session or key authentication to create an artifact

    [hdf5ref]: https://en.wikipedia.org/wiki/Hierarchical_Data_Format

    Args:
        body (NewArtifactRequest): SatNOGS Network New Artifact API Serializer
        body (NewArtifactRequest): SatNOGS Network New Artifact API Serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NewArtifact
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        NewArtifactRequest,
        NewArtifactRequest,
    ],
) -> Response[NewArtifact]:
    """Creates observation artifact from an [HDF5 formatted file][hdf5ref]
    * Requires session or key authentication to create an artifact

    [hdf5ref]: https://en.wikipedia.org/wiki/Hierarchical_Data_Format

    Args:
        body (NewArtifactRequest): SatNOGS Network New Artifact API Serializer
        body (NewArtifactRequest): SatNOGS Network New Artifact API Serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NewArtifact]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Union[
        NewArtifactRequest,
        NewArtifactRequest,
    ],
) -> Optional[NewArtifact]:
    """Creates observation artifact from an [HDF5 formatted file][hdf5ref]
    * Requires session or key authentication to create an artifact

    [hdf5ref]: https://en.wikipedia.org/wiki/Hierarchical_Data_Format

    Args:
        body (NewArtifactRequest): SatNOGS Network New Artifact API Serializer
        body (NewArtifactRequest): SatNOGS Network New Artifact API Serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NewArtifact
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
