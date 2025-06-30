# Exchange WebSocket

一个用于连接各大加密货币交易所 WebSocket API 的 Python 包。

## 功能特性

- 支持多个主流交易所：Binance、OKX、Bitget、Bybit、Gate.io
- 异步 WebSocket 连接管理
- 自动重连机制
- 统一的接口设计
- 完整的错误处理
- 支持身份验证的私有频道
- 数据持久化支持

## 支持的交易所

- **Binance** - 币安交易所
- **OKX** - 欧易交易所
- **Bitget** - Bitget 交易所
- **Bybit** - Bybit 交易所
- **Gate.io** - 芝麻开门交易所

## 安装

### 使用 pip 安装

```bash
pip install exchange-websocket
```

### 从源码安装

```bash
git clone https://github.com/yourusername/exchange-websocket.git
cd exchange-websocket
pip install -e .
```

## 快速开始

### 基本用法

```python
import asyncio
from exchange_websocket.exchanges.okx import Okx

async def main():
    # 创建OKX WebSocket连接
    url = "wss://wspap.okx.com:8443/ws/v5/public"
    okx = Okx(url, needLogin=False)

    # 订阅资金费率数据
    await okx.subscribe([{"channel": "funding-rate", "instId": "BTC-USD-SWAP"}])

    # 运行WebSocket连接
    await okx.run()

if __name__ == "__main__":
    asyncio.run(main())
```

### 订阅多个交易对

```python
import asyncio
from exchange_websocket.exchanges.binance import Binance

async def main():
    url = "wss://fstream.binance.com/ws"
    binance = Binance(url, needLogin=False)

    # 订阅多个交易对的标记价格
    symbols = ["btcusdt@markPrice@1s", "ethusdt@markPrice@1s"]
    await binance.subscribe(symbols)

    await binance.run()

if __name__ == "__main__":
    asyncio.run(main())
```

### 需要身份验证的私有频道

```python
import asyncio
from exchange_websocket.exchanges.okx import Okx

async def main():
    url = "wss://wspap.okx.com:8443/ws/v5/private"

    # 需要提供API凭证
    okx = Okx(
        url,
        needLogin=True,
        apikey="your_api_key",
        secret="your_secret",
        passphrase="your_passphrase"
    )

    # 订阅账户信息
    await okx.subscribe([{"channel": "account"}])
    await okx.run()

if __name__ == "__main__":
    asyncio.run(main())
```

## API 文档

### 基础类 - ExchangeWebsocket

所有交易所 WebSocket 客户端的基类。

#### 构造函数参数

- `url` (str): WebSocket 连接地址
- `needLogin` (bool): 是否需要登录认证
- `pingInterval` (int, 可选): Ping 间隔时间，默认 20 秒
- `pingTimeout` (int, 可选): Ping 超时时间，默认 10 秒
- `queueMaxSize` (int, 可选): 请求队列最大大小，默认 100

#### 主要方法

- `connect()`: 建立 WebSocket 连接
- `subscribe(args)`: 订阅数据频道
- `addRequest(request)`: 添加请求到队列
- `run()`: 运行 WebSocket 客户端

### 交易所特定类

#### Binance

```python
from exchange_websocket.exchanges.binance import Binance

binance = Binance(url, needLogin=False)
await binance.subscribe(["btcusdt@ticker"])
```

#### OKX

```python
from exchange_websocket.exchanges.okx import Okx

okx = Okx(url, needLogin=False)
await okx.subscribe([{"channel": "tickers", "instId": "BTC-USDT-SWAP"}])
```

#### Bitget

```python
from exchange_websocket.exchanges.bitget import Bitget

bitget = Bitget(url, needLogin=False)
await bitget.subscribe([{"instType": "USDT-FUTURES", "channel": "ticker", "instId": "BTCUSDT"}])
```

## 工具函数

### 获取交易对列表

```python
from exchange_websocket.exchanges.okx import getAllOkxSymbols
from exchange_websocket.exchanges.binance import getAllBinanceSymbols
from exchange_websocket.exchanges.bitget import getAllBitgetSymbols

# 获取所有OKX USDT永续合约
okx_symbols = getAllOkxSymbols()

# 获取所有Binance USDT交易对
binance_symbols = getAllBinanceSymbols()

# 获取所有Bitget USDT期货合约
bitget_symbols = getAllBitgetSymbols()
```

### 资金费率信息

```python
from exchange_websocket.exchanges.getFundingInfo import (
    getBinanceFundingInfoBySombol,
    getBitgetFundingInfoBySombol
)

# 获取Binance指定交易对的资金费率信息
binance_funding = getBinanceFundingInfoBySombol("BTCUSDT")

# 获取Bitget指定交易对的资金费率信息
bitget_funding = getBitgetFundingInfoBySombol("BTCUSDT")
```

## 配置选项

可以通过构造函数参数自定义 WebSocket 连接的行为：

```python
okx = Okx(
    url="wss://wspap.okx.com:8443/ws/v5/public",
    needLogin=False,
    pingInterval=30,  # 30秒发送一次ping
    pingTimeout=15,   # 15秒ping超时
    queueMaxSize=200, # 请求队列最大200
    checkRequestInterval=0.1,  # 0.1秒检查一次请求队列
    processRecvInterval=0.001  # 0.001秒处理一次接收消息
)
```

## 数据处理

项目包含了数据处理模块，可以将接收到的数据保存为 CSV 格式：

```python
from exchange_websocket.exchanges.handler import okxSingleMsgHandler

# 在自定义的_processRecv方法中使用
class CustomOkx(Okx):
    async def _processRecv(self, recvMsg):
        okxSingleMsgHandler(recvMsg)
```

## 开发

### 安装开发依赖

```bash
pip install -e ".[dev]"
```

### 运行测试

```bash
pytest
```

### 代码格式化

```bash
black .
```

### 类型检查

```bash
mypy .
```

## 贡献

欢迎提交 Issue 和 Pull Request 来改进这个项目。

## 许可证

MIT License

## 联系方式

如果您有任何问题或建议，请通过以下方式联系：

- Email: your.email@example.com
- GitHub: https://github.com/yourusername/exchange-websocket
