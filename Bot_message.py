import telebot

from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

api_token = os.getenv('API_TOKEN')

bot = telebot.TeleBot(api_token)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Thank you for coming !!!")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()