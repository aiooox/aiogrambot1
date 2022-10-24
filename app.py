from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher



async def startup(dp):
    import middleware
    middleware.setup(dp)
    from utils.notifyadmins import startup_not
    await startup_not(dp)
    from loader import db
    from utils.dbapi.db_gino import on_startup

    print('подключение к гресу')
    await on_startup(dp)

    print('Удаление бд')
    await db.gino.drop_all()

    print('создание таблицы')
    await db.gino.create_all()

    print('готово')

    from utils.botcommands import set_default_commands
    await set_default_commands(dp)
    print('Бот запущен ///')

if __name__ == '__main__':
    from aiogram import executor
    from loader import dp

    executor.start_polling(dp, on_startup=startup)