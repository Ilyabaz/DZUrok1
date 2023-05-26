# urok 7 
# 1. Создайте пользовательский аналог метода map().

import random
import time

def hometask1():
    def costom_map(func, numbers):
        res = []
        for i in numbers:
            res.append(func(i))
        return res


    def square(x):
        return x**2 
    numbers = [random.randint(1,10)]
    squared_numbers = costom_map(square, numbers)
    print(squared_numbers)



# 2. Создайте декоратор, повторяющий функцию заданное количество раз.

def hometask2():
    def repeat(times):
        def decorator(func):
            def wrapper(*args, **kwargs):
                for _ in range(times):
                    result = func(*args, **kwargs)
                return result
            return wrapper
        return decorator
  
    @repeat(times=3)

    def greet(name):
        print(f"Zdarova, {name}!")


    greet("Denis")


# 3.  Добавьте в telegram-бота игру «Угадай числа». 
# Бот загадывает число от 1 до 1000. Когда игрок угадывает его, бот выводит количество сделанных ходов.

import telebot
import random

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

   