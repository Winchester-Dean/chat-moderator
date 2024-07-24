from aiogram import types, Dispatcher
from .base_handle import BaseHandler

class BanHandler(BaseHandler):
    def register(self, dp: Dispatcher):
        dp.register_message_handler(self.ban, commands=["ban"], is_admin=True)

    async def ban(self, msg: types.Message):
        args = msg.get_args()

        if args:
            try:
                user_id = int(args)
            except ValueError:
                return await msg.reply("Указан неправильный формат ID пользователя.")

            chat_members = await msg.bot.get_chat_member(msg.chat.id, user_id)
            for member in chat_members:
                if member.user.id == user_id:
                    try:
                        await msg.bot.kick_chat_member(msg.chat.id, user_id)
                    except Exception as e:
                        return await msg.answer(str(e))
                    else:
                        return await msg.reply(f"Пользователь с ID {user_id} забанен.")

            return await msg.reply("Пользователя с таким ID нет в чате.")
        elif msg.reply_to_message:
            user_id = msg.reply_to_message.from_user.id
            try:
                await msg.bot.kick_chat_member(msg.chat.id, user_id)
            except Exception as e:
                return await msg.answer(str(e))
            else:
                return await msg.reply(f"Пользователь {msg.reply_to_message.from_user.get_mention()} забанен.")
        else:
            return await msg.reply("Эту команду нужно использовать с аргументом ID пользователя или ответом на сообщение.")

class DBanHandler(BaseHandler):
    def register(self, dp: Dispatcher):
        dp.register_message_handler(self.dban, commands=["dban"], is_admin=True)

    async def dban(self, msg: types.Message):
        args = msg.get_args()
        
        if args:
            try:
                user_id = int(args)
            except ValueError:
                return await msg.reply("Указан неправильный формат ID пользователя.")
            
            chat_member = await msg.bot.get_chat_member(msg.chat.id, user_id)
            for member in chat_members:
                if member.user.id == user_id:
                    try:
                        await msg.bot.kick_chat_member(msg.chat.id, user_id)
                        await msg.delete()
                        async for message in msg.chat.history():
                            if message.text.startswith("/dban") and message.from_user.id == msg.from_user.id:
                                await message.delete()
                    except Exception as e:
                        return await msg.answer(str(e))
                    else:
                        return await msg.reply(f"Пользователь с ID {user_id} забанен и все его сообщения в чате удалены.")
            return await msg.reply("Пользователя с таким ID нет в чате.")
        elif msg.reply_to_message:
            user_id = msg.reply_to_message.from_user.id
            try:
                await msg.bot.kick_chat_member(msg.chat.id, user_id)
                await msg.delete()
            except Exception as e:
                return await msg.answer(str(e))
            else:
                return await msg.reply(f"Пользователь {msg.reply_to_message.from_user.get_mention()} забанен и все его сообщения в чате удалены.")
        else:
            return await msg.reply("Эту команду нужно использовать с аргументом ID пользователя или ответом на сообщение.")

