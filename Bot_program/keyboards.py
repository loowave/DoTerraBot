from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

# Buttons
CountrySngButton = InlineKeyboardButton(
    text='СНГ',
    callback_data='СНГ'
)

CountryEuroButton = InlineKeyboardButton(
    text='Европа',
    callback_data='Европа'
)

CountryOtherButton = InlineKeyboardButton(
    text='Другое',
    callback_data='Другое'
)

SharedButton = KeyboardButton(
    text='да, уже поделился',
)

SharingButton = KeyboardButton(
    text='еще нет, уже бегу',
)

WillShareButton = KeyboardButton(
    text='еще не дочитал, но в течении дня поделюсь',
)

ShareText = "Уже рассказал своему наставнику, что тебе больше всего понравилось в этом эфире?"

ShareKeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [SharedButton, SharingButton, WillShareButton]
    ]
)

# Keyboards
CountryKeyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [CountrySngButton, CountryEuroButton, CountryOtherButton]
    ]
)

