import telebot
from telebot import types # для указание типов
token = '5189222022:AAHwMwbam7yvCOFoHlfzYcqpYOA3FOyW21o'
bot = telebot.TeleBot(token)




@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,text="Привет, {0.first_name}!". format(message.from_user))
    
@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1= types.KeyboardButton("Игрок идет налево")
    item2= types.KeyboardButton("Игрок идет направо")
    markup.add(item1, item2)
    bot.send_message(message.chat.id,'Выберите куда идти', reply_markup=markup)
    
 
    
  
         


if __name__ == '__main__':
     bot.infinity_polling()
