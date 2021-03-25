import telebot

bot = telebot.TeleBot('1632001696:AAElATgcEfvNbfIfSviGr6YI-upjeJ7_5WA')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
    
bot.polling()