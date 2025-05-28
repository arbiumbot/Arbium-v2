from aiogram import Router, types
from aiogram.types import Message
import i18n

router = Router()

@router.message(lambda m: m.text == i18n.t("chart"))
async def handle_chart(message: Message):
    # Тестова відповідь (сюди вставиш генерацію графіку)
    await message.answer("📈 Відображення графіка в розробці.")