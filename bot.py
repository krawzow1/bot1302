import telebot
from telebot import types # для указание типов
token = '5189222022:AAHwMwbam7yvCOFoHlfzYcqpYOA3FOyW21o'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Кнопка")
    item2=types.KeyboardButton("Кнопка2")
    item3=types.KeyboardButton("Игра")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Кнопка":
        bot.send_photo(message.chat.id, photo=open('vze2.jpg', 'rb'))
    if message.text=="Кнопка2":
        bot.send_message(message.chat.id, "vk.com/goshkazavr")

@bot.message_handler(content_types='text')
def game(message):
    if message.text=="Игра":
        bot.send_message(message.chat.id, "игра началась")
    else:
        bot.send.message(message.chat.id, "игра началась")
    
  
         


if __name__ == '__main__':
     bot.infinity_polling()
