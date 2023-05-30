
# Дан список элементов. Используя библиотеку NumPy, 
# подсчитайте количество уникальных элементов в нём.

import numpy as np
import random
def task1():
    size = 10
    numbers = np.random.randint(1, 10, size), 
    print(numbers)

    uniq_list, uniq_counts = np.unique(numbers, return_counts=True)
    print(f'уникальные элементы {uniq_list}')
    print(f'их количество       {uniq_counts}')
    




# Создайте двумерный массив, размером 5х5. 
# Определите, есть ли в нём одинаковые строки.

def task2():
    def has_duplicate_rows(matrix):
        unique_rows = np.unique(matrix, axis=0)
        return len(unique_rows) < len(matrix)
    
    size = (5,5)
    numbers = np.random.randint(1, 10, size)

    if has_duplicate_rows(numbers):
     print("В массиве есть одинаковые строки.")
    else:
     print("В массиве нет одинаковых строк.")    


# Создайте двумерный массив случайного размера. Найдите индексы максимального и минимального элементов в нём.
# Выведите элементы главной диагонали матрицы в виде одномерного массива.

def task3():
    

    rows = np.random.randint(3, 6)  
    cols = np.random.randint(3, 6)  
    numbers = np.random.randint(0, 100, size=(rows, cols))  

    max_index = np.unravel_index(np.argmax(numbers), numbers.shape)
    min_index = np.unravel_index(np.argmin(numbers), numbers.shape)

    diagonal_elements = np.diag(numbers)

   
    print("Двумерный массив:")
    print(numbers)
    print()
    print("Индекс максимального элемента:", max_index)
    print("Индекс минимального элемента:", min_index)
    print()
    print("Элементы главной диагонали:")
    print(diagonal_elements)


task3()


