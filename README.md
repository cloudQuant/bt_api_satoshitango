# SATOSHITANGO

Exchange plugin for bt_api framework.

[![PyPI Version](https://img.shields.io/pypi/v/bt_api_satoshitango.svg)](https://pypi.org/project/bt_api_satoshitango/)
[![Python Versions](https://img.shields.io/pypi/pyversions/bt_api_satoshitango.svg)](https://pypi.org/project/bt_api_satoshitango/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/cloudQuant/bt_api_satoshitango/actions/workflows/ci.yml/badge.svg)](https://github.com/cloudQuant/bt_api_satoshitango/actions)
[![Docs](https://readthedocs.org/projects/bt-api-satoshitango/badge/?version=latest)](https://bt-api-satoshitango.readthedocs.io/)

---

## English | [中文](#中文)

### Overview

This package provides **SatoshiTango exchange plugin for bt_api** for the [bt_api](https://github.com/cloudQuant/bt_api_py) framework. It offers a unified interface for interacting with **SATOSHITANGO** exchange.

### Features

- Exchange integration with bt_api
- REST API support
- Market data access
- Basic trading operations

### Installation

```bash
pip install bt_api_satoshitango
```

Or install from source:

```bash
git clone https://github.com/cloudQuant/bt_api_satoshitango
cd bt_api_satoshitango
pip install -e .
```

### Quick Start

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

### Supported Operations

| Operation | Status |
|-----------|--------|
| Ticker | ✅ |
| OrderBook | ✅ |
| Trades | ✅ |
| Bars/Klines | ✅ |
| Orders | ✅ |
| Balances | ✅ |
| Positions | ✅ |

### Online Documentation

| Resource | Link |
|----------|------|
| English Docs | https://bt-api-satoshitango.readthedocs.io/ |
| Chinese Docs | https://bt-api-satoshitango.readthedocs.io/zh/latest/ |
| GitHub Repository | https://github.com/cloudQuant/bt_api_satoshitango |
| Issue Tracker | https://github.com/cloudQuant/bt_api_satoshitango/issues |

### Requirements

- Python 3.9+
- bt_api_base >= 0.15

### Architecture

```
bt_api_satoshitango/
├── src/bt_api_satoshitango/     # Source code
│   ├── containers/     # Data containers
│   ├── feeds/          # API feeds
│   ├── gateway/       # Gateway adapter
│   └── plugin.py      # Plugin registration
├── tests/             # Unit tests
└── docs/             # Documentation
```

### License

MIT License - see [LICENSE](LICENSE) for details.

### Support

- Report bugs via [GitHub Issues](https://github.com/cloudQuant/bt_api_satoshitango/issues)
- Email: yunjinqi@gmail.com

---

## 中文

### 概述

本包为 [bt_api](https://github.com/cloudQuant/bt_api_py) 框架提供 **SatoshiTango exchange plugin for bt_api**。它提供了与 **SATOSHITANGO** 交易所交互的统一接口。

### 功能特点

- bt_api交易所集成
- REST API支持
- 市场数据访问
- 基本交易操作

### 安装

```bash
pip install bt_api_satoshitango
```

或从源码安装：

```bash
git clone https://github.com/cloudQuant/bt_api_satoshitango
cd bt_api_satoshitango
pip install -e .
```

### 快速开始

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

### 支持的操作

| 操作 | 状态 |
|------|------|
| Ticker | ✅ |
| OrderBook | ✅ |
| Trades | ✅ |
| Bars/Klines | ✅ |
| Orders | ✅ |
| Balances | ✅ |
| Positions | ✅ |

### 在线文档

| 资源 | 链接 |
|------|------|
| 英文文档 | https://bt-api-satoshitango.readthedocs.io/ |
| 中文文档 | https://bt-api-satoshitango.readthedocs.io/zh/latest/ |
| GitHub 仓库 | https://github.com/cloudQuant/bt_api_satoshitango |
| 问题反馈 | https://github.com/cloudQuant/bt_api_satoshitango/issues |

### 系统要求

- Python 3.9+
- bt_api_base >= 0.15

### 架构

```
bt_api_satoshitango/
├── src/bt_api_satoshitango/     # 源代码
│   ├── containers/     # 数据容器
│   ├── feeds/          # API 源
│   ├── gateway/        # 网关适配器
│   └── plugin.py       # 插件注册
├── tests/             # 单元测试
└── docs/             # 文档
```

### 许可证

MIT 许可证 - 详见 [LICENSE](LICENSE)。

### 技术支持

- 通过 [GitHub Issues](https://github.com/cloudQuant/bt_api_satoshitango/issues) 反馈问题
- 邮箱: yunjinqi@gmail.com
