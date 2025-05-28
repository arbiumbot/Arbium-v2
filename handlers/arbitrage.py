from aiogram import Router
from aiogram.types import Message
from utils.api_clients.binance import format_p2p_result

router = Router()

@router.message(lambda m: m.text == "📊 Арбітраж")
async def show_binance_arbitrage(message: Message):
    result = await format_p2p_result(asset="USDT", fiat="UAH")
    await message.answer(result)