from aiogram import Router, F
from aiogram.types import Message
from keyboards.main_menu import get_main_menu

router = Router()

@router.message(F.text == "/start")
async def start_handler(message: Message):
    await message.answer(
        "👋 Вітаю! Я бот для моніторингу арбітражу між біржами.\n\n"
        "Оберіть опцію нижче ⬇️",
        reply_markup=get_main_menu()
    )