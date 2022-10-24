import asyncio
from aiogram import types, dispatcher, Dispatcher
from aiogram.dispatcher import DEFAULT_RATE_LIMIT
from aiogram.dispatcher.handler import CancelHandler, current_handler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils.exceptions import Throttled

def rate_limit(limit: int, key=None):

    """

    Decorator for configuring rate limit and key in different functions.


    :param limit:

    :param key:

    :return:

    """


    def decorator(func):

        setattr(func, 'throttling_rate_limit', limit)

        if key:

            setattr(func, 'throttling_key', key)

        return func


    return decorator


