from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton('🌊 Саппорт', url='t.me/Fafafafaf647'),
                                        InlineKeyboardButton('💎Наша группа', url='t.me/Fafafafaf647'), #ИЗМЕНИТЬ ССЫЛКУ
                                        InlineKeyboardButton('🦋Наш чат', url='t.me/areaa24'),
                                    ],
                                    [
                                        InlineKeyboardButton('💦О нас', callback_data='Мы пиарим чаты за счет вас, а вы взамен получаете деньги!')
                                    ]
                                ])

