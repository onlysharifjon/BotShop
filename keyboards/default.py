from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

tel_nomer = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📞Telefon Raqam',request_contact=True)
        ]
    ],
    resize_keyboard=True
)
