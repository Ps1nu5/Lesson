
def add_everything_up(arg1, arg2):
    try:
        return arg1 + arg2
    except TypeError:
        return str(arg1) + str(arg2)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
