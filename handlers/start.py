from aiogram import Router, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from config import ADMIN_ID
import i18n

router = Router()

# Головне меню для користувача
def get_user_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=i18n.t("arbitrage"))],
            [KeyboardButton(text=i18n.t("chart")), KeyboardButton(text=i18n.t("history"))],
            [KeyboardButton(text=i18n.t("topTokens")), KeyboardButton(text=i18n.t("topExchanges"))],
            [KeyboardButton(text=i18n.t("settings"))]
        ],
        resize_keyboard=True
    )

# Головне меню для адміна
def get_admin_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=i18n.t("arbitrage"))],
            [KeyboardButton(text=i18n.t("chart")), KeyboardButton(text=i18n.t("history"))],
            [KeyboardButton(text=i18n.t("topTokens")), KeyboardButton(text=i18n.t("topExchanges"))],
            [KeyboardButton(text=i18n.t("settings"))],
            [KeyboardButton(text="📣 Розсилка")]
        ],
        resize_keyboard=True
    )

@router.message(commands=["start"])
async def start_command(message: Message):
    user_id = message.from_user.id

    if user_id == ADMIN_ID:
        menu = get_admin_menu()
        await message.answer("👮‍♂️ Привіт, адміністраторе! Обери опцію нижче:", reply_markup=menu)
    else:
        menu = get_user_menu()
        await message.answer("👋 Привіт! Обери команду з меню:", reply_markup=menu)