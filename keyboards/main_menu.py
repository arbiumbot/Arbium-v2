from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🔍 Арбітраж")],
            [KeyboardButton(text="📊 Арбітраж")],
            [KeyboardButton(text="💱 KuCoin ціна")],
            [KeyboardButton(text="💱 MEXC ціна")],
            [KeyboardButton(text="💱 OKX ціна")],
            [KeyboardButton(text="💱 Bitget ціна")]
        ],
        resize_keyboard=True
    )
