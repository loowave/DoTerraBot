from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

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

SharedButton = InlineKeyboardButton(
    text='да, уже поделился',
)

SharingButton = InlineKeyboardButton(
    text='еще нет, уже бегу',
)

WillShareButton = InlineKeyboardButton(
    text='еще не дочитал, но в течении дня поделюсь',
)

ShareText = "Уже рассказал своему наставнику, что тебе больше всего понравилось в этом эфире?"

ShareKeyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [SharedButton, SharingButton, WillShareButton]
    ]
)

# Keyboards
CountryKeyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [CountrySngButton, CountryEuroButton, CountryOtherButton]
    ]
)

