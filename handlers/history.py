from aiogram import Router, types
from aiogram.types import Message
import i18n

router = Router()

@router.message(lambda m: m.text == i18n.t("history"))
async def handle_history(message: Message):
    # Тестова відповідь (сюди вставляється історія арбітражів)
    await message.answer("🕓 Історія ще не реалізована. Очікуйте оновлень.")