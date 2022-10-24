from loader import dp
from aiogram import types
from keyboards.inline.inline import ikb_menu

@dp.message_handler(text='/inline')
async def process_inline_command(message: types.Message):
    await message.answer('Инлайн кнопки ниже', reply=ikb_menu)