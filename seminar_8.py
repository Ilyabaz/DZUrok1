import telebot
import random

token = "6266203253:AAGQMBNStSEsjTCmDWqObp7OW6_RRy5sMb0"
bot = telebot.TeleBot(token)

secret_number = None
attempts = 0

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я загадал число от 1 до 1000. Попробуй угадать!")


@bot.message_handler(func=lambda message: True)
def guess_number(message):
    global secret_number
    global attempts

    if secret_number is None:
        secret_number = random.randint(1, 1000)
        attempts = 0

    try:
        guess = int(message.text)

        if guess == secret_number:
            attempts += 1
            bot.reply_to(message, f"Поздравляю! Ты угадал число {secret_number} за {attempts} попыток.")
            secret_number = None
        elif guess < secret_number:
            attempts += 1
            bot.reply_to(message, "Загаданное число больше.")
        elif guess > secret_number:
            attempts += 1
            bot.reply_to(message, "Загаданное число меньше.")
    except ValueError:
        bot.reply_to(message, "Пожалуйста, введите число от 1 до 1000.")


bot.polling()

   
       
