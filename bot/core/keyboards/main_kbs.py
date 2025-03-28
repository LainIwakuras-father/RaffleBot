from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from create_bot import WEBAPP_URL

def create_raffle_kbs():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🎲 Создать розыгрыш",
                    web_app=WebAppInfo(url=WEBAPP_URL)
                )
            ]
        ]
    )
    return keyboard