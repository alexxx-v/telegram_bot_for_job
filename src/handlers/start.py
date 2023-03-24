from aiogram import types
from src.main import dp


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Привет!\nЯ бот и вам пи**а!\nШутка.")