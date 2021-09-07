import telebot
from telebot import types
import os


API_TOKEN = os.getenv('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)


# commands=[список_придуманных_команд_типа_/команда], регистр важен
@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message, 'Hi, how are you?')  # использует "Ответ" для сообщения пользователю


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Hi, can I help you?')
    else:
        bot.send_message(message.chat.id, 'Use /help')


def test_rq(message):
    request = message.text.split()
    return True


@bot.message_handler(func=test_rq)
def send_ans_for_rq(message):
    pass


bot.polling(none_stop=True, interval=0)

