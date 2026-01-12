import datetime

from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message, Chat

from utils.conf import RULES_MESSAGE
from utils.prepare import prepare_datetime

router = Router()

START_TIME = datetime.datetime.now()


def _welcome_message(username):
    message = (f'Привет, @{username}! ✌️\n'
               f'Добро пожаловать в чат автоклуба WV T5&T6! 🚘\n'
               f'Перед началом общения почитай 👉 '
               f'<a href="{RULES_MESSAGE}">правила</a>')
    return message


@router.message(Command(commands=['status']))
async def get_status_bot(message: Message):
    chat_admins = await message.bot.get_chat_administrators(message.chat.id)
    chat_admins_ids = [admin.user.id for admin in chat_admins]
    if message.from_user.id in chat_admins_ids:
        uptime = datetime.datetime.now() - START_TIME
        text = f'Бот работает {prepare_datetime(uptime)}'
        await message.answer(text)


@router.message(F.new_chat_members)
async def new_member(message: Message):
    for user in message.new_chat_members:
        name = user.username if user.username else user.full_name
        await message.answer(_welcome_message(name), parse_mode=ParseMode.HTML)
