import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv

# лоадим переменные окружения из файла .env 
load_dotenv()
TOKEN = os.getenv("TOKEN", "")
ADMIN_ID = os.getenv("ADMIN_ID", "")
WEBAPP_URL = os.getenv("WEBAPP_URL")


bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


async def start_bot():
    try:
        await bot.send_message(ADMIN_ID, f"Я запущен🥳.")
    except:
        pass


async def stop_bot():
    try:
        await bot.send_message(ADMIN_ID, "Бот остановлен. За что?😔")
    except:
        pass
