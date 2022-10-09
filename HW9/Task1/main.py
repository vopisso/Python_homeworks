from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from controller import *

bot = Bot(token='')
updater = Updater(token='')
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
reduce_handler = MessageHandler(Filters.text, message)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(reduce_handler)

updater.start_polling()
updater.idle()
