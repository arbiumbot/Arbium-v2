import aiohttp

MEXC_SPOT_URL = "https://api.mexc.com/api/v3/ticker/price?symbol={symbol}"

async def get_spot_price_mexc(symbol: str = "BTCUSDT"):
    async with aiohttp.ClientSession() as session:
        async with session.get(MEXC_SPOT_URL.format(symbol=symbol)) as resp:
            data = await resp.json()
            if "price" in data:
                return float(data["price"])
            return None