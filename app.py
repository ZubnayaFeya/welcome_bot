import asyncio
import contextlib
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.types import ChatJoinRequest

BOT_TOKEN = ''
CHANNEL_ID = ''
CHAT_ID = ''
ADMIN_ID = ''

WELCOME_MESSAGE = ''


async def approve_request(chat_join: ChatJoinRequest, bot: Bot):
    welcome_message = WELCOME_MESSAGE
    await bot.send_message(chat_id=chat_join.from_user.id, text=welcome_message)
    await chat_join.approve()


async def start():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s'
    )

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.chat_join_request.register(approve_request, F.chat.id == CHAT_ID)

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as e:
        logging.error(f'[Exception] - {e}', exc_info=True)
    finally:
        bot.session.close()


if __name__ == '__main__':
    with contextlib.suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(start())
