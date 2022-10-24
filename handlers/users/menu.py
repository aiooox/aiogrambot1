from loader import dp
from aiogram.dispatcher.filters import Command
from aiogram import types
from keyboards.default import kb_menu
from utils.misc import rate_limit


@rate_limit(limit=15)
@dp.message_handler(Command("menu"))
async def process_hmenu_command(message: types.Message):
    await message.answer('Выбери любую кнопку из меню', reply_markup=kb_menu)
