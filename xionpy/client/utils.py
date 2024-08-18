from datetime import timedelta
from typing import Any, Callable, List, Optional, Union

from xionpy.client.tx import SigningCfg, SubmittedTx
from xionpy.protos.cosmos.base.query.v1beta1.pagination_pb2 import PageRequest


def tx_submit_basic(
        client: "LedgerClient",  # type: ignore # noqa: F821
        tx: "Transaction",  # type: ignore # noqa: F821
        sender: "Wallet",  # type: ignore # noqa: F821
        account: Optional["Account"] = None,  # type: ignore # noqa: F821
        gas_limit: Optional[int] = None,
        memo: Optional[str] = None,
) -> SubmittedTx:

    if account is None:
        account = client.query_account(sender.address())

    if gas_limit is not None:
        fee = client.estimate_fee_from_gas(gas_limit)
    else:
        fee = f"{client.network_config.fee_minimum_gas_price}{client.network_config.fee_denomination}"
        tx.seal(
            SigningCfg.direct(sender.public_key(), account.sequence),
            fee=fee,
            gas_limit=client.gas_strategy.block_gas_limit(),
            memo=memo,
        )
        tx.sign(sender.signer(), client.network_config.chain_id, account.number)
        tx.complete()

        gas_limit, fee = client.estimate_gas_and_fee_for_tx(tx)

    # finally, build the final transaction that will be executed with the correct gas and fee values
    tx.seal(
        SigningCfg.direct(sender.public_key(), account.sequence),
        fee=fee,
        gas_limit=gas_limit,
        memo=memo,
    )
    tx.sign(sender.signer(), client.network_config.chain_id, account.number)
    tx.complete()

    return client.broadcast_tx(tx)


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
