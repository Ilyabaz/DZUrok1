
def our_match_str():
    num = '132'
    result = int(num) + int(num*2) + int(num*3)
    print(result)


def our_math_int():
    num = 132
    result = num + num*100 + num + num*100000 + num*1000 + num 
    print(result)



def greetings(hello):
    def our_greetings(func):
        def decorator():
            name = func()
            print(f'{hello}, {name}')
        return decorator
    return our_greetings

@greetings('Привет')
def get_name():
    return input('как тебя зовут?\n')





def stopwatch(func):
    import time
    def decorator():
        start_time = time.time()
        func()
        print(f'время выполнения {time.time() - start_time}')
    return decorator

@stopwatch
def our_math_str():
    num = '132'
    result = int(num) + int(num*2) + int(num*3)
    print(result)

@stopwatch
def our_math_int():
    num = 132
    result = num + num*1000 + num + num*1000000 + num*1000 + num
    print(result)





