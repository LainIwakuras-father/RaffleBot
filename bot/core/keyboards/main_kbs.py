from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           WebAppInfo)

from create_bot import WEBAPP_URL


def create_raffle_kbs():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🎲 Создать розыгрыш", web_app=WebAppInfo(url="https://179ae10e045df0a4c9dd1a5c9bfcd8d2.serveo.net") #WEBAPP_URL домен на tuna при хостинге заменить!
                )
            ]
        ]
    )
    return keyboard
