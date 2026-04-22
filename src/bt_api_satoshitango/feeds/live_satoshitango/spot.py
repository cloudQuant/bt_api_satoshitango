from __future__ import annotations

from typing import Any

from bt_api_base.feeds.capability import Capability
from bt_api_base.functions.utils import update_extra_data

from bt_api_satoshitango.feeds.live_satoshitango.request_base import SatoshiTangoRequestData


class SatoshiTangoRequestDataSpot(SatoshiTangoRequestData):
    @classmethod
    def _capabilities(cls) -> set[Capability]:
        return {
            Capability.GET_TICK,
            Capability.GET_DEPTH,
            Capability.GET_KLINE,
            Capability.GET_EXCHANGE_INFO,
            Capability.GET_BALANCE,
            Capability.GET_ACCOUNT,
            Capability.MAKE_ORDER,
            Capability.CANCEL_ORDER,
        }

    def __init__(self, data_queue: Any = None, **kwargs: Any) -> None:
        super().__init__(data_queue, **kwargs)
        self.exchange_name = kwargs.get("exchange_name", "SATOSHITANGO___SPOT")

    def _get_tick(self, symbol, extra_data=None, **kwargs):
        path = "GET /v1/ticker"
        extra_data = update_extra_data(
            extra_data,
            **{
                "request_type": "get_tick",
                "symbol_name": symbol,
                "asset_type": self.asset_type,
                "exchange_name": self.exchange_name,
                "normalize_function": self._get_tick_normalize_function,
            },
        )
        return path, {"symbol": symbol}, extra_data

    @staticmethod
    def _get_tick_normalize_function(input_data, extra_data):
        if not input_data:
            return [], False
        ticker = input_data if isinstance(input_data, dict) else {}
        return [ticker], bool(ticker)

    def get_tick(self, symbol, extra_data=None, **kwargs):
        path, params, extra_data = self._get_tick(symbol, extra_data, **kwargs)
        return self.request(path, params=params, extra_data=extra_data)

    def async_get_tick(self, symbol, extra_data=None, **kwargs):
        path, params, extra_data = self._get_tick(symbol, extra_data, **kwargs)
        self.submit(
            self.async_request(path, params=params, extra_data=extra_data),
            callback=self.async_callback,
        )

    get_ticker = get_tick
    async_get_ticker = async_get_tick

    def _get_depth(self, symbol, count=20, extra_data=None, **kwargs):
        path = "GET /v1/orderbook"
        extra_data = update_extra_data(
            extra_data,
            **{
                "request_type": "get_depth",
                "symbol_name": symbol,
                "asset_type": self.asset_type,
                "exchange_name": self.exchange_name,
                "normalize_function": self._get_depth_normalize_function,
            },
        )
        return path, {"symbol": symbol, "depth": count}, extra_data

    @staticmethod
    def _get_depth_normalize_function(input_data, extra_data):
        if not input_data:
            return [], False
        depth = input_data if isinstance(input_data, dict) else {}
        return [depth], bool(depth)

    def get_depth(self, symbol, count=20, extra_data=None, **kwargs):
        path, params, extra_data = self._get_depth(symbol, count, extra_data, **kwargs)
        return self.request(path, params=params, extra_data=extra_data)

    def async_get_depth(self, symbol, count=20, extra_data=None, **kwargs):
        path, params, extra_data = self._get_depth(symbol, count, extra_data, **kwargs)
        self.submit(
            self.async_request(path, params=params, extra_data=extra_data),
            callback=self.async_callback,
        )

    def _get_kline(self, symbol, period, count=20, extra_data=None, **kwargs):
        path = "GET /v1/klines"
        extra_data = update_extra_data(
            extra_data,
            **{
                "request_type": "get_kline",
                "symbol_name": symbol,
                "asset_type": self.asset_type,
                "exchange_name": self.exchange_name,
                "normalize_function": self._get_kline_normalize_function,
            },
        )
        return (
            path,
            {
                "symbol": symbol,
                "interval": self._params.get_period(period),
                "limit": count,
            },
            extra_data,
        )

    @staticmethod
    def _get_kline_normalize_function(input_data, extra_data):
        if not input_data:
            return [], False
        klines = input_data if isinstance(input_data, list) else []
        return klines, bool(klines)

    def get_kline(self, symbol, period, count=20, extra_data=None, **kwargs):
        path, params, extra_data = self._get_kline(symbol, period, count, extra_data, **kwargs)
        return self.request(path, params=params, extra_data=extra_data)

    def async_get_kline(self, symbol, period, count=20, extra_data=None, **kwargs):
        path, params, extra_data = self._get_kline(symbol, period, count, extra_data, **kwargs)
        self.submit(
            self.async_request(path, params=params, extra_data=extra_data),
            callback=self.async_callback,
        )

    def _get_exchange_info(self, extra_data=None, **kwargs):
        path = "GET /v1/markets"
        extra_data = update_extra_data(
            extra_data,
            **{
                "request_type": "get_exchange_info",
                "symbol_name": "ALL",
                "asset_type": self.asset_type,
                "exchange_name": self.exchange_name,
                "normalize_function": self._get_exchange_info_normalize_function,
            },
        )
        return path, {}, extra_data

    @staticmethod
    def _get_exchange_info_normalize_function(input_data, extra_data):
        if not input_data:
            return [], False
        info = input_data if isinstance(input_data, dict) else {}
        return [info], bool(info)

    def get_exchange_info(self, extra_data=None, **kwargs):
        path, params, extra_data = self._get_exchange_info(extra_data, **kwargs)
        return self.request(path, params=params, extra_data=extra_data)

    def _get_balance(self, symbol=None, extra_data=None, **kwargs):
        path = "GET /v1/balance"
        extra_data = update_extra_data(
            extra_data,
            **{
                "request_type": "get_balance",
                "symbol_name": symbol or "",
                "asset_type": self.asset_type,
                "exchange_name": self.exchange_name,
                "normalize_function": self._get_balance_normalize_function,
            },
        )
        return path, {}, extra_data

    @staticmethod
    def _get_balance_normalize_function(input_data, extra_data):
        if not input_data:
            return [], False
        return [input_data], True

    def get_balance(self, symbol=None, extra_data=None, **kwargs):
        path, params, extra_data = self._get_balance(symbol, extra_data, **kwargs)
        return self.request(path, params=params, extra_data=extra_data)

    def _get_account(self, extra_data=None, **kwargs):
        path = "GET /v1/balance"
        extra_data = update_extra_data(
            extra_data,
            **{
                "request_type": "get_account",
                "symbol_name": "",
                "asset_type": self.asset_type,
                "exchange_name": self.exchange_name,
                "normalize_function": self._get_account_normalize_function,
            },
        )
        return path, {}, extra_data

    @staticmethod
    def _get_account_normalize_function(input_data, extra_data):
        if not input_data:
            return [], False
        return [input_data], True

    def get_account(self, symbol="ALL", extra_data=None, **kwargs):
        path, params, extra_data = self._get_account(extra_data, **kwargs)
        return self.request(path, params=params, extra_data=extra_data)

    def _make_order(self, symbol, volume, price, order_type, offset="open", extra_data=None, **kwargs):
        path = "POST /v1/order"
        params = {
            "symbol": symbol,
            "amount": str(volume),
            "price": str(price),
            "side": "buy" if "buy" in order_type.lower() else "sell",
            "type": "limit",
        }
        extra_data = update_extra_data(
            extra_data,
            **{
                "request_type": "make_order",
                "symbol_name": symbol,
                "asset_type": self.asset_type,
                "exchange_name": self.exchange_name,
                "normalize_function": self._make_order_normalize_function,
            },
        )
        return path, params, extra_data

    @staticmethod
    def _make_order_normalize_function(input_data, extra_data):
        if not input_data:
            return [], False
        return [input_data], True

    def make_order(
        self,
        symbol,
        volume,
        price=None,
        order_type="buy-limit",
        offset="open",
        post_only=False,
        client_order_id=None,
        extra_data=None,
        **kwargs,
    ):
        path, params, extra_data = self._make_order(symbol, volume, price, order_type, offset, extra_data, **kwargs)
        return self.request(path, body=params, extra_data=extra_data)

    def _cancel_order(self, symbol, order_id, extra_data=None, **kwargs):
        path = "POST /v1/order/cancel"
        params = {"order_id": order_id}
        extra_data = update_extra_data(
            extra_data,
            **{
                "request_type": "cancel_order",
                "symbol_name": symbol,
                "asset_type": self.asset_type,
                "exchange_name": self.exchange_name,
                "order_id": order_id,
            },
        )
        return path, params, extra_data

    def cancel_order(self, symbol, order_id, extra_data=None, **kwargs):
        path, params, extra_data = self._cancel_order(symbol, order_id, extra_data, **kwargs)
        return self.request(path, body=params, extra_data=extra_data)
