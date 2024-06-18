import telegram
from dotenv import load_dotenv
import os


load_dotenv()
token = os.environ['TELEGRAM_BOT_TOKEN']
chat_id = os.environ['TELEGRAM_CHAT_ID']
bot = telegram.Bot(token)

bot.send_message(chat_id=chat_id, text='Hello!')