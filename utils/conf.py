import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

RULES_MESSAGE = os.getenv('LINK_MESSAGE')
CHANNEL_ID = ''
CHAT_ID = ''
ADMIN_ID = ''

logging_format = '%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s'





