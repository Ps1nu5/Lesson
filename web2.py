# l = [1, 2, 3, 4, 5]
#
# for i in range(6):
#     print(i in l)

# def hello_func(name, age):
#     print(f'Привет, {name}!')
#     print(f'Тебе {age} лет!')
#
# hello_func('Святослав', 24)

# for i in range(3):
#     for j in range(5):
#         print(i, j)
#     print('Работа внутреннего цикла закончена!')
# print('Работа внешнего цикла закончена!')


# num = int(input())
# result = ''
# for i in range(1, num):
#     for j in range(i+1, num):
#         if ...:
#             result += f'{i}{j}'
# print(result)

# def get_matrix(n, m, value):
#     matrix = []
#     for i in range(n):
#         matrix.append([])
#         for j in range(m):
#             matrix[i] ...
#
#     return matrix




name = 'Святослав'
# Привет, ИМЯ!
print('Привет, ', name, '!', sep='', end=' ')
print('Привет, '+name+'!')
print(f'Привет, {name}!')
print('Привет, {}!'.format(name))

