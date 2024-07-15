#  ------------------------------------------------------------------------------- Использование %
team1_num = 5
team2_num = 15
print('В команде Мастера кода участников: %d!' % team1_num)
print('Итого сегодня в командах участников: %d и %i!' % (team1_num, team2_num ))


#  ------------------------------------------------------------------------------- Использование format()
score_2 = 42
print('Команда Волшебники данных решила задач: {}!'.format(score_2))
team1_time = 1552.512
team2_time = 2153.31451
print('Волшебники данных решили задачи за {} c!'.format(team1_time))


#  ------------------------------------------------------------------------------- Использование f-строки
score_1 = 40
score_2 = 42
print(f'Команды решили {score_1} и {score_2} задач.')

tasks_total = score_1 + score_2
time_avg = 45.2

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Сегодня было решенно {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
print(f'Результат битвы: {challenge_result}')