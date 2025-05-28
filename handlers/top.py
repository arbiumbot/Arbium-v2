from aiogram import Router, types
from aiogram.types import Message
import i18n

router = Router()

@router.message(lambda m: m.text == i18n.t("topTokens"))
async def handle_top_tokens(message: Message):
    # Тестова відповідь (сюди вставити аналіз топ монет)
    await message.answer("🏅 Топ монет буде доступний найближчим часом.")

@router.message(lambda m: m.text == i18n.t("topExchanges"))
async def handle_top_exchanges(message: Message):
    # Тестова відповідь (сюди вставити аналіз бірж)
    await message.answer("🏆 Топ бірж ще не реалізовано.")