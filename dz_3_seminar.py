
# Создайте список. Запишите в него N первых элементов последовательности Фибоначчи.
def task1():
     n = int(input("Введите количество элементов последовательности Фибоначчи: "))
     fibonacci = [0, 1] 

     for i in range(2, n):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

     print(fibonacci)



# В списке находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
def task2():

    fruits = ['абрикос', 'авокадо', 'апельсин', 'айва', 'банан', 'виноград', 'груша', 'дыня', 'ежевика', 'женьшень', 'земляника']
    letter = input('Ввидите букву: ')
    for fruit in fruits:
        if fruit.startswith(letter):
            print(fruit)
    


# Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. 
# Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». 
# Если фраза ему неизвестна, он выводит соответствующую фразу.

def task3():

  
    answers = {
        "привет": "Привет!",
        "как тебя зовут": "Меня зовут Бот. А тебя?",
        "что делаешь": "Отвечаю на твои вопросы. А ты?",
        "спасибо": "Не за что!",
        "до свидания": "До свидания! Хорошего дня!"
    }

    def get_answer(question, answers):
        answer = answers.get(question)
        if answer:
            return answer
        else:
            return "Извините, я не знаю, что на это ответить."

    
    while True:
        # считываем вопрос пользователя
        question = input("Задайте свой вопрос: ").lower()

        # проверяем вопрос и получаем ответ
        answer = get_answer(question, answers)

        # выводим ответ
        print(answer)
task3()