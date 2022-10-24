from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher



async def set_default_commands(dp):
    await dp.bot.set_my_commands([
types.BotCommand('start', 'Запускает бот *ТЫК*'),
types.BotCommand('help', 'Быстрый гайд по боту *ТЫК*'),
types.BotCommand('menu', 'Основное меню бота *ТЫК*'),
types.BotCommand('register', 'Регистрация в чат *ТЫК*'),
types.BotCommand('profile', 'Получит данные с греаса *ТЫК*')



#types.BotCommand('inline', 'Меню с инлайн кнопками *ТЫК*')
    ])
