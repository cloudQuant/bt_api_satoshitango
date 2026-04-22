# SATOSHITANGO Documentation

## English

Welcome to the SATOSHITANGO documentation for bt_api.

### Quick Start

```bash
pip install bt_api_satoshitango
```

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "SATOSHITANGO___SPOT": {
        "api_key": "your_key",
        "secret": "your_secret",
    }
})

ticker = api.get_tick("SATOSHITANGO___SPOT", "BTCUSD")
balance = api.get_balance("SATOSHITANGO___SPOT")
```

## 中文

欢迎使用 bt_api 的 SATOSHITANGO 文档。

### 快速开始

```bash
pip install bt_api_satoshitango
```

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "SATOSHITANGO___SPOT": {
        "api_key": "your_key",
        "secret": "your_secret",
    }
})

ticker = api.get_tick("SATOSHITANGO___SPOT", "BTCUSD")
balance = api.get_balance("SATOSHITANGO___SPOT")
```

## API Reference

See source code in `src/bt_api_satoshitango/` for detailed API documentation.
