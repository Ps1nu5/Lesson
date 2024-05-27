from random import choice
quiz_dict = {'q1': 'a1', 'q2': 'a2'}
print('Игра QUIZ')
points = 0
while len(quiz_dict) > 0:
    print(f'Вопросов осталось: {len(quiz_dict)}')
    random_q = choice(list(quiz_dict.keys()))
    random_a = quiz_dict.pop(random_q)
    #print(random_q, random_a)
    print(random_q)
    user_answer = input('Ваш ответ: ').lower()
    if user_answer == random_a:
        points += 1
    # else:
    #     points -= 1
    print('Спасибо за ответ!\nСледующий вопрос:\n')

print(f'Ваш результат {points}/5')
match points:
    case 5:
        print('Отлично!')
