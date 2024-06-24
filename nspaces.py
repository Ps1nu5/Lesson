num = 10


def my_func():
    num = 1
    def inner_func():
        num = 5

        print(num)

    inner_func()




my_func()

