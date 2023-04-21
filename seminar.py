
# def calculate(n_1,n_2):
#     return n_1+n_2 , n_1-n_2, n_1*n_2, n_1/n_2

# n_1 = int(input('Ввидите число: '))
# n_2 = int(input('Ввидите число: '))
# res = calculate(n_1,n_2)
# print(*res)

import random

numbers = [random.randint(1,20) for _ in range (10)]
length = len(numbers)
numbers = set(numbers)
print(numbers)
print(f' Элементов было удаленo {length - len(numbers)}')