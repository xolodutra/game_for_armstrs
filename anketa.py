from telegram import ParseMode, ReplyKeyboardRemove, ReplyKeyboardMarkup
from telegram.ext import ConversationHandler
from utils import main_keyboard

def anketa_start(update, context):
    update.message.reply_text(
        "Привет! Как вас там?!",
        reply_markup=ReplyKeyboardRemove()
    )
    return "name"
def anketa_name(update, context):
    user_name = update.message.text
    if len(user_name.split()) < 2:
        update.message.reply_text("Мне нужны твои имя и фамилия!")
        return "name"
    else:
        context.user_data["anketa"] = {"name": user_name}
        reply_keyboard = [["1", "2", "3", "4", "5"]]
        update.message.reply_text(
            "Пожалуйста оцените бота от 1 до 5",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        )
        return "rating"
def anketa_rating(update, context):
    context.user_data["anketa"]["rating"] = int(update.message.text)

    update.message.reply_text(
        "Оставьте комментарий или скипните /skip"
    )
    return "comment"

def anketa_comment(update, context):
    context.user_data['anketa']['comment'] = update.message.text
    user_text = anketa_format(context.user_data['anketa'])
    update.message.reply_text(user_text, reply_markup=main_keyboard(),
                                parse_mode=ParseMode.HTML)
    return ConversationHandler.END

def anketa_skip(update, context):
    user_text = anketa_format(context.user_data['anketa'])
    update.message.reply_text(user_text, reply_markup=main_keyboard(),
                                parse_mode=ParseMode.HTML)
    return ConversationHandler.END

def anketa_format(user_anketa):
    user_text = f"""<b>Имя Фамилия:</b> {user_anketa['name']}
<b>Оценка:</b> {user_anketa['rating']}
"""
    if user_anketa.get('comment'):
        user_text += f"<b>Комментарий:</b> {user_anketa['comment']}"
    return user_text