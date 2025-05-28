import aiohttp

BINANCE_P2P_URL = "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"
BINANCE_SPOT_URL = "https://api.binance.com/api/v3/ticker/price?symbol={symbol}"

HEADERS = {
    "Content-Type": "application/json"
}


async def get_spot_price(symbol: str = "BTCUSDT"):
    async with aiohttp.ClientSession() as session:
        async with session.get(BINANCE_SPOT_URL.format(symbol=symbol)) as resp:
            data = await resp.json()
            return float(data["price"])


async def get_p2p_offers(asset: str = "USDT", trade_type: str = "BUY", fiat: str = "UAH", rows: int = 5):
    payload = {
        "asset": asset,
        "fiat": fiat,
        "tradeType": trade_type,
        "merchantCheck": False,
        "page": 1,
        "rows": rows,
        "payTypes": []
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(BINANCE_P2P_URL, json=payload, headers=HEADERS) as resp:
            data = await resp.json()
            return data.get("data", [])


async def format_p2p_result(asset: str, fiat: str = "UAH"):
    result = f"📊 <b>P2P {asset}/{fiat}</b>\n\n"

    buy_offers = await get_p2p_offers(asset=asset, trade_type="BUY", fiat=fiat)
    sell_offers = await get_p2p_offers(asset=asset, trade_type="SELL", fiat=fiat)

    result += "🟢 <b>Купити:</b>\n"
    for offer in buy_offers:
        adv = offer["adv"]
        user = offer["advertiser"]
        price = adv["price"]
        nickname = user["nickName"]
        result += f"{price} {fiat} — {nickname}\n"

    result += "\n🔴 <b>Продати:</b>\n"
    for offer in sell_offers:
        adv = offer["adv"]
        user = offer["advertiser"]
        price = adv["price"]
        nickname = user["nickName"]
        result += f"{price} {fiat} — {nickname}\n"

    return result