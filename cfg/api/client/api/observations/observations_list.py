import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.observations_list_status import ObservationsListStatus
from ...models.observations_list_transmitter_type import ObservationsListTransmitterType
from ...models.observations_list_vetted_status import ObservationsListVettedStatus
from ...models.observations_list_waterfall_status import ObservationsListWaterfallStatus
from ...models.paginated_observation_list import PaginatedObservationList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cursor: Union[Unset, str] = UNSET,
    end: Union[Unset, datetime.datetime] = UNSET,
    ground_station: Union[Unset, int] = UNSET,
    id: Union[Unset, int] = UNSET,
    observation_id: Union[Unset, List[int]] = UNSET,
    observer: Union[Unset, int] = UNSET,
    satellite_norad_cat_id: Union[Unset, int] = UNSET,
    start: Union[Unset, datetime.datetime] = UNSET,
    status: Union[Unset, ObservationsListStatus] = UNSET,
    transmitter_mode: Union[Unset, str] = UNSET,
    transmitter_type: Union[Unset, ObservationsListTransmitterType] = UNSET,
    transmitter_uuid: Union[Unset, str] = UNSET,
    vetted_status: Union[Unset, ObservationsListVettedStatus] = UNSET,
    vetted_user: Union[Unset, int] = UNSET,
    waterfall_status: Union[Unset, ObservationsListWaterfallStatus] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["cursor"] = cursor

    json_end: Union[Unset, str] = UNSET
    if not isinstance(end, Unset):
        json_end = end.isoformat()
    params["end"] = json_end

    params["ground_station"] = ground_station

    params["id"] = id

    json_observation_id: Union[Unset, List[int]] = UNSET
    if not isinstance(observation_id, Unset):
        json_observation_id = observation_id

    params["observation_id"] = json_observation_id

    params["observer"] = observer

    params["satellite__norad_cat_id"] = satellite_norad_cat_id

    json_start: Union[Unset, str] = UNSET
    if not isinstance(start, Unset):
        json_start = start.isoformat()
    params["start"] = json_start

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["transmitter_mode"] = transmitter_mode

    json_transmitter_type: Union[Unset, str] = UNSET
    if not isinstance(transmitter_type, Unset):
        json_transmitter_type = transmitter_type.value

    params["transmitter_type"] = json_transmitter_type

    params["transmitter_uuid"] = transmitter_uuid

    json_vetted_status: Union[Unset, str] = UNSET
    if not isinstance(vetted_status, Unset):
        json_vetted_status = vetted_status.value

    params["vetted_status"] = json_vetted_status

    params["vetted_user"] = vetted_user

    json_waterfall_status: Union[Unset, int] = UNSET
    if not isinstance(waterfall_status, Unset):
        json_waterfall_status = waterfall_status.value

    params["waterfall_status"] = json_waterfall_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/observations/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedObservationList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedObservationList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedObservationList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, str] = UNSET,
    end: Union[Unset, datetime.datetime] = UNSET,
    ground_station: Union[Unset, int] = UNSET,
    id: Union[Unset, int] = UNSET,
    observation_id: Union[Unset, List[int]] = UNSET,
    observer: Union[Unset, int] = UNSET,
    satellite_norad_cat_id: Union[Unset, int] = UNSET,
    start: Union[Unset, datetime.datetime] = UNSET,
    status: Union[Unset, ObservationsListStatus] = UNSET,
    transmitter_mode: Union[Unset, str] = UNSET,
    transmitter_type: Union[Unset, ObservationsListTransmitterType] = UNSET,
    transmitter_uuid: Union[Unset, str] = UNSET,
    vetted_status: Union[Unset, ObservationsListVettedStatus] = UNSET,
    vetted_user: Union[Unset, int] = UNSET,
    waterfall_status: Union[Unset, ObservationsListWaterfallStatus] = UNSET,
) -> Response[PaginatedObservationList]:
    """SatNOGS Network Observation API view class

    Args:
        cursor (Union[Unset, str]):
        end (Union[Unset, datetime.datetime]):
        ground_station (Union[Unset, int]):
        id (Union[Unset, int]):
        observation_id (Union[Unset, List[int]]):
        observer (Union[Unset, int]):
        satellite_norad_cat_id (Union[Unset, int]):
        start (Union[Unset, datetime.datetime]):
        status (Union[Unset, ObservationsListStatus]):
        transmitter_mode (Union[Unset, str]):
        transmitter_type (Union[Unset, ObservationsListTransmitterType]):
        transmitter_uuid (Union[Unset, str]):
        vetted_status (Union[Unset, ObservationsListVettedStatus]):
        vetted_user (Union[Unset, int]):
        waterfall_status (Union[Unset, ObservationsListWaterfallStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedObservationList]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        end=end,
        ground_station=ground_station,
        id=id,
        observation_id=observation_id,
        observer=observer,
        satellite_norad_cat_id=satellite_norad_cat_id,
        start=start,
        status=status,
        transmitter_mode=transmitter_mode,
        transmitter_type=transmitter_type,
        transmitter_uuid=transmitter_uuid,
        vetted_status=vetted_status,
        vetted_user=vetted_user,
        waterfall_status=waterfall_status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, str] = UNSET,
    end: Union[Unset, datetime.datetime] = UNSET,
    ground_station: Union[Unset, int] = UNSET,
    id: Union[Unset, int] = UNSET,
    observation_id: Union[Unset, List[int]] = UNSET,
    observer: Union[Unset, int] = UNSET,
    satellite_norad_cat_id: Union[Unset, int] = UNSET,
    start: Union[Unset, datetime.datetime] = UNSET,
    status: Union[Unset, ObservationsListStatus] = UNSET,
    transmitter_mode: Union[Unset, str] = UNSET,
    transmitter_type: Union[Unset, ObservationsListTransmitterType] = UNSET,
    transmitter_uuid: Union[Unset, str] = UNSET,
    vetted_status: Union[Unset, ObservationsListVettedStatus] = UNSET,
    vetted_user: Union[Unset, int] = UNSET,
    waterfall_status: Union[Unset, ObservationsListWaterfallStatus] = UNSET,
) -> Optional[PaginatedObservationList]:
    """SatNOGS Network Observation API view class

    Args:
        cursor (Union[Unset, str]):
        end (Union[Unset, datetime.datetime]):
        ground_station (Union[Unset, int]):
        id (Union[Unset, int]):
        observation_id (Union[Unset, List[int]]):
        observer (Union[Unset, int]):
        satellite_norad_cat_id (Union[Unset, int]):
        start (Union[Unset, datetime.datetime]):
        status (Union[Unset, ObservationsListStatus]):
        transmitter_mode (Union[Unset, str]):
        transmitter_type (Union[Unset, ObservationsListTransmitterType]):
        transmitter_uuid (Union[Unset, str]):
        vetted_status (Union[Unset, ObservationsListVettedStatus]):
        vetted_user (Union[Unset, int]):
        waterfall_status (Union[Unset, ObservationsListWaterfallStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedObservationList
    """

    return sync_detailed(
        client=client,
        cursor=cursor,
        end=end,
        ground_station=ground_station,
        id=id,
        observation_id=observation_id,
        observer=observer,
        satellite_norad_cat_id=satellite_norad_cat_id,
        start=start,
        status=status,
        transmitter_mode=transmitter_mode,
        transmitter_type=transmitter_type,
        transmitter_uuid=transmitter_uuid,
        vetted_status=vetted_status,
        vetted_user=vetted_user,
        waterfall_status=waterfall_status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, str] = UNSET,
    end: Union[Unset, datetime.datetime] = UNSET,
    ground_station: Union[Unset, int] = UNSET,
    id: Union[Unset, int] = UNSET,
    observation_id: Union[Unset, List[int]] = UNSET,
    observer: Union[Unset, int] = UNSET,
    satellite_norad_cat_id: Union[Unset, int] = UNSET,
    start: Union[Unset, datetime.datetime] = UNSET,
    status: Union[Unset, ObservationsListStatus] = UNSET,
    transmitter_mode: Union[Unset, str] = UNSET,
    transmitter_type: Union[Unset, ObservationsListTransmitterType] = UNSET,
    transmitter_uuid: Union[Unset, str] = UNSET,
    vetted_status: Union[Unset, ObservationsListVettedStatus] = UNSET,
    vetted_user: Union[Unset, int] = UNSET,
    waterfall_status: Union[Unset, ObservationsListWaterfallStatus] = UNSET,
) -> Response[PaginatedObservationList]:
    """SatNOGS Network Observation API view class

    Args:
        cursor (Union[Unset, str]):
        end (Union[Unset, datetime.datetime]):
        ground_station (Union[Unset, int]):
        id (Union[Unset, int]):
        observation_id (Union[Unset, List[int]]):
        observer (Union[Unset, int]):
        satellite_norad_cat_id (Union[Unset, int]):
        start (Union[Unset, datetime.datetime]):
        status (Union[Unset, ObservationsListStatus]):
        transmitter_mode (Union[Unset, str]):
        transmitter_type (Union[Unset, ObservationsListTransmitterType]):
        transmitter_uuid (Union[Unset, str]):
        vetted_status (Union[Unset, ObservationsListVettedStatus]):
        vetted_user (Union[Unset, int]):
        waterfall_status (Union[Unset, ObservationsListWaterfallStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedObservationList]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        end=end,
        ground_station=ground_station,
        id=id,
        observation_id=observation_id,
        observer=observer,
        satellite_norad_cat_id=satellite_norad_cat_id,
        start=start,
        status=status,
        transmitter_mode=transmitter_mode,
        transmitter_type=transmitter_type,
        transmitter_uuid=transmitter_uuid,
        vetted_status=vetted_status,
        vetted_user=vetted_user,
        waterfall_status=waterfall_status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, str] = UNSET,
    end: Union[Unset, datetime.datetime] = UNSET,
    ground_station: Union[Unset, int] = UNSET,
    id: Union[Unset, int] = UNSET,
    observation_id: Union[Unset, List[int]] = UNSET,
    observer: Union[Unset, int] = UNSET,
    satellite_norad_cat_id: Union[Unset, int] = UNSET,
    start: Union[Unset, datetime.datetime] = UNSET,
    status: Union[Unset, ObservationsListStatus] = UNSET,
    transmitter_mode: Union[Unset, str] = UNSET,
    transmitter_type: Union[Unset, ObservationsListTransmitterType] = UNSET,
    transmitter_uuid: Union[Unset, str] = UNSET,
    vetted_status: Union[Unset, ObservationsListVettedStatus] = UNSET,
    vetted_user: Union[Unset, int] = UNSET,
    waterfall_status: Union[Unset, ObservationsListWaterfallStatus] = UNSET,
) -> Optional[PaginatedObservationList]:
    """SatNOGS Network Observation API view class

    Args:
        cursor (Union[Unset, str]):
        end (Union[Unset, datetime.datetime]):
        ground_station (Union[Unset, int]):
        id (Union[Unset, int]):
        observation_id (Union[Unset, List[int]]):
        observer (Union[Unset, int]):
        satellite_norad_cat_id (Union[Unset, int]):
        start (Union[Unset, datetime.datetime]):
        status (Union[Unset, ObservationsListStatus]):
        transmitter_mode (Union[Unset, str]):
        transmitter_type (Union[Unset, ObservationsListTransmitterType]):
        transmitter_uuid (Union[Unset, str]):
        vetted_status (Union[Unset, ObservationsListVettedStatus]):
        vetted_user (Union[Unset, int]):
        waterfall_status (Union[Unset, ObservationsListWaterfallStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedObservationList
    """

    return (
        await asyncio_detailed(
            client=client,
            cursor=cursor,
            end=end,
            ground_station=ground_station,
            id=id,
            observation_id=observation_id,
            observer=observer,
            satellite_norad_cat_id=satellite_norad_cat_id,
            start=start,
            status=status,
            transmitter_mode=transmitter_mode,
            transmitter_type=transmitter_type,
            transmitter_uuid=transmitter_uuid,
            vetted_status=vetted_status,
            vetted_user=vetted_user,
            waterfall_status=waterfall_status,
        )
    ).parsed
