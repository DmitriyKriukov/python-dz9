import telebot
from config import TOKEN
import random
from datetime import datetime

bot = telebot.TeleBot(TOKEN)


"""Команда СТАРТ"""


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = telebot.types.KeyboardButton('Анекдот')
    item2 = telebot.types.KeyboardButton('Факт')
    item3 = telebot.types.KeyboardButton('Дата и время')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, 'Добро пожаловать! Выберите нужный вам пункт меню: ', reply_markup=markup)

def random_number(message):
    bot.send_message(message.chat.id, str(random.randint(1, 10)))

with open('fun.txt', 'r', encoding='utf-8') as file:
    fun = file.read().split('\n')

with open('facts.txt', 'r', encoding='utf-8') as file:
    fact = file.read().split('\n')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Анекдот':
        bot.send_message(message.chat.id, random.choice(fun))
    elif message.text == 'Факт':
        bot.send_message(message.chat.id, random.choice(fact))
    elif message.text == 'Дата и время':
        bot.send_message(message.chat.id, str(datetime.now()))



bot.polling(none_stop=True)