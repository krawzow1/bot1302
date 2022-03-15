import telebot
token = '5189222022:AAHwMwbam7yvCOFoHlfzYcqpYOA3FOyW21o'
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)
    bot.send_photo(chat_id=chat_id, photo=open('tests/test.png', 'rb'))

if __name__ == '__main__':
     bot.infinity_polling()
