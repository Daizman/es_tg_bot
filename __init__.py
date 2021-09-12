import telebot
import os
import nltk
import re
import pymorphy2
from nltk.corpus import stopwords as nltk_sw
from controller.Shell import Shell


API_TOKEN = os.getenv('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)
shell = Shell()


def print_help(chat_id):
    bot.send_message(chat_id, 'Привет, я бот созданный для консультации по вопросам, связанным '
                              'с поиском ТЗ, инструкций и других документов. Задай мне вопрос, '
                              'в котором укажи кто ты (разработчик/аналитик/тестировщик/оператор), '
                              'и что ты ищешь, а дальше я постараюсь найти нужную тебе статью или '
                              'задам уточняющие вопросы.')


def tokenize(message):
    morph = pymorphy2.MorphAnalyzer()
    sw = nltk_sw.words('russian')
    return [morph.parse(word)[0].normal_form
            for sent in nltk.sent_tokenize(message)
            for word in nltk.word_tokenize(sent)
            if len(word) >= 3 and re.search(r'[\w\d]+', word) and word not in sw]


default_handlers = {
    'help': print_help,
    '/help': print_help,
    'что ты можешь?': print_help,
    'что ты умеешь?': print_help,
    'привет': print_help
}


@bot.message_handler(content_types=['text'])
def text_messages_handler(message):
    message = message.strip().lower()
    if message in default_handlers.keys():
        default_handlers[message](message.chat.id)
        return True
    message_tokens = tokenize(message.text)


bot.polling(none_stop=True, interval=0)
