from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import config
from config import TOKEN, CHATLINK, GROUPLINK
from loader import dp
from utils.misc import rate_limit


@rate_limit(limit=15)
@dp.message_handler(text='💎Наша группа')
async def process_group_command(message: types.Message):
    await message.answer(f'Наша группа {config.GROUPLINK}')

@rate_limit(limit=15)
@dp.message_handler(text='🦋Наш чат')
async def process_group_command(message: types.Message):
    await message.answer(f'Наш чат {config.CHATLINK}')

@rate_limit(limit=15)
@dp.message_handler(text='🌕 Реферальная система')
async def process_group_command(message: types.Message):
    await message.answer(f'Пригласи друга по своей индивидуальной ссылке "bot.start.code" и получи за это бонус') #СДЕЛАТЬ ПЛЕЙС XОЛДЕР!

@rate_limit(limit=15)
@dp.message_handler(text='💦О нас')
async def process_group_command(message: types.Message):
    await message.answer('Мы пиарим чаты за счет вас, а вы взамен получаете деньги!')

@rate_limit(limit=15)
@dp.message_handler(text='🌊 Саппорт')
async def process_group_command(message: types.Message):
    await message.answer('Для вывода денег и/или по другим вопросам пишите админам. Узнать тг админо можно командой /help')



