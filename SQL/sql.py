import sqlite3
import logging
import telebot
import const
global auth


from telebot import types
#tg_conn
bot = telebot.TeleBot(const.token)

#sql_conn
conn = sqlite3.connect(const.adr_con)
cursor = conn.cursor()
conn.close()

# настройки для журнала
logger = logging.getLogger('log')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('someTestBot.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s | %(levelname)-7s | %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)

#klava

@bot.message_handler(commands=["auth"])
def geophone(message):
    global auth
    if auth != 0:
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
        keyboard.add(button_phone)
        bot.send_message(message.chat.id,
                        "Отправе нам свой текущий номер телефона для аунтификации",
                        reply_markup=keyboard)
        if str(message.text) == "89995252655":
            bot.send_message(message.chat.id,
                        "Аунтификация прошла успешно",
                        )
            auth = 0
        else:
            bot.send_message(message.chat.id,
                             "Обратитесь к администратору",
                             )

@bot.message_handler(commands=["start"])
def text (message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
    button1 = types.KeyboardButton(text='Изменение')
    button2 = types.KeyboardButton(text='Добавление')
    button3 = types.KeyboardButton(text='Удаление')
    keyboard.add(button1, button2, button3)


@bot.message_handler(func=lambda item: item.text == 'Изменение', content_types=['text'])
def change(item):
    if auth == 0:
        pass
    else:
        print("Пожалуйста, авторизуйтесь (/auth)")

@bot.message_handler(func=lambda item: item.text == 'Добавление', content_types=['text'])
def add(item):
    if auth == 0:
        pass
    else:
        print("Пожалуйста, авторизуйтесь (/auth)")

@bot.message_handler(func=lambda item: item.text == 'Удаление', content_types=['text'])
def dell(item):
    if auth == 0:
        pass
    else:
        print("Пожалуйста, авторизуйтесь (/auth)")
