from math import inf

#__all__ = ['summ', 'divide']




def divide(num1, num2):
    return inf if num2 == 0 else num1 / num2


def module_func():
    print(__name__)


if __name__ == '__main__':



    module_func()
    divide(10, 1)


def summ(num1, num2):
    return num1 + num2


