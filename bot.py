import telebot
token = '5189222022:AAHwMwbam7yvCOFoHlfzYcqpYOA3FOyW21o'
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)
    bot.send_photo(message.chat.id, photo=open('img/q.jpg', 'rb'))

if __name__ == '__main__':
     bot.infinity_polling()
