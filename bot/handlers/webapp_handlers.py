from aiogram import Router,types,F
from aiogram.utils.web_app import check_webapp_signature
from create_bot import TOKEN
router = Router()
@router.message(F.web_app_data)
async def handle_web_app_data(message:types.Message):
    if check_webapp_signature(token=TOKEN,message=message.web_app_data.data):
        return await message.answer("Ошибка проверки данных.")
