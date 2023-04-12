

def task1():
    def factorial_list(n):
            factorial_list(n)
            factorials = [1]
            for i in range(1, n+1):
                    factorials.append(factorials[-1]*i)
            return factorials[1:]

    n = int(input("Введите число N: "))
    factorials = factorial_list(n)
    print(factorials)



def task2():
        print("X\tY\tZ\t¬(X ∧ Y) ∨ Z")
print("-" * 30)

for X in [False, True]:
    for Y in [False, True]:
        for Z in [False, True]:
            result = not(X and Y) or Z
            print(f"{int(X)}\t{int(Y)}\t{int(Z)}\t{int(result)}")


def task3():
    string1 = input("Введите первую строку: ")
    string2 = input("Введите вторую строку: ")
    counts = {}
    for char in string1:
        counts[char] = string2.count(char)
    print("Результат подсчета:")
    for char, count in counts.items():
        print(f"{char} - {count}")

def task4():
        
    N = int(input("Введите размер списка: "))

    # Создаем список из N элементов, заполненный числами из промежутка [-N, N]
    lst = list(range(-N, N+1))

    # Сдвигаем все элементы списка на 2 позиции вправо
    lst = lst[-2:] + lst[:-2]

    # Выводим результат на экран
    print("Исходный список:", list(range(-N, N+1)))
    print("Список со сдвигом на 2 позиции вправо:", lst)

task4()