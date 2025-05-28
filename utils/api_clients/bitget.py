import aiohttp

BITGET_SPOT_URL = "https://api.bitget.com/api/v2/spot/market/ticker?symbol={symbol}"

async def get_spot_price_bitget(symbol: str = "BTCUSDT"):
    async with aiohttp.ClientSession() as session:
        async with session.get(BITGET_SPOT_URL.format(symbol=symbol)) as resp:
            data = await resp.json()
            if "data" in data and "close" in data["data"]:
                return float(data["data"]["close"])
            return None