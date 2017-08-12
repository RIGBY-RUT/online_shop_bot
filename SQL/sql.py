import sqlite3
import logging
import telebot
import const
global auth, flag


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


#auth
@bot.message_handler(commands=["auth"])
def auth(message):
    global auth
    auth = 1
    if auth != 0:
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
        keyboard.add(button_phone)
        bot.send_message(message.chat.id,
                        "Отправте нам свой текущиё номер телефона для аунтификации",
                        reply_markup=keyboard)

@bot.message_handler(content_types=['contact'])
def restart(message):
    nomer = message.contact.phone_number
    IDmes = message.contact.user_id
    #IDuser = telebot.user.id

    #bot.send_message(message.chat.id,
    #                IDuser)
    if (str(nomer) == "79175312197"): ####and (IDmes) == IDuser#### тут нужно проверить чей контакт скинул пользователь, свой или рандомного человека
        bot.send_message(message.chat.id,
                         "Аунтификация прошла успешно, можно перейти к меню (/start)",
                         )
        bot.send_message(message.chat.id,
                         "Не забудьте выйти после окончания изменений",
                         )
        global auth
        auth = 0

    else:
        bot.send_message(message.chat.id,
                         "Обратитесь к администратору",
                         )



#klava

@bot.message_handler(commands=["start"])
def text(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
    button1 = types.KeyboardButton(text='Изменить')
    button2 = types.KeyboardButton(text='Добавить')
    button3 = types.KeyboardButton(text='Удалить')
    button4 = types.KeyboardButton(text='Выход')
    keyboard.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id,
                     "Что нужно сделать с товаром?",
                     reply_markup=keyboard)


@bot.message_handler(func=lambda item: item.text == 'Изменить', content_types=['text'])
def change(message):
    if auth == 0:
        global flag
        flag = "izm"






        pass
    else:
        bot.send_message(message.chat.id,"Пожалуйста, авторизуйтесь (/auth)")

@bot.message_handler(func=lambda item: item.text == 'Добавить', content_types=['text'])
def add(message):
    if auth == 0:
        global flag
        flag = "dob"






        pass
    else:
        bot.send_message(message.chat.id,"Пожалуйста, авторизуйтесь (/auth)")

@bot.message_handler(func=lambda item: item.text == 'Удалить', content_types=['text'])
def dell(message):
    if auth == 0:
        global flag
        flag = "uda"





        pass
    else:
        bot.send_message(message.chat.id,"Пожалуйста, авторизуйтесь (/auth)")

#Exet
@bot.message_handler(func=lambda item: item.text == 'Выход', content_types=['text'])
def dell(message):
    global auth
    auth = 1
    bot.send_message(message.chat.id, "Вы успешно вышли!")


@bot.message_handler(content_types=['text'])
def restart(message):
    global flag
    if flag = 
    bot.send_message(chat_id=message.chat.id, text='Выберите пункт меню или введите корректный запрос')

if __name__ == '__main__':
    bot.polling(none_stop=True)