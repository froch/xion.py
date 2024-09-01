from datetime import timedelta
from typing import Any, Callable, List, Optional, Union

from xionpy.protos.cosmos.base.query.v1beta1.pagination_pb2 import PageRequest


def ensure_timedelta(interval: Union[int, float, timedelta]) -> timedelta:
    return interval if isinstance(interval, timedelta) else timedelta(seconds=interval)


DEFAULT_PER_PAGE_LIMIT = None


def get_paginated(
        initial_request: Any,
        request_method: Callable,
        pages_limit: int = 0,
        per_page_limit: Optional[int] = DEFAULT_PER_PAGE_LIMIT,
) -> List[Any]:
    pages: List[Any] = []
    pagination = PageRequest(limit=per_page_limit)

    while pagination and (len(pages) < pages_limit or pages_limit == 0):
        request = initial_request.__class__()
        request.CopyFrom(initial_request)
        request.pagination.CopyFrom(pagination)

        resp = request_method(request)
        pages.append(resp)
        pagination = None

        if resp.pagination.next_key:
            pagination = PageRequest(limit=per_page_limit, key=resp.pagination.next_key)

    return pages
