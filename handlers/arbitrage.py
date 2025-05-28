from aiogram import Router, types
from aiogram.types import Message
import i18n

router = Router()

@router.message(lambda m: m.text == i18n.t("arbitrage"))
async def handle_arbitrage(message: Message):
    # Тестова відповідь (сюди вставиш аналіз)
    await message.answer("📊 Арбітражні можливості зараз недоступні.\nОчікуйте оновлення 🔄")