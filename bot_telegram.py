
# import telebot
# import requests
# import time

# bot = telebot.TeleBot("6266203253:AAGQMBNStSEsjTCmDWqObp7OW6_RRy5sMb0")

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")
        
# @bot.message_handler(commands=['text'])
# def greeting(message):
#     text = message.text
#     if 'привет' in text:
#      bot.reply_to(message, f'Привет, {message.from_user.first_name}')
        
   

# bot.polling()