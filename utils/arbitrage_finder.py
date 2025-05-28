from utils.api_clients.binance import get_spot_price as binance_price
from utils.api_clients.kucoin import get_spot_price_kucoin
from utils.api_clients.mexc import get_spot_price_mexc
from utils.api_clients.okx import get_spot_price_okx
from utils.api_clients.bitget import get_spot_price_bitget
from utils.api_clients.symbols import get_all_common_symbols
import asyncio

async def get_prices_for_symbol(symbol):
    prices = {}

    symbol_dash = symbol.replace("USDT", "-USDT")  # Для KuCoin, OKX

    try:
        prices["Binance"] = await binance_price(symbol)
    except: pass

    try:
        prices["KuCoin"] = await get_spot_price_kucoin(symbol_dash)
    except: pass

    try:
        prices["MEXC"] = await get_spot_price_mexc(symbol)
    except: pass

    try:
        prices["OKX"] = await get_spot_price_okx(symbol_dash)
    except: pass

    try:
        prices["Bitget"] = await get_spot_price_bitget(symbol)
    except: pass

    return prices

async def analyze_symbol(symbol):
    prices = await get_prices_for_symbol(symbol)
    if len(prices) < 2:
        return None

    sorted_prices = sorted(prices.items(), key=lambda x: x[1])
    low = sorted_prices[0]
    high = sorted_prices[-1]
    profit = high[1] - low[1]
    percent = (profit / low[1]) * 100

    return {
        "symbol": symbol,
        "buy": low,
        "sell": high,
        "profit": profit,
        "percent": percent
    }

async def find_top_arbitrages(top_n=3):
    symbols = await get_all_common_symbols()
    tasks = [analyze_symbol(symbol) for symbol in symbols]
    results = await asyncio.gather(*tasks)

    arbitrage_opportunities = [r for r in results if r and r["percent"] > 0.5]
    sorted_opportunities = sorted(arbitrage_opportunities, key=lambda x: x["percent"], reverse=True)

    top = sorted_opportunities[:top_n]
    report = "<b>🔍 Топ арбітражних можливостей:</b>\n\n"

    for arb in top:
        report += (
            f"🔸 <b>{arb['symbol']}</b>\n"
            f"🟢 Купити на <b>{arb['buy'][0]}</b> за <b>{arb['buy'][1]:.2f}</b>\n"
            f"🔴 Продати на <b>{arb['sell'][0]}</b> за <b>{arb['sell'][1]:.2f}</b>\n"
            f"💰 Прибуток: <b>{arb['profit']:.2f} USDT</b> ({arb['percent']:.2f}%)\n\n"
        )

    return report if top else "❌ Не знайдено вигідних арбітражних можливостей"