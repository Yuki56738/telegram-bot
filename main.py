import datetime
import logging
import os
from zoneinfo import ZoneInfo

import pytz
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
async def poland(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dt_utc = datetime.datetime.utcnow()
    # dt_now_poland = datetime.datetime(dt_utc.year, dt_utc.month, dt_utc.day, dt_utc.hour, dt_utc.minute, dt_utc.second, tzinfo=ZoneInfo('Poland'))
    dt_now_poland = pytz.timezone('Poland').localize(dt_utc)
    dt_dst = dt_now_poland.dst()
    print(dt_dst)
    if str(dt_dst) == '0:00:00':
        dt_now_poland = dt_now_poland + datetime.timedelta(hours=1)
    print(str(dt_now_poland))
    # dt_now_poland_dst = dt_now_poland.dst()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=str(dt_now_poland))
async def japan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dt_now = datetime.datetime.now()
    # dt_japan = pytz.timezone('Japan').localize(dt_utc)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=str(dt_now))
application = ApplicationBuilder().token(os.getenv('TOKEN')).build()
start_handler = CommandHandler('start', start)
poland_handler = CommandHandler('poland', poland)
japan_handler = CommandHandler('japan', japan)
application.add_handler(start_handler)
application.add_handler(poland_handler)
application.add_handler(japan_handler)

application.run_polling()