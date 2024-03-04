import logging
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters.state import State, StatesGroup


API_TOKEN = "7141900346:AAGiH5QZ-05_PQtAzaEyLaZL7t7F1Z7ZCEk"
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def starter(message: types.Message):
    await message.answer(f"<i>Assalomu ALeykum</i> <b>{message.from_user.first_name}</b> \n\n<i>636 chi gurux tomonidan yaratilgan \n\nbotga xush kelibsiz</i>")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)