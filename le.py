# my_string = input('введите марку вашего автомобиля ')
# print(my_string.upper())
# print(my_string.lower())
# print(my_string.replace(' ', ''))
# print(my_string[0])
# print(my_string[-1])


my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i < len(my_list):
    if my_list[i] > 0:
        print(my_list[i])
    elif my_list[i] < 0:
        break
    i += 1




