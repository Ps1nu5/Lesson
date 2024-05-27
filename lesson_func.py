
# 1 1 2 3 5 8 13 21 ...

def fib(x):
    if x in (1, 2):
        return 1
    return fib(x-1)+fib(x-2)


print(fib(40))
