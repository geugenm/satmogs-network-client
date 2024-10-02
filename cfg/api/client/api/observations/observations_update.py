from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_observation import UpdateObservation
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    body: Union[
        UpdateObservation,
        UpdateObservation,
        UpdateObservation,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/api/observations/{id}/",
    }

    if isinstance(body, UpdateObservation):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateObservation):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, UpdateObservation):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UpdateObservation]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UpdateObservation.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[UpdateObservation]:
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
    body: Union[
        UpdateObservation,
        UpdateObservation,
        UpdateObservation,
    ],
) -> Response[UpdateObservation]:
    """Updates observation with audio, waterfall or demoded data

    Args:
        id (int):
        body (UpdateObservation): SatNOGS Network Observation API Serializer for uploading audio
            and waterfall.
            This is Serializer is used temporarily until waterfall_old and payload_old fields are
            removed.
        body (UpdateObservation): SatNOGS Network Observation API Serializer for uploading audio
            and waterfall.
            This is Serializer is used temporarily until waterfall_old and payload_old fields are
            removed.
        body (UpdateObservation): SatNOGS Network Observation API Serializer for uploading audio
            and waterfall.
            This is Serializer is used temporarily until waterfall_old and payload_old fields are
            removed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateObservation]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateObservation,
        UpdateObservation,
        UpdateObservation,
    ],
) -> Optional[UpdateObservation]:
    """Updates observation with audio, waterfall or demoded data

    Args:
        id (int):
        body (UpdateObservation): SatNOGS Network Observation API Serializer for uploading audio
            and waterfall.
            This is Serializer is used temporarily until waterfall_old and payload_old fields are
            removed.
        body (UpdateObservation): SatNOGS Network Observation API Serializer for uploading audio
            and waterfall.
            This is Serializer is used temporarily until waterfall_old and payload_old fields are
            removed.
        body (UpdateObservation): SatNOGS Network Observation API Serializer for uploading audio
            and waterfall.
            This is Serializer is used temporarily until waterfall_old and payload_old fields are
            removed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateObservation
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateObservation,
        UpdateObservation,
        UpdateObservation,
    ],
) -> Response[UpdateObservation]:
    """Updates observation with audio, waterfall or demoded data

    Args:
        id (int):
        body (UpdateObservation): SatNOGS Network Observation API Serializer for uploading audio
            and waterfall.
            This is Serializer is used temporarily until waterfall_old and payload_old fields are
            removed.
        body (UpdateObservation): SatNOGS Network Observation API Serializer for uploading audio
            and waterfall.
            This is Serializer is used temporarily until waterfall_old and payload_old fields are
            removed.
        body (UpdateObservation): SatNOGS Network Observation API Serializer for uploading audio
            and waterfall.
            This is Serializer is used temporarily until waterfall_old and payload_old fields are
            removed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateObservation]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateObservation,
        UpdateObservation,
        UpdateObservation,
    ],
) -> Optional[UpdateObservation]:
    """Updates observation with audio, waterfall or demoded data

    Args:
        id (int):
        body (UpdateObservation): SatNOGS Network Observation API Serializer for uploading audio
            and waterfall.
            This is Serializer is used temporarily until waterfall_old and payload_old fields are
            removed.
        body (UpdateObservation): SatNOGS Network Observation API Serializer for uploading audio
            and waterfall.
            This is Serializer is used temporarily until waterfall_old and payload_old fields are
            removed.
        body (UpdateObservation): SatNOGS Network Observation API Serializer for uploading audio
            and waterfall.
            This is Serializer is used temporarily until waterfall_old and payload_old fields are
            removed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateObservation
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
