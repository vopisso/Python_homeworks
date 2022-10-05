def start(update, context):
    context.bot.send_message(update.effective_chat.id, f'Привет, {update.effective_user.first_name}!\nЯ бот и я умею '
                                                       f'удалять слова, которые содержат "абв"')


def message(update, context):
    text = update.message.text
    context.bot.send_message(update.effective_chat.id, f'Твой текст без "абв":\n\n{reduce_abv(text)}')


def reduce_abv(line):
    text_list = line.split()
    fragment = 'абв'
    new_text = []
    for word in text_list:
        if fragment not in word:
            new_text.append(word)

    return ' '.join(new_text)

