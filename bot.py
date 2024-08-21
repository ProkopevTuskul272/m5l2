import telebot
from config import *
from logic import *

bot = telebot.TeleBot(TOKEN)

commands = ['/start', '/help', '/show_city', '/remember_city', '/show_my_cities НЕ РАБОТАЕТ', '/about']

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я бот, который может показывать города на карте. Напиши /help для списка команд.")

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, "Доступные команды:  ...")
    # Допиши команды бота
    for x in commands:
        bot.send_message(message.chat.id, x)

@bot.message_handler(commands=['about'])
def handle_about(message):
    bot.send_message(message.chat.id, "Привет! Этот бот был создан для показа города на карте, сохранение города и показать все сохраннёные города на карте.")

@bot.message_handler(commands=['show_city'])
def handle_show_city(message):
    city_name = message.text.split()[-1]
    # Реализуй отрисовку города по запросу
    manager.create_grapf('output.png',[city_name])
    bot.send_document(message.chat.id, open('output.png', 'rb'))

@bot.message_handler(commands=['remember_city'])
def handle_remember_city(message):
    user_id = message.chat.id
    city_name = message.text.split()[-1]
    if manager.add_city(user_id, city_name):
        bot.send_message(message.chat.id, f'Город {city_name} успешно сохранен!')
    else:
        bot.send_message(message.chat.id, 'Такого города я не знаю. Убедись, что он написан на английском!')

@bot.message_handler(commands=['show_my_cities'])
def handle_show_visited_cities(message):
    cities = manager.select_cities(message.chat.id)
    # Реализуй отрисовку всех городов

if __name__=="__main__":
    manager = DB_Map(DATABASE)
    bot.polling()
