import asyncio

from aiogram import Bot, Dispatcher, executor, types
from src.config import Config
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=Config.token)
dp = Dispatcher(bot)


async def main():
    from handlers import dp
    try:
        await dp.start_polling()
    finally:
        await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped!')

