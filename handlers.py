from glob import glob
from random import choice
from utils import get_smile, play_random_numbers, main_keyboard

# Создадим функцию обработки события /start в телеге:

def greet_user(update, context):
    print("Вызыван /start")
    context.user_data['emoji'] = get_smile(context.user_data)
    # my_keyboard = ReplyKeyboardMarkup([['Очень нужен котик']])
    update.message.reply_text(
        f"Ну здорова, отец {context.user_data['emoji']}!",
        reply_markup=main_keyboard()
    )

# Создадим функцию __inpu_bot__ где и будет происходить вся логика работы бота:

def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(f"{user_text} {context.user_data['emoji']}", reply_markup=main_keyboard())


# Создаём функцию send_cat_picture для рандомной выдачи картинки с котиком

def send_cat_picture(update, context):
    # сперва получим все картинки в список с помощью glob
    cat_photos_list = glob('images/cat*.*')
    # с помощью функции choice берём рандомное название картинки из этого списка
    cat_pic_filename = choice(cat_photos_list)
    # получаем id чата пользователя
    chat_id = update.effective_chat.id
    # и отправляем явно в чат с этим id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_pic_filename, 'rb'), reply_markup=main_keyboard())
    # pass
    # message = "Введите целого кота"
    # update.message.reply_text(message)

# Создаем функцию guess_number для игры с пользователем в числа


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


def user_coordinates(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    coords = update.message.location
    update.message.reply_text(
        f"Ваши координаты {coords} {context.user_data['emoji']}!",
        reply_markup=main_keyboard()
    )
    print(coords)

