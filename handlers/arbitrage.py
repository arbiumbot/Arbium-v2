from aiogram import Router
from aiogram.types import Message
from utils.api_clients.binance import format_p2p_result
from utils.api_clients.kucoin import get_spot_price_kucoin
from utils.api_clients.mexc import get_spot_price_mexc
from utils.api_clients.okx import get_spot_price_okx
from utils.api_clients.bitget import get_spot_price_bitget

router = Router()

@router.message(lambda m: m.text == "📊 Арбітраж")
async def show_binance_arbitrage(message: Message):
    result = await format_p2p_result(asset="USDT", fiat="UAH")
    await message.answer(result)

@router.message(lambda m: m.text == "💱 KuCoin ціна")
async def show_kucoin_price(message: Message):
    price = await get_spot_price_kucoin("BTC-USDT")
    if price:
        await message.answer(f"💱 Поточна ціна BTC на KuCoin: <b>{price:.2f} USDT</b>")
    else:
        await message.answer("❌ Не вдалося отримати ціну з KuCoin.")

@router.message(lambda m: m.text == "💱 MEXC ціна")
async def show_mexc_price(message: Message):
    price = await get_spot_price_mexc("BTCUSDT")
    if price:
        await message.answer(f"💱 Поточна ціна BTC на MEXC: <b>{price:.2f} USDT</b>")
    else:
        await message.answer("❌ Не вдалося отримати ціну з MEXC.")

@router.message(lambda m: m.text == "💱 OKX ціна")
async def show_okx_price(message: Message):
    price = await get_spot_price_okx("BTC-USDT")
    if price:
        await message.answer(f"💱 Поточна ціна BTC на OKX: <b>{price:.2f} USDT</b>")
    else:
        await message.answer("❌ Не вдалося отримати ціну з OKX.")

@router.message(lambda m: m.text == "💱 Bitget ціна")
async def show_bitget_price(message: Message):
    price = await get_spot_price_bitget("BTCUSDT")
    if price:
        await message.answer(f"💱 Поточна ціна BTC на Bitget: <b>{price:.2f} USDT</b>")
    else:
        await message.answer("❌ Не вдалося отримати ціну з Bitget.")