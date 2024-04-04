import asyncio
import contextlib
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.utils.markdown import link

BOT_TOKEN = '7007068357:AAHAEquXPhQzgTB_gi4EHPBHZSP-rGzd_RE'
RULES_MESSAGE = 'https://t.me/c/1600777995/16'
CHANNEL_ID = ''
CHAT_ID = ''
ADMIN_ID = ''


dp = Dispatcher()


def welcome_message(username):
    message = (f'Привет, @{username}. '
               f'В нашем чате царит дружеская атмосфера, а потому мы просим тебя представиться. '
               f'Для этого достаточно написать '
               f'своё настоящее имя(без ников и прозвищ), '
               f'город где живёшь, и '
               f'машину на которой ездишь.\n'
               f'Если представляться нет желания, то увы, тебе наш чат не подходит.'
               f'С правилами чата можно ознакомиться '
               f'<a href="{RULES_MESSAGE}">в закреплённом сообщении.</a>')
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
        bot.session.close()


if __name__ == '__main__':
    with contextlib.suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(main())
