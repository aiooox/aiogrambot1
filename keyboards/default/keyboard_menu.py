from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='💎Наша группа'),
            KeyboardButton(text='🦋Наш чат'),
        ],
        [
        KeyboardButton(text='🌕 Реферальная система'),
        ],
        [
        KeyboardButton(text='💦О нас'),
        KeyboardButton(text='🌊 Саппорт'),
        ],
        [
        KeyboardButton(text='🌑Регистрация')
        ]
    ],
    resize_keyboard=True
)