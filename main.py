import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from fastapi import FastAPI
from config import BOT_TOKEN, WEBHOOK_URL

from handlers import (
    start,
    arbitrage,
    chart,
    history,
    top,
    settings,
    push  # додано push
)

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

# Підключення обробників
dp.include_routers(
    start.router,
    arbitrage.router,
    chart.router,
    history.router,
    top.router,
    settings.router,
    push.router
)

# FastAPI
app = FastAPI()

@app.on_event("startup")
async def on_startup():
    logging.basicConfig(level=logging.INFO)
    await bot.set_webhook(WEBHOOK_URL)

@app.on_event("shutdown")
async def on_shutdown():
    await bot.delete_webhook()
    await bot.session.close()

@app.post(f"/webhook/bot/{BOT_TOKEN}")
async def bot_webhook(update: dict):
    await dp.feed_raw_update(bot=bot, update=update)
    return {"status": "ok"}