import logging
from contextlib import asynccontextmanager

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from fastapi import FastAPI, Request

from config import BOT_TOKEN, WEBHOOK_URL
from handlers import start, arbitrage, chart, history, top, settings, push

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
dp.include_routers(
    start.router,
    arbitrage.router,
    chart.router,
    history.router,
    top.router,
    settings.router,
    push.router
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.basicConfig(level=logging.INFO)
    print("🔄 Setting webhook...")
    await bot.set_webhook(WEBHOOK_URL)
    print("✅ Webhook set!")
    yield
    print("♻️ Shutting down...")
    await bot.delete_webhook()
    await bot.session.close()

app = FastAPI(lifespan=lifespan)

@app.post(f"/webhook/bot/{BOT_TOKEN}")
async def telegram_webhook(request: Request):
    update = await request.json()
    await dp.feed_raw_update(bot=bot, update=update)
    return {"status": "ok"}