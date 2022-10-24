from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram import types

from loader import dp
from states import register
from utils.misc import rate_limit


@rate_limit(limit=15)
@dp.message_handler(Command('register'))
async def register_process(message: types.Message):
    await message.answer(f'{message.from_user.full_name}, пожалуйста зарегистрируйся!\n'
                         f'1. Введи свое имя')
    await register.test1.set()

@rate_limit(limit=15)
@dp.message_handler(text='🌑Регистрация')
async def register_process(message: types.Message):
    await message.answer(f'{message.from_user.full_name}, пожалуйста зарегистрируйся!\n'
                         f'1. Введи свое имя')
    await register.test1.set()

@rate_limit(limit=15)
@dp.message_handler(state=register.test1)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test1=answer)
    await message.answer('2. Введи свой возраст')
    await register.test2.set()

@rate_limit(limit=15)
@dp.message_handler(state=register.test2)
async def state2(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test1=answer)
    data = await state.get_data()
    name = data.get('test2')
    years = data.get('test1')
    try:
        intyears = int(years)
    except:
        await message.answer(f'Пройдите регистрацию еще раз и укажите ваш возраст корректно')
    if intyears > 13:
        await message.answer(f'Регистрация завершена! теперь ты имеешь доступ в чат!')
        await register.test2.set()
    else:
        await message.answer('Извините, но ваш возраст не совпадает с минимальным, пожалуйста напишите саппорту, если вы указали свой возраст не правильно и/или по случайности. /help для подтверждения вашего возраста')
    await state.finish()


