import time

def fib():
    x1 = 0
    x2 = 1
    def get_next_number():
        nonlocal x1, x2
        x3 = x1 + x2
        x1, x2 = x2, x3
        return x3
    return get_next_number

def fib_recursion(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursion(n-1) + fib_recursion(n-2)

def fib_closure(n):
    f = fib()
    for i in range(2, n+1):
        num = f()
    return num

fib_num = 4000
print(f'{"Замыкание" : ^30}')
time_start = time.time_ns()
num = fib_closure(fib_num)
time_end = time.time_ns()
print(f'Элемент ряда Фибоначчи №{fib_num} - {num}')
print(f'Затраченное время - {time_end-time_start}')

print(f'{"Рекурсия" : ^30}')
time_start = time.time_ns()
num = fib_recursion(fib_num)
time_end = time.time_ns()
print(f'Элемент ряда Фибоначчи №{fib_num} - {num}')
print(f'Затраченное время - {time_end-time_start}')
