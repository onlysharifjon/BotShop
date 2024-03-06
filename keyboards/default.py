from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

tel_nomer = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📞Telefon Raqam',request_contact=True)
        ]
    ],
    resize_keyboard=True
)

bolimlar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Kiyimlar')
        ],
        [
            KeyboardButton(text="Aksesuarlar")
        ],
        [
            KeyboardButton('Oziq ovqat')
        ],
        [
            KeyboardButton(text = 'Oyinchoqlar')
        ],
        [
            KeyboardButton(text='Kompyuterlar')
        ],
        [
            KeyboardButton(text='Telefonlar')
        ],
        [
            KeyboardButton('Televizorlar')
        ],
        [
            KeyboardButton('Muzlatgichlar')
        ],

    ],
    resize_keyboard=True
)