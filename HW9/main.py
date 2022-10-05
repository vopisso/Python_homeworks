from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from controller import *

bot = Bot(token='5717925844:AAE1IjA_6FmDoiy0deyrJVoqRRZzNY3ueGo')
updater = Updater(token='5717925844:AAE1IjA_6FmDoiy0deyrJVoqRRZzNY3ueGo')
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
reduce_handler = MessageHandler(Filters.text, message)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(reduce_handler)

updater.start_polling()
updater.idle()