import sqlite3
import logging
import telebot
import const
global auth, flag, prod
prod = 0
flag = "nothing"

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
                        "Отправьте нам свой текущий номер телефона для аунтификации",
                        reply_markup=keyboard)

@bot.message_handler(content_types=['contact'])
def restart(message):
    nomer = message.contact.phone_number
    IDmes = message.contact.user_id
    #IDuser = telebot.user.id

    #bot.send_message(message.chat.id,
    #                IDuser)
    if (str(nomer) == str("+79251296901") or str("+79175312197") or str("+79850752856")): ####and (IDmes) == IDuser#### тут нужно проверить чей контакт скинул пользователь, свой или рандомного человека
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
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
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
        bot.send_message(message.chat.id,
                         "В списке товаров присутствуют:")

        conn = sqlite3.connect(const.adr_con)
        cursor = conn.cursor()

        cursor.execute("SELECT name FROM products")
        results = cursor.fetchall()

        kolich = len(results)
        for kolich in range(len(results)):
            name = str(results[kolich])
            bot.send_message(message.chat.id,
                             name[2:-3])
        conn.close()
        bot.send_message(message.chat.id,
                         "Напишите боту какое наименование вы хотите редактиповать")






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

@bot.message_handler(func=lambda item: item.text == 'Название товара', content_types=['text'])
def change(message):
    if auth == 0:
        global prod, flag
        flag = "c_name"
        bot.send_message(message.chat.id,
                         "Текущее назвние: " + prod + "\nОтправьте боту новое название.")
        pass
    else:
        bot.send_message(message.chat.id,"Пожалуйста, авторизуйтесь (/auth)")

@bot.message_handler(func=lambda item: item.text == 'Количество единиц товара', content_types=['text'])
def change(message):
    if auth == 0:
        global flag
        flag = "c_quantity"
        bot.send_message(message.chat.id,
                        "Отправьте боту актуальное количество единиц товара.")
        pass
    else:
        bot.send_message(message.chat.id,"Пожалуйста, авторизуйтесь (/auth)")

@bot.message_handler(func=lambda item: item.text == 'Количество единиц товара в предзаказе', content_types=['text'])
def change(message):
    if auth == 0:
        global prod, flag
        flag = "c_preorder"
        bot.send_message(message.chat.id,
                         "Отправьте боту актуальное количество единиц товара в предзаказе")
        pass
    else:
        bot.send_message(message.chat.id,"Пожалуйста, авторизуйтесь (/auth)")


@bot.message_handler(func=lambda item: item.text == 'Изображение товара', content_types=['text'])
def change(message):
    if auth == 0:
        global prod, flag
        flag = "c_image"
        bot.send_message(message.chat.id,
                         "Отправьте боту новое изображение товара")
        pass
    else:
        bot.send_message(message.chat.id,"Пожалуйста, авторизуйтесь (/auth)")


@bot.message_handler(content_types=['photo'])
def change(message):
    print("ahvabonga")



@bot.message_handler(content_types=['text'])
def restart(message):
    global flag, prod
    #if flag != ("izm" or "dob" or "uda"):
     #   #print (flag)
     #   bot.send_message(chat_id=message.chat.id, text='Выберите пункт меню или введите корректный запрос')

    if flag == "izm":
        finder = 0
        prod = message.text
        conn = sqlite3.connect(const.adr_con)
        cursor = conn.cursor()

        cursor.execute("SELECT name FROM products ")
        results = cursor.fetchall()

        print(results)
        kolich = results
        conn.close()
        for kolich in results:
            name = str(kolich)
            print (name[2:-3])
            print (prod)
            if str(name[2:-3]) == str(prod):
                bot.send_message(chat_id=message.chat.id, text="Веденное значение найдено")
                finder = 1


                #выделение строки с выбранным товаром

                prod = message.text
                conn = sqlite3.connect(const.adr_con)
                cursor = conn.cursor()

                cursor.execute("""SELECT num, name, quantity, pre_order, Image_title
                                FROM products
                                WHERE name = '""" + prod +"'")
                results = cursor.fetchall()
                print (results)
                for rec in results:
                    num, name, quantity, pre_order, Image_title = rec
                    #print (num, name, quantity, pre_order, Image_title)\

                    #### KLAVA DLA IZMENENIYA TABLIC ####

                bot.send_message(chat_id=message.chat.id, text=(" Номер товара: " + str(num) +"\n Название: " + str(name) +"\n В наличии: " + str(quantity) +"\n В предзаказе: " + str(pre_order) +"\n Изображение товара " + str(Image_title)))
                keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
                с_name = types.KeyboardButton(text="Название товара")
                с_quantity = types.KeyboardButton(text="Количество единиц товара")
                c_preorder = types.KeyboardButton(text="Количество единиц товара в предзаказе")
                c_image = types.KeyboardButton(text="Изображение товара")
                keyboard.add(с_name, с_quantity, c_preorder, c_image)
                bot.send_message(message.chat.id,
                                 "Изменить",
                                 reply_markup=keyboard)

                conn.close()
                break
        conn.close()

    elif flag == "dob":
        pass
    elif flag == "uda":

        prod = message.text
        conn = sqlite3.connect(const.adr_con)
        cursor = conn.cursor()

        cursor.execute("SELECT name FROM products")
        results = cursor.fetchall()

        print(results)
        kolich = len(results)
        for kolich in range(len(results)):
            name = str(results[kolich])
            if str(name[2:-3]) == str(prod):
                print(name[2:-3])
                print (prod)
                bot.send_message(chat_id=message.chat.id, text="Веденное значение найдено")


                print(results)
                kolich = len(results)

            else:
                bot.send_message(chat_id=message.chat.id, text="Введенное значение отсутствует")

    elif flag == "c_name":
        new_name = message.text
        conn = sqlite3.connect(const.adr_con)
        cursor = conn.cursor()

        cursor.execute("SELECT name FROM products ")
        results = cursor.fetchall()
        old_name = results

        #print(results)
        cursor.execute("SELECT COUNT(*) FROM `products`")
        results = cursor.fetchall()
        kolich = str(results)[2:-3]
        kolich = int(kolich)
        conn.close()
        conn.close()
        #print(kolich)

        for word in old_name:
            if int(kolich) > 0:
                kolich = int(kolich) - 1
                name = str(old_name[int(kolich)])
                #print(name[2:-3])
                #print(new_name)
                #print(kolich)
                if str(name[2:-3]) == str(new_name):
                    bot.send_message(message.chat.id,
                                     "Hазвние: '" + new_name + "' yже используется.")
                    break
                elif int(kolich) == 0:
                    conn.close()
                    bot.send_message(message.chat.id,
                                    "Новое название товара: " + new_name + "\n Для продолжения введите /start")
                    #print(prod)
                    conn = sqlite3.connect(const.adr_con)
                    cursor = conn.cursor()

                    cursor.execute("UPDATE products SET name = '" + str(new_name) + "' WHERE name = '" + str(prod) + "';")

                    conn.commit()

                    conn.close()
                    flag = "nothing"

    elif flag == "c_quantity":
        enter_num = message.text

        def isfloat(value):
            try:
                float(value)
                return True
            except ValueError:
                return False
        if isfloat(enter_num):
            print('это число')
            conn = sqlite3.connect(const.adr_con)
            cursor = conn.cursor()
            cursor.execute("UPDATE products SET quantity = '" + str(enter_num) + "' WHERE name = '" + str(prod) + "';")
            conn.commit()
            conn.close()
            bot.send_message(message.chat.id, "Количество товара '"+str(prod)+"' = "+str(enter_num)+"\n /start")
            flag = "nothing"
        else:
            bot.send_message(message.chat.id, 'Это не число')

    elif flag == "c_preorder":
        enter_num = message.text

        def isfloat(value):
            try:
                float(value)
                return True
            except ValueError:
                return False

        if isfloat(enter_num):
            print('это число')
            conn = sqlite3.connect(const.adr_con)
            cursor = conn.cursor()
            cursor.execute("UPDATE products SET pre_order = '" + str(enter_num) + "' WHERE name = '" + str(prod) + "';")
            conn.commit()
            conn.close()
            bot.send_message(message.chat.id, "Количество товара в предзаказе '" + str(prod) + "' = " + str(enter_num) + "\n /start")
            flag = "nothing"
        else:
            bot.send_message(message.chat.id, 'Это не число')

    else:
        bot.send_message(message.chat.id, "Что это за символы? Я не понимаю вас!")

if __name__ == '__main__':
    bot.polling(none_stop=True)