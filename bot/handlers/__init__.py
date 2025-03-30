from aiogram import Router

from bot.handlers.start import start_router

router = Router()

router.include_router(start_router)
