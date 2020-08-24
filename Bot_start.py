#!/usr/bin/env python
# coding: utf-8

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

from anketa import anketa_start, anketa_name
from handlers import (greet_user, guess_number, send_cat_picture, user_coordinates, 
                talk_to_me)
import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)


def inpu_bot():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
# ОБработка анкеты - диалогового бота - начало
    anketa = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.regex('^(Заполнить анкету)$'), anketa_start)
        ],
        states={
            "name":[MessageHandler(Filters.text, anketa_name)]
        },
        fallbacks=[]
    )
    dp.add_handler(anketa)
# Обработка анкеты - диалогового бота - конец


    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("guess", guess_number))
    dp.add_handler(CommandHandler("cat", send_cat_picture))
    dp.add_handler(MessageHandler(Filters.regex('^(Очень нужен котик)$'), send_cat_picture))
    dp.add_handler(MessageHandler(Filters.location, user_coordinates))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

# Запрашиваем у телеги есть ли новые сообщения?
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__=="__main__":
    inpu_bot()