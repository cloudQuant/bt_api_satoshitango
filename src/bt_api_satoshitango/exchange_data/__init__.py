from __future__ import annotations

from bt_api_base.containers.exchanges.exchange_data import ExchangeData


class SatoshiTangoExchangeData(ExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.exchange_name = "SATOSHITANGO___SPOT"
        self.rest_url = "https://api.satoshitango.com"
        self.wss_url = ""
        self.rest_paths = {}
        self.wss_paths = {}
        self.kline_periods = {
            "1m": "1",
            "5m": "5",
            "15m": "15",
            "30m": "30",
            "1h": "60",
            "4h": "240",
            "1d": "1d",
            "1w": "1w",
        }
        self.legal_currency = ["ARS", "USD", "BTC", "ETH", "USDT"]

    def get_period(self, period: str) -> str:
        return self.kline_periods.get(period, period)


class SatoshiTangoExchangeDataSpot(SatoshiTangoExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.asset_type = "spot"
