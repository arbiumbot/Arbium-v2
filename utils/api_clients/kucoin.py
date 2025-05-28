import aiohttp

KUCOIN_SPOT_URL = "https://api.kucoin.com/api/v1/market/orderbook/level1?symbol={symbol}"

async def get_spot_price_kucoin(symbol: str = "BTC-USDT"):
    async with aiohttp.ClientSession() as session:
        async with session.get(KUCOIN_SPOT_URL.format(symbol=symbol)) as resp:
            data = await resp.json()
            if "data" in data:
                return float(data["data"]["price"])
            return None