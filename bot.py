import telebot
token = '5189222022:AAHwMwbam7yvCOFoHlfzYcqpYOA3FOyW21o'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, text = "Ты заблудился ночью в лесу. Долго ходил-бродил и искал выход из леса, но ТУТ ты увидел жутко темный, жутко подозрительный и жутко жуткий замок.")  
        
      
if __name__ == '__main__':
    bot.infinity_polling()
