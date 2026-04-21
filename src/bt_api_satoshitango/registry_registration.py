from __future__ import annotations

from bt_api_base.balance_utils import simple_balance_handler as _satoshitango_balance_handler
from bt_api_base.registry import ExchangeRegistry

from bt_api_satoshitango.exchange_data import SatoshiTangoExchangeDataSpot
from bt_api_satoshitango.feeds.live_satoshitango.spot import SatoshiTangoRequestDataSpot


def register_satoshitango(registry: type[ExchangeRegistry]) -> None:
    registry.register_feed("SATOSHITANGO___SPOT", SatoshiTangoRequestDataSpot)
    registry.register_exchange_data("SATOSHITANGO___SPOT", SatoshiTangoExchangeDataSpot)
    registry.register_balance_handler("SATOSHITANGO___SPOT", _satoshitango_balance_handler)
