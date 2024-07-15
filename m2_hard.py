n = int(input('Первое число: '))
password = ''

for i in range(1, n):
    for j in range(i+1, n):
        if n % (i + j) == 0:
            password += f'{i}{j}'

print(password)














