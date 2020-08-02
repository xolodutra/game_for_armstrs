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
    updater = Updater(settings.API_KEY, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

# Запрашиваем у телеги есть ли новые сообщения?
    updater.start_polling()
    updater.idle()

if __name__=="__main__":
    inpu_bot()
