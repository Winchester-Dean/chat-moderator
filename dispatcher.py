from aiogram import Bot, Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from filters import IsAdminFilter
from config import TOKEN

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

dp.middleware.setup(LoggingMiddleware())
dp.filters_factory.bind(IsAdminFilter)

