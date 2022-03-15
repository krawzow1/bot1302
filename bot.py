import telebot
token = '5189222022:AAHwMwbam7yvCOFoHlfzYcqpYOA3FOyW21o'
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)
    bot.send_photo(message.chat.id, photo=open('img/q.jpg', 'rb'))
    
@bot.message_handler(commands=['start']) #создаем команду
def start(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Сайт Хабр", url='https://habr.com/ru/all/')
    markup.add(button1)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди на сайт)".format(message.from_user), reply_markup=markup)kup)

if __name__ == '__main__':
     bot.infinity_polling()
