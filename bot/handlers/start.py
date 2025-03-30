from aiogram import Router, types
from aiogram.filters import Command

from bot.core.keyboards.main_kbs import create_raffle_kbs

start_router = Router()


@start_router.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Добро пожаловать!\n"
        "Это бот с мини приложением для выявления Случайного победителя розыгрышей в Вконтакте\n"
        "Нажмите кнопку ниже, чтобы начать.",
        reply_markup=create_raffle_kbs(),
    )
