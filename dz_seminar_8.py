


# Задача 1 Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.


import telebot

token = 
bot = telebot.TeleBot(token)

@bot.message_handler(func=lambda message: True)
def support_chat(message):
    user_id = message.from_user.id
    user_name = message.from_user.username if message.from_user.username else message.from_user.first_name
    message_text = message.text

   
    with open("support_logs.txt", "a") as file:
        file.write(f"User ID: {user_id}\n")
        file.write(f"User Name: {user_name}\n")
        file.write(f"Message: {message_text}\n")
        file.write("-" * 20)
        file.write("\n")

    bot.reply_to(message, "Спасибо что обратились, с вами свяжутся в ближайшее время.")

bot.polling()



# задача 2 Напишите программу, которая позволяет считывать из файла вопрос, отвечать на него и отправлять ответ обратно пользователю.

token = 
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я готов отвечать на вопросы. Отправь мне вопрос из файла.")


@bot.message_handler(content_types=['document'])
def handle_document(message):
    if message.document.mime_type == 'text/plain':
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        decoded_text = downloaded_file.decode('utf-8')

        question = decoded_text.strip()  

        answer = get_answer(question)

        bot.reply_to(message, answer)
    else:
        bot.reply_to(message, "Извините, я принимаю только текстовые файлы (расширение .txt).")


def get_answer(question):
    return "Спасибо за ваш вопрос. Мы ответим вам в ближайшее время."


bot.polling()
