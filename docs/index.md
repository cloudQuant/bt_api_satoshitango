# SATOSHITANGO Documentation

## English

Welcome to the SATOSHITANGO documentation for bt_api.

### Quick Start

```bash
pip install bt_api_satoshitango
```

```python
from bt_api_satoshitango import SatoshitangoApi
feed = SatoshitangoApi(api_key="your_key", secret="your_secret")
ticker = feed.get_ticker("BTCUSDT")
```

## 中文

欢迎使用 bt_api 的 SATOSHITANGO 文档。

### 快速开始

```bash
pip install bt_api_satoshitango
```

```python
from bt_api_satoshitango import SatoshitangoApi
feed = SatoshitangoApi(api_key="your_key", secret="your_secret")
ticker = feed.get_ticker("BTCUSDT")
```

## API Reference

See source code in `src/bt_api_satoshitango/` for detailed API documentation.
