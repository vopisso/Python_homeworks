from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from scripts import check
from random import choice as ch


bot = Bot(token=' ')
updater = Updater(token=' ')
dispatcher = updater.dispatcher

data = {6: 4, 7: 4, 8: 4, 9: 4, 10: 4, 'Валет': 4, 'Дама': 4, 'Король': 4,
        'Туз': 4}

count_points_user = []
count_points_bot = 0

WINNER = None # 0 - ничья, 1 - выиграл пользователь, -1 - выиграл бот

BOT = 1
USER = 2

bot_points = 0
user_points = 0


def winner_check(user, bots):
    global WINNER
    if sum(user) > 21 and bots < 22 or sum(user) < bots and sum(user) <= 21 and bots <= 21:
        WINNER = -1
    elif bots > 21 and sum(user) < 22 or sum(user) > bots and sum(user) <= 21 and bots <= 21:
        WINNER = 1
    elif sum(user) > 21 and bots > 21:
        WINNER = 0


def start(update, context):
    global count_points_user, count_points_bot, WINNER
    global bot_points, user_points

    count_points_user.clear()
    count_points_bot = 0
    WINNER = None

    for i in range(2):
        data_object = ch(list(data.keys()))
        while data[data_object] == 0:
            data_object = ch(list(data.keys()))
        data[data_object] -= 1
        points = check(data_object)
        count_points_user.append(points)

    for i in range(2):
        data_object = ch(list(data.keys()))
        print(data_object)
        while data[data_object] == 0:
            data_object = ch(list(data.keys()))
        data[data_object] -= 1
        points = check(data_object)
        count_points_bot += points

    if sum(count_points_user) > 21 and count_points_bot < 22:
        context.bot.send_message(update.effective_chat.id, "Перебор выиграл бот")
        bot_points += 1
    elif count_points_bot > 21 and sum(count_points_user) < 22:
        context.bot.send_message(update.effective_chat.id, "Перебор выиграл ты")
        user_points += 1
    elif sum(count_points_user) > 21 and count_points_bot > 21:
        context.bot.send_message(update.effective_chat.id, "Перебор вы лузеры")
    else:
        a = '\n'.join([str(i) for i in count_points_user])
        context.bot.send_message(update.effective_chat.id, f"{a}\nСумма: {sum(count_points_user)}")


def yet(update, context):
    global count_points_user
    global bot_points
    global user_points
    if sum(count_points_user) < 21:
        data_object = ch(list(data.keys()))
        while data[data_object] == 0:
            data_object = ch(list(data.keys()))
        data[data_object] -= 1
        points = check(data_object)
        count_points_user.append(points)

        a = '\n'.join([str(i) for i in count_points_user])
        winner_check(count_points_user, count_points_bot)
        if sum(count_points_user) > 21:
            context.bot.send_message(update.effective_chat.id, f"{update.effective_user.first_name}, ты проиграл")
            bot_points += 1
        context.bot.send_message(update.effective_chat.id, f"{a}\nСумма: {sum(count_points_user)}")
    else:
        context.bot.send_message(update.effective_chat.id, "Ты не можешь взять больше!")


def stop(update, context):
    if WINNER == None:
        global count_points_bot
        global bot_points
        global user_points
        context.bot.send_message(update.effective_chat.id, 'Вы закончили набор, теперь набирает бот')
        if count_points_bot > 15 and ch([True, False]) or count_points_bot <= 12:
            data_object = ch(list(data.keys()))
            while data[data_object] == 0:
                data_object = ch(list(data.keys()))
            data[data_object] -= 1
            points = check(data_object)
            count_points_bot += points

        winner_check(count_points_user, count_points_bot)
        context.bot.send_message(update.effective_chat.id, f'Кол-во очков у бота: {count_points_bot}\n'
                                                           f'Кол-во очков у {update.effective_user.first_name}: {sum(count_points_user)}')
        if WINNER == -1:
            context.bot.send_message(update.effective_chat.id, f"{update.effective_user.first_name}, "
                                                               f"у тебя перебор выиграл бот")
            bot_points += 1
        elif WINNER == 1:
            context.bot.send_message(update.effective_chat.id, f"{update.effective_user.first_name}, ты выиграл")
            user_points += 1
        elif WINNER == 0:
            context.bot.send_message(update.effective_chat.id, f"{update.effective_user.first_name} вы с ботом лузеры")
    else:
        context.bot.send_message(update.effective_chat.id, f"Игра окончена, чтобы начать заново напишите /start")


def count_check(update, context):
    context.bot.send_message(update.effective_chat.id, f" Счёт:\n{update.effective_user.first_name} - {user_points}\n"
                                                       f"бот - {bot_points}")


start_handler = CommandHandler('start', start)
still_handler = CommandHandler('yet', yet)
stop_handler = CommandHandler('stop', stop)
count_check_handler = CommandHandler('count', count_check)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(still_handler)
dispatcher.add_handler(stop_handler)
dispatcher.add_handler(count_check_handler)

updater.start_polling()
updater.idle()  # ctrl + c