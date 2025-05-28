from aiogram import Router, types
from aiogram.types import Message
import i18n

router = Router()

@router.message(lambda m: m.text == i18n.t("settings"))
async def handle_settings(message: Message):
    await message.answer("⚙️ Налаштування в розробці.\nСкоро тут буде вибір мови, бірж, монет та інше.")