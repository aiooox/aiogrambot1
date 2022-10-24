import logging
from aiogram import Dispatcher
from config import admins
from config import TOKEN

async def startup_not(dp: Dispatcher):
    for admin in admins:
        try:
           await dp.bot.send_message(chat_id=admin, text=f'Бот "{TOKEN}" успешно запущен')
        except Exception as err:
            logging.exception((err))