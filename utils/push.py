from aiogram import Bot
from utils.db import get_users

async def send_push_to_all(bot: Bot, text: str):
    user_ids = get_users()
    count = 0

    for uid in user_ids:
        try:
            await bot.send_message(uid, text)
            count += 1
        except Exception as e:
            print(f"Не вдалося надіслати {uid}: {e}")

    return count