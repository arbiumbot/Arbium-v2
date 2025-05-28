import aiohttp

# Binance
async def get_binance_symbols():
    url = "https://api.binance.com/api/v3/exchangeInfo"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            return [s["symbol"] for s in data["symbols"] if s["status"] == "TRADING" and s["quoteAsset"] == "USDT"]

# KuCoin
async def get_kucoin_symbols():
    url = "https://api.kucoin.com/api/v1/market/allTickers"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            return [item["symbol"] for item in data["data"]["ticker"] if "-USDT" in item["symbol"]]

# MEXC
async def get_mexc_symbols():
    url = "https://api.mexc.com/api/v3/exchangeInfo"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            return [s["symbol"] for s in data["symbols"] if s["quoteAsset"] == "USDT"]

# OKX
async def get_okx_symbols():
    url = "https://www.okx.com/api/v5/market/tickers?instType=SPOT"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            return [s["instId"] for s in data["data"] if "-USDT" in s["instId"]]

# Bitget
async def get_bitget_symbols():
    url = "https://api.bitget.com/api/v2/spot/public/symbols"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            return [s["symbol"] for s in data["data"] if s["quoteCoin"] == "USDT"]

# Унікальні пари для аналізу
async def get_all_common_symbols():
    binance = await get_binance_symbols()
    kucoin = await get_kucoin_symbols()
    mexc = await get_mexc_symbols()
    okx = await get_okx_symbols()
    bitget = await get_bitget_symbols()

    all_symbols = set(binance) | set(kucoin) | set(mexc) | set(okx) | set(bitget)
    return list(all_symbols)