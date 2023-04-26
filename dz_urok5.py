
# Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию
import random
def task1():
        num = [random.randint(1,10) for _ in range(10) ]
        print(num)
        num = list(filter(lambda x: x>5, num))
        print (num)



# Дан список случайных чисел. Создайте список, в который попадают числа, описывающие случайную возрастающую последовательность. 
# Порядок элементов менять нельзя.



def task2():
    numbers = [random.randint(1,10) for _ in range(8)] 
    print(numbers)
    result = [numbers[0]]
    for num in numbers[1:]:
          if num > result[-1]:
                result.append(num)
   
    print(result)



# Задайте список случайных чисел от 1 до 10. 
# Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.

def task3():
      numbers = list(random.randint(1,10) for _ in range(8))
      print(numbers) 
      s = set(numbers)
      for i in s:
            print(f'{i} повторяется => {numbers.count(i)} ' )
      uniq_numbers = list(set(numbers))
            
      print(uniq_numbers)      

            
     

task3()