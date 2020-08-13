#!/usr/bin/env python
# coding: utf-8

# Импортируем из библиотеки python-telegram-bot класс Updater
# который коммуницирует с платформой телеги

import logging

from random import randint
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename='bot.log',
                    level=logging.INFO)
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

# Создадим функцию обработки события в телеге:

def sand_cat_picture(update, context):
    message = "Введите целого кота"
    update.message.reply_text(message)

def greet_user(update, context):
    print("Вызыван /start")
    update.message.reply_text('Здорова!!!!!!')

# Создадим функцию __inpu_bot__ где и будет происходить вся логика работы бота:


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def inpu_bot():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("guess", guess_number))
    dp.add_handler(CommandHandler("cat", sand_cat_picture))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

# Запрашиваем у телеги есть ли новые сообщения?
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__=="__main__":
    inpu_bot()
