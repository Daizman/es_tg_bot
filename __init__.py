import telebot
import os
import nltk
from telebot import types


API_TOKEN = os.getenv('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)


def print_help(chat_id):
    bot.send_message(chat_id, 'Привет, я бот созданный для консультации по вопросам, связанным '
                              'с поиском ТЗ, инструкций и других документов. Задай мне вопрос, '
                              'в котором укажи кто ты (разработчик/аналитик/тестировщик/оператор), '
                              'и что ты ищешь, а дальше я постараюсь найти нужную тебе статью или '
                              'задам уточняющие вопросы.')


def parse_message():
    pass


default_handlers = {
    'HELP': print_help,
    '/HELP': print_help,
    'ЧТО ТЫ МОЖЕШЬ?': print_help,
    'ЧТО ТЫ УМЕЕШЬ?': print_help,
    'ПРИВЕТ': print_help
}


@bot.message_handler(content_types=['text'])
def text_messages_handler(message):
    message = message.strip().upper()
    if message in default_handlers.keys():
        default_handlers[message](message.chat.id)
        return True


bot.polling(none_stop=True, interval=0)
