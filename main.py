import logging
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters.state import State, StatesGroup

from keyboards.default import tel_nomer, bolimlar

API_TOKEN = "7141900346:AAGiH5QZ-05_PQtAzaEyLaZL7t7F1Z7ZCEk"
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def starter(message: types.Message):
    await message.answer(f"<i>Assalomu ALeykum</i> <b>{message.from_user.first_name}</b> \n\n<i>636 chi gurux tomonidan yaratilgan \n\nbotga xush kelibsiz</i>",reply_markup=tel_nomer)

@dp.message_handler(content_types=types.ContentType.CONTACT)
async def soramasdan_nomer_olamiz(message :types.Message):
    with open("contact_info.txt", "a",encoding="utf-8") as file:
        file.write(str(message.contact) + "\n\n")
    await message.answer("Siz ro`yxatdan o`tdingiz",reply_markup=bolimlar)

@dp.message_handler(text = 'Kiyimlar')
async def kiyim(message:types.Message):
    await message.answer_photo("https://mykaleidoscope.ru/x/uploads/posts/2022-10/1666186521_37-mykaleidoscope-ru-p-kofta-fasonlari-zhenskie-instagram-37.jpg",caption='Ayollar ko`ylagi')




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)