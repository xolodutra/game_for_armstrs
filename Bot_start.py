#!/usr/bin/env python
# coding: utf-8

from emoji import emojize
from glob import glob
import logging
from random import choice, randint
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)


# Создадим функцию обработки события в телеге:

def greet_user(update, context):
    print("Вызыван /start")
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(f"Ну здорова, отец {context.user_data['emoji']}!")


# Создадим функцию __inpu_bot__ где и будет происходить вся логика работы бота:

def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(f"{user_text} {context.user_data['emoji']}")

def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']


# Создаём функцию send_cat_picture для рандомной выдачи картинки с котиком

def send_cat_picture(update, context):
    # сперва получим все картинки в список с помощью glob
    cat_photos_list = glob('images/cat*.*')
    # с помощью функции choice берём рандомное название картинки из этого списка
    cat_pic_filename = choice(cat_photos_list)
    # получаем id чата пользователя
    chat_id = update.effective_chat.id
    # и отправляем явно в чат с этим id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_pic_filename, 'rb'))
    # pass
    # message = "Введите целого кота"
    # update.message.reply_text(message)

# Создаем функцию guess_number для игры с пользователем в числа

def play_random_numbers(user_number):
    bot_number = randint(user_number-10, user_number+10)
    if user_number > bot_number:
        message = f"Ты загадал {user_number}, я загадал {bot_number}, ты выиграл!"
    elif user_number == bot_number:
        message = f"Ты загадал {user_number}, я загадал {bot_number}, ничья!"
    else: 
        message = f"Ты загадал {user_number}, я загадал {bot_number}, я выиграл!"
    return message

def guess_number(update, context):
    print(context.args)
    # проверяем какие данные ввёл пользователь
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_numbers(user_number)
        except (TypeError, ValueError):
            message = "Введите целое число"
    else:
        message = "Введите целое число"
    update.message.reply_text(message)



def inpu_bot():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("guess", guess_number))
    dp.add_handler(CommandHandler("cat", send_cat_picture))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

# Запрашиваем у телеги есть ли новые сообщения?
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__=="__main__":
    inpu_bot()
