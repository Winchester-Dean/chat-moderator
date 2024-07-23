from aiogram import types, Dispatcher
from .base_handle import BaseHandler

class EchoHandler(BaseHandler):
    def register(self, dispatcher: Dispatcher):
        dispatcher.register_message_handler(self.echo, commands=['echo'])
    
    async def echo(self, message: types.Message):
        await message.answer(message.text)

