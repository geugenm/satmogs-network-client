import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_telemetry_list import PaginatedTelemetryList
from ...models.telemetry_list_format import TelemetryListFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    app_source: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    end: Union[Unset, datetime.datetime] = UNSET,
    format_: Union[Unset, TelemetryListFormat] = UNSET,
    is_decoded: Union[Unset, bool] = UNSET,
    observer: Union[Unset, str] = UNSET,
    sat_id: Union[Unset, str] = UNSET,
    satellite: Union[Unset, str] = UNSET,
    start: Union[Unset, datetime.datetime] = UNSET,
    transmitter: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["app_source"] = app_source

    params["cursor"] = cursor

    json_end: Union[Unset, str] = UNSET
    if not isinstance(end, Unset):
        json_end = end.isoformat()
    params["end"] = json_end

    json_format_: Union[Unset, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params["is_decoded"] = is_decoded

    params["observer"] = observer

    params["sat_id"] = sat_id

    params["satellite"] = satellite

    json_start: Union[Unset, str] = UNSET
    if not isinstance(start, Unset):
        json_start = start.isoformat()
    params["start"] = json_start

    params["transmitter"] = transmitter

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/telemetry/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedTelemetryList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedTelemetryList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedTelemetryList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    app_source: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    end: Union[Unset, datetime.datetime] = UNSET,
    format_: Union[Unset, TelemetryListFormat] = UNSET,
    is_decoded: Union[Unset, bool] = UNSET,
    observer: Union[Unset, str] = UNSET,
    sat_id: Union[Unset, str] = UNSET,
    satellite: Union[Unset, str] = UNSET,
    start: Union[Unset, datetime.datetime] = UNSET,
    transmitter: Union[Unset, str] = UNSET,
) -> Response[PaginatedTelemetryList]:
    """Lists data from satellite if they are filtered by NORAD ID or Satellite ID. Also logs the
    requests if it is set to do so.

    Args:
        app_source (Union[Unset, str]):
        cursor (Union[Unset, str]):
        end (Union[Unset, datetime.datetime]):
        format_ (Union[Unset, TelemetryListFormat]):
        is_decoded (Union[Unset, bool]):
        observer (Union[Unset, str]):
        sat_id (Union[Unset, str]):
        satellite (Union[Unset, str]):
        start (Union[Unset, datetime.datetime]):
        transmitter (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedTelemetryList]
    """

    kwargs = _get_kwargs(
        app_source=app_source,
        cursor=cursor,
        end=end,
        format_=format_,
        is_decoded=is_decoded,
        observer=observer,
        sat_id=sat_id,
        satellite=satellite,
        start=start,
        transmitter=transmitter,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    app_source: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    end: Union[Unset, datetime.datetime] = UNSET,
    format_: Union[Unset, TelemetryListFormat] = UNSET,
    is_decoded: Union[Unset, bool] = UNSET,
    observer: Union[Unset, str] = UNSET,
    sat_id: Union[Unset, str] = UNSET,
    satellite: Union[Unset, str] = UNSET,
    start: Union[Unset, datetime.datetime] = UNSET,
    transmitter: Union[Unset, str] = UNSET,
) -> Optional[PaginatedTelemetryList]:
    """Lists data from satellite if they are filtered by NORAD ID or Satellite ID. Also logs the
    requests if it is set to do so.

    Args:
        app_source (Union[Unset, str]):
        cursor (Union[Unset, str]):
        end (Union[Unset, datetime.datetime]):
        format_ (Union[Unset, TelemetryListFormat]):
        is_decoded (Union[Unset, bool]):
        observer (Union[Unset, str]):
        sat_id (Union[Unset, str]):
        satellite (Union[Unset, str]):
        start (Union[Unset, datetime.datetime]):
        transmitter (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedTelemetryList
    """

    return sync_detailed(
        client=client,
        app_source=app_source,
        cursor=cursor,
        end=end,
        format_=format_,
        is_decoded=is_decoded,
        observer=observer,
        sat_id=sat_id,
        satellite=satellite,
        start=start,
        transmitter=transmitter,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    app_source: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    end: Union[Unset, datetime.datetime] = UNSET,
    format_: Union[Unset, TelemetryListFormat] = UNSET,
    is_decoded: Union[Unset, bool] = UNSET,
    observer: Union[Unset, str] = UNSET,
    sat_id: Union[Unset, str] = UNSET,
    satellite: Union[Unset, str] = UNSET,
    start: Union[Unset, datetime.datetime] = UNSET,
    transmitter: Union[Unset, str] = UNSET,
) -> Response[PaginatedTelemetryList]:
    """Lists data from satellite if they are filtered by NORAD ID or Satellite ID. Also logs the
    requests if it is set to do so.

    Args:
        app_source (Union[Unset, str]):
        cursor (Union[Unset, str]):
        end (Union[Unset, datetime.datetime]):
        format_ (Union[Unset, TelemetryListFormat]):
        is_decoded (Union[Unset, bool]):
        observer (Union[Unset, str]):
        sat_id (Union[Unset, str]):
        satellite (Union[Unset, str]):
        start (Union[Unset, datetime.datetime]):
        transmitter (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedTelemetryList]
    """

    kwargs = _get_kwargs(
        app_source=app_source,
        cursor=cursor,
        end=end,
        format_=format_,
        is_decoded=is_decoded,
        observer=observer,
        sat_id=sat_id,
        satellite=satellite,
        start=start,
        transmitter=transmitter,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    app_source: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    end: Union[Unset, datetime.datetime] = UNSET,
    format_: Union[Unset, TelemetryListFormat] = UNSET,
    is_decoded: Union[Unset, bool] = UNSET,
    observer: Union[Unset, str] = UNSET,
    sat_id: Union[Unset, str] = UNSET,
    satellite: Union[Unset, str] = UNSET,
    start: Union[Unset, datetime.datetime] = UNSET,
    transmitter: Union[Unset, str] = UNSET,
) -> Optional[PaginatedTelemetryList]:
    """Lists data from satellite if they are filtered by NORAD ID or Satellite ID. Also logs the
    requests if it is set to do so.

    Args:
        app_source (Union[Unset, str]):
        cursor (Union[Unset, str]):
        end (Union[Unset, datetime.datetime]):
        format_ (Union[Unset, TelemetryListFormat]):
        is_decoded (Union[Unset, bool]):
        observer (Union[Unset, str]):
        sat_id (Union[Unset, str]):
        satellite (Union[Unset, str]):
        start (Union[Unset, datetime.datetime]):
        transmitter (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedTelemetryList
    """

    return (
        await asyncio_detailed(
            client=client,
            app_source=app_source,
            cursor=cursor,
            end=end,
            format_=format_,
            is_decoded=is_decoded,
            observer=observer,
            sat_id=sat_id,
            satellite=satellite,
            start=start,
            transmitter=transmitter,
        )
    ).parsed
