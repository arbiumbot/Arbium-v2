from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📊 P2P-аналіз")],
            [KeyboardButton(text="⚙️ Налаштування")]
        ],
        resize_keyboard=True
    )