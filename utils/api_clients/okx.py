import aiohttp

OKX_SPOT_URL = "https://www.okx.com/api/v5/market/ticker?instId={symbol}"

async def get_spot_price_okx(symbol: str = "BTC-USDT"):
    async with aiohttp.ClientSession() as session:
        async with session.get(OKX_SPOT_URL.format(symbol=symbol)) as resp:
            data = await resp.json()
            if "data" in data and len(data["data"]) > 0:
                return float(data["data"][0]["last"])
            return None