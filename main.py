from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from fastapi import FastAPI, Request
import logging
from config import BOT_TOKEN, WEBHOOK_URL
from handlers import start, arbitrage, history, chart, top, settings

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
dp.include_routers(
    start.router,
    arbitrage.router,
    history.router,
    chart.router,
    top.router,
    settings.router,
)

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
async def telegram_webhook(request: Request):
    update = await request.json()
    await dp.feed_raw_update(bot=bot, update=update)
    return {"status": "ok"}
