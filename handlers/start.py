from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

router = Router()

@router.message(F.text == "/start")
async def start_handler(message: Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="👤 Мій профіль")],
            [KeyboardButton(text="📊 P2P-аналіз")],
            [KeyboardButton(text="⚙️ Адмінка")]
        ],
        resize_keyboard=True
    )

    await message.answer(
        "👋 Вітаю! Я бот для моніторингу арбітражу між біржами.\n\nОберіть опцію нижче ⬇️",
        reply_markup=kb
    )