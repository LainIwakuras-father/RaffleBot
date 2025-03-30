import asyncio
import logging

from bot.core.utils.logger_config import loggerConfig
from bot.handlers import router as main_router
from create_bot import bot, dp

logging.basicConfig(
    level=loggerConfig.level,
    format=loggerConfig.format,
)


async def main():
    try:
        logging.info("Запускаю бота...")
        dp.include_router(main_router)
        await dp.start_polling(bot)
    except Exception as ex:
        logging.error(f"Ошибка при запуске: {ex}")


if __name__ == "__main__":
    # Base.metadata.create_all(bind=engine)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Работа завершена")
