from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN
from loader import dp
from utils.misc import rate_limit


@rate_limit(limit=15)
@dp.message_handler(text='/help')
async def process_help_command(message: types.Message):
    await message.answer(f'Привет {message.from_user.first_name}! \n'
                        f'Тебе нужна помощь? Если да, то обратись к @Fafafafaf647 и/или к @moscow1996')