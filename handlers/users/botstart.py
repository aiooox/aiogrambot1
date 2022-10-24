from aiogram import types

from loader import dp
from utils.dbapi import quick_commands as commands
from utils.misc.throttling import rate_limit


@rate_limit(limit=3)
@dp.message_handler(text='/start')
async def process_start_command(message: types.Message):
    try:
        user = await commands.select_user(message.from_user.id)
        if user.status == 'active':
            await message.answer(f'Привет {message.from_user.first_name}\n'
                                 f'Ты уже зарегистрирован')
        elif user.status == 'banned':
            await message.answer('Ты забанен')
    except Exception:
        await commands.add_user(user_id=message.from_user.id,
                                first_name=message.from_user.first_name,
                                last_name=message.from_user.last_name,
                                username=message.from_user.username,
                                status='active')
        await message.answer('Вы успешно зарегистрированы')

@rate_limit(limit=3)
@dp.message_handler(text='/ban')
async def getban_command(message: types.Message):
    await commands.update_username('ban')
    await message.answer('Ты забанен')

@rate_limit(limit=3)
@dp.message_handler(text='/unban')
async def getban_command(message: types.Message):
    await commands.update_username('ban')
    await message.answer('Ты забанен')
