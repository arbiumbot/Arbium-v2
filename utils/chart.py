from aiogram import Router, types
from aiogram.types import Message, FSInputFile
from utils.chart import generate_profit_chart
import base64

router = Router()

@router.message(lambda m: m.text == "📈 Графік" or m.text == "📈 Chart")
async def handle_chart(message: Message):
    base64_image = generate_profit_chart()

    if not base64_image:
        await message.answer("Немає даних для побудови графіка 📉")
        return

    with open("chart.png", "wb") as f:
        f.write(base64.b64decode(base64_image))

    await message.answer_photo(FSInputFile("chart.png"), caption="📈 Прибутковість за 7 днів")