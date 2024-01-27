import logging
import os

from telegram import *
from telegram.ext import *
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! I'm a bot!")

application = ApplicationBuilder().token(os.getenv('TOKEN')).build()
start_handler = CommandHandler('start', start)
application.add_handler(start_handler)

application.run_polling()