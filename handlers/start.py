from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from keyboards.main_menu import get_main_menu

router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "👋 Вітаю! Я бот для моніторингу арбітражу між біржами.\n\n"
        "Оберіть опцію нижче ⬇️",
        reply_markup=get_main_menu()
    )