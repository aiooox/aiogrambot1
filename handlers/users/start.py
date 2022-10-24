from aiogram import types

from loader import dp
from utils.misc.throttling import rate_limit


@rate_limit(limit=15)
@dp.message_handler(text='/start')
async def process_start_command(message: types.Message):
    await message.answer(f'Привет {message.from_user.first_name}! \n'
                        f'Твой ID: {message.from_user.id}')