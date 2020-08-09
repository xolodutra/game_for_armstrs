#!/usr/bin/env python
# coding: utf-8

# Импортируем из библиотеки python-telegram-bot класс Updater
# который коммуницирует с платформой телеги

import logging


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='bot.log',
                    level=logging.INFO)
# Создаем функцию guess_number для игры с пользователем в числа

def guess_number(update, context):
    print(context.args)
    # проверяем какие данные ввёл пользователь
    if context.args:
        message = "Вы ввели число"
    else:
        message = "Введите целое число"
    update.message.reply_text(message)


# Создадим функцию обработки события в телеге:

def greet_user(update, context):
    print("Вызыван /start")
    update.message.reply_text('Здорова!!!!!!')

# Создадим функцию __inpu_bot__ где и будет происходить вся логика работы бота:

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def inpu_bot():
#ключ бота от botFather
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("guess", guess_number))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

# Запрашиваем у телеги есть ли новые сообщения?
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()




if __name__=="__main__":
    inpu_bot()
