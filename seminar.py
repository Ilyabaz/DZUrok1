
# # def calculate(n_1,n_2):
# #     return n_1+n_2 , n_1-n_2, n_1*n_2, n_1/n_2

# # n_1 = int(input('Ввидите число: '))
# # n_2 = int(input('Ввидите число: '))
# # res = calculate(n_1,n_2)
# # print(*res)

# import random

# numbers = [random.randint(1,20) for _ in range (10)]
# length = len(numbers)
# numbers = set(numbers)
# print(numbers)
# print(f' Элементов было удаленo {length - len(numbers)}')



# import random
# def zadacha_0():
#     num = [random.randint(1,25) for _ in range(6)]
#     print(num)
#     num = list(filter(lambda x: not (x%5), num))
#     print (num)
# zadacha_0()

def zadacha_1():
    num = input('Ввидите число: ')
    numbers = [int(letter) for letter in num]
    print(numbers)
    numbers = list(map(lambda x: x+10, numbers))
    print (numbers)

def ToBinary(num):
    result=''
    while num>0:
        result= str(num%2) + result
        num //=2
    return '0'*(6-len(result)) + result

def decoder(code):
    animal = [code[i:i+6]for i in range(0,len(code),6)]
    print(animal)
    


def zadacha_2():
    animals = ['010100001100001001010011001011000000',
                '000001011100001011',
                '001011001111010011',
                '010010010011001111010001001111000111',
                '001100000101000010',
                '001011010001001111001100001001001011',
                '001101010100001100',
                '000001000000010001010010010100001011',
                '000011000101010000000000010001000100',
                '010010001111001101',
                '010010001111000001000000001011000000',
                '011000001001000111']
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alphabet = list(alphabet)
    d= {}
    for i in range(len(alphabet)):

        d[ToBinary(i)] = alphabet[i]
    print(d)

    result = list(map (lambda x: [d[x[i:i+6]] for i in range(0,len(x),6)],animals))
    result = list(map(lambda x: ''.join(x), result))  
    print (result)             
zadacha_2()
