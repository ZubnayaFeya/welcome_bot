import asyncio
import contextlib
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.types import Message

from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

RULES_MESSAGE = 'https://t.me/c/1600777995/16'
CHANNEL_ID = ''
CHAT_ID = ''
ADMIN_ID = ''


dp = Dispatcher()


def welcome_message(username):
    message = (f'Привет, @{username}! ✌️\n'
               f'Добро пожаловать в чат автоклуба WV T5&T6! 🚘\n'
               f'Перед началом общения почитай 👉 '
               f'<a href="{RULES_MESSAGE}">правила</a>')
    return message


@dp.message(F.new_chat_members)
async def new_member(message: Message):
    for user in message.new_chat_members:
        name = user.username if user.username else user.full_name
        await message.answer(welcome_message(name), parse_mode=ParseMode.HTML)


async def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s'
    )

    bot = Bot(token=BOT_TOKEN)

    try:
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f'[Exception] - {e}', exc_info=True)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    with contextlib.suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(main())
