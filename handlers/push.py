from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import Bot
from config import ADMIN_ID
from utils.push import send_push_to_all

router = Router()

class PushState(StatesGroup):
    waiting_for_text = State()

@router.message(F.text == "📣 Розсилка")
async def ask_text(message: Message, state: FSMContext):
    if message.from_user.id != ADMIN_ID:
        await message.answer("⛔️ У вас немає доступу до розсилки.")
        return
    await message.answer("✏️ Введіть текст розсилки:")
    await state.set_state(PushState.waiting_for_text)

@router.message(PushState.waiting_for_text)
async def do_push(message: Message, state: FSMContext, bot: Bot):
    await state.clear()
    count = await send_push_to_all(bot, message.text)
    await message.answer(f"✅ Розсилка завершена. Надіслано {count} користувачам.")