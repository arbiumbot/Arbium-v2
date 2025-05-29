import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from config import BOT_TOKEN, WEBHOOK_URL
from handlers import start

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

# Підключення роутерів
dp.include_router(start.router)

# Lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.basicConfig(level=logging.INFO)
    await bot.set_webhook(WEBHOOK_URL)
    yield
    await bot.delete_webhook()
    await bot.session.close()

# FastAPI instance
app = FastAPI(lifespan=lifespan)

# Webhook endpoint
@app.post(f"/webhook/bot/{BOT_TOKEN}")
async def telegram_webhook(req: Request):
    body = await req.body()
    await dp.feed_raw_update(bot=bot, update=body)
    return {"status": "ok"}